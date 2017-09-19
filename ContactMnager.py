class Contact:
    def __init__(self, name, phone_number, gender, email_address, postal_address):
        # address_book = {'George': ['0707187390', 'M', 'georgeosodo2010@gmail.com']}

        self.name = name
        self.phone_number = phone_number
        self.gender = gender
        self.email_address = email_address
        self. postal_address = postal_address


class PhoneBook:
    def __init__(self, p_book={}):
        self.phone_book = p_book

    def add_number(self):
        my_name = input("Enter name: ")
        my_number = input("Enter phone number: ")
        my_gender = input("Enter gender: ")
        my_email = input("Enter email: ")
        my_address = input("Enter postal address: ")

        self.phone_book.setdefault(my_name, []).append(my_number)
        self.phone_book[my_name].append(my_gender)
        self.phone_book[my_name].append(my_email)
        self.phone_book[my_name].append(my_address)

    def delete_number(self, delete_contact):
        if delete_contact in self.phone_book.keys():
            del self.phone_book[delete_contact]
            print('Contact successfully deleted')
        else:
            print("Contact not available")

    def search_number(self, check_name):
        if check_name in self.phone_book.keys():
            return self.phone_book[name]
        else:
            print("Contact not available")


my_contacts = PhoneBook()
user_prompt = input("Enter number to proceed: 1 to add number, 2 to delete contact, 3 to search contact"
                    " and 4 to Exit: ")

while user_prompt != '4':
    if user_prompt == '1':
        my_contacts.add_number()       # add contact

    elif user_prompt == '2':
        contact_to_delete = input("Enter contact name: ")
        my_contacts.delete_number(contact_to_delete)                            # delete contact

    elif user_prompt == '3':
        name = input("Enter name: ")          # Search contact
        my_details = my_contacts.search_number(name)

        if my_details is not None:
            print('Name: ' + name + ' Phone number: ' + my_details[0] + ' Gender: ' + my_details[1] +
                  ' Email Address: ' + my_details[2]+'  Postal address:  ' + my_details[3])

    user_prompt = input("Enter number to proceed: 1 to add number, 2 to delete contact, 3 to search contact"
                        " and 4 to Exit: ")










