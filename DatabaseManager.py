import pyodbc
class DatabaseManager:
    def __init__(self, server, port, database, username, password):
        self.server = server
        self.database = database
        self.username = username
        self.port = port
        self.password = password
        self.conn = None
    
    def connect(self):
        try:
            self.conn = pyodbc.connect('DRIVER=FreeTDS;Server={};PORT={};DATABASE={};UID={};PWD={};TDS_Version=7.2;'.format(self.server,self.port,self.database,self.username,self.password,self.password))
            print('Connessione avvenuta con successo')
        except Exception as e:
            print(e)
            print("Error: Impossibile connettersi al database")
            self.close()
            return False

    def testConnection(self):
        try:
            list = self.select("SELECT * FROM AE_Paese")
            #first element of list
            print(list[0])
            print('Connection successful')
            return True
        except Exception as e:
            print(e)
            print("Error: Unable to connect to database")
            self.close()
            return False
    
    def select(self, query,parameters=[]):
        try:
            cursor = self.conn.cursor()
            cursor.execute(query,parameters)
            return cursor.fetchall()
        except Exception as e:
            print(e)
            self.close()
            raise Exception("Errore: Impossibile recuperare i dati")

    def updateInsert(self, query,parameters=[]):
        try:
            cursor = self.conn.cursor()
            cursor.execute(query,parameters)
            self.conn.commit()
            return True
        except Exception as e:
            print(e)
            print("Errore: Impossibile inserire o aggiornare i dati")
            self.close()
            return False

    def close(self):
        self.conn.close()
        print('Connesione al database chiusa')
        return True