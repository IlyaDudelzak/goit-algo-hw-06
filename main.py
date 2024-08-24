from collections import UserDict

class Field:
    def __init__(self, value: str):
        self.value = value

    def __str__(self):
        return str(self.value)
    
    def edit(self, value:str):
         self.__init__(value)

class Name(Field):
    # реалізація класу
		pass

class Phone(Field):
    def __init__(self, value: str):
        if(len(value) != 10 or not value.isnumeric()):
            raise ValueError("Wrong phone format!")
        super().__init__(value)

class Record:
    def __init__(self, name: str):
        self.name = Name(name)
        self.phones = []

    def find_phone(self, phone):
         for i in self.phones:
              if(i.value == phone):
                   return Phone(phone)

         return None

    def has_phone(self, phone):
         for i in self.phones:
              if(i.value == i):
                   return True
         return False

    def add_phone(self, phone: str):
         if(self.has_phone(phone)):
              raise ValueError("Phone already registried")
         self.phones.append(Phone(phone))

    def remove_phone(self, phone: str):
         self.phones.remove(Phone(phone))

    def edit_phone(self, phone1, phone2):
         Phone(phone1)
         Phone(phone2)
         for i, phone in enumerate(self.phones):
              if(phone.value == phone1):
                   self.phones[i].edit(phone2)

    def __str__(self):
        return f"Contact name: {self.name.value}, phones: {'; '.join(p.value for p in self.phones)}"

class AddressBook(UserDict):
    def add_record(self, record: Record):
         if(not record.name.value in self.data):
            self.data[record.name.value] = record
         else:
            raise ValueError("Record already registried")

    def find(self, name):
         if(name in self.data):
              return self.data[name]
         else:
              return None      

    def delete(self, name):
         if(name in self.data):
              del self.data[name]    
         else:
              raise ValueError(f"Record({name}) not registried")   

    def __str__(self) -> str:
         string = "AdressBook:"
         for i in self.data:
              string += "\n"
              string += str(self.data[i])      
         return string                        

# Створення нової адресної книги
book = AddressBook()

# Створення запису для John
john_record = Record("John")
john_record.add_phone("1234567890")
john_record.add_phone("5555555555")
     
# Додавання запису John до адресної книги
book.add_record(john_record)

# Створення та додавання нового запису для Jane
jane_record = Record("Jane")
jane_record.add_phone("9876543210")
book.add_record(jane_record)

# Виведення всіх записів у книзі
    
print(book)

# Знаходження та редагування телефону для John
john = book.find("John")
john.edit_phone("1234567890", "1112223333")

print(john)  # Виведення: Contact name: John, phones: 1112223333; 5555555555

# Пошук конкретного телефону у записі John
found_phone = john.find_phone("5555555555")
print(f"{john.name}: {found_phone}")  # Виведення: John: 5555555555

# Видалення запису Jane
book.delete("Jane")