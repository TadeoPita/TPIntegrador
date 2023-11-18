from peewee import *
# from gestionar_obras import *

sqlite_db = SqliteDatabase('obras_urbanas.db', pragmas={'journal_mode': 'wal'})


class BaseModel(Model):
    class Meta:
        database = sqlite_db


class EntornoF(BaseModel):
    id = PrimaryKeyField()
    nombreEntorno = CharField(unique=True)
    def __str__(self):
        return self.nombreEntorno
    class Meta:
        db_table = "EntornoF"


class EtapaF(BaseModel):
    id = PrimaryKeyField()
    nombreEtapa = CharField(unique=True)
    def __str__(self):
        return self.nombreEtapa
    class Meta:
        db_table = "EtapaF"


class ObrasF(BaseModel):
    id = PrimaryKeyField()
    nombreDeObra = CharField(unique=True)
    def __str__(self):
        return self.nombreDeObra
    class Meta:
        db_table = "ObrasF"


class AreaResponsableF(BaseModel):
    id = PrimaryKeyField()
    nombreAreaR = CharField(unique=True)
    def __str__(self):
        return self.nombreAreaR
    class Meta:
        db_table = "AreaResponsableF"


class ComunaF(BaseModel):
    id = PrimaryKeyField()
    nombreComuna = CharField(unique=True)
    def __str__(self):
        return self.nombreComuna
    class Meta:
        db_table = "ComunaF"


class BarrioF(BaseModel):
    id = PrimaryKeyField()
    nombreBarrio = CharField(unique=True)
    def __str__(self):
        return self.nombreBarrio
    class Meta:
        db_table = "BarrioF"


class CompromisoF(BaseModel):
    id = PrimaryKeyField()
    nombreCompromiso = CharField(unique=True)
    def __str__(self):
        return self.nombreCompromiso
    class Meta:
        db_table = "CompromisoF"


class DestacadaF(BaseModel):
    id = PrimaryKeyField()
    nombreDestacada = CharField(unique=True)
    def __str__(self):
        return self.nombreDestacada
    class Meta:
        db_table = "DestacadaF"


class ObrasPublicas(BaseModel):
    ID = PrimaryKeyField()
    entorno = ForeignKeyField(EntornoF, backref="entornos")
    nombre = CharField(max_length=80)
    etapa = ForeignKeyField(EtapaF, backref="etapas")
    Obras = ForeignKeyField(ObrasF, backref="nombreDeObra")
    area_responsable = ForeignKeyField(AreaResponsableF, backref="areaResponsables")
    descripcion = CharField(max_length=255)
    monto_contrato = IntegerField()
    comuna = ForeignKeyField(ComunaF, backref="comunas")
    barrio = ForeignKeyField(BarrioF, backref="barrios")
    direccion = CharField(max_length=80)
    lat = CharField(max_length=20)
    lng = CharField(max_length=20)
    fecha_inicio = DateField()
    fecha_fin_inicial = DateField()
    plazo_meses = FloatField()
    porcentaje_avance = FloatField()
    imagen_1 = CharField(max_length=80)
    imagen_2 = CharField(max_length=80)
    imagen_3 = CharField(max_length=80)
    imagen_4 = CharField(max_length=80)
    licitacion_oferta_empresa = CharField(max_length=60)
    licitacion_anio = IntegerField()
    contratacion_tipo = CharField(max_length=60)
    nro_contratacion = CharField(max_length=60)
    cuit_contratista = IntegerField()
    beneficiarios = CharField(max_length=60)
    mano_obra = CharField(max_length=40)
    compromiso = ForeignKeyField(CompromisoF, backref="compromisos")
    destacada = ForeignKeyField(DestacadaF, backref="destacadas")
    ba_elige = CharField(max_length=3)
    link_interno = CharField(max_length=80)
    pliego_descarga = CharField(max_length=80)
    expediente_numero = CharField(max_length=80)
    estudio_ambiental_descarga = CharField(max_length=80)
    financiamiento = CharField(max_length=20)
    def __str__(self):
        pass
    class meta:
        db_table = 'DatosObra'