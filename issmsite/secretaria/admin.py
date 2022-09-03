from django.contrib import admin

# Register your models here.
from secretaria.models import Carrera, Materia, EstadoCivil, Mesa, Docente, MesaDetalle, Tribunal, Concepto, Alumno, \
    Recibo, Recibor, Empleado, Cargo, Persona


class CarreraAdmin(admin.ModelAdmin):
    list_display = ('id', 'abreviatura', 'nombre', 'tipo')
    list_filter = ('tipo', 'duracion')


class MateriaAdmin(admin.ModelAdmin):
    list_display = ('id', 'nombre', 'anio', 'cuatrimestre', 'carrera_id')
    list_filter = ('carrera_id', 'anio', 'cuatrimestre')


class EstadoCivilAdmin(admin.ModelAdmin):
    list_display = ('id', 'nombre')


class DocenteAdmin(admin.ModelAdmin):
    list_display = ('id', 'persona', 'foto')


class MesaAdmin(admin.ModelAdmin):
    list_display = ('id', 'nombre', 'inicia', 'cierra', 'llamados', 'carreras')
    list_filter = ('inicia', 'carreras')
    readonly_fields = ('created', 'updated')


class TribunalInstanceInline(admin.TabularInline):
    model = Tribunal


class MesaDetalleAdmin(admin.ModelAdmin):
    list_display = ('id', 'mesas', 'materias', 'fecha1', 'fecha2', 'hora')
    list_filter = ('fecha1', 'mesas')
    inlines = [TribunalInstanceInline]


class AlumnoAdmin(admin.ModelAdmin):
    list_display = ('id', 'alumno', 'foto', 'ingreso')
    list_filter = ('ingreso', 'baja')


class ConceptoAdmin(admin.ModelAdmin):
    list_display = ('id', 'nombre', 'importe', 'descuento', 'created', 'updated')
    list_filter = ('descuento', 'created')
    readonly_fields = ('created', 'updated')


class ReciboDetalleInline(admin.TabularInline):
    model = Recibor


class ReciboAdmin(admin.ModelAdmin):
    list_display = ('id', 'fecha', 'importe', 'descuento', 'neto', 'alumno', 'carrera', 'empleado')
    list_filter = ('carrera', 'fecha', 'empleado')
    readonly_fields = ('created', 'updated')
    inlines = [ReciboDetalleInline]


class ReciborAdmin(admin.ModelAdmin):
    list_display = ('id', 'recibo', 'anio', 'importe', 'concepto')


class EmpleadoAdmin(admin.ModelAdmin):
    list_display = ('id', 'persona', 'display_cargo', 'foto')


class CargoAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'id')


class PersonaAdmin(admin.ModelAdmin):
    list_display = ('id', 'dni', 'apellido', 'nombre', 'fechanac', 'genero', 'email', 'vive')
    list_filter = ('vive', 'fechanac', 'genero', 'created')
    readonly_fields = ('updated', 'id')


admin.site.register(Cargo, CargoAdmin)
admin.site.register(Persona, PersonaAdmin)
admin.site.register(Empleado, EmpleadoAdmin)
admin.site.register(EstadoCivil, EstadoCivilAdmin)
admin.site.register(Docente, DocenteAdmin)
admin.site.register(Carrera, CarreraAdmin)
admin.site.register(Materia, MateriaAdmin)
admin.site.register(Mesa, MesaAdmin)
admin.site.register(MesaDetalle, MesaDetalleAdmin)
admin.site.register(Alumno, AlumnoAdmin)
admin.site.register(Concepto, ConceptoAdmin)
admin.site.register(Recibo, ReciboAdmin)

