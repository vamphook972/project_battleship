import random
import os
import time


# esta funcion simplemente sirve para esperar a que el usuario de enter, y la utilizaremos para empezar el juego o talvez en otros momentos.
def esperar_tecla():
    input("""
                                      𝐏𝐑𝐄𝐒𝐈𝐎𝐍𝐀 "𝐄𝐍𝐓𝐄𝐑" 𝐏𝐀𝐑𝐀 𝐂𝐎𝐍𝐓𝐈𝐍𝐔𝐀𝐑
    """)


# de la libreria os utilizaremos la funcion que limpia la terminal.
# la funcion detecta en que sistema se esta ejecutando, ya que dependiendo del sistema se llama a la funcion de una manera u otra.
def clear():
    if os.name == "nt":
        os.system("cls")
    else:
        os.system("clear")


# guardamos el titulo en una funcion para poder llamarla cuando queramos inciciar el juego.
def mostrar_titulo():
    print("""

    ██████╗  █████╗ ████████╗ █████╗ ██╗     ██╗      █████╗     ███╗   ██╗ █████╗ ██╗   ██╗ █████╗ ██╗
    ██╔══██╗██╔══██╗╚══██╔══╝██╔══██╗██║     ██║     ██╔══██╗    ████╗  ██║██╔══██╗██║   ██║██╔══██╗██║
    ██████╔╝███████║   ██║   ███████║██║     ██║     ███████║    ██╔██╗ ██║███████║██║   ██║███████║██║
    ██╔══██╗██╔══██║   ██║   ██╔══██║██║     ██║     ██╔══██║    ██║╚██╗██║██╔══██║╚██╗ ██╔╝██╔══██║██║
    ██████╔╝██║  ██║   ██║   ██║  ██║███████╗███████╗██║  ██║    ██║ ╚████║██║  ██║ ╚████╔╝ ██║  ██║███████╗
    ╚═════╝ ╚═╝  ╚═╝   ╚═╝   ╚═╝  ╚═╝╚══════╝╚══════╝╚═╝  ╚═╝    ╚═╝  ╚═══╝╚═╝  ╚═╝  ╚═══╝  ╚═╝  ╚═╝╚══════╝
⊰━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━⊱ ⛴ ⊰━━━━ ◥꧁☠ ☠ ꧂◤ ━━━━⊱ ⛴ ⊰━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━⊱

                                 ───│─────────────────────────────────────
                                 ───│────────▄▄───▄▄───▄▄───▄▄───────│────
 ───│─────▄▄───▄▄───▄▄───│────   ───▌────────▒▒───▒▒───▒▒───▒▒───────▌────     ───│─────▄▄───▄▄───▄▄───│────
 ───▌─────▒▒───▒▒───▒▒────▌────   ──▌──────▄▀█▀█▀█▀█▀█▀█▀█▀█▀█▀▄─────▌────     ───▌─────▒▒───▒▒───▒▒────▌────
 ───▌──▄▀█▀█▀█▀█▀█▀█▀█▀▄───▌──── ───▌────▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄───▋────    ───▌──▄▀█▀█▀█▀█▀█▀█▀█▀▄───▌────
▀██████████████████████████▄─     ▀██████████████████████████████████████▄─     ▀██████████████████████████▄─
──▀███████████████████████▀──    ──▀███████████████████████████████████▀──     ──▀████████████████████████▀──
▒▒▒▒▒████████████████████▒▒▒▒▒▒▒▒▒▒▒▒▒████████████████████████████████▒▒▒▒▒▒▒▒▒▒▒▒▒██████████████████████▒▒▒▒▒▒▒▒
▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒
    """)


# esta funcion guarda todo lo que lleva el inicio del juego
def reglas():
    print("""
        𝐁𝐢𝐞𝐧𝐯𝐞𝐧𝐢𝐝𝐨 𝐚𝐥 𝐣𝐮𝐞𝐠𝐨 𝐝𝐞 𝐛𝐚𝐭𝐚𝐥𝐥𝐚 𝐧𝐚𝐯𝐚𝐥, 𝐞𝐬𝐭𝐚𝐬 𝐬𝐨𝐧 𝐥𝐚𝐬 𝐫𝐞𝐠𝐥𝐚𝐬 𝐝𝐞𝐥 𝐣𝐮𝐞𝐠𝐨:

        𝟏) 𝐄𝐥 𝐭𝐚𝐛𝐥𝐞𝐫𝐨 𝐞𝐬 𝟓𝐱𝟓 (𝐟𝐢𝐥𝐚𝐬 𝐲 𝐜𝐨𝐥𝐮𝐦𝐧𝐚𝐬)
        𝟐) 𝐋𝐚𝐬 𝐟𝐢𝐥𝐚𝐬 𝐬𝐨𝐧 𝐧𝐮𝐦é𝐫𝐢𝐜𝐚𝐬 𝐝𝐞𝐥 (𝟏-𝟓) 𝐲 𝐥𝐚𝐬 𝐜𝐨𝐥𝐮𝐦𝐧𝐚𝐬 𝐚𝐥𝐟𝐚𝐛é𝐭𝐢𝐜𝐚𝐬 (𝐀-𝐄)
        𝟑) 𝐂𝐚𝐝𝐚 𝐣𝐮𝐠𝐚𝐝𝐨𝐫 𝐭𝐢𝐞𝐧𝐞 𝐮𝐧𝐚 𝐟𝐥𝐨𝐭𝐚 𝐝𝐞 𝟑 𝐛𝐚𝐫𝐜𝐨𝐬, 𝐥𝐨𝐬 𝐜𝐮𝐚𝐥𝐞𝐬 𝐬𝐞 𝐮𝐛𝐢𝐜𝐚𝐧 𝐞𝐧 𝐞𝐥 𝐭𝐚𝐛𝐥𝐞𝐫𝐨
        𝟒) 𝐏𝐚𝐫𝐚 𝐮𝐛𝐢𝐜𝐚𝐫 𝐮𝐧 𝐛𝐚𝐫𝐜𝐨 𝐬𝐞 𝐞𝐥𝐢𝐠𝐞 𝐥𝐚 𝐢𝐧𝐭𝐞𝐫𝐬𝐞𝐜𝐜𝐢ó𝐧 𝐝𝐞 𝐥𝐚𝐬 𝐟𝐢𝐥𝐚𝐬 𝐲 𝐜𝐨𝐥𝐮𝐦𝐧𝐚𝐬 𝐄𝐣𝐞𝐦𝐩𝐥𝐨 (𝟑 𝐂)
        𝟓) 𝐄𝐥 𝐦𝐚𝐩𝐚 𝐝𝐞𝐥 𝐜𝐨𝐧𝐭𝐫𝐢𝐧𝐜𝐚𝐧𝐭𝐞 𝐞𝐬𝐭á 𝐨𝐜𝐮𝐥𝐭𝐨 𝐲 𝐭𝐢𝐞𝐧𝐞𝐬 𝐪𝐮𝐞 𝐝𝐞𝐫𝐫𝐢𝐛𝐚𝐫 𝐬𝐮𝐬 𝐞𝐦𝐛𝐚𝐫𝐜𝐚𝐜𝐢𝐨𝐧𝐞𝐬
        𝟔) 𝐄𝐧 𝐭𝐨𝐭𝐚𝐥 𝐡𝐚𝐲 𝟒 𝐢𝐧𝐝𝐢𝐜𝐚𝐝𝐨𝐫𝐞𝐬 𝐪𝐮𝐞 𝐭𝐞 𝐚𝐲𝐮𝐝𝐚𝐫á𝐧 𝐚 𝐨𝐫𝐢𝐞𝐧𝐭𝐚𝐫𝐭𝐞 𝐞𝐧 𝐞𝐥 𝐣𝐮𝐞𝐠𝐨
        𝟕) 𝐈𝐧𝐝𝐢𝐜𝐚𝐝𝐨𝐫 𝐝𝐞 𝐚𝐠𝐮𝐚(🌊) 𝐄𝐬𝐭𝐞 𝐢𝐧𝐝𝐢𝐜𝐚𝐝𝐨𝐫 𝐞𝐬 𝐞𝐥 𝐩𝐫𝐢𝐧𝐜𝐢𝐩𝐚𝐥 𝐢𝐧𝐝𝐢𝐜𝐚𝐧𝐝𝐨 𝐞𝐥 𝐞𝐬𝐩𝐚𝐜𝐢𝐨 𝐪𝐮𝐞 𝐭𝐢𝐞𝐧𝐞𝐬 𝐞𝐧 𝐞𝐥 𝐭𝐚𝐛𝐥𝐞𝐫𝐨
        𝟖) 𝐈𝐧𝐝𝐢𝐜𝐚𝐝𝐨𝐫 𝐝𝐞 𝐛𝐚𝐫𝐜𝐨(🚢) 𝐄𝐬𝐭𝐞 𝐬𝐢𝐫𝐯𝐞 𝐩𝐚𝐫𝐚 𝐩𝐨𝐬𝐢𝐜𝐢𝐨𝐧𝐚𝐫 𝐭𝐮𝐬 𝐞𝐦𝐛𝐚𝐫𝐜𝐚𝐜𝐢𝐨𝐧𝐞𝐬 𝐞𝐧 𝐞𝐥 𝐭𝐚𝐛𝐥𝐞𝐫𝐨
        𝟗) 𝐈𝐧𝐝𝐢𝐜𝐚𝐝𝐨𝐫 𝐝𝐞 𝐜𝐚𝐥𝐚𝐯𝐞𝐫𝐚 (💥) 𝐄𝐬𝐭𝐞 𝐢𝐧𝐝𝐢𝐜𝐚𝐝𝐨𝐫 𝐯𝐚 𝐚 𝐚𝐩𝐚𝐫𝐞𝐜𝐞𝐫 𝐜𝐮𝐚𝐧𝐝𝐨 𝐝𝐞𝐫𝐫𝐢𝐛𝐞𝐬 𝐮𝐧 𝐛𝐚𝐫𝐜𝐨 𝐞𝐧𝐞𝐦𝐢𝐠𝐨 𝐨 𝐮𝐧 𝐛𝐚𝐫𝐜𝐨 𝐭𝐮𝐲𝐨 𝐬𝐞𝐚 𝐝𝐞𝐫𝐫𝐢𝐛𝐚𝐝𝐨
        𝟏𝟎) 𝐈𝐧𝐝𝐢𝐜𝐚𝐝𝐨𝐫 𝐝𝐞 𝐞𝐫𝐫𝐨𝐫 (⛔) 𝐄𝐬𝐭𝐞 𝐢𝐧𝐝𝐢𝐜𝐚𝐝𝐨𝐫 𝐚𝐩𝐚𝐫𝐞𝐜𝐞 𝐜𝐮𝐚𝐧𝐝𝐨 𝐟𝐚𝐥𝐥𝐚𝐬 𝐮𝐧 𝐭𝐢𝐫𝐨 𝐨 𝐞𝐥 𝐜𝐨𝐧𝐭𝐫𝐢𝐧𝐜𝐚𝐧𝐭𝐞 𝐟𝐚𝐥𝐥𝐚 𝐬𝐮 𝐭𝐢𝐫𝐨

        𝐄𝐥 𝐣𝐮𝐞𝐠𝐨 𝐭𝐞𝐫𝐦𝐢𝐧𝐚 𝐜𝐮𝐚𝐧𝐝𝐨 𝐮𝐧𝐨 𝐝𝐞 𝐥𝐨𝐬 𝐝𝐨𝐬 𝐛𝐚𝐧𝐝𝐨𝐬 𝐪𝐮𝐞𝐝𝐞 𝐬𝐢𝐧 𝐛𝐚𝐫𝐜𝐨𝐬, 𝐲 𝐬𝐞 𝐠𝐚𝐧𝐚 𝐭𝐞𝐧𝐢𝐞𝐧𝐝𝐨 𝐦í𝐧𝐢𝐦𝐨 𝟏 𝐛𝐚𝐫𝐜𝐨 𝐚 𝐟𝐥𝐨𝐭𝐞

                                        ⚓¡𝐁𝐔𝐄𝐍𝐀 𝐒𝐔𝐄𝐑𝐓𝐄, 𝐌𝐀𝐑𝐈𝐍𝐄𝐑𝐎!⚓
        """)
    time.sleep(5)
    esperar_tecla()
    clear()


# esta funcion guarda todo lo que lleva el inicio del juego
def start():
    clear()  # limpiamos la terminal para que no se vea cuando el codigo lo ejecutamos en la terminal, asi se vea limpio el titulo
    mostrar_titulo()  # llamamos a la funcion que imprime el titulo
    time.sleep(
        2
    )  # de la librearia time llamamos a la funcion sleep, para que espere 2 segundo antes de ejecutar el siguiente codigo
    esperar_tecla()  # llamos a la funcion que hace que espere un espacio para continuar
    reglas()  # imprimir las reglas


# esta funcion guarda el tablero por defecto.
# podriamos simplemente reducir el codigo: [[]*5]*5] pero el problema es que si lo hacemos es dificil cambiar valores especificos, por que python guarda la misma memoria (o algo asi...)
# el punto es que si lo hacemos de esa manera no se puede modificar la matriz en un punto especifico, por que se cambia toda la matriz
def tablero_example():
    tablero = [
        ["🌊", "🌊", "🌊", "🌊", "🌊"],
        ["🌊", "🌊", "🌊", "🌊", "🌊"],
        ["🌊", "🌊", "🌊", "🌊", "🌊"],
        ["🌊", "🌊", "🌊", "🌊", "🌊"],
        ["🌊", "🌊", "🌊", "🌊", "🌊"],
    ]
    return tablero


# Funcion para mostrar el tablero los parametros son los tablero que le llegen a la funcion
# Si la funcion es llamada sin parametros imprimira por defecto el tablero de ejemplo
def mostrar_tablero(
    tablero_usuario=tablero_example(), tablero_ataque=tablero_example()
):
    print("""
            𝐓𝐔 𝐓𝐀𝐁𝐋𝐄𝐑𝐎                          𝐓𝐀𝐁𝐋𝐄𝐑𝐎 𝐃𝐄 𝐀𝐓𝐀𝐐𝐔𝐄
______________________________________  |  ________________________________________
                                        |
  |  𝐀  |  𝐁  |  𝐂  |  𝐃  |  𝐄  |            |  𝐀  |  𝐁  |  𝐂  |  𝐃  |  𝐄  |
""")
    # iteramos en cada lista de la lista grande para que se imprima una debajo de otra y se vea como un tablero
    for i in range(len(tablero_usuario)):
        print(f"{i + 1} | {tablero_usuario[i]}    |   {i + 1} | {tablero_ataque[i]}")
        # mostramos el tablero del usuario y el tablero que atacara el usuario
    print(
        "\n"
    )  # dejamos un espacio para que lo que se quiera mostrar debajo no se vea tan pegado del tablero


# funcion para pedir al usuario cordenadas
def pedir_cordenadas():
    condicion_x = "ABCDE"
    condicion_y = "12345"
    while True:
        letras = input("𝐈𝐍𝐆𝐑𝐄𝐒𝐄 𝐋𝐀𝐒 𝐂𝐎𝐎𝐑𝐃𝐄𝐍𝐀𝐃𝐀𝐒 𝐃𝐄𝐒𝐄𝐀𝐃𝐀𝐒, (𝐄𝐉𝐄𝐌𝐏𝐋𝐎 𝐃𝟏): ")
        letras = letras.upper()
        if (
            (len(letras) == 2)  # una cordenada esta formada por dos caracteres
            and (letras[0] in condicion_x)  # el primer caracter debe ser una letra
            and (
                letras[1] in condicion_y
            )  # el segundo caracter corresponde a un numero
        ):
            return letras
        elif letras == "" or " " in letras:
            print("❗𝐍𝐎 𝐇𝐀𝐒 𝐈𝐍𝐆𝐑𝐄𝐒𝐀𝐃𝐎 𝐂𝐎𝐎𝐑𝐃𝐄𝐍𝐀𝐃𝐀𝐒 ❗")

        elif (
            letras != condicion_x or letras != condicion_y
        ):  # si no se ingresa una cordenada, se le avisa al usuario y se vuevle a pedir
            print(
                "❗𝐈𝐍𝐆𝐑𝐄𝐒𝐀𝐒𝐓𝐄 𝐔𝐍 𝐂𝐀𝐑𝐀𝐂𝐓𝐄𝐑 𝐈𝐍𝐂𝐎𝐑𝐑𝐄𝐂𝐓𝐎. ¡𝐈𝐍𝐆𝐑𝐄𝐒𝐀 𝐔𝐍𝐀 𝐂𝐎𝐎𝐑𝐃𝐄𝐍𝐀𝐃𝐀 𝐂𝐎𝐑𝐑𝐄𝐂𝐓𝐀! ❗:"
            )


# funcion que traduce cordenadas en indices para utilizar en el codigo, o de indices a cordenadas
def traductor_cordenadas(val):
    condicion_x = "ABCDE"
    condicion_y = "12345"
    # si es una tupla la funcion detecta que le llego como parametro dos indices
    if type(val) == tuple:
        i_1, i_2 = val  # desempaquetamos los indices
        cordenadas = (
            condicion_x[i_2] + condicion_y[i_1]
        )  # escribimos la cordenada teniendo en cuenta, que el usuario escribe primero columnas y luego filas, pero el codigo lee indices como primero filas y luego columnas, por lo que ay que invertir los indices
        return cordenadas  # devolvemos un string con la cordenada
    else:  # de lo contrario sabemos que el parametro que llegan son cordenadas, por lo que traduciremos a indices
        for i in range(len(condicion_x)):  # iteramos 5 veces
            if (
                condicion_x[i] == val[0]
            ):  # si encontramos la misma letra que ingreso el usuario en la condicion_x, significa que encontramos el indice para esa letra en especi
                index_2 = i  # el usuario escribe primero columnas y luego filas, pero en index es alreves por lo que el indice ay que invertirlo

        # repetimos lo mismo con el numero de la cordenada osea la fila, pero sabiendo que seria el primer index
        for i in range(len(condicion_x)):
            if condicion_y[i] == val[1]:
                index_1 = i

        return index_1, index_2  # devolvemos los indices


# funciones que generan los barcos
# -------------------------------------------------------------------
# funcion que genera los barcos de maquina
def posiciones_IA():
    IA = tablero_example()
    contador = 3  # tiene 3 barcos
    while contador > 0:  # mientras ayan barcos que los siga creando
        # generamos los index de manera aleatoria
        i_1 = random.randint(0, 4)
        i_2 = random.randint(0, 4)
        if (
            IA[i_1][i_2] != "🚢"
        ):  # si el espacio esta vasio osea no ay barcos, si los puede dibujar
            IA[i_1][i_2] = "🚢"
            contador -= 1  # restamos un barco, hasta que ya no quede mas que poner
    print("¡𝐄𝐋 𝐎𝐏𝐎𝐍𝐄𝐍𝐓𝐄 𝐇𝐀 𝐏𝐎𝐒𝐈𝐂𝐈𝐎𝐍𝐀𝐃𝐎 𝐓𝐎𝐃𝐎𝐒 𝐒𝐔𝐒 𝐁𝐀𝐑𝐂𝐎𝐒!")
    return IA


# funcion que genera los barcos del usuario
def posiciones_usuario():
    tablero = tablero_example()  # tomamos el tablero por defecto osea el tablero vasio para empezar a llenarlo de barcos
    contador = 3  # de nuevo tenemos 3 barcos para posicionar
    while contador > 0:
        if (
            contador == 1
        ):  # si el contador es igual a uno que diga barco en vez de barcos
            print(f"¡𝐓𝐄 𝐐𝐔𝐄𝐃𝐀 {contador} 𝐁𝐀𝐑𝐂𝐎 𝐏𝐎𝐑 𝐏𝐎𝐒𝐈𝐂𝐈𝐎𝐍𝐀𝐑!")
        else:
            print(f"¡𝐓𝐄 𝐐𝐔𝐄𝐃𝐀𝐍 {contador} 𝐁𝐀𝐑𝐂𝐎𝐒 𝐏𝐎𝐑 𝐏𝐎𝐒𝐈𝐂𝐈𝐎𝐍𝐀𝐑!")

        # desempaquetamos los indices que utilizaremos para generar los barcos
        i_1, i_2 = traductor_cordenadas(
            pedir_cordenadas()
        )  # llamamos a la funcion pedir cordenadas, y pasamos ese parametro al traductor de cordenadas para que las convierta en indices para luego ser desempaquetadas
        clear()  # limpiamos la terminal para luego muestre la nmueva posicion del barco recien ingresado
        if tablero[i_1][i_2] != "🚢":  # Si no ay un barco ay si se puede dibujar
            tablero[i_1][i_2] = "🚢"
            contador -= 1
            mostrar_tablero(
                tablero
            )  # mostramos el tablero con el cambio recien ingreado
        else:  # si ay un barco, avisarle al usuario que ingreso un lugar que ya fue ingresado y volver al bucle
            mostrar_tablero(tablero)
            print("❗𝐘𝐀 𝐇𝐀𝐒 𝐈𝐍𝐆𝐑𝐄𝐒𝐀𝐃𝐎 𝐀𝐍𝐓𝐄𝐒 𝐄𝐒𝐓𝐀 𝐏𝐎𝐒𝐈𝐂𝐈𝐎𝐍❗")
    # devolvemos el tablero con los cambios que se hicieron
    return tablero


# -------------------------------------------------------------------------------------------------------


# funciones que generan los ataques
# ----------------------------------------------------------------------------------------------------
# funcion que genera los ataques de la IA
# toma una tablero para evaluar, cuando el juego se este ejecutando es necesario que constantemente el tablero pase por esta funcion para evaluarla constantemte y saber si es posible atacar en esa posicion
def posiciones_ataque_IA(tablero):
    while True:  # bucle infinito
        # generamos los indices de manera aleatorio, obviamente que correspondan a la matriz 5 * 5
        i_1 = random.randint(0, 4)
        i_2 = random.randint(0, 4)
        # si en la posicion no ay ningun ataque los indices son correctos
        if tablero[i_1][i_2] != "⛔" and tablero[i_1][i_2] != "💥":
            return i_1, i_2
            # retornamos los indices y el return actua como break para el bucle infinito


# funcion que genera los ataques del usuario
# toma como parametro un tablero al igual que la anterior funcion, pero en este caso evaluaria el tablero de la maquina, ya que ese es el que el usuario quiere atacar
def posiciones_ataque_usuario(tablero):
    print("¡𝐇𝐎𝐑𝐀 𝐃𝐄 𝐀𝐓𝐀𝐂𝐀𝐑!")
    while True:
        # pedimos al usuario las cordenadas y las traducimos a indices que seran desempaquetados
        i_1, i_2 = traductor_cordenadas(pedir_cordenadas())
        # si ya hubo un ataque, hacerselo saber al usuario y volver al ciclo
        if tablero[i_1][i_2] == "⛔" or tablero[i_1][i_2] == "💥":
            print("❗𝐘𝐀 𝐇𝐀𝐒 𝐈𝐍𝐆𝐑𝐄𝐒𝐀𝐃𝐎 𝐀𝐍𝐓𝐄𝐒 𝐄𝐒𝐓𝐀 𝐏𝐎𝐒𝐈𝐂𝐈𝐎𝐍❗")
        else:  # de lo contrario los indices son validos para atacar y ser utilizados luego
            clear()  # limpiamos la terminal para que se siga el transcurso del juego
            return i_1, i_2


# funcion que verifica si el ataque dio en un barco o no
# debemos pedir tres parametros:
# tablero_examinar: es necesario por que por ejemplo en el caso de la maquina, su tablero real no se muesta al usuario, asi que este tablero sirve para evaluar
# tablero_real: por el contrario el tablero real si es el que se muestra al usuario osea el tablero de ataque, y en se debe dibujar en los dos tableros el ataque
def verificar_ataque(tablero_examinar, tablero_real, index):
    # los indices llegaran como tuplas, ya que las demas funciones que devuelven indices lo hacen en tuplas por lo que tendran que ser desempaquetadas
    index_1, index_2 = index
    # si encuentra un barco el dissparo acerto, por lo que se dibuja una explocion
    if "🚢" in tablero_examinar[index_1][index_2]:
        # es necesario tambien agregar el diseño al tablero examina, por que aunque este no se muestra al usuario otras funciones si evaluan si este tiene estos iconos
        tablero_examinar[index_1][index_2] = "💥"
        tablero_real[index_1][index_2] = "💥"
        condicion = True
    else:  # de lo contrario sabemos que no acerto el disparo y lo representamos con ese simbolo
        tablero_examinar[index_1][index_2] = "⛔"
        tablero_real[index_1][index_2] = "⛔"
        condicion = False
        # retornamos el tablero que si se va a mostrar, los indices como llegaron osea como tupla, y condicion que es un extra que agregamos para un if que dice algo especifico al usuario si le destruyeron un barco o no
        # Y no podemos poner el print aqui mismo, porque el print depende si es un mensaje de destruccion de la maquina al usuario o al revez
    return tablero_real, index, condicion


# ----------------------------------------------------------------------------------------------------------------


# funcion que verifica si el tablero que se esta evaluando gano o no
def verificar_ganador(tablero):
    # iteramos en cada fila buscando un barco, con tan solo encontrar uno sabemos que todavia no se a ganado
    for fila in tablero:
        if "🚢" in fila:
            return False
    return True


# ---------------------------------------------------------------------------------------------------------------


# funcion principal del juego
def battelship():
    start()  # llamamos a la funcion start con todo el titulo y todo las cosas del inicio del juego
    mostrar_tablero()  # mostramos el tablero para que pueda ver como es tablero y que seleccionar
    tablero_user = (
        posiciones_usuario()
    )  # guardamos las posiciones de los barcos del usuario
    tablero_IA = posiciones_IA()  # guardamos las posiciones de la maquina
    tablero_ataque = tablero_example()  # generamos el tablero de tablero que atacara el usuario, con el tablero vasio de ejemplo

    # logica del juego
    # -----------------------------------------------------------------------------------------------------------------------
    while True:
        # ataque jugador
        # --------------------------------------------------------------------------------------------------------------
        # llamamos a la funcion verificar ataque, recordemos que esta toma dos tableros en el caso del ataque del jugador el que evalua: el tablero_IA. y el que realmente se muestra: tablero_ataque. ademas esta funcion necesita los indices para verificar el ataque, asi que los toma de posiciondes_ataque_usuario, uqe ya explicamos...
        # verificar_ataque devulve tres valores, asi que los desempaquetamos, pero recordemos que el index es una tupla
        tablero_ataque, index, condicion = verificar_ataque(
            tablero_IA, tablero_ataque, posiciones_ataque_usuario(tablero_IA)
        )
        # la funcion nos devuelve el tablero con los cambios
        mostrar_tablero(
            tablero_user, tablero_ataque
        )  # mostrar_tablero toma dos parametros y el tablero de ataque lo recibimos de la funcion anterior
        if condicion:  # la funcion tambien devuelve una condicion de la que hablamos en la linea 248 para imprimir si destruyo o no un barco
            # index como mencionamos es una tupla con los indices, perfecto para como funciona el traductor de cordenadas que ya hemos mencionado
            # de esa manera le mostramos al usuario que cordenada es la que ataco (solo por diseño)
            print(
                f"💥¡𝐇𝐀𝐒 𝐀𝐓𝐀𝐂𝐀𝐃𝐎 𝐋𝐀𝐒 𝐂𝐎𝐎𝐑𝐃𝐄𝐍𝐀𝐃𝐀𝐒 {traductor_cordenadas(index)}, 𝐘 𝐃𝐄𝐒𝐓𝐑𝐔𝐈𝐒𝐓𝐄 𝐔𝐍 𝐁𝐀𝐑𝐂𝐎 𝐃𝐄 𝐓𝐔 𝐎𝐏𝐎𝐍𝐄𝐍𝐓𝐄💥"
            )
        else:
            print(
                f"🌊¡𝐇𝐀𝐒 𝐀𝐓𝐀𝐂𝐀𝐃𝐎 𝐋𝐀𝐒 𝐂𝐎𝐎𝐑𝐃𝐄𝐍𝐀𝐃𝐀𝐒 {traductor_cordenadas(index)} . 𝐏𝐄𝐑𝐎 𝐂𝐀𝐘Ó 𝐀𝐋 𝐀𝐆𝐔𝐀!🌊"
            )

        # verificamos si la maquina ha ganado, si es correcto que salga del bucle osea del juego
        if verificar_ganador(tablero_IA):
            clear()
            print(
                """
                                    🏆¡𝐇𝐀𝐒 𝐇𝐔𝐍𝐃𝐈𝐃𝐎 𝐓𝐎𝐃𝐎𝐒 𝐋𝐎𝐒 𝐁𝐀𝐑𝐂𝐎𝐒 𝐃𝐄 𝐓𝐔 𝐎𝐏𝐎𝐍𝐄𝐍𝐓𝐄! ¡𝐆𝐀𝐍𝐀𝐒𝐓𝐄! 🏆

                """
            )
            break
        # -------------------------------------------------------------------------------------------------------------------------
        # intermedio de ataque
        # imprimos un medio tiempo para que el usuario lea y vea que ataco, con la excusa que el oponente esta pensando
        print("¡𝐓𝐔 𝐎𝐏𝐎𝐍𝐄𝐍𝐓𝐄 𝐒𝐄 𝐄𝐒𝐓Á 𝐏𝐑𝐄𝐏𝐀𝐑𝐀𝐍𝐃𝐎 𝐏𝐀𝐑𝐀 𝐀𝐓𝐀𝐂𝐀𝐑! . . .")
        time.sleep(3)
        clear()
        # --------------------------------------------------------------------------------------------------------------------------

        # ataque maquina
        # ---------------------------------------------------------------------------------------------------------------------------
        # hacemos lo mismo que con el ataque del usuario pero esta vez el tablero a evaluar (atacar) es el tablero del usuario,
        # si vemos el tablero user se repite como parametro dos veces, debido a que el tablero a evaluar y el tablero a mostrar es el mismo a diferencia del el caso del ataque del usuario
        tablero_user, index, condicion = verificar_ataque(
            tablero_user, tablero_user, posiciones_ataque_IA(tablero_user)
        )
        mostrar_tablero(
            tablero_user, tablero_ataque
        )  # volvemos a mostrar el tablero con el cambio del tablero del usuario, osea el ataque
        # con la condicion la utilizamos igual que con el ataque del usuario pero con mensajes diferentes
        if condicion:
            print(
                f"💥¡𝐓𝐔 𝐎𝐏𝐎𝐍𝐄𝐍𝐓𝐄 𝐇𝐀 𝐃𝐄𝐒𝐓𝐑𝐔𝐈𝐃𝐎 𝐔𝐍𝐎 𝐃𝐄 𝐓𝐔𝐒 𝐁𝐀𝐑𝐂𝐎𝐒 𝐄𝐍 𝐋𝐀𝐒 𝐂𝐎𝐎𝐑𝐃𝐄𝐍𝐀𝐃𝐀𝐒 {traductor_cordenadas(index)}!💥"
            )
        else:
            print(
                f"🌊¡𝐓𝐔 𝐎𝐏𝐎𝐍𝐄𝐍𝐓𝐄 𝐀𝐓𝐀𝐂Ó 𝐄𝐍 𝐋𝐀𝐒 𝐂𝐎𝐎𝐑𝐃𝐄𝐍𝐀𝐃𝐀𝐒 {traductor_cordenadas(index)}. 𝐏𝐄𝐑𝐎 𝐂𝐀𝐘Ó 𝐀𝐋 𝐀𝐆𝐔𝐀!🌊"
            )

        # verificamos si el jugador gano
        if verificar_ganador(tablero_user):
            clear()
            print("""
                                    ☠️¡𝐓𝐔 𝐎𝐏𝐎𝐍𝐄𝐍𝐓𝐄 𝐇𝐀 𝐇𝐔𝐍𝐃𝐈𝐃𝐎 𝐓𝐎𝐃𝐎𝐒 𝐓𝐔𝐒 𝐁𝐀𝐑𝐂𝐎𝐒! ¡𝐏𝐄𝐑𝐃𝐈𝐒𝐓𝐄!☠️
            """)
            break

    # esperamos 3 segundo para que se lea el mensaje de si ganaste o perdiste
    time.sleep(3)
    clear()  # limpiamos terminal para que al terminar el juego se vea mas limpio (solo pór diseño)


# -------------------------------------------------------------------------------------------------------------------


# Está funcion permite que cuando termine de ejecutarse el codigo preguntemos al usuario quieres volver a jugar
# lo haremos por medio de un bucle while con condicional True
def volver_a_empezar():
    while True:
        # con un input en la variable desicion preguntamos si quieres volver a jugar, esperando recibir un string con
        # si o no
        desicion = input("""

                                                ⚓¿𝐐𝐔𝐈𝐄𝐑𝐄𝐒 𝐕𝐎𝐋𝐕𝐄𝐑 𝐀 𝐉𝐔𝐆𝐀𝐑? (𝐒𝐈/𝐍𝐎) ⚓
                         """)
        desicion = (
            desicion.upper()
        )  # convertimos el string a mayúsculas (tambien se puede hacer con lower)
        if (
            desicion == "SI"
        ):  # si el usuario responde SI, volvemos a llamar a la funcion battelship para que se vuelva a ejecutar el juego
            battelship()
        elif (
            desicion == "NO"
        ):  # si el usuario responde NO, salimos del bucle e imprimimos el mensaje de despedida
            mostrar_titulo()
            print("""
                                                  ⚓¡𝐆𝐑𝐀𝐂𝐈𝐀𝐒 𝐏𝐎𝐑 𝐉𝐔𝐆𝐀𝐑, 𝐂𝐀𝐌𝐀𝐑𝐀𝐃𝐀!⚓
            """)

            break
        else:
            clear()
            print("""
                                                 ❗𝐈𝐍𝐆𝐑𝐄𝐒𝐀 𝐔𝐍𝐀 𝐑𝐄𝐒𝐏𝐔𝐄𝐒𝐓𝐀 𝐕𝐀𝐋𝐈𝐃𝐀 ❗
                  """)  # Si el usuario pone algo diferente imprimimos un mensaje y volvemos a preguntar
            time.sleep(1)
            clear()


battelship()
volver_a_empezar()  # Ejecutamos tanto la funcion battelship como la funcion volver_a_empezar para que se ejecute el juego

