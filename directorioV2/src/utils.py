import re
import os
import json

class Menu:
    """
    @Methods: show_menu, get_option
    @Attributes: optionList dict, tittle str
    """

    def __init__ (self, optionList, tittle = '--MENU--', tabLevel = 0):
        """"
        @Arguments: optionList dict, tittle str
        @Returns: True if the arguments have the rigth type
        """
        self.optionList = {'1': '1. Salir'}
        self.opmin = '0'
        self.tittle = '--MENU--'
        self.tabLevel = tabLevel
        if type(optionList) == dict:
            self.optionList = optionList
            self.opmin = str(int(min(self.optionList)) - 1)
        self.salir = str(len(self.optionList))
        if type(tittle) == str:    
            self.tittle = tittle
        
        if type(tabLevel) == int:
            self.tabLevel = tabLevel
    
    def set_tittle(self, tittle):
        """
        Args:
            tittle: type str. Value od the new tittle of the menu 
        
        """
        self.tittle = tittle
    
    def show_menu (self):
        """
        @Method
        show_menu: print the options provided at __init__ method argument  
        """
        print("\t"*self.tabLevel, self.tittle)
        print('\n'.join(["\t" * self.tabLevel + self.optionList[x] for x in sorted(self.optionList)]))
    
    def get_option(self):
        """
        @Method
        show_menu: print the options provided at __init__ method argument  
        """
        op = self.opmin
        while op not in self.optionList:
            op = input("\t"*self.tabLevel + "*Digite su opcion: ")
            if(op not in (self.optionList)):
                print("\t"*self.tabLevel + "Los números del menú... Hijo!!!")
        return(op)

    def getSalir(self):
        """
        @Method
        show_menu: returns the number of elements of the elements´s dict. 
        Means exit option
        """
        return(self.salir)

class utils:
    """
    @Methods: validate_phone, validate_email, readData,  
    @Atributtes:  
    """
    
    def __init__ (self):
        """ @__init__ function"""
        pass

    def find_file(self, namefile, path):
        """ @__init__ function"""
        #root, dirs, files
        for info in os.walk(path):
            if namefile in info[2]:
                return True
        return False            

    def validate_phone(self, phone):
        """
        @Arguments: 
        @Description: Validates a telephon number string
        """
        patron = r"[^0-9] -"
        return(not re.search(patron, phone))

    def validate_email(self, email):
        #Validates a mail string
        patron = r"([\w\.\-]+)@([\w\.-]+)\.([\w\.-]+)"
        return(re.search(patron, email))

    def agreed(self, label, opcions):
        """
        @Arguments: 
        @Description: Shows a "Label to" the user and reads an input comparing it
        to the "options". 
        """
        op = opcions[0].lower()
        opcions = [x[0].upper() for x in opcions]
        while op[0] not in opcions:
            op = input(label + ' (' + '/'.join(opcions) + '): ')
            op = [x[0].upper() for x in op]
        return(op)

    def get_data(self, label, contenedor, validacion):
        """
        Args: 
            label: The text that will be showed to the user
            Contenedor: the dict where will be put the data
            VAlidation: the function that will be used to be validations
        Description: 
            Shows a message to the user,
            validate the input and returns it into the container." 
        """
        key = str(len(contenedor) + 1)
        respuesta = ['S']
        
        print('Digite su ' + label + ": ")
        while respuesta[0] == 'S':
            newData = (input(label + ': '))
            if not validacion(newData):
                print(label + ' no valido')
                respuesta = ['S']
            else:
                contenedor[key] = newData
                key = str(int(key) + 1)
                respuesta = self.agreed('Desea ingresar otro ' +
                label, ['S', 'N'])
        return(contenedor)
        
    
class contact:
    """
    @Methods:  set_name, get_name, setPhone, getPhone, setMails, getMails,
    getMailsMenu, get_phonesMenu
    @Atributtes: name str, phones dict, emails dict 
    """

    def __init__ (self, datos = {"name": "", "phones": dict(), "emails": dict()}, tab = 3):
        """ @__init__ function"""
        self.datos = datos
        self.__phonesKey = "1"
        self.__emailsKey = "1"
        self.tab = tab
        self.util = utils()
        
    def set_name (self, name):
        """
        @Arguments: name(str)
        @Description: set the value of the attribute name
        """
        if type(name) == str:
            self.datos["name"] = name
            return(True)
        else:
            return(False)    
    
    def get_name (self):
        """
        @Arguments: self 
        @Description: Return the value of the attribute name(str) 
        """
        return (self.datos["name"])

    def aid(self, nombredatos, mode = True):
        menu_tellist = {x: x + '. ' + self.datos[nombredatos][x] for x in self.datos[nombredatos]}
        menu_email = Menu(menu_tellist, "--" + nombredatos, 4)
        opt = '0'
        while opt != menu_email.getSalir():
            menu_email.show_menu()
            opt = menu_email.get_option()
            del self.datos[nombredatos][opt]
            if mode : 
                self.util.get_data(nombredatos, self.datos[nombredatos], self.util.validate_phone)
            print("\t" * self.tab + "**" + self.datos["name"] + "\n" + "\t"*self.tab + nombredatos )
            print("\n".join("\t" * self.tab + x + '. ' + self.datos[nombredatos][x] for x in sorted(self.datos[nombredatos])))
        
    def set_phones (self, phones):
        """
        @Arguments: key str, phone str
        @Description: set the value of the phone 
        """
        if type(phones) == dict: 
            #self.datos["phones"][self.__phonesKey] = phone
            self.datos["phones"] = phones
            #self.__phonesKey = str(int(self.__phonesKey) + 1)
            return(True)
        else:   
            return(False) 
        
    def set_emails (self, emails):
        """
        @Arguments: str key, str email
        @Description: set the value of the attribute 
        """
        if type(emails) == dict: 
            self.datos["emails"] = emails
            #self.__emailsKey = str(int(self.__emailsKey) + 1)
            return(True)
        else:   
            return(False) 
        
    def get_emails (self):
        """
        @Arguments: None
        @Description: Return a dictionary with the emails 
        """
        return (self.datos["emails"])

    def get_emailsMenu (self):
        """
        @Arguments: Self
        @Description: Return a dictionary with the emails 
        """
        emailsMenu = dict(self.datos["emails"])
        emailsMenu[self.__emailsKey] = "Salir"
        return (emailsMenu)

    def get_phonesMenu (self):
        """
        @Arguments: Self
        @Description: Return a dictionary with the emails 
        """
        phonesMenu = dict(self.datos["phones"])
        phonesMenu[self.__phonesKey] = "Salir"
        return (phonesMenu)

    def get_datos(self):
        """
        @Arguments: Self
        @Description: Return a dictionary with the emails 
        """
        return(dict(self.datos))

    def set_datos(self, datos):
        """
        @Arguments: Self
        @Description: Return a dictionary with the emails 
        """
        self.datos = datos    
    
    def run_menu(self):
        """
        @Arguments: Self
        @Description: Return a dictionary with the emails 
        """
        
        print("\t" * self.tab + "**" + self.datos["name"] + "\n" + "\t" * self.tab + "Telefonos" )
        print("\n".join("\t"*self.tab + x + '. ' + self.datos["phones"][x] for x in sorted(self.datos["phones"])))
        print("\t" * self.tab + "Correos" + "\t" * self.tab)
        print("\n".join("\t"*self.tab + x + '. ' + self.datos["emails"][x] for x in sorted(self.datos["emails"])))
        print("\n\n")
        menu_dic = {
            "1": "1. Modificar nombre", 
            "2": "2. Agregar Teléfono", 
            "3": "3. Modificar Teléfono",
            "4": "4. Eliminar Teléfono",
            "5": "5. Agregar correo",
            "6": "6. Modificar Correo",
            "7": "7. Eliminar Correo",
            "8": "8. Salir"
        }    
        menu_contact = Menu(menu_dic, "--Opciones--", 3)
        opc = '0'
        while opc != '8':
            menu_contact.show_menu()
            opc = menu_contact.get_option()
            if opc == '1':
                print(self.get_name())
                self.set_name(input('Digite el nuevo nombre: '))
                menu_contact.set_tittle(self.get_name())
            if opc == '2':
                self.datos["phones"]
                self.util.get_data("telefono", self.datos["phones"], self.util.validate_phone)
                
            if opc == '3':
                self.aid("phones")
                """
                menu_tellist = {x: x + '. ' + self.datos["phones"][x] for x in self.datos["phones"]}
                menu_telefono = Menu(menu_tellist, "--Telefonos", 4)
                opt = '0'
                while opt != menu_telefono.getSalir():
                    menu_telefono.show_menu()
                    opt = menu_telefono.get_option()
                    del self.datos["phones"][opt]
                    self.util.get_data("telefono", self.datos["phones"], self.util.validate_phone)
                    print("\t"*self.tab + "**" + self.datos["name"] + "\n" + "\t"*self.tab + "Telefonos" )
                    print("\n".join("\t"*self.tab + x + '. ' + self.datos["phones"][x] for x in sorted(self.datos["phones"])))
                """                
            if opc == '4':
                """
                menu_tellist = {x: x + '. ' + self.datos["phones"][x] for x in self.datos["phones"]}
                menu_telefono = Menu(menu_tellist, "--Telefonos", 4)
                opt = '0'
                while opt != menu_telefono.getSalir():
                    menu_telefono.show_menu()
                    opt = menu_telefono.get_option()
                    del self.datos["phones"][opt]
                    print("\t"*self.tab + "**" + self.datos["name"] + "\n" + "\t"*self.tab + "Telefonos" )
                    print("\n".join("\t"*self.tab + x + '. ' + self.datos["phones"][x] for x in sorted(self.datos["phones"])))
                pass
                #presenta un menu de los telefonos y elimia el solicitado 
                """
                self.aid("phones", False)
            if opc == '5':
                self.datos["emails"]
                self.util.get_data("correo", self.datos["emails"], self.util.validate_phone)
            if opc == '6':
                """
                menu_tellist = {x: x + '. ' + self.datos["emails"][x] for x in self.datos["emails"]}
                menu_email = Menu(menu_tellist, "--Emails", 4)
                opt = '0'
                while opt != menu_email.getSalir():
                    menu_email.show_menu()
                    opt = menu_email.get_option()
                    del self.datos["emails"][opt]
                    self.util.get_data("email", self.datos["emails"], self.util.validate_phone)
                    print("\t"*self.tab + "**" + self.datos["name"] + "\n" + "\t"*self.tab + "Emails" )
                    print("\n".join("\t"*self.tab + x + '. ' + self.datos["emails"][x] for x in sorted(self.datos["emails"])))
                """
                self.aid("emails")
            if opc == '7':
                """
                menu_tellist = {x: x + '. ' + self.datos["emails"][x] for x in self.datos["emails"]}
                menu_email = Menu(menu_tellist, "--Emails", 4)
                opt = '0'
                while opt != menu_email.getSalir():
                    menu_email.show_menu()
                    opt = menu_email.get_option()
                    del self.datos["emails"][opt]
                    print("\t"*self.tab + "**" + self.datos["name"] + "\n" + "\t"*self.tab + "Emails" )
                    print("\n".join("\t"*self.tab + x + '. ' + self.datos["emails"][x] for x in sorted(self.datos["emails"])))
                """
                self.aid("emails", False)
            #imprimir nombre
            #ller nombre y cambiar

            #Agregar Telefono


class dir_contacts:
    """
    @Methods: loadfile, savefile, dircontacts, addcontact, buildDirectory, buildConMenu 
    @Atributtes: contacts, pathTxt, contactsKey
    """
    
    def __init__ (self, namefile, path):
        """ @__init__ function"""
        self.path = ""
        self.namefile = ""
        self.util = utils()
        self.dircontacts = dict()
        self.contactsKey = '1'
        if type(path) == str: 
            self.path = path
        if type(namefile) == str:
            self.namefile = namefile
        if type(path) == str and type(namefile) == str:
            if self.util.find_file(self.namefile, self.path):
                print("WTF: Found")
                if not os.stat(path + "\\"+ self.namefile):
                    self.dircontacts = dict()
                    self.contactsKey = '1'
                else:
                    with open(self.path + "\\" + self.namefile, "r") as file:
                        if bool(file):
                            string = file.read()
                            if len(string) > 0:
                                self.dircontacts = dict(json.loads(string))
                                self.contactsKey = str(int(max(self.dircontacts)) + 1)
                        else:
                            print("El directorio no pudo ser abierto")
            else:
                print('file not Found')
        
        
    
    def loadDirectory (self):
        """
        @Arguments: self 
        @Description: loads a fiel txt 
        """
        pass
    
    def newcontact(self):
        """
        @Arguments: self 
        @Description: loads a fiel txt 
        """
        person = contact()
        person.set_name(input('Nombre del contacto: '))
        person.set_phones(self.util.get_data('Teléfono', dict(),
        self.util.validate_phone))
        person.set_emails(self.util.get_data('Correo',dict(), 
        self.util.validate_email))
        self.dircontacts[self.contactsKey] = person.get_datos()
        self.contactsKey = str(int(self.contactsKey) + 1)
        self.savecontacts()
        del person
        

    def getcont_menu(self):
        """
        @Arguments: self 
        @Description: returns a dictionary showing the contacts
        """
        contactsMenu = dict()
        
        for x in self.dircontacts:
            contactsMenu[x] = x +'. ' + self.dircontacts[x]['name']
        strSalir = str(len(contactsMenu) + 1) + '. Salir'
        contactsMenu[str(len(contactsMenu) + 1)] = strSalir
        return(contactsMenu) 

    def getcontacts(self):
        """
        @Arguments: self 
        @Description: returns a dictionary showing the contacts
        """
        return(self.dircontacts)
    
    def listcontacts (self):
        """
        @Arguments: self 
        @Description: Shows a list of contacts menu
        """
        contactsMenu = Menu(self.getcont_menu(), 'contactos', 1)
        opc = '0'
        while opc != contactsMenu.getSalir():
            contactsMenu.show_menu()
            opc = contactsMenu.get_option()
            if opc != contactsMenu.getSalir():
                persona = contact(self.dircontacts[opc])
                persona.run_menu()
                self.savecontacts()
    
    def savecontacts (self):
        """
        @Arguments: self 
        @Description: saves the contacts
        """
        with open(self.path + "\\" + self.namefile, "w") as file:
            if bool(file):
                file.write(json.dumps(self.dircontacts))
            else:
                print('El directorio no pudo ser abierto para guardar')

    def read_dir(self):
        """
        @Arguments: self 
        @Description: load the contacts from text file
        """
        statinfo = os.stat("directorio\\directorio.txt")
        if not statinfo:
            self.datos = {}
            self.llave = '1'
        else:
            with open(self.path + "\\" + self.namefile, "r") as file:
                if bool(file):
                    self.datos = json.loads(file.read())
                    self.llave = str(int(max(self.datos)) + 1)
                else:
                    print("El directorio no pudo ser abierto")

    