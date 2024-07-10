import psycopg2

connection = psycopg2.connect(database="chinook")

cursor = connection.cursor() 

#query1
#cursor.execute('SELECT * FROM "Artist"')

#query2
#cursor.execute('SELECT "Name" FROM "Artist')

#query3
#cursor.execute('SELECT * FROM "Artist" WHERE "Name" = %s', ["Queen"])

#query4
#cursor.execute('SELECT * FROM "Artist" WHERE "ArtistID" = %s', [51])

#fetch results
results = cursor.fetchall()

connection.close()

for result in results:
    print(result)

