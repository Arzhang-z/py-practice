# Contact Book (Python CLI)

A simple command-line contact book application written in Python.
Supports adding, viewing, updating, and deleting contacts, with optional email validation.

## Features

-Add contacts with name and phone number

-Optional email field with basic validation

-Update existing contacts

-Delete contacts

-View all saved contacts

-Simple CLI interface

-Uses defaultdict for contact storage


## Requirements
- Python 3.9+ (for type hints like defaultdict[str, dict[str, str]])


## How It Works
Each contact is stored internally as:

```python 
{
    "Name": {
        "phone": "123456789",
        "email": "example@email.com"  # optional
    }
}
```

Email input is optional.
If provided, the program checks that it contains "@".
If invalid, the user is prompted to re-enter the email or skip it.

## Usage

Run the script:

```bash
python contact_book.py 
```

You will see a menu:
1. Add Contact
2. Edit Contact
3. View Contacts
4. Delete Contact
5. Quit

#### Add Contact

-Name: required

-Phone: required

-Email: optional (validated)

#### Edit Contact

- Update phone and/or email

- Leave fields empty to skip updating them

#### View Contacts

- Displays all saved contacts and their details.

#### Delete Contact

- Removes a contact by name.


----
## Email Validation Logic

```python
    def _validate_email(self, email: str) -> bool:
    return "@" in email
```

if the email is invalid, the user is prompted again until:

- A valid email is entered, or

- The input is left empty to skip

## Project Structure

```
.
├── contact_book.py
└── README.md
```