
import pyfirmata
import time
import mysql.connector

pin = 13
port = 'COM3'
board = pyfirmata.Arduino(port)

dataBase = mysql.connector.connect(host = "localhost",user = "root",passwd = "",database = "arduino")
registro = dataBase.cursor()
query = "SELECT piscar FROM led"
registro.execute(query)
 
resultado = registro.fetchall()

for x in resultado:
    piscar = x[0]

dataBase.close()
print("Piscando " + piscar + " vezes.")
 
for x in range(int(piscar)):
  board.digital[13].write(1)
  time.sleep(1)
  board.digital[13].write(0)
  time.sleep(1)
