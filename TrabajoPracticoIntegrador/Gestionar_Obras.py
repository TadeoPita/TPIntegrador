from abc import ABC
import pandas as pd
from peewee import *
import sqlite3
from modelo_orm import *

class GestionarObra(ABC):
    nombre_archivo = "datos.csv"
    df = None
    conexion = None
    
    @classmethod
    def extraer_datos(cls):
        try:
            cls.df = pd.read_csv(cls.nombre_archivo)
            return cls.df
        except FileNotFoundError as e:
            print(f"Error: El archivo no se encontro. {e}")
            return None
        except pd.errors.EmptyDataError as e:
            print(f"Error: El archivo esta vacio. {e}")
            return None


    @classmethod
    def conectar_db(cls):
        try:
            cls.conexion = sqlite3.connect("obras_urbanas.db")
            print("Base de datos abierta")
            return cls.conexion
        except sqlite3.DatabaseError as e:
            print(f"Error al conectar a la base de datos: {e}")
            return None

    @classmethod    
    def mapear_orm(cls):  
     try:
        sqlite_db.create_tables([ObrasPublicas,EntornoF,EtapaF,ObrasF,AreaResponsableF,ComunaF,BarrioF,CompromisoF,DestacadaF] )
        print("Se mapearon las tablas y las columnas")
        return sqlite_db
     except sqlite3.DataError as e:
         print(f"Error al conectar la base de datos: {e}")
         return None
         
        
    @classmethod
    def limpiar_datos(cls, nombre_archivo_salida=None):
        # if cls.df is not None:
        #     cls.df = cls.df.dropna(subset=["entorno","nombre","etapa","tipo","area_responsable","comuna", "barrio","fecha_inicio","monto_contrato","licitacion_anio", "contratacion_tipo", "mano_obra", "porcentaje_avance","plazo_meses"], axis=0 , inplace=True)
        # else:
        #  print("Error: No se han cargado datos para limpiar.")
        
        
        ### El codigo de arriba es el que va pero este es para probar que datos nos conviene eliminar ###
        if cls.df is not None:
         df_limpio = cls.df.dropna(subset=["entorno", "nombre", "etapa", "tipo", "area_responsable", "comuna", "barrio", "fecha_inicio", "monto_contrato", "licitacion_anio", "contratacion_tipo", "mano_obra", "porcentaje_avance", "plazo_meses"])
        
         if nombre_archivo_salida is None:
            nombre_archivo_salida = "datos_limpios.csv"

        # Guardar el DataFrame limpio en un nuevo archivo CSV
         df_limpio.to_csv(nombre_archivo_salida, index=False)
        
         print(f"Datos limpios correctamente y guardados en {nombre_archivo_salida}.")
        
        else: print("error")
        
        
    @classmethod
    def cargar_datos(cls):
        pass

    @classmethod
    def nueva_obra(cls):
        pass
    @classmethod
    def obtener_indicadores(cls):
        pass


# Ejemplo de uso
gestor_obra = GestionarObra()
datos_extraidos = gestor_obra.extraer_datos()
conectarBD= gestor_obra.conectar_db()
mapear = gestor_obra.mapear_orm()
limpiar_datos = gestor_obra.limpiar_datos(nombre_archivo_salida="mi_archivo_limpio.csv")

