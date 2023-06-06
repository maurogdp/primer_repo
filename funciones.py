import clases as c

def registrar():
    pass

def iniciar_sesion():
    user = input("ingresa tu nombre de usuario para iniciar tu sesión\nUsuario: ")
    try:
        archivo_de_usuarios = open("users.txt", "r")
        lista_lineas = archivo_de_usuarios.readlines()
        lista_usuarios_password = [linea.rstrip("\n").split(",") for linea in lista_lineas]
        lista_usuarios = [datos[0] for datos in lista_usuarios_password]
        lista_password = [datos[1] for datos in lista_usuarios_password]

        while True:
            if user in lista_usuarios:
                posicion_usuario = lista_usuarios.index(user)
                while True:
                    password = input("Contraseña: ")
                    if password == lista_password[posicion_usuario]:
                        a = c.Usuario(user)
                    else:
                        print("Contraseña incorrecta. Intenta nuevamente.") 
            else:
                print("El usuario no existe")

                respuesta = input("¿Te deseas registrar? (s/n)")

                if respuesta.lower() == "s":
                    registrar()
                    break
                elif respuesta.lower() == "n":
                    print("vuelve pronto! Te estaremos esperando!")
                    break
                else:
                    print('Respuesta no válida. Responde "s" para sí y responde "n" para no.')
    except:
        print("Aún nom existe ningun usuario registrado.")
        
        while True:
            respuesta = input("¿Te deseas registrar? (s/n): ")

            if respuesta.lower() == "s":
                registrar()
                break
            elif respuesta.lower() == "n":
                print("vuelve pronto! Te estaremos esperando!")
                break
            else:
                print('Respuesta no válida. Responde "s" para sí y responde "n" para no.')
    
    

iniciar_sesion()

