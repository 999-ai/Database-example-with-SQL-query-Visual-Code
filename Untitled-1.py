import pyodbc

# Veritabanı bağlantısı
connection = pyodbc.connect(
    "Driver={ODBC Driver 17 for SQL Server};"
    "Server=VIVOBOOK\SQLEXPRESS;"
    "Database=TEST3;"
    "Trusted_Connection=yes;"
)
cursor = connection.cursor()
print("SQL is connected")

create_table_query = """CREATE TABLE Students (
    StudentID INT PRIMARY KEY IDENTITY(1,1),
    Name NVARCHAR(50) NOT NULL,
    Age INT NOT NULL,
    Grade INT NOT NULL
);"""
#cursor.execute(create_table_query)
#connection.commit()
print("Students table is made")

# Veri ekleme sorgusu
insert_query = """INSERT INTO Students(Name, Age, Grade) VALUES
('Ali', 25, 5),
('Ahmet', 22, 6),
('Aslı', 54, 2);"""
#cursor.execute(insert_query)
#connection.commit()
print("Data is added")

# Tüm veriyi görüntüleme (isteğe bağlı)
alldata_in_studentstable = "SELECT * FROM Students"
cursor.execute(alldata_in_studentstable)
rows = cursor.fetchall()#Her bir satır, bir tuple olarak döndürülür ve bu tuple'da tablodaki sütunlar arasındaki veriler bulunur.
for row in rows:
    print(row)
print("All data is here from Students table")

# Veri güncelleme
update_query = "UPDATE Students SET Age = 98 WHERE Name = 'Ali';"
#cursor.execute(update_query)
#connection.commit()
print("Data is updated")

delete_query="DELETE FROM Students wHERE Name='Ali'; "
#cursor.execute(delete_query)
#connection.commit()
print("Name of Ali  is deleted from Student Table")


alter_table_query="ALTER TABLE Students ADD ADRESS TEXT"
#cursor.execute(alter_table_query)
#connection.commit()
print("Adress table is added")

determine_class_query="SELECT *FROM STUDENTS WHERE GRADE=6"
#cursor.execute(determine_class_query)
#connection.commit()
print("Person who get 6 grade is determined")

drop_Students_table="DROP TABLE IF EXISTS Students"
cursor.execute(drop_Students_table)
connection.commit()
print("Students table is deleted")
