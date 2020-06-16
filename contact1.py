import sqlite3

db = sqlite3.connect('contacts.db')
from contacts import *

cmd = ''
print('contact app:')
print('operation is : ')
while cmd != 'exit':
    cmd = input('>>> ')
    tokens = cmd.split()
    cmd = tokens[0]
    if cmd == 'add':
        name = input('enter contact name: ')
        number= input('enter contact number : ')
        email_address=input('enter emailID')
        city= input('enter city')
        if add(db,name,number,email_address,city)==True:
            print('contact added')
        else:
            print('contact is available ')

    elif cmd == 'view':
        cts=view(db)
        for contact in cts:
            name, number,email_address,city = contact
            print(name, ':', number, ':',email_address,':',city)

    elif cmd == 'delete':
        name = input('enter contact name: ')
        if delete(db,name,email_address,city)==True:
            print('contact deleted')
        else:
            print('contact is not available ')
    elif cmd == 'edit':
        name = input('enter contact name: ')
        number=input('enter contact number :')
        email_address=input('enter the new emailID')
        city = input('enter the city')
        if update(db,name,email_address,city)==True:
            print('contact updated ')
        else:
            print('contact is not available')

    elif cmd == 'find':
        contact = (input('enter the contact'))
        if find(db,name,email_address,city)!=True:
            print(find(db,name,email_address,city))
        else:
            print('Invalid')
    elif cmd != 'exit':
        #print('contact app closed')
        print('option is not avilable ')
