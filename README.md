
# Ethereum Vanity Address Generator

This Python script generates a custom Ethereum vanity address with a user-defined prefix, leveraging multi-processing to improve performance. It provides real-time feedback on the number of generated addresses until the desired vanity address is found.

## Prerequisites

Make sure you have Python 3.6 or higher installed.

## Setup

1.  Clone this repository or download the `ethereum_vanity_address_generator.py` script.
2.  Open a terminal and navigate to the directory containing the script.
3.  Create a virtual environment using the following command:
`python -m venv venv` 
4.  Activate the virtual environment:
-   On Windows:
`venv\Scripts\activate` 
-   On macOS and Linux:
`source venv/bin/activate` 
5.  Install the required libraries:
`pip install -r requirements.txt` 


## Usage

1.  Ensure your virtual environment is activated.
2.  Run the script by executing `python ethereum_vanity_address_generator.py`.
3.  When prompted, enter the desired vanity address prefix (without `0x`).
4.  When prompted, enter the number of processes to be used (default is 8).
5.  The script will start generating Ethereum addresses and display the count of generated addresses in real-time.
6.  When a vanity address matching the desired prefix is found, the script will display the address and its corresponding private key.

**Warning**: The private key generated is crucial for accessing the Ethereum account. Make sure to securely store the private key and never share it with anyone.

## Disclaimer

Generating vanity addresses with longer prefixes may take a considerable amount of time, even with multi-processing. The performance improvement depends on your system's hardware. Always securely store your private keys and never share them with anyone. The authors of this script are not responsible for any loss or issues arising from the use of this code.

## License

This project is released under the [MIT License](https://opensource.org/licenses/MIT).
