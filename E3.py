import easygui
import csv
import math

2
titulo = "Registro de estudiantes"
menu = '1. ingresar estudiante', '2. visualizar estudiantes', '3. buscar estudiante', '4. exportar datos estudiantes', '5. salir'
expmenu = '1. exportar todos', '2. exportar aprobados', '3. exportar reprobados'
estudiantes_total= []
aprobados=[]
reprobados=[]

def añadir():
    nombre_estudiante= easygui.enterbox("Ingrese el nombre del estudiante, sin espacios", titulo)
    while not nombre_estudiante.isalpha():
        easygui.msgbox("No use caracteres especiales o números")
        nombre_estudiante= easygui.enterbox("Ingrese el nombre del estudiante, sin espacios", titulo)
    rut_estudiante= easygui.enterbox("Ingrese el RUT del estudiante, sin guión", titulo)
    limite=len(rut_estudiante)
    while not rut_estudiante.isdigit():
        easygui.msgbox("Use sólo números", titulo)
        rut_estudiante= easygui.enterbox("Ingrese el RUT del estudiante, sin guión", titulo)
    if limite != 9:
        easygui.msgbox("Ingrese nueve números, sin guión", titulo)
        rut_estudiante= easygui.enterbox("Ingrese el RUT del estudiante, sin guión", titulo)


    nota1= easygui.enterbox('Ingrese la primera nota del estudiante', titulo)
    while not nota1.isdigit():
        easygui.msgbox("Use sólo números")
        nota1= easygui.enterbox('Ingrese la primera nota del estudiante', titulo)
    
    nota2= easygui.enterbox('Ingrese la segunda nota del estudiante', titulo)
    while not nota2.isdigit():
        easygui.msgbox("Use sólo números")
        nota2= easygui.enterbox('Ingrese la segunda nota del estudiante', titulo)
    
    nota3= easygui.enterbox('Ingrese la tercera nota del estudiante', titulo)
    while not nota3.isdigit():
        easygui.msgbox("Use sólo números")
        nota3= easygui.enterbox('Ingrese la tercera nota del estudiante', titulo)

    nota4= easygui.enterbox('Ingrese la cuarta nota del estudiante', titulo)
    while not nota4.isdigit():
        easygui.msgbox("Use sólo números")
        nota4= easygui.enterbox('Ingrese la cuarta nota del estudiante', titulo)

    notaexamen= easygui.enterbox('Ingrese la nota de Examen', titulo)
    while not notaexamen.isdigit():
        easygui.msgbox("Use sólo números")
        notaexamen= easygui.enterbox('Ingrese la cuarta nota del estudiante', titulo)

   
    nota1= int(nota1)
    nota2= int(nota2)    
    nota3= int(nota3)    
    nota4= int(nota4)    
    notaexamen= int(notaexamen)
    notas= nota1, nota2, nota3, nota4
    presentacion= int((nota1+nota2+nota3+nota4)/4)
    notafinal= (presentacion+notaexamen)/2
    if notafinal >= 40:
        estado= 'aprobado'
    else:
        estado= 'reprobado'

    rut_estudiante= {
        'nombre': nombre_estudiante,
        'rut': rut_estudiante,
        'notas': notas,
        'nota presentacion': presentacion,
        'nota final': notafinal,
        'estado': estado

    }
    estudiantes_total.append(nombre_estudiante)









def mostrar(estudiantes_total):
    easygui.msgbox(estudiantes_total)






def buscar(estudiantes_total):
    busqueda= easygui.enterbox("Ingrese el rut del estudiante que desea encontrar", titulo)
    for estudiante in estudiantes_total:
        if  estudiante==busqueda:
            print(busqueda)
            print(estudiante)
        else:
            print(busqueda)
            print(estudiante)
            easygui.msgbox(estudiante)











def exportar(estudiantes_total, aprobados, reprobados):
    TipoExp= easygui.choicebox("Eliga una opción", titulo, expmenu)
    if TipoExp == '1. exportar todos':
        with open("estudiantes_total", "w", newline="") as archivo_csv:
            escritor_csv = csv.writer(archivo_csv)
            escritor_csv.writerow(['A', 'B'])
        


while True:
    opcion=easygui.choicebox("Bienvenido, eliga una opción", titulo, menu)
    if opcion == '1. ingresar estudiante':
        añadir()
    if opcion == '2. visualizar estudiantes':
        mostrar(estudiantes_total)
    if opcion == '3. buscar estudiante':
        buscar(estudiantes_total)
    if opcion == '4. exportar datos estudiantes':
        exportar(estudiantes_total, aprobados, reprobados)
    if opcion == '5. salir':
        break