import speech
import random as r
import time

levels = {
    "facil":["hola","perfecto","gracias"],
    "intermedio":["inteligente","sobre","licuadora"],
    "Difivil":["ininteligibile","otorrinolaringólogo","saxofon"]
}

def play_game(level):
    words = levels.get(level,[])

    if not words:
        print("Nivel de dificultad incorrecto")
        return
    score = 0
    attemps = 3

    selected_words = r.sample(words, len(words))
    
    for _ in range(len(words)):
        if attempts == 0:
            print("¡Te quedaste sin intentos!")
            break
        
        r_word = r.choice(words)
        print(f"\nPronuncie esta palabra: {r_word}")
        
        try:
            rec_word = speech.speech_es().lower()
            print(f"Usted dijo: {rec_word}")
        except:
            print("No se escuchó. Intenta de nuevo.")
            attempts -= 1
            continue

        if r_word == rec_word:
            print("¡Genial!")
            score += 1
        else:
            print(f"La palabra era {r_word}")
            attempts -= 1
        
        print(f"Intentos restantes: {attempts}")
        
        time.sleep (2)
    print(f"El juego terminó, tu puntuación es: {score}/{len(words)}")


select_level = input("Selecciona un nivel (facil/intermedio/dificil)").lower().strip()
play_game(select_level)