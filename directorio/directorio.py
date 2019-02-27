import re
import os
import json
import Utilidades


#import Utilidades
#import Menu
#import Contactos


class Utilidades:

    def validaTelefono(self, telefono):
        #Validates a telephon number string
        patron = r"[^0-9] -"
        return(not re.search(patron, telefono))

    def validaCorreo(self, correo):
        #Validates a mail string
        patron = r"([\w\.\-]+)@([\w\.-]+)\.([\w\.-]+)"
        return(re.search(patron, correo))

    def confirmacion(self, label, opciones):
        '''Shows a "Label to" the user and reads an input comparing it
        to the "options". '''
        op = opciones[0].lower()
        opciones = [x[0].upper() for x in opciones]
        while op[0] not in opciones:
            op = input(label + ' (' + '/'.join(opciones) + '): ')
            op = [x[0].upper() for x in op]
        return(op)

    def capturaDatos(self, label, contenedor, validacion):
        '''Shows a message to the user,
        validate the input and returns it into the container'''
        respuesta = ['S']
        print('Digite su ' + label)
        while respuesta[0] == 'S':
            contenedor.append(input(label + ': '))
            if not validacion(contenedor[len(contenedor) - 1]):
                contenedor.pop()
                print(label + ' no valido')
                print('pos val ', contenedor)
            if len(contenedor):
                respuesta = self.confirmacion('Desea ingresar otro ' +
                label, ['S', 'N'])
        return(contenedor)


class Menu:

    def __init__(self, opciones):
            self.opciones = opciones
            self.salir = max(opciones)
            #self.objeto = objeto
            self.listaOpciones = list(x for x in self.opciones)
            self.opmin = str(int(min(self.listaOpciones)) - 1)

    def imprimirMenu(self, titulo='GUIA TELEFONICA\n'):
        print(titulo)
        print('\n'.join(self.opciones[x] for x in sorted(self.opciones)))

    def leerOpcion(self):
        op = self.opmin
        while op not in self.listaOpciones:
            op = input('Digite su opcion: ')
            if(op not in (self.listaOpciones)):
                print('\tLos números del menú... Hijo!!!')
        return(op)


class Contactos:

    def __init__(self):
        self.util = Utilidades()

    def leerDir(self):
        statinfo = os.stat('directorio.txt')
        if not statinfo:
            self.datos = {}
            self.llave = '1'
        else:
            with open("directorio.txt", "r") as File:
                if bool(File):
                    self.datos = json.loads(File.read())
                    self.llave = str(int(max(self.datos)) + 1)
                    #print(self.datos, type(self.datos))
                else:
                    print('El directorio no pudo ser abierto')

    def crearContacto(self):
        nombre = input('Nombre del contacto: ')
        telefonos = self.util.capturaDatos('Teléfono', [],
        self.util.validaTelefono)
        correos = self.util.capturaDatos('Correo', [], self.util.validaCorreo)
        self.datos[self.llave] = [nombre, telefonos, correos]
        self.llave = str(int(self.llave) + 1)

    def guardaDir(self):
        with open("directorio.txt", "w") as File:
            if bool(File):
                File.write(json.dumps(self.datos))
            else:
                print('El directorio no pudo ser abierto para guardar')

    def correMenuP(self):

        menup = {
            '3': '3. Salir',
            '2': '2. Listar contactos',
            '1': '1. Crear contacto'
        }
        m = Menu(menup)
        salir = '3'
        op = '0'
        while op != salir:
            m.imprimirMenu()
            op = m.leerOpcion()
            if(op == '1'):
                print('\t', '1. CREAR CONTACTO')
                self.crearContacto()
                self.guardaDir()
            elif(op == '2'):
                self.listarContactos()
            elif(op == '3'):
                print('\n\n', menup[op][0], '\n')

    def listarContactos(self):
        #for x in self.datos:
        #    print('\t', x.ljust(10, '.'), self.datos[x][0])
        #print('\t', self.llave.ljust(10, '.'), 'Menu Principal')
        menuContactos = {x:'\t' + x.ljust(10, '.') + self.datos[x][0] for x in self.datos}
        menuContactos[self.llave] = '\t' + self.llave.ljust(10, '.') + 'Menu Principal'
        conmenu = Menu(menuContactos)
        conmenu.imprimirMenu('\n\n\tContactos')
        op = conmenu.leerOpcion()

        if(op != self.llave):
            print('\n\n\t\tDatos ', self.datos[op][0])
            print('\t\t-Telefonos')
            for x in self.datos[op][1]:
                print('\t\t\t', x)
            print('\t\t-Correos')
            for x in self.datos[op][2]:
                print('\t\t\t', x)






contactos = Contactos()
contactos.leerDir()
contactos.correMenuP()



