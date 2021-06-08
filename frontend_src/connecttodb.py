import pyodbc
# Some other example server values are
# server = 'localhost\sqlexpress' # for a named instance
# server = 'myserver,port' # to specify an alternate port
server = 'seattleart.cjhbuvf3dom6.us-west-2.rds.amazonaws.com,1433'
database = 'SeattleArt'
username = ''
password = ''
with open('pw.txt','r') as pw:
    lines = pw.readlines()
    username = lines[0].strip()
    password = lines[1].strip()
cnxn = pyodbc.connect('DRIVER={ODBC Driver 17 for SQL Server};SERVER='+server+';DATABASE='+database+';UID='+username+';PWD='+ password)
cursor = cnxn.cursor()

if __name__ == "__main__":
    #Sample select query
    cursor.execute("select 'hello'")
    row = cursor.fetchone()
    while row:
        print(row[0])
        row = cursor.fetchone()

    cnxn.commit()
