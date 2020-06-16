#functions for adding deleting,updating ,editing , searching and finding 

def add(db, name, number,email_address,city):
    cond = find(db, name,email_address,city)
    if cond == True:
        return False
    else:
        cur = db.cursor()
        cur.execute('insert into contacts values(?,?,?,?)', (name, number,email_address,city))
        return True
    pass


def update(db, name, number,email_address,city):
    if find(db, name,email_address,city) != True:
        return False
    else:
        cur = db.cursor()
        cur.execute('update contacts set name=? where number=? and email_address=? city=?', (name, number,email_address,city))
        return True
    pass


def delete(db, name,email_adress,city):
    if find(db, name,email_adress,city) != True:
        return False
    else:
        cur = db.cursor()
        cur.execute('delete from contacts where name=?', (name,))
        return True
    pass

    pass


def view(db):
    cur = db.cursor()
    cur.execute('select name,number,email_address,city from contacts')
    cts = cur.fetchall()
    print(cts)
    return cts
    pass



#def search(db,number):
    #cur = db.cursor()
    #cur.execute('select * from contacts where name=? and number=?',(name,number))
    #cts = cur.fetchall()
    #for contact in cts:
   #     name1, number = contact
  #      if name == name1:
 #           return True
#pass


def find(db, name, email_address, city):
    cur = db.cursor()
    cur.execute('select * from contacts')
    cts = cur.fetchall()
    for contact in cts:
        name1 ,number ,email_address,city = contact
        if name == name1:
            return number,email_address,city
