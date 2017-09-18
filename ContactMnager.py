class Contact:
    def __init__(self, name, phone_number, gender, email_address, postal_address):
        self.name = name
        self.phone_number = phone_number
        self.gender = gender
        self.email_address = email_address
        self. postal_address = postal_address


def add_number():
    my_name = input("Enter name: ")
    my_number = input("Enter phone number: ")
    my_gender = input("Enter gender: ")
    my_email = input("Enter email: ")
    my_address = input("Enter postal address: ")

    add_contact = Contact(my_name, my_number, my_gender, my_email, my_address)
    print("Name: " + add_contact.name + "Phone number: " + add_contact.phone_number)

add_number()






