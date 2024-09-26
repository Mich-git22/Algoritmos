import tkinter as tk
from tkinter import messagebox
import random
import time

# Palabras y sus pistas correspondientes para el juego (usando dict)
categories: dict[str, dict[str, str]] = {
    'fácil': {
        'función': 'Bloque de código que realiza una tarea específica',
        'variable': 'Espacio para almacenar un valor',
        'bucle': 'Estructura que repite un bloque de código'
    },
    'intermedio': {
        'módulo': 'Archivo que contiene definiciones de funciones y variables',
        'clase': 'Plantilla para crear objetos en programación orientada a objetos',
        'booleano': 'Tipo de dato que puede ser verdadero o falso'
    },
    'difícil': {
        'programación': 'Conjunto de instrucciones para una computadora',
        'abstracción': 'Concepto en programación orientada a objetos',
        'algoritmo': 'Conjunto de pasos para resolver un problema'
    }
}

# Datos del jugador
player_data: dict[str, int] = {
    'name': '',
    'score': 0,
    'level': 1
}

# Variables del juego
word: str = ''
guessed_letters: list[str] = []
attempts: int = 6
hint_used: bool = False  # Variable para verificar si se ha usado la pista
start_time: float = 0.0


# Función para mostrar un mensaje en una nueva ventana
def show_message(title: str, message: str) -> None:
    message_window: tk.Toplevel = tk.Toplevel(root)
    message_window.title(title)
    lbl_message: tk.Label = tk.Label(message_window, text=message, padx=10, pady=10)
    lbl_message.pack()
    btn_close: tk.Button = tk.Button(message_window, text="Cerrar", command=message_window.destroy)
    btn_close.pack(pady=10)


# Función para comenzar un nuevo juego
def new_game(difficulty: str = 'fácil') -> None:
    global word, guessed_letters, attempts, hint_used, start_time
    word = random.choice(list(categories[difficulty].keys()))
    guessed_letters = ['_' for _ in word]

    # Ajustar intentos según dificultad
    difficulty_settings = {'fácil': 8, 'intermedio': 6, 'difícil': 4}
    attempts = difficulty_settings[difficulty]
    hint_used = False  # Reiniciar uso de pistas
    start_time = time.time()  # Iniciar el temporizador

    lbl_word.config(text=' '.join(guessed_letters))
    lbl_attempts.config(text=f"Intentos restantes: {attempts}")
    lbl_message.config(text="¡Adivina la palabra!")
    lbl_score.config(text=f"Puntaje: {player_data['score']}")
    btn_start.pack_forget()  # Ocultar botón de comenzar
    lbl_word.pack()  # Mostrar la palabra
    lbl_attempts.pack()  # Mostrar intentos
    entry_letter.pack()  # Mostrar entrada de letra
    btn_check.pack()  # Mostrar botón de verificar
    lbl_message.pack()  # Mostrar mensaje
    lbl_score.pack()  # Mostrar puntaje
    btn_hint.pack()  # Mostrar botón de pista

    # Mostrar el nivel actual
    show_message("Nivel Actual", f"Estás en el nivel: {difficulty}")


# Función para mostrar las instrucciones
def show_instructions() -> None:
    instructions: str = """
    Bienvenido al juego del ahorcado.

    Reglas:
    - Tienes intentos para adivinar la palabra secreta.
    - Puedes adivinar una letra a la vez.
    - Cada error te costará un intento.
    - Ganas si adivinas todas las letras.
    - Puedes usar una pista una vez por juego.
    """
    messagebox.showinfo("Instrucciones", instructions)


# Función para verificar la letra ingresada
def check_letter() -> None:
    global attempts
    letter: str = entry_letter.get().lower()

    if len(letter) != 1 or not letter.isalpha():
        lbl_message.config(text="Por favor, ingresa una letra válida.")
        return

    if letter in word:
        for i, l in enumerate(word):
            if l == letter:
                guessed_letters[i] = letter
        lbl_word.config(text=' '.join(guessed_letters))
        lbl_message.config(text="¡Correcto!")
    else:
        attempts -= 1
        lbl_attempts.config(text=f"Intentos restantes: {attempts}")
        lbl_message.config(text="¡Incorrecto!")

    entry_letter.delete(0, tk.END)
    check_win()


# Función para dar la pista
def give_hint() -> None:
    global hint_used
    if not hint_used:
        hint: str = categories['fácil'][word]  # Cambia 'fácil' si tienes múltiples categorías
        show_message("Pista", f"Pista: {hint}")
        hint_used = True  # Marcar que se ha usado la pista
    else:
        messagebox.showwarning("Sin Pistas", "Ya has usado la pista en este juego.")


# Función para verificar si ganó o perdió
def check_win() -> None:
    if '_' not in guessed_letters:
        elapsed_time = time.time() - start_time
        score_increase = max(100 - int(elapsed_time), 0)  # Puntaje basado en el tiempo
        player_data['score'] += score_increase
        player_data['level'] += 1
        show_message("¡Felicidades!", f"Adivinaste la palabra: {word}. Nivel {player_data['level']}")
        lbl_score.config(text=f"Puntaje: {player_data['score']}")

        # Incrementar dificultad según puntaje
        if player_data['score'] > 500:
            current_difficulty = 'difícil'
        elif player_data['score'] > 250:
            current_difficulty = 'intermedio'
        else:
            current_difficulty = 'fácil'

        new_game(current_difficulty)  # Reiniciar el juego con nueva dificultad
    elif attempts == 0:
        show_message("Juego Terminado", f"Buen intento. La palabra era: {word}. Fin del juego.")


# Función para guardar el historial de partidas
def save_history() -> None:
    with open('game_history.txt', 'a') as file:
        file.write(f"{player_data['name']}: {player_data['score']}, {player_data['level']}\n")


# Función para salir del juego
def exit_game() -> None:
    save_history()  # Guardar historial antes de salir
    root.quit()


# Crear la ventana principal
root: tk.Tk = tk.Tk()
root.title("Juego del Ahorcado")

# Widgets de la interfaz gráfica
lbl_welcome: tk.Label = tk.Label(root, text="¡Bienvenido al juego del ahorcado!")
lbl_welcome.pack()

# Botón para comenzar el juego
btn_start: tk.Button = tk.Button(root, text="Comenzar", command=lambda: new_game())
btn_start.pack()

# Widgets del juego
lbl_word: tk.Label = tk.Label(root, text="_ _ _ _ _")
lbl_attempts: tk.Label = tk.Label(root, text="Intentos restantes: 6")
entry_letter: tk.Entry = tk.Entry(root)
btn_check: tk.Button = tk.Button(root, text="Verificar letra", command=check_letter)
lbl_message: tk.Label = tk.Label(root, text="Adivina la palabra")
lbl_score: tk.Label = tk.Label(root, text="Puntaje: 0")
btn_exit: tk.Button = tk.Button(root, text="Salir", command=exit_game)

# Botón de pista
btn_hint: tk.Button = tk.Button(root, text="Obtener Pista", command=give_hint)

# Agregar el botón de instrucciones
btn_instructions: tk.Button = tk.Button(root, text="Instrucciones", command=show_instructions)
btn_instructions.pack()

# Agregar el botón de salir
btn_exit.pack()

root.mainloop()
