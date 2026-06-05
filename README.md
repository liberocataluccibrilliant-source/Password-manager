# Password Manager (Python)

A simple command-line password manager written in Python.
This project allows you to store, view, search, delete, and generate passwords using a JSON file as local storage.

## Features

* Add new passwords associated with a service and username.
* Save passwords in a JSON file.
* View all saved passwords.
* Search passwords by service name.
* Delete saved passwords.
* Generate random passwords.
* Simple terminal-based interface.

## How It Works

The program stores all credentials inside a JSON file (`Passwords.json` by default). Each entry follows this structure:

```json
{
    "GitHub": {
        "username": "my_username",
        "password": "my_password"
    }
}
```

## Requirements

* Python 3.x
* Standard Python libraries only:

  * os
  * json
  * random

No external dependencies are required.

## Usage

Run the script:

```bash
python main.py
```

You will see a menu similar to:

```text
[1] Add a password
[2] Show all passwords
[3] Search a password
[4] Delete a password
[5] Generate a random password
```

Choose an option by typing the corresponding number.

## Current Limitations

* Passwords are stored in plain text.
* Search by username is not yet implemented.
* The password search system needs improvements.
* Error handling can be improved.
* No encryption is currently used.

## Future Improvements

* [ ] Complete username-based password search.
* [ ] Improve password search functionality.
* [ ] Add password encryption.
* [ ] Export and import password databases.
* [ ] Improve user interface.
* [ ] Add password strength validation.
* [ ] Add master password protection.

## Author

Created as a personal Python project to practice:

* File handling
* JSON management
* Dictionaries
* Functions
* Command-line applications
