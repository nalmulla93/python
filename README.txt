

This is a command-line application written in Python 3 that allows users to store and manage lyrics, music scores, and audio recordings securely. The application provides different roles, such as administrators and regular users, with varying levels of access and permissions.

## Features

- **User Authentication**: Users can log in with their username and role (admin or regular user).
- **Item Management**: Users can create, retrieve, and manage items (lyrics, music scores, and audio recordings).
- **Encryption**: All items are stored in an encrypted format to ensure data security.
- **Checksums**: Checksums are generated for each item to verify data integrity.
- **Timestamping**: Creation and modification timestamps are recorded for each item.
- **Admin Capabilities**: Admin users can create, retrieve, and remove users, as well as view all items in the database.

## Installation

1. Clone the repository or download the source code files.
2. Make sure you have Python 3.x installed on your system.
3. Install the required dependencies:
pip install cryptography
Copy code
## Usage

1. Navigate to the project directory.
2. Run the application:
python main.py
Copy code
3. Follow the prompts in the command-line interface to log in, create items, retrieve items, and perform other actions.

## Testing

The application includes a set of unit tests in the `test_item.py` file. To run the tests, execute the following command:
python test_item.py
Copy code
Additionally, security testing tools such as `bandit` can be used to identify potential security vulnerabilities in the code:
bandit -r .
Copy code
## Contributing

Contributions are welcome! If you find any issues or want to add new features, please open an issue or submit a pull request.

## Acknowledgments

- The `cryptography` library for encryption and decryption: https://cryptography.io/en/latest/
- Python documentation: https://docs.python.org/3/