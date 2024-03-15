import random

def seleccionar_palabra():
    """Selecciona una palabra aleatoria de una lista predefinida."""
    palabras = ["python", "programacion", "juego", "computadora", "tecnologia", "inteligencia"]
    return random.choice(palabras)

def adivinar_palabra(palabra_secreta):
    """Función principal para adivinar la palabra."""
    longitud_palabra = len(palabra_secreta)
    letras_adivinadas = ["_"] * longitud_palabra
    intentos = 0
    
    print("¡bienvenido al juego de adivinar la palabra!")
    print("la palabra tiene", longitud_palabra, "letras.")
    print(" ".join(letras_adivinadas))  # Mostrar las letras adivinadas hasta el momento
    
    while "_" in letras_adivinadas:
        letra = input("Adivina una letra: ").lower()
        
        if len(letra) != 1 or not letra.isalpha():
            print("Por favor ingresa una única letra válida.")
            continue
        
        if letra in palabra_secreta:
            for i in range(longitud_palabra):
                if palabra_secreta[i] == letra:
                    letras_adivinadas[i] = letra
            print("¡Correcto!")
        else:
            print("¡Incorrecto!")
        
        print(" ".join(letras_adivinadas))
        intentos += 1
    
    print("¡felicidades! has adivinado la palabra en", intentos, "intentos.")

# Llamada a las funciones para iniciar el juego
palabra_secreta = seleccionar_palabra()
adivinar_palabra(palabra_secreta)
