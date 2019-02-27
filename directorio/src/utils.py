import re

class Utilidades:
    """Docstring
    @methods:
    """

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
