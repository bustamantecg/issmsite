from ckeditor.fields import RichTextField
from django.db import models
from django.contrib.auth.models import User
from django.core.validators import MaxValueValidator, MinValueValidator


class Empresa(models.Model):
    nombre = models.CharField(max_length=100)
    domicilio = models.CharField(max_length=100)
    telefono = models.CharField(max_length=100, verbose_name='Teléfono')
    email = models.EmailField(max_length=200)
    mision = RichTextField()
    vision = RichTextField()
    facebook = models.CharField(max_length=254, null=True, blank=True)
    instagram = models.CharField(max_length=254, null=True, blank=True)
    twitter = models.CharField(max_length=254, null=True, blank=True)

    def __str__(self):
        return f'{self.id} {self.nombre}'


class MotivoBaja(models.Model):
    nombre = models.CharField(max_length=40, unique=True, verbose_name='Motivo de Baja')

    def __str__(self):
        return f'{self.nombre}'

    class Meta:
        verbose_name = 'Motivo de Baja'


class EstadoCivil(models.Model):
    nombre = models.CharField(max_length=20)

    def __str__(self):
        return f'{self.id} {self.nombre}'

    class Meta:
        verbose_name = 'Estado Civil'
        verbose_name_plural = 'Estado Civiles'
        ordering = ['nombre']


class Cargo(models.Model):
    nombre = models.CharField(max_length=30, unique=True, verbose_name='Nombre del Cargo')

    def __str__(self):
        return f'{self.nombre}'

    class Meta:
        verbose_name = 'Cargo'
        verbose_name_plural = 'Cargos'


class Persona(models.Model):
    dni = models.CharField(max_length=8, verbose_name='D.N.I.', unique=True)
    apellido = models.CharField(max_length=40)
    nombre = models.CharField(max_length=40)
    fechanac = models.DateField(verbose_name='Fecha de Nacimiento')
    GENERO = [
        ('Femenino', 'Femenino'),
        ('Masculino', 'Masculino'),
        ('Otro', 'Otro'),
    ]
    genero = models.CharField(max_length=9, choices=GENERO, default='Otro')
    estado_civil = models.ForeignKey(EstadoCivil, on_delete=models.SET_NULL, null=True, blank=True)
    email = models.EmailField(max_length=254)
    domicilio = models.CharField(max_length=150)
    vive = models.BooleanField(default=True)
    baja = models.DateField(null=True, blank=True)
    motivo_baja = models.ForeignKey(MotivoBaja, on_delete=models.SET_NULL, null=True, blank=True)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = 'Persona'
        verbose_name_plural = 'Personas'

    def __str__(self):
        return f'{self.dni} - {self.apellido}, {self.nombre}'


class Carrera(models.Model):
    nombre = models.CharField(max_length=100, verbose_name='Carrera')
    abreviatura = models.CharField(max_length=4, unique=True)
    legal = models.CharField(max_length=100, verbose_name='Resolución Oficial')
    fecha_inicio = models.DateField()
    duracion = models.IntegerField(verbose_name='Año Duración', default=3,
                                   validators=[MinValueValidator(1), MaxValueValidator(6)])
    cuatrimestre = models.IntegerField(default=1, verbose_name='Cantidad de Cuatrimestres')
    TIPOCARRERA = [
        ('Tecnicatura', 'Tecnicatura'),
        ('Profesorado', 'Profesorado'),
        ('Licenciatura', 'Licenciatura'),
        ('PostGrado', 'PostGrado'),
        ('Curso', 'Curso'),
        ('Seminario', 'Seminario'),
        ('Otro', 'Otro'),
    ]
    tipo = models.CharField(max_length=15, choices=TIPOCARRERA, default='Tec')

    def __str__(self):
        return f'{self.nombre}'


class Materia(models.Model):
    carrera_id = models.ForeignKey(Carrera, on_delete=models.SET_NULL, null=True, blank=True, verbose_name='Carrera')
    nombre = models.CharField(max_length=120, verbose_name='Nombre de Materia')
    TIPOMATERIA = [
        ('A', 'Anual'),
        ('C', 'Cuatrimestral'),
        ('O', 'Otra'),
    ]
    tipo = models.CharField(max_length=1, choices=TIPOMATERIA, default='C', blank=False, null=False)
    ANIO = [
        ('1', '1 Año'),
        ('2', '2 Año'),
        ('3', '3 Año'),
        ('4', '4 Año'),
        ('5', '5 Año'),
        ('6', '6 Año'),
    ]
    anio = models.CharField(max_length=2, choices=ANIO, verbose_name='Año', default='1', blank=False, null=False)
    CUATRIMESTRE = [
        ('1', '1 Cuat.'),
        ('2', '2 Cuat.'),
        ('3', '3 Cuat.'),
        ('4', '4 Cuat.'),
        ('5', '5 Cuat.'),
        ('6', '6 Cuat.'),
        ('7', '7 Cuat.'),
        ('8', '8 Cuat.'),
    ]
    cuatrimestre = models.CharField(max_length=2, choices=CUATRIMESTRE, default='1', blank=False, null=False)

    def __str__(self):
        return f'{self.nombre}'


class Mesa(models.Model):
    nombre = models.CharField(max_length=60)
    habilitada = models.BooleanField(default=False)
    inicia = models.DateField()
    cierra = models.DateField()
    carreras = models.ForeignKey(Carrera, on_delete=models.SET_NULL, null=True, blank=True)
    choices = LLAMADOS = [
        ('Uno', 'Uno'),
        ('Dos', 'Dos'),
        ('Tres', 'Tres'),
    ]
    llamados = models.CharField(max_length=4, verbose_name='Cantidad de llamados', choices=LLAMADOS, default='Dos')
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.nombre}'

    class Meta:
        verbose_name = 'Mesa'
        verbose_name_plural = 'Mesas'
        ordering = ['nombre']


class Docente(models.Model):
    persona = models.ForeignKey(Persona, on_delete=models.SET_NULL, null=True, blank=True)
    legajo = models.CharField(max_length=50)
    titulo = models.CharField(max_length=80, null=True, blank=True)
    horas_catedras = models.CharField(max_length=100)
    carreras = models.ManyToManyField(Carrera)
    legajo = RichTextField(help_text='Puede describir Altas, Bajas, Titulos, ect.')
    foto = models.ImageField(upload_to='docente', verbose_name='Foto 4x4', null=True, blank=True)

    def __str__(self):
        return f'{self.persona}'

    class Meta:
        verbose_name = 'Docente'
        verbose_name_plural = 'Docentes'
        ordering = ['persona']


class MesaDetalle(models.Model):
    mesas = models.ForeignKey(Mesa, on_delete=models.CASCADE)
    materias = models.ForeignKey(Materia, on_delete=models.CASCADE)
    fecha1 = models.DateField()
    fecha2 = models.DateField(null=True, blank=True)
    hora = models.TimeField()
    # tribunales = models.ManyToManyField(Docente, models.SET_NULL, null=True, blank=True)

    def __str__(self):
        return f'detalle_id:({self.id}) {self.materias}'

    class Meta:
        verbose_name = 'Mesa Detalle'
        ordering = ['fecha1', 'materias']


class Tribunal(models.Model):
    mesadetalles = models.ForeignKey(MesaDetalle, models.SET_NULL, null=True, blank=True)
    docente = models.ForeignKey(Docente, models.SET_NULL, null=True, blank=True)
    AUTORIDAD = [
        ('Titular', 'Titular'),
        ('Vocal 1', 'Vocal 1'),
        ('Vocal 2', 'Vocal 2'),
        ('Suplente', 'Suplente'),
    ]
    autoridad = models.CharField(max_length=8, choices=AUTORIDAD, default='Vocal 1')

    def __str__(self):
        return f'{self.autoridad} {self.docente}'

    class Meta:
        verbose_name = 'Tribunal'
        verbose_name_plural = 'Tribunales'
        ordering = ['mesadetalles']


class Concepto(models.Model):
    nombre = models.CharField(max_length=100, help_text='Ejemplo: Cuota Enero')
    importe = models.DecimalField(max_digits=9, decimal_places=2)
    descuento = models.BooleanField(default=False, help_text='Es un descuento [Si - No]')
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = 'Concepto'
        verbose_name_plural = 'Conceptos'

    def __str__(self):
        return f'{self.nombre}'


class Alumno(models.Model):
    carrera = models.ForeignKey(Carrera, on_delete=models.SET_NULL, null=True, blank=True)
    persona = models.ForeignKey(Persona, on_delete=models.SET_NULL, null=True, blank=True)
    ingreso = models.DateField()
    foto = models.ImageField(upload_to='alumno', verbose_name='Foto 4x4', null=True, blank=True)
    legajo = RichTextField(help_text='Puede describir Altas, Bajas, Documentación, ect.')
    user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True)
    baja = models.DateField(null=True, blank=True)
    motivo_baja = models.ForeignKey(MotivoBaja, on_delete=models.SET_NULL, null=True, blank=True)

    def __str__(self):
        return f' Matricula: {self.id} {self.persona} {self.carrera}'

    class Meta:
        verbose_name = 'Alumno'
        verbose_name_plural = 'Alumnos'


class Empleado(models.Model):
    persona = models.ForeignKey(Persona, on_delete=models.SET_NULL, null=True, blank=True)
    cargo = models.ManyToManyField(Cargo)
    horario = models.CharField(max_length=200)
    carga_horaria = models.CharField(max_length=100)
    legajo = RichTextField(help_text='Puede describir Altas, Bajas, Titulos, ect.')
    foto = models.ImageField(upload_to='secretaria', verbose_name='Foto 4x4', null=True, blank=True)

    def __str__(self):
        return f'{self.persona}'

    def display_cargo(self):
        return ', '.join([cargo.nombre for cargo in self.cargo.all()[:3]])

    display_cargo.short_description = 'Cargo'

    class Meta:
        verbose_name = 'Empleado'
        verbose_name_plural = 'Empleados'


class Recibo(models.Model):
    alumno = models.ForeignKey(Alumno, on_delete=models.SET_NULL, null=True, blank=True)
    carrera = models.ForeignKey(Carrera, on_delete=models.SET_NULL, null=True, blank=True)
    fecha = models.DateTimeField()
    importe = models.DecimalField(max_digits=8, decimal_places=2)
    descuento = models.DecimalField(max_digits=8, decimal_places=2)
    neto = models.DecimalField(max_digits=8, decimal_places=2)
    empleado = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True)
    rendido = models.DateField(null=True, blank=True)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'Recibo {self.id}: {self.alumno}'

    class Meta:
        verbose_name = 'Recibo'
        verbose_name_plural = 'Recibos'
        ordering = ['id']


class Recibor(models.Model):
    recibo = models.ForeignKey(Recibo, on_delete=models.CASCADE)
    ANIO = [
        ('1', '1 Año'),
        ('2', '2 Año'),
        ('3', '3 Año'),
        ('4', '4 Año'),
        ('5', '5 Año'),
        ('6', '6 Año'),
    ]
    anio = models.CharField(max_length=5, choices=ANIO, verbose_name='Año Cursado', default='1 Año', blank=False, null=False)
    concepto = models.ForeignKey(Concepto, on_delete=models.SET_NULL, null=True, blank=True)
    MES = [
        ('Enero', 'Enero'),
        ('Marzo', 'Marzo'),
        ('Abril', 'Abril'),
        ('Mayo', 'Mayo'),
        ('Junio', 'Junio'),
        ('Julio', 'Julio'),
        ('Agosto', 'Agosto'),
        ('Septiembre', 'Septiembre'),
        ('Octubre', 'Octubre'),
        ('Noviembre', 'Noviembre'),
        ('Diciembre', 'Diciembre'),
    ]
    mes = models.CharField(max_length=10, choices=MES, verbose_name='Mes', default='Junio', blank=False, null=False)
    importe = models.DecimalField(max_digits=8, decimal_places=2)

    class Meta:
        verbose_name = 'Recibo Detalle'
        verbose_name_plural = 'Recibos Detalles'


