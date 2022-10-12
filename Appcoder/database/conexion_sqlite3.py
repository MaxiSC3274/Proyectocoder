from logging import exception
import sqlite3
try:
    mi_conexion= sqlite3.connect("Appcoder_cursomodel.sqlite3")
    #cursor=mi_conexion.cursor()
    #cursor.execute("CREATE TABLE Cursomodel (nombre VARCHAR(50)")
except Exception as ex:
    print(ex)    
    