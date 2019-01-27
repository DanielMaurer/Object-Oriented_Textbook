class ContactList(list):
    
    def search(self, name):
        """Return all contacts that contain the serach value in their nam."""
        matching_contacts = []
        for contact in self:
            if name in contact.name:
                matching_contacts.append(contact)
            return matching_contacts
        

class Contact:
    all_contacts = ContactList()

    def __init__(self, name, email):
        self.name = name
        self.email = email
        Contact.all_contacts.append(self)

class Supplier(Contact): # Creates a new class with inheriting the methods from Contact
    def order(self, order):
        "If this were a real system we would send "
        "'{order}' order to '{self.name}'" 

class Friend(Contact, AddressHolder):
    def __init__(self, name, email, phone, street, city, state, code):
        Contact.__init__(self, name, email)
        AddressHolder.__init__(seld, street, cidy, state, code)
        self.phone = phone

def AddressHolder:
    def __init__(self, street, city, state, code):
        self.street = street
        self.city = city
        self.state = state
        self.code = code

class MailSender:
    def send_mail(self, message):
        print("Sent email to " + self.email)
        # Email logic

class EmailableContact(Contact, MailSender):
    pass
