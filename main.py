# Importaciones
from fastapi import FastAPI # Framework fastapi
from pydantic import BaseModel # Entidad que define usuarios

app = FastAPI() # Instancia de la aplicacion

# Definicion de la entidad usuario
class Usuario(BaseModel):
    id: int
    nombreCompleto: str
    matricula: int
    edad: int
    carrera: str
    genero: str
    facultad: str
    correo: str
    semestre: int
    ciudadEstado: str
    lenguajeProgramacion: str
    especialidad: str
    nivelIngles: str
    estadoCivil: str

# Crear la lista de usuarios
lista_usuarios = [
    Usuario(id=1, nombreCompleto="Francisco Javier Alvarez Bonilla", matricula=202272044, edad=20, carrera="Ingeniería en Tecnologías de la Información", genero="Masculino", facultad="FCC", correo="francisco.alvarezb@alumno.buap.mx", semestre=7, ciudadEstado="Cd. Sahagún, Hidalgo", lenguajeProgramacion="Python", especialidad="Python", nivelIngles="Avanzado", estadoCivil="Soltero"),
    Usuario(id=2, nombreCompleto="Andy Pérez Pavón", matricula=202247824, edad=21, carrera="Tecnologías de la Información", genero="Masculino", facultad="FCC", correo="andy.perezp@alumno.buap.mx", semestre=7, ciudadEstado="San Salvador el Verde, Puebla", lenguajeProgramacion="Python", especialidad="Administración de Redes", nivelIngles="Intermedio", estadoCivil="Soltero"),
    Usuario(id=3, nombreCompleto="Diego Alberto Nava Rivera", matricula=202234640, edad=20, carrera="Licenciatura en Ingeniería en Tecnologías de la Información", genero="Masculino", facultad="FCC", correo="diego.navar@alumno.buap.mx", semestre=7, ciudadEstado="Huauchinango, Puebla", lenguajeProgramacion="Python", especialidad="Mineria de datos", nivelIngles="Intermedio", estadoCivil="Soltero"),
    Usuario(id=4, nombreCompleto="Nelson Ricardo Sosa Francisco", matricula=202254416, edad=20, carrera="Ingeniería en Tecnologías de la Información", genero="Masculino", facultad="FCC", correo="nelson.sosa@alumno.buap.mx", semestre=7, ciudadEstado="Puebla, Puebla", lenguajeProgramacion="Python", especialidad="Desarrollo Web", nivelIngles="Intermedio", estadoCivil="Soltero"),
    Usuario(id=5, nombreCompleto="Aldo Palacios Medel", matricula=202276746, edad=22, carrera="Ingeniería en tecnologías de la información", genero="Masculino", facultad="FCC", correo="aldo.palaciosm@alumno.buap.mx", semestre=7, ciudadEstado="Puebla", lenguajeProgramacion="C++", especialidad="Desarrollo de videojuegos", nivelIngles="Básico", estadoCivil="Soltero"),
    Usuario(id=6, nombreCompleto="Miguel Angel Castillo Corona", matricula=202221447, edad=21, carrera="Ingeniería en Tecnologías de la Información", genero="Masculino", facultad="FCC", correo="miguel.castilloc@alumno.buap.mx", semestre=7, ciudadEstado="Puebla", lenguajeProgramacion="PHP", especialidad="Desarrollo web", nivelIngles="Intermedio", estadoCivil="Soltero"),
    Usuario(id=7, nombreCompleto="Iván Pérez Sánchez", matricula=202247984, edad=20, carrera="Ingeniería en Tecnologías de la Información", genero="Masculino", facultad="FCC", correo="ivan.perezsa@alumno.buap.mx", semestre=6, ciudadEstado="Puebla, Puebla", lenguajeProgramacion="Python", especialidad="Ciencia de Datos", nivelIngles="Avanzado", estadoCivil="Soltero"),
    Usuario(id=8, nombreCompleto="Nidia Sanchez Tequihuactle", matricula=202473196, edad=20, carrera="Administración pública y gestión para el Desarrollo", genero="Femenino", facultad="Administración", correo="st202473196@alm.buap.mx", semestre=3, ciudadEstado="Córdoba", lenguajeProgramacion="Ninguno", especialidad="Finanzas públicas", nivelIngles="Básico", estadoCivil="Unión libre"),
    Usuario(id=9, nombreCompleto="Jhoel Boset Hernández Hernández", matricula=202240624, edad=26, carrera="Ingeniería en Tecnologías de la Información", genero="Masculino", facultad="Facultad de Ciencias de la Computacion", correo="jhoel.hernandezhe@alumno.buap.mx", semestre=6, ciudadEstado="Zongozotla, Puebla", lenguajeProgramacion="Python", especialidad="Ciberseguridad", nivelIngles="Intermedio", estadoCivil="Soltero"),
    Usuario(id=10, nombreCompleto="Ingrid Arleth Rosas Díaz", matricula=202457501, edad=18, carrera="Lic. en Economía", genero="Femenino", facultad="Economía", correo="rd202457501@alm.buap.mx", semestre=3, ciudadEstado="Córdoba, Veracruz", lenguajeProgramacion="Python, Javascript,", especialidad="Python", nivelIngles="Intermedio", estadoCivil="Soltero"),
    Usuario(id=11, nombreCompleto="Alan de Jesús Valerdi Pérez", matricula=202269430, edad=20, carrera="Ingeniería en Tecnologías de la información", genero="Masculino", facultad="Ciencias de la computación", correo="alan.valerdip@alumno.buap.mx", semestre=7, ciudadEstado="Puebla", lenguajeProgramacion="Typescript", especialidad="Backend", nivelIngles="Avanzado", estadoCivil="Soltero"),
    Usuario(id=12, nombreCompleto="Sonia Ramirez Sanchez", matricula=202154004, edad=27, carrera="ICC", genero="Femenino", facultad="FCC", correo="sonia.ramirezs@alumno.buap.mx", semestre=8, ciudadEstado="Puebla", lenguajeProgramacion="Python", especialidad="Back ed", nivelIngles="Avanzado", estadoCivil="Soltero"),
    Usuario(id=13, nombreCompleto="Heidy santiago Ortiz", matricula=202253771, edad=21, carrera="Ingeniería en Tecnologías de la Información", genero="Femenino", facultad="Ciencias de la Computación", correo="Heidy.santiago@alumno.buap.mx", semestre=7, ciudadEstado="Tlaxiaco, Oaxaca", lenguajeProgramacion="Python", especialidad="Diseño web", nivelIngles="Básico", estadoCivil="Soltero"),
    Usuario(id=14, nombreCompleto="Jovany Solis Ortiz", matricula=202268439, edad=23, carrera="Licenciatura en Ingeniería en Tecnologías de la Información", genero="Masculino", facultad="Facultad de Computación", correo="jovany.solis@alumno.buap.mx", semestre=7, ciudadEstado="Tlaxcala", lenguajeProgramacion="JAVA", especialidad="Backend y cyberseguridad", nivelIngles="Intermedio", estadoCivil="Soltero"),
    Usuario(id=15, nombreCompleto="Azalea Belinda Medrano Parra", matricula=202437848, edad=18, carrera="Administración de empresas", genero="Femenino", facultad="Facultad de Administración", correo="mp202437848@alm.buap.mx", semestre=3, ciudadEstado="Veracruz, Coatzacoalcos", lenguajeProgramacion="Excel", especialidad="En el área de logistica o Recursos humanos", nivelIngles="Básico", estadoCivil="Soltero"),
    Usuario(id=16, nombreCompleto="Belinda Muñoz Villanueva", matricula=202449962, edad=20, carrera="Relaciones Internacionales", genero="Femenino", facultad="Ciencias sociales y políticas", correo="mv202449962@alm.buap.mx", semestre=2, ciudadEstado="Zimapán, Hidalgo", lenguajeProgramacion="Español e inglés", especialidad="Economía internacional", nivelIngles="Básico", estadoCivil="Soltero"),
    Usuario(id=17, nombreCompleto="Beatriz Cárdenas Rodríguez", matricula=202143726, edad=22, carrera="Derecho", genero="Femenino", facultad="Facultad de derecho", correo="beatriz.cardenasr@alumno.buap.mx", semestre=8, ciudadEstado="Puebla", lenguajeProgramacion="Ninguno", especialidad="Derecho penal", nivelIngles="Básico", estadoCivil="Soltero"),
    Usuario(id=18, nombreCompleto="Angel Jesús Ramírez Márquez", matricula=202454039, edad=18, carrera="Economía", genero="Masculino", facultad="Facultad de Economía", correo="rm202454039@alm.buap.mx", semestre=2, ciudadEstado="Acayucan, Veracruz", lenguajeProgramacion="Ninguno", especialidad="Python y JavaScript", nivelIngles="Intermedio", estadoCivil="Soltero"),
    Usuario(id=19, nombreCompleto="Kristian Enrique Moreno Cruz", matricula=202449575, edad=18, carrera="Economia", genero="Masculino", facultad="Economia", correo="mc202449575@alm.buap.mx", semestre=3, ciudadEstado="Huauchinango Puebla", lenguajeProgramacion="Java", especialidad="No sé aun", nivelIngles="Avanzado", estadoCivil="Soltero"),
    Usuario(id=20, nombreCompleto="Esmeralda Urbina Cinto", matricula=202269252, edad=21, carrera="Licenciatura en ingeniería en tecnologías de la información", genero="Femenino", facultad="Facultad de Ciencias de la Computación", correo="esmeralda.urbina@alumno.buap.mx", semestre=7, ciudadEstado="Puebla, Puebla", lenguajeProgramacion="C++ y python", especialidad="Inteligencia Artificial", nivelIngles="Intermedio", estadoCivil="Soltero"),
    Usuario(id=21, nombreCompleto="Jonathan Tiro Cuanenemi", matricula=202268865, edad=20, carrera="Ingeniería en Ciencias de la Computación", genero="Masculino", facultad="Facultad de Ciencias de la Computación", correo="jonathan.tiroc@alumno.buap.mx", semestre=7, ciudadEstado="Puebla, Puebla", lenguajeProgramacion="C++", especialidad="Ciberseguridad.", nivelIngles="Intermedio", estadoCivil="Soltero"),
    Usuario(id=22, nombreCompleto="Monserrath Anais Melchor Martinez", matricula=202447987, edad=19, carrera="Administración Pública y Gestión para el Desarrollo", genero="Femenino", facultad="Administración", correo="mm202447987@alm.buap.mx", semestre=3, ciudadEstado="Puebla", lenguajeProgramacion="Ningúno", especialidad="Docente", nivelIngles="Básico", estadoCivil="Soltero"),
    Usuario(id=23, nombreCompleto="Emilio Giles Vélez", matricula=202146154, edad=22, carrera="TICS", genero="Masculino", facultad="Computación", correo="emiliogiles0@gmail.com", semestre=7, ciudadEstado="Acatzingo", lenguajeProgramacion="C++", especialidad="Herramientas web", nivelIngles="Intermedio", estadoCivil="Soltero"),
    Usuario(id=24, nombreCompleto="Ivan", matricula=202119456, edad=22, carrera="Ingeniería en tecnologías de la información", genero="Masculino", facultad="Ciencias de la computación", correo="ivan.floresr@alumno.buap.mx", semestre=7, ciudadEstado="Puebla", lenguajeProgramacion="Python", especialidad="Backend", nivelIngles="Intermedio", estadoCivil="Soltero"),
    Usuario(id=25, nombreCompleto="Jose Armando Ramos Ramos", matricula=202154423, edad=22, carrera="Ingenieria en Tecnologias de la Información", genero="Masculino", facultad="FCC", correo="jose.ramos@alumno.buap.mx", semestre=7, ciudadEstado="Coatzacoalcoa Veracruz", lenguajeProgramacion="Angular, Python, C++", especialidad="Ciencia de Datos", nivelIngles="Básico", estadoCivil="Soltero"),
    Usuario(id=26, nombreCompleto="Jesús Eduardo Aulis", matricula=202117232, edad=21, carrera="Ingeniería en tecnologías de la información", genero="Masculino", facultad="Facultad de ciencias de la computación", correo="Jesús.aulis@alumno.buap.mx", semestre=8, ciudadEstado="Boca del río, Veracruz", lenguajeProgramacion="Python y Java", especialidad="Base de datos", nivelIngles="Intermedio", estadoCivil="Soltero"),
    Usuario(id=27, nombreCompleto="Hristo Guzmán", matricula=201919840, edad=26, carrera="ING. Ciencias de la computación", genero="Masculino", facultad="FCC", correo="hristo.corne@alumno.buap.mx", semestre=10, ciudadEstado="Puebla", lenguajeProgramacion="Java", especialidad="Ciberseguridad o Scrum master", nivelIngles="Intermedio", estadoCivil="Casado"),
    Usuario(id=28, nombreCompleto="Alexander Cruz", matricula=202214498, edad=20, carrera="ICC", genero="Masculino", facultad="FCC", correo="Ney.cruz@alumno.buap.mx", semestre=5, ciudadEstado="Puebla", lenguajeProgramacion=".net", especialidad="Backend", nivelIngles="Intermedio", estadoCivil="Soltero"),
    Usuario(id=29, nombreCompleto="Jaqueline Flores", matricula=202260643, edad=20, carrera="Ingeniería en ciencias de la computación", genero="Femenino", facultad="FCC", correo="Jaqueline.floresa@alumno.buap.mx", semestre=5, ciudadEstado="Huaquechula, Puebla", lenguajeProgramacion="Java", especialidad="Ciber seguridad", nivelIngles="Intermedio", estadoCivil="Soltero"),
    Usuario(id=30, nombreCompleto="Rutsaanay Hernández Pérez", matricula=202387373, edad=20, carrera="Ingeniería en Ciencias De la Computación", genero="Femenino", facultad="ICC", correo="hp202387373@alm.buap.com", semestre=5, ciudadEstado="Xicohtzinco -Tlaxcala", lenguajeProgramacion="C++", especialidad="Plataformas", nivelIngles="Básico", estadoCivil="Soltero"),
    Usuario(id=31, nombreCompleto="Erendira Giovana González Martínez", matricula=202261438, edad=21, carrera="Licenciatura en ciencias de la computación", genero="Femenino", facultad="Facultad de ciencias de la computación", correo="Erendira.gonzalez@alumno.buap.mx", semestre=7, ciudadEstado="Morelos", lenguajeProgramacion="C++,java", especialidad="Base de datos o graficación", nivelIngles="Básico", estadoCivil="Soltero"),
    Usuario(id=32, nombreCompleto="Jesed Rubí Sánchez Bonilla", matricula=202366521, edad=20, carrera="Químico Farmacobiólogo", genero="Femenino", facultad="Ciencias Químicas", correo="sb202366521@alm.buap.mx", semestre=5, ciudadEstado="Puebla, Puebla", lenguajeProgramacion="Ninguno", especialidad="Microbiologia", nivelIngles="Básico", estadoCivil="Soltero"),
    Usuario(id=33, nombreCompleto="Jose Manuel Farfan Nuñez", matricula=202361560, edad=20, carrera="QFB", genero="Masculino", facultad="Ciencias químicas", correo="fn202361560@alm.buap.mx", semestre=4, ciudadEstado="Acayucan, Veracruz", lenguajeProgramacion="Ninguno", especialidad="Fármacos", nivelIngles="Avanzado", estadoCivil="Soltero"),
    Usuario(id=34, nombreCompleto="Abril Romero Soria", matricula=201820242, edad=23, carrera="Ingeniería en alimentos", genero="Femenino", facultad="Ingeniería Química", correo="abril.rs@alumno.buap.mx", semestre=10, ciudadEstado="Puebla", lenguajeProgramacion="Ninguno", especialidad="Industria", nivelIngles="Básico", estadoCivil="Soltero"),
    Usuario(id=35, nombreCompleto="Fernando Kolya Méndez Flores", matricula=202233640, edad=22, carrera="Ingeniería Química", genero="Masculino", facultad="Ingeniería Química", correo="fernando.mendezfl@alumno.buap.mx", semestre=7, ciudadEstado="Puebla, Puebla.", lenguajeProgramacion="Ninguno.", especialidad="Petroquímica.", nivelIngles="Intermedio", estadoCivil="Unión libre"),
    Usuario(id=36, nombreCompleto="Ezequiel Pérez Ayala", matricula=202247275, edad=20, carrera="ING Química", genero="Masculino", facultad="Fiq", correo="Ezequiel.pereza@alumno.buap.mx", semestre=7, ciudadEstado="Puebla, Pue", lenguajeProgramacion="C++", especialidad="Metalurgia", nivelIngles="Sin conocimiento", estadoCivil="Soltero"),
    Usuario(id=37, nombreCompleto="Jael Roque Pacheco", matricula=202157764, edad=22, carrera="Ing.Alimentos", genero="Femenino", facultad="Facultad de ingeniería química", correo="Jael.roquep@alumno.buap.mx", semestre=9, ciudadEstado="Puebla", lenguajeProgramacion="Ninguno", especialidad="Ing", nivelIngles="Básico", estadoCivil="Soltero"),
    Usuario(id=38, nombreCompleto="Edgar González López", matricula=201923239, edad=24, carrera="Ing. Ambientale", genero="Masculino", facultad="Ing. Quimica", correo="edgarbuap17@gmail.com", semestre=13, ciudadEstado="Puebla", lenguajeProgramacion="Ninguno", especialidad="Tratamiento de agua", nivelIngles="Intermedio", estadoCivil="Soltero"),
    Usuario(id=39, nombreCompleto="Luis Ángel Nolasco González", matricula=202139783, edad=21, carrera="Ingeniería Ambiental", genero="Masculino", facultad="Ingeniería Química", correo="Luis.nolascog@alumno.buap.mx", semestre=9, ciudadEstado="Puebla", lenguajeProgramacion="Ninguno", especialidad="Seguridad e Higiene", nivelIngles="Avanzado", estadoCivil="Soltero"),
    Usuario(id=40, nombreCompleto="MARCOS CASTRO LUNA", matricula=202143960, edad=23, carrera="Ingeniería ambiental", genero="Masculino", facultad="FIQ", correo="marcos.catro@alumno.buap", semestre=8, ciudadEstado="Córdoba, Veracruz", lenguajeProgramacion="Piton", especialidad="Seguridad e higiene", nivelIngles="Intermedio", estadoCivil="Soltero"),
    Usuario(id=41, nombreCompleto="Josué Castro Castro", matricula=202315894, edad=16, carrera="Bachillerato 5 de meyo", genero="Masculino", facultad="Bachillerato 5 de mayo", correo="cc202315894@alm.buap.mx", semestre=5, ciudadEstado="Puebla, Puebla", lenguajeProgramacion="Ninguno", especialidad="Arquitectura", nivelIngles="Intermedio", estadoCivil="Unión libre"),
    Usuario(id=42, nombreCompleto="Shaila Reyes Domínguez", matricula=202306722, edad=17, carrera="Bachillerato 5 de mayo", genero="Femenino", facultad="Bachillerato 5 de mayo", correo="rd202306722@alm.buap.mx", semestre=5, ciudadEstado="Puebla, Pue", lenguajeProgramacion="Ninguno", especialidad="Médico", nivelIngles="Básico", estadoCivil="Soltero"),
    Usuario(id=43, nombreCompleto="Diana Jaqueline Valera Pérez", matricula=202164014, edad=22, carrera="Ingeniería Ambiental", genero="Femenino", facultad="Ingeniería química", correo="diana.valerap@alumno.buap mx", semestre=8, ciudadEstado="Puebla", lenguajeProgramacion="Phyton", especialidad="Aguas residuales", nivelIngles="Básico", estadoCivil="Soltero"),
    Usuario(id=44, nombreCompleto="Mayra bello Vazquez", matricula=202029066, edad=27, carrera="Ing. Ambiental", genero="Femenino", facultad="Facultad de ingeniería química", correo="Mayra.bellov@alumno.buap.mx", semestre=6, ciudadEstado="Puebla", lenguajeProgramacion="Pyton, macros, MATLAB", especialidad="Me gustaría especializarme en el área de suelo o agua", nivelIngles="Intermedio", estadoCivil="Soltero"),
    Usuario(id=45, nombreCompleto="García Zayas Luis Uriel", matricula=202037763, edad=22, carrera="Ingeniería Química", genero="Masculino", facultad="Ingeniería Química", correo="luis.garciaz@alumno.buap.mx", semestre=10, ciudadEstado="Puebla", lenguajeProgramacion="Ninguno", especialidad="Procesos industriales", nivelIngles="Intermedio", estadoCivil="Soltero"),
    Usuario(id=46, nombreCompleto="Giovanni leal Santos", matricula=202063708, edad=23, carrera="Actuación", genero="Masculino", facultad="Cine", correo="giovanni.leal.@alumo.buap.mx", semestre=9, ciudadEstado="Puebla", lenguajeProgramacion="Ninguno", especialidad="No se", nivelIngles="Intermedio", estadoCivil="Divorciado"),
    Usuario(id=47, nombreCompleto="Giovanni leal flores", matricula=202042951, edad=23, carrera="Actuaría", genero="Masculino", facultad="Ciencia físico matematicas", correo="Lealflresgiovanni", semestre=8, ciudadEstado="Puebla", lenguajeProgramacion="Phyton", especialidad="Seguros y fianzas", nivelIngles="Intermedio", estadoCivil="Soltero"),
    Usuario(id=48, nombreCompleto="Gael García Rivera", matricula=202222961, edad=21, carrera="Ingiemeria química", genero="Masculino", facultad="Fiq", correo="gael.garciari@alumno.buap.mx", semestre=6, ciudadEstado="Morelos", lenguajeProgramacion="Payton java", especialidad="Laboratorio", nivelIngles="Avanzado", estadoCivil="Soltero"),
    Usuario(id=49, nombreCompleto="Litzy Manzo Hernández", matricula=202045005, edad=23, carrera="Comercio Internacional", genero="Femenino", facultad="Administración", correo="litzy.manzoh@alumno.buap.mx", semestre=9, ciudadEstado="Puebla", lenguajeProgramacion="Ninguno", especialidad="Logística", nivelIngles="Intermedio", estadoCivil="Soltero"),
    Usuario(id=50, nombreCompleto="Diego Ortiz de la Peña", matricula=202246291, edad=22, carrera="Criminología", genero="Masculino", facultad="Derecho", correo="diego.ortizdelap@alumno.buap.mx", semestre=7, ciudadEstado="Puebla, puebla", lenguajeProgramacion="Ninguno", especialidad="Agente de investigación", nivelIngles="Intermedio", estadoCivil="Soltero"),
    Usuario(id=51, nombreCompleto="Lopez Montiel José Ángel", matricula=202228339, edad=21, carrera="Criminología", genero="Masculino", facultad="Derecho", correo="jose.lopezmon@alumno.buap.mx", semestre=7, ciudadEstado="Puebla", lenguajeProgramacion="Ninguno", especialidad="Control social", nivelIngles="Intermedio", estadoCivil="Soltero"),
    Usuario(id=52, nombreCompleto="Mabel Sánchez Hernández", matricula=202253032, edad=20, carrera="Criminología", genero="Femenino", facultad="Derecho", correo="mabel.sanchezh@alumno.buap.mx", semestre=7, ciudadEstado="Tlaxcala", lenguajeProgramacion="Ninguno", especialidad="Peritaje", nivelIngles="Básico", estadoCivil="Soltero")
]

# Rutas de la API con solo GET

# Mostrar todos los usuarios
@app.get("/usuarios")
async def get_users():
    return lista_usuarios

############### Primer Nivel ################
# 1. Primer Nivel: Mostrar todos los usuarios por ID
@app.get("/usuarios/id/{usuarioId}")
async def get_user_by_id(usuarioId: int):
    usuario = next((usuario for usuario in lista_usuarios if usuario.id == usuarioId), None)
    if usuario:
        return usuario
    return {"error": "Usuario no encontrado"}

# 2. Primer Nivel: Mostrar usuarios por semestre
@app.get("/usuarios/semestre/{semestre}")
async def get_users_by_semester(semestre: int):
    usuarios_filtrados = [usuario for usuario in lista_usuarios if usuario.semestre == semestre]
    if usuarios_filtrados:
        return usuarios_filtrados
    return {"error": "No se encontraron usuarios en este semestre"}

# 3. Primer Nivel: Mostrar usuarios por género
@app.get("/usuarios/genero/{genero}")
async def get_user_by_gender(genero: str):
    usuarios_filtrados = [usuario for usuario in lista_usuarios if usuario.genero.lower() == genero.lower()]
    if usuarios_filtrados:
        return usuarios_filtrados
    return {"error": "No se encontraron usuarios con este género"}

# ############### Segundo Nivel ################
# 4. Segundo Nivel: Mostrar usuarios por facultad y semestre
@app.get("/usuarios/facultad/{facultad}/semestre/{semestre}")
async def get_users_by_faculty_and_semester(facultad: str, semestre: int):
    usuarios_filtrados = [usuario for usuario in lista_usuarios if usuario.facultad.lower() == facultad.lower() and usuario.semestre == semestre]
    if usuarios_filtrados:
        return usuarios_filtrados
    return {"error": "No se encontraron usuarios en esta facultad y semestre"}

# 5. Segundo Nivel: Mostrar un usuario por edad Y estado civil
@app.get("/usuarios/edad/{edad}/estado_civil/{estadoCivil}")
async def get_users_by_age_and_marital_status(edad: int, estadoCivil: str):
    usuarios_filtrados = [usuario for usuario in lista_usuarios if usuario.edad == edad and usuario.estadoCivil.lower() == estadoCivil.lower()]
    if usuarios_filtrados:
        return usuarios_filtrados
    return {"error": "No se encontraron usuarios con esta edad y estado civil"}

# 6. Segundo Nivel: Mostrar un usuario por carrera y lenguaje de programación
@app.get("/usuarios/carrera/{carrera}/lenguaje/{lenguajeProgramacion}")
async def get_users_by_career_and_programming_language(carrera: str, lenguajeProgramacion: str):
    usuarios_filtrados = [usuario for usuario in lista_usuarios if usuario.carrera.lower() == carrera.lower() and usuario.lenguajeProgramacion.lower() == lenguajeProgramacion.lower()]
    if usuarios_filtrados:
        return usuarios_filtrados
    return {"error": "No se encontraron usuarios con esta carrera y lenguaje de programación"}

# ############### Tercer Nivel ################
# 7. Tercer Nivel: Mostrar un usuario por facultad, edad y especialidad
@app.get("/usuarios/facultad/{facultad}/edad/{edad}/especialidad/{especialidad}")
async def get_users_by_faculty_and_age_and_specialty(facultad: str, edad: int, especialidad: str):
    usuarios_filtrados = [usuario for usuario in lista_usuarios if usuario.facultad.lower() == facultad.lower() and usuario.edad == edad and usuario.especialidad.lower() == especialidad.lower()]
    if usuarios_filtrados:
        return usuarios_filtrados
    return {"error": "No se encontraron usuarios con esta facultad, edad y especialidad"}

# 8. Tercer Nivel: Mostrar un usuario por facultad, edad y nivel de ingles
@app.get("/usuarios/facultad/{facultad}/edad/{edad}/nivel_ingles/{nivelIngles}")
async def get_users_by_faculty_and_age_and_english_level(facultad: str, edad: int, nivelIngles: str):
    usuarios_filtrados = [usuario for usuario in lista_usuarios if usuario.edad == edad and usuario.facultad.lower() == facultad.lower() and usuario.nivelIngles.lower() == nivelIngles.lower()]
    if usuarios_filtrados:
        return usuarios_filtrados
    return {"error": "No se encontraron usuarios con esta facultad, edad y nivel de inglés"}

# 9. Tercer Nivel: Mostrar un usuario por carrera, genero y estado civil
@app.get("/usuarios/carrera/{carrera}/genero/{genero}/estado_civil/{estadoCivil}")
async def get_usuarios_by_career_and_gender_and_marital_status(carrera: str, genero: str, estadoCivil: str):
    usuarios_filtrados = [usuario for usuario in lista_usuarios if usuario.carrera.lower() == carrera.lower() and usuario.genero.lower() == genero.lower() and usuario.estadoCivil.lower() == estadoCivil.lower()]
    if usuarios_filtrados:
        return usuarios_filtrados
    return {"error": "No se encontraron usuarios con esta carrera, género y estado civil"}

# 10. Tercer Nivel: Mostrar un usuario por semestre, lenguaje de programacion y especialidad
@app.get("/usuarios/semestre/{semestre}/lenguaje/{lenguajeProgramacion}/especialidad/{especialidad}")
async def get_users_by_semester_and_programing_language_and_specialty(semestre: int, lenguajeProgramacion: str, especialidad: str):
    usuarios_filtrados = [usuario for usuario in lista_usuarios if usuario.semestre == semestre and usuario.lenguajeProgramacion.lower() == lenguajeProgramacion.lower() and usuario.especialidad.lower() == especialidad.lower()]
    if usuarios_filtrados:
        return usuarios_filtrados
    return {"error": "No se encontraron usuarios con este semestre, lenguaje de programación y especialidad"}