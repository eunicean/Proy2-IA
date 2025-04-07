from agent import mastermindGameAgent
import random

colors = ['azul', 'rojo', 'blanco', 'negro', 'verde',  'purpura']

#modo automático
def modo_automatico():
    
    print("Colores disponibles:", ", ".join(colors))
    while True:
        entrada = input("Ingresa la combinación secreta (4 colores separados por coma): ").strip().lower()
        secret = tuple(map(str.strip, entrada.split(',')))
        if len(secret) == 4 and all(c in colors for c in secret):
            print(f"(Modo automático) La combinación secreta es: {secret}")
            break
        print("Entrada inválida. Asegúrate de ingresar 4 colores válidos separados por coma.")

    solver = mastermindGameAgent(colors)
    guess = solver.next_guess()

    while guess:
        feedback = solver.feedback(guess, secret)
        print(f"Intento #{solver.attempts + 1}: {guess}\n  - Fichas exactas: {feedback[0]}\n  - Posición incorrecta: {feedback[1]}")
        if feedback[0] == 4:
            break
        solver.update_knowledge(guess, feedback)
        guess = solver.next_guess()

    print("\n--------------------------------------------------------------------------")
    print(f"INTENTOS -> {solver.attempts + 1}")
    print(" Combinación secreta:", secret)
    print(" Evolución del espacio de búsqueda (combinaciones restantes):")
    for i in range(len(solver.history)):
        print(f"  -> Intento #{i+1} - {solver.history[i]} combinaciones disponibles")
    print("--------------------------------------------------------------------------")

# TODO: modo tiempo real
def modo_tiempo_real():
    return

  

menu = True
while(menu):
    print("+--------------------------------------------------------------+")
    print("|                       MASTERMIND GAME                        |")
    print("+--------------------------------------------------------------+")
    print("Selecciona el modo:")
    print("1. Modo Automático")
    print("2. Modo Tiempo Real")
    print("3. Salir")
    mode = input(" -> ").strip()

    if mode == "1":
        modo_automatico()
    elif mode == "2":
        modo_tiempo_real()
    elif mode == "3":
        menu = False
    else:
        print("Modo inválido.")

