from src.utils import Menu, dir_contacts
from os import getcwd


def main():
    #directorioV2
    directorio = dir_contacts("directorio.txt", getcwd())
    menup = {
            '3': '3. Salir',
            '2': '2. Listar contactos',
            '1': '1. Crear contacto'
    }

    menuObj = Menu(menup, "\n\n***Menu Principal ***")
    op = '0'
    while op != '3':
        menuObj.show_menu()
        op = menuObj.get_option()
        #print('Opcion: '+ op)
        if op == '1':
            directorio.newcontact()
        if op == '2':
            directorio.listcontacts()    


if __name__ == "__main__":
        main()
