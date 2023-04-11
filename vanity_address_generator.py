import os
import re
import time
from eth_keys import keys
from eth_utils import to_checksum_address
from multiprocessing import Process, Queue, Value, Manager


def generate_vanity_address(prefix, queue, counter):
    regex = re.compile("^0x" + prefix.lower())
    while True:
        private_key = keys.PrivateKey(os.urandom(32))
        public_key = private_key.public_key
        address = public_key.to_checksum_address()

        with counter.get_lock():
            counter.value += 1

        if regex.match(address.lower()):
            queue.put((private_key, address))
            break


def monitor(queue, target_vanity, counter):
    while True:
        try:
            result = queue.get(timeout=1)
            print(f"\nFound vanity address with {target_vanity} prefix:")
            print(f"Address: {result[1]}")
            print(f"Private Key: {result[0].to_hex()}")
            os._exit(0)
        except:
            print(f"Generated addresses so far: {counter.value}", end="\r")


def main(target_vanity, num_processes=8):
    work_queue = Queue()
    counter = Value("i", 0)

    print(f"Generating Ethereum vanity address with {target_vanity} prefix...")

    monitor_process = Process(target=monitor, args=(work_queue, target_vanity, counter))
    monitor_process.daemon = True
    monitor_process.start()

    worker_processes = []
    for _ in range(num_processes):
        worker = Process(target=generate_vanity_address, args=(target_vanity, work_queue, counter))
        worker.daemon = True
        worker.start()
        worker_processes.append(worker)

    try:
        while True:
            time.sleep(1)
    except KeyboardInterrupt:
        print("\nStopping...")
        os._exit(0)


if __name__ == "__main__":
    target_vanity = input("Enter desired vanity address prefix (without 0x): ")
    num_processes = int(input("Enter number of processes (default is 8): ") or 8)
    main(target_vanity, num_processes)
