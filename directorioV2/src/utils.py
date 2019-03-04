import re
import os
import json

class Menu:
    """
    Attributes: 
        option_list dict: contains the menu's options {str(int): str_option}.
            the last elemente may be the 'exit' option.
        tittle str: contains the menu's tittle

    Methods: 
        show_menu: prints a menu in text mode 
        get_option: read a keyboard input forced into the option´s list
        tab_level: factor of \\t used for print the menu
    """

    def __init__ (self, option_list, tittle = '--MENU--', tab_level = 0):
        """"
        Description:
            Object´s inicialization
        Arguments:
            option_list: dict with menu's options
            tittle:  str with menu's tittle
            tab_level: int with the factor of tabs used for print the menu
        Returns: None
        """
        self.option_list = {'1': '1. Salir'}
        self.opmin = '0'
        self.tittle = '--MENU--'
        self.tab_level = tab_level
        if type(option_list) == dict:
            self.option_list = option_list
            self.opmin = str(int(min(self.option_list)) - 1)
        self.salir = str(len(self.option_list))
        if type(tittle) == str:    
            self.tittle = tittle
        
        if type(tab_level) == int:
            self.tab_level = tab_level
    
    def set_tittle(self, tittle):
        """
        Description:
            Sets the tittle attribute
        Arguments:
            tittle: type str. Value od the new tittle of the menu 
        Returns: 
            None    
        """
        self.tittle = tittle
    
    def show_menu (self):
        """
        Description:
            show_menu: shows a text mode menu          
        Returns: 
            None    
        """

        print("\t"*self.tab_level, self.tittle)
        print('\n'.join(["\t" * self.tab_level + self.option_list[x] for x in sorted(self.option_list)]))
    
    def get_option(self):
        """
        Arguments:
            None
        Description:
            Trolls the user until he or she type a option in the menu
        Returns:
            returns the user´s choose  option
        """
        op = self.opmin
        while op not in self.option_list:
            op = input("\t"*self.tab_level + "*Digite su opcion: ")
            if(op not in (self.option_list)):
                print("\t"*self.tab_level + "Los números del menú... Hijo!!!")
        return(op)

    def getSalir(self):
        """
        Arguments:
            None
        Returns:
            returns the exit option
        """
        return(self.salir)

class utils:
    """
    Description:
        class with methods to make nice things like validate input strings  
    Atributtes:  
        None
    """
    
    def __init__ (self):
        """ @__init__ function"""
        pass

    def find_file(self, file_name, path):
        """ 
        Arguments:
            file_name: 
                name.ext of file
            path:
                path of the file that will be found
        Return:
            Returns True if the file was found at the path
        """
        for info in os.walk(path):
            if file_name in info[2]:
                return True
        return False            

    def validate_phone(self, phone):
        """
        Arguments: 
            phone: string with phone typed by the user        
        Returns: 
            returns True if the phone match with the regex
        """
        patron = r"[^0-9] -"
        return(not re.search(patron, phone))

    def validate_email(self, email):
        """
        Arguments: 
            phone: string with email typed by the user        
        Returns: 
            returns True if the email match with the regex
        """
        patron = r"([\w\.\-]+)@([\w\.-]+)\.([\w\.-]+)"
        return(re.search(patron, email))

    def agreed(self, label, options):
        """
        Description:
            Shows a "Label to" the user and reads an input comparing it
            to the "options".  
        Arguments:
            label: Text to be printed
            option: list woth the options to be validated
        Return: 
            Returns the option choose for the user   
        """
        op = options[0].lower()
        options = [x[0].upper() for x in options]
        while op[0] not in options:
            op = input(label + ' (' + '/'.join(options) + '): ')
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
        Description:
            Class to manage the contact data
    """

    def __init__ (self, datos = {"name": "", "phones": dict(), "emails": dict()}, tab = 3):
        """
        Argments: 
            datos:
                Dictionary with the Data of the contact like this
                {"name": "", "phones": {keystr: str}}, "emails": {keystr:str}}}
            tab:
                number of "\t" used to print the menu
        """
        self.datos = datos
        self.__phonesKey = "1"
        self.__emailsKey = "1"
        self.tab = tab
        self.util = utils()
        
    def set_name (self, name):
        """
        Arguments: 
            name (str): name of the contac
        Description: 
            set the value of the attribute name
        returns: 
            True when the name was set     
        """
        if type(name) == str:
            self.datos["name"] = name
            return(True)
        else:
            return(False)    
    
    def get_name (self):
        """
        Return: 
            Returns the value of the attibute name.
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
        Arguments: 
            phones: dictionary with the phones of the contact
        Description: 
            set a dictionarary with the value of the phones of the contact 
        """
        if type(phones) == dict: 
            self.datos["phones"] = phones
            return(True)
        else:   
            return(False) 
        
    def set_emails (self, emails):
        """
        Arguments: 
            emails: dictionary with the emails of the contact
        Description: 
            set a dictionarary with the value of the emails of the contact 
        """
        if type(emails) == dict: 
            self.datos["emails"] = emails
            return(True)
        else:   
            return(False) 
        
    def get_emails (self):
        """
        Arguments: None
        Return: Returns a dictionary with the emails 
        """
        return (self.datos["emails"])

    def get_emailsMenu (self):
        """
        Arguments: Nonne
        
        Returns: 
            Returns a dictionary with the emails 
        """
        emailsMenu = dict(self.datos["emails"])
        emailsMenu[self.__emailsKey] = "Salir"
        return (emailsMenu)

    def get_phonesMenu (self):
        """
        Arguments: None

        Return: Returns a dictionary with the phones for be used to build a dict
            with the class Menu
        """
        phonesMenu = dict(self.datos["phones"])
        phonesMenu[self.__phonesKey] = "Salir"
        return (phonesMenu)

    def get_datos(self):
        """
        Arguments: None
        Description: Return a dictionary with contact's data 
        """
        return(dict(self.datos))

    def set_datos(self, datos):
        """
        Arguments:
            datos: dictionary with the contact´s data

        Description: setter of contact´s data
        """
        self.datos = datos    
    
    def run_menu(self):
        """
        @Arguments: 
            None
        @Description: 
            it´s a menu with the options to manage the contacts and executes the option
            choosed fo the user
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
            

class dir_contacts:
    """
    Description:
        manage the data of a contact
    """
    
    def __init__ (self, file_name, path):
        """ @__init__ function"""
        self.path = ""
        self.file_name = ""
        self.util = utils()
        self.dircontacts = dict()
        self.contactsKey = '1'
        if type(path) == str: 
            self.path = path
        if type(file_name) == str:
            self.file_name = file_name
        if type(path) == str and type(file_name) == str:
            if self.util.find_file(self.file_name, self.path):
                print("WTF: Found")
                if not os.stat(path + "\\"+ self.file_name):
                    self.dircontacts = dict()
                    self.contactsKey = '1'
                else:
                    with open(self.path + "\\" + self.file_name, "r") as file:
                        if bool(file):
                            string = file.read()
                            if len(string) > 0:
                                self.dircontacts = dict(json.loads(string))
                                self.contactsKey = str(int(max(self.dircontacts)) + 1)
                        else:
                            print("El directorio no pudo ser abierto")
            else:
                print('file not Found')
        
    
    def newcontact(self):
        """
        Description: 
            Method to create a new contact.
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
        Arguments:  None
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
        Arguments: self 
        Description: returns a dictionary showing the contacts
        """
        return(self.dircontacts)
    
    def listcontacts (self):
        """
        Arguments: self 
        Description: Shows a list of contacts menu
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
        Arguments: self 
        Description: saves the contacts
        """
        with open(self.path + "\\" + self.file_name, "w") as file:
            if bool(file):
                file.write(json.dumps(self.dircontacts))
            else:
                print('El directorio no pudo ser abierto para guardar')

    def read_dir(self):
        """
        Arguments: self 
        Description: load the contacts from text file
        """
        statinfo = os.stat("directorio\\directorio.txt")
        if not statinfo:
            self.datos = {}
            self.llave = '1'
        else:
            with open(self.path + "\\" + self.file_name, "r") as file:
                if bool(file):
                    self.datos = json.loads(file.read())
                    self.llave = str(int(max(self.datos)) + 1)
                else:
                    print("El directorio no pudo ser abierto")

    