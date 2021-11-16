import os
from db.db import connect, db_name

def init_db():
    db_path  = os.path.dirname(os.path.abspath(__file__))

    if(not os.path.isfile(db_path + "/" + db_name)):

        conn = connect()
        c = conn.cursor()

        for filename in os.listdir(db_path + "/sql/"):
            file = open(db_path + "/sql/" + filename)
            sqlFile = file.read()
            file.close()
            sqlCommands = sqlFile.split(';')
            for sql in sqlCommands:
                c.execute(sql)
            conn.commit()
