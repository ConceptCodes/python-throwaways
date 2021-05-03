import re

class Contact:
    def __init__(self, name: str, number: str, address: str):
        self.__name = name
        self.__number = number
        self.__address = address

    def validate_number(self, number: str) -> bool:
        return re.match(r'^(\+0?1\s)?\(?\d{3}\)?[\s.-]\d{3}[\s.-]\d{4}$',number)

    @property
    def full_name(self) -> str:
        return self.__name.title()
    
    @property
    def phone_number(self) -> str:
        return self.__number

    @property
    def address(self) -> str:
        return self.__address

    def call(self, target: Contact) -> str:
        if self.validate_number(target.phone_number): return "Calling {}\nNo one's available at the moment".format(target.full_name)
        
    def text(self, target: Contact) -> str:
        if self.validate_number(target.phone_number): return 'Sending Text Message to {}\nThey must have airplane mode on'


class AddressBook:
    def __init__(self):
        self.contacts = []
        self.groups = {}
    

    def _add_to_group(self, title: str, person: Contact):
        #check if title exist, if not create it
        # add user to group
        self.groups[title] = self.groups[title].append(person)


    def _add_contact(self, person: Contact):
        self.contacts.append(person)
        print('{} has been added Successfully!'.format(person.full_name))

    def __str__(self):
        print('-------------- Address Book --------------')
        return [str(x) for x in self.contacts].join(",")




if __name__ == '__main__':
    


