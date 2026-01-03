from collections import defaultdict


class ContactBook:
    def __init__(self):
        #self.contacts = {}
        self.contacts: defaultdict[str,dict[str,str]]  = defaultdict(dict)

    def _validate_email(self, email: str) -> bool:
        return "@" in email

    def add_contact(self, name: str, phone: str, email: str = ""):
        """
        Add a contact to the contact book

        :param name: Name of the contact 
        :param phone: phone number of the conatct
        :param email: email address of the contact, defaults to None
        """
        if name in self.contacts:
            print("Contact Already Exists!")
            return

        #self.contacts[name] = {}
        self.contacts[name]["phone"] = phone
        while email:
            if self._validate_email(email):
                self.contacts[name]["email"] = email
                break
            else:
                email = input("Enter again (or press Enter to skip)) ")
            
    def view_contacts(self):
        """
        view all contacts in the contact book
        """
        for name, info in self.contacts.items():
            print(f"Name: {name}")
            print(f"phone: {info['phone']}")
            if info.get("email") is not None:
                print(f"Email: {info['email']}")
            print("_" * 50)

    def delete_contact(self, name: str):
        """
        delete a especial contact from contact book

        :param name: Name of the contact to be deleted.
        """
        if name in self.contacts:
            del self.contacts[name]
            print("Contact deleted successfully")
        else:
            print("Contact not found")

    def update_contact(self, name: str, phone: str = "", email: str = ""):
        """
        update a contact in the contact book

        :param name: Name of the contact to be updated
        :param phone: phone number of the conatct to be updated, defaults to None
        :param email: email address of the contact to be updated, defaults to None
        """
        if name in self.contacts:
            if phone:
                self.contacts[name]["phone"] = phone
            while email:
                if self._validate_email(email):
                    self.contacts[name]["email"] = email
                    break
                else:
                    email = input("Enter again (or press Enter to skip)) ")

            print("Contact updated successfully!")
            return
        
        print("Contact not found")


if __name__ == "__main__":
    book = ContactBook()

    while True:
        print("\n\nWelcome to contact book application!")
        print("1. Add Contact")
        print("2. Edit Contact")
        print("3. View Contacts")
        print("4. Delete Contact")
        print("5. Quit")

        user_choice = input("Please choose an option: ")

        if user_choice == "5":
            break

        elif user_choice == "1":
            name = input("\nEnter contact name: ")
            phone = input("Enter contact phone: ")
            email = input("Enter contact email: (skip if u don't wanna add) ")
            book.add_contact(name, phone, email)

        elif user_choice == "2":
            name = input("\nEnter contact name: ")
            phone = input("Enter contact phone: (skip if u don't wanna add change) ")
            email = input("Enter contact email: (skip if u don't wanna add change) ")
        
            book.update_contact(name, phone, email)
        
        elif user_choice == "3":
            print("\nList of Contacts: ")
            book.view_contacts()
        
        elif user_choice == "4":
            name = input("\nEnter contact name: ")
            book.delete_contact(name)