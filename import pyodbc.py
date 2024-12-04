
import pyodbc

connection = pyodbc.connect(
    "Driver={ODBC Driver 17 for SQL Server};"
    "Server=VIVOBOOK\SQLEXPRESS;"
    "Database=Test14;"
    "Trusted_Connection=yes;"
)

cursor = connection.cursor()
print("SQL is connected")

create_table_query = """CREATE TABLE Products (ProductID INT PRIMARY KEY IDENTITY(1,1), Name NVARCHAR(50) NOT NULL,Price DECIMAL(20,2)  NOT NULL,Stock INT NOT NULL);"""
#cursor.execute(create_table_query)#execute() metodu, SQL komutlarını çalıştırarak belirtilen sorguyu veritabanına iletir.SQL komutunu çalıştırır, ancak henüz kalıcı hale getirmez.
#connection.commit()#commit() komutu, yapılan işlemi veritabanına kalıcı olarak uygular.Yapılan değişikliği kaydeder ve veritabanına uygular, böylece tablo oluşturulur ve işlemler kalıcı hale gelir.
print("Product table is made")

insert_query="INSERT INTO Products(Name,Price,Stock) VALUES(?,?,?)"
cursor.execute(insert_query,("Sibel",1500.99,10))
connection.commit()
print("Data is added")

update_query="UPDATE Products SET Stock=? WHERE Name=?"
cursor.execute(update_query,(50,"Sibel"))
connection.commit()
print("Info is updated")

delete_query="DELETE FROM Products  WHERE Name=?"
cursor.execute(delete_query,("Sibel"))
connection.commit()
print("Name  called Sibel is deleted from table")

alter_table_query="ALTER TABLE Products ADD DESCRIPTION NVARCHAR(100)"#Products tablosunda bir değişiklik yapacağınızı belirtir
#Bu ifade, tablonuza yeni bir DESCRIPTION sütunu ekler ve her satırda bu sütun için 100 karaktere kadar veri saklanabilir.
#cursor.execute(alter_table_query)
#connection.commit()
print("New coloumn is added")

drop_table_query="DROP TABLE IF EXISTS Products"
cursor.execute(drop_table_query)
connection.commit()
print("Product table is deleted")



                