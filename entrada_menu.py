def pedir_numero(invitacion, MIN, MAX):
    invitacion += "entre " + str(MIN) + " y " + str(MAX) + ": "

    while True:
        entrada = input(invitacion)
        try:
            entrada = int(entrada)
        except:
            pass
        else: 
            if MIN <= entrada <= MAX:
                break
    return entrada




    






