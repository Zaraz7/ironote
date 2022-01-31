from DB_controller import *

import json

k = """ """

list_ = []

path = './DB_PASS.sqlite'
connect = create_connection(path)
listQueryDB = execute_read_query(connect, "SELECT id, site, login, pass from main")

for i in listQueryDB:
    list_.append( 
        {
        "{}".format(i[0]) : {
                "site" : i[1],
                "login" : i[2],
                "pass" : i[3]
            }
        }
    )

obj0 = {'0' : 'Null'}

obj0 = {obj0, {'1': 'One'}}

print(obj0)