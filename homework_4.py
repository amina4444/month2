class Contact:
    def __init__(self, name, phone_number,id):
        self.name = name
        self.phone_number = phone_number
        self.id = id

    @classmethod
    def validate_phone_number(cls, phone_number):
         if len(phone_number) == 10:
            return True
         else:
                return False


class ContactList:
    all_contacts = []
    last_id = 0

    @classmethod
    def add_contact(cls, name, phone_number):
        if  Contact.validate_phone_number(phone_number) == True:
            ContactList.last_id += 1
            contact = Contact(name, phone_number,ContactList.last_id)

        else:
            raise ValueError

        cls.all_contacts.append(contact)

    @classmethod
    def remove_contact(cls, id):
        for c in cls.all_contacts:
          if c.id == id:
            ContactList.all_contacts.remove(c)
            return
        raise ValueError



ContactList.add_contact("Вася Пупкин", "0700100200")
ContactList.add_contact("Виктор Цой", "0500123456")

for contact in ContactList.all_contacts:
    print(contact.name, contact.phone_number)



print(ContactList.last_id) # 0

print(ContactList.last_id) # 2

ContactList.remove_contact(1)

for contact in ContactList.all_contacts:
    print(contact.name, contact.phone_number, contact.id)
    # Виктор Цой 0500123456 2



