import re
import os
import json
from src.utils import  Utilidades, Menu

class Contactos:

    def __init__(self):
        self.util = Utilidades()

    def leerDir(self):
        statinfo = os.stat("directorio\directorio.txt")
        if not statinfo:
            self.datos = {}
            self.llave = '1'
        else:
            with open("directorio\directorio.txt", "r") as File:
                if bool(File):
                    self.datos = json.loads(File.read())
                    self.llave = str(int(max(self.datos)) + 1)
                    #print(self.datos, type(self.datos))
                else:
                    print("El directorio no pudo ser abierto")

    def crearContacto(self):
        nombre = input('Nombre del contacto: ')
        telefonos = self.util.capturaDatos('Teléfono', [],
        self.util.validaTelefono)
        correos = self.util.capturaDatos('Correo', [], self.util.validaCorreo)
        self.datos[self.llave] = [nombre, telefonos, correos]
        self.llave = str(int(self.llave) + 1)

    def guardaDir(self):
        with open("directorio\directorio.txt", "w") as File:
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





def main():
    contactos = Contactos()
    contactos.leerDir()
    contactos.correMenuP()

if __name__ == "__main__":
    main()


