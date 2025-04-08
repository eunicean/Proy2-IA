from agent import mastermindGameAgent
import random
import matplotlib.pyplot as plt

colors = ['azul', 'rojo', 'blanco', 'negro', 'verde',  'purpura']

#modo automático
def modo_automatico(jugar_200_veces=False):
    histories = []
    total_attempts = 0

    partidas = 200 if jugar_200_veces else 1

    for partida in range(partidas):
        secret = tuple(random.choices(colors, k=4))
        myAgent = mastermindGameAgent(colors)
        guess = myAgent.next_guess()

        while guess:
            feedback = myAgent.feedback(guess, secret)
            if feedback[0] == 4:
                break
            myAgent.update_knowledge(guess, feedback)
            if not jugar_200_veces:
                print(f"  - Posibles combinaciones - {len(myAgent.possible_combinations)}")
            guess = myAgent.next_guess()

        total_attempts += myAgent.attempts
        histories.append(myAgent.history)

        if not jugar_200_veces:
            print("\n--------------------------------------------------------------------------")
            print(f"INTENTOS -> {myAgent.attempts}")
            print(" Combinación secreta:", secret)
            print(" Evolución del espacio de búsqueda (combinaciones restantes):")
            for i, h in enumerate(myAgent.history):
                print(f"  -> Intento #{i+1} - {h} combinaciones disponibles")
            print("--------------------------------------------------------------------------")

    # si se jugaron las 200 partidas, hacer gráfica y mostrar resumen
    if jugar_200_veces:
        # calcular promedio
        max_intentos = max(len(h) for h in histories)
        promedio_por_intento = []

        for i in range(max_intentos):
            suma = 0
            cuenta = 0
            for h in histories:
                if i < len(h):
                    suma += h[i]
                    cuenta += 1
            promedio = suma / cuenta if cuenta else 0
            promedio_por_intento.append(promedio)

        # Grafico
        promedio_intentos = total_attempts / partidas
        print(f"\n Promedio de intentos para resolver el juego en 200 partidas: {promedio_intentos:.2f}")

        # promedio de intentos del espacio por intento
        plt.figure(figsize=(10, 6))
        x_vals = range(1, len(promedio_por_intento) + 1)
        plt.bar(x_vals, promedio_por_intento, color='#ffafcc')

        # línea vertical en el promedio de intentos
        plt.axvline(x=promedio_intentos, color='#457b9d', linestyle='--', linewidth=2,
                    label=f'Promedio de intentos: {promedio_intentos:.2f}')

        plt.xlabel('Número de Intento')
        plt.ylabel('Tamaño Promedio del Espacio de Búsqueda')
        plt.title('Reducción Promedio del Espacio de Búsqueda por Intento (200 juegos)')
        plt.legend()
        plt.tight_layout()
        plt.grid(False)
        plt.show()

# modo tiempo real
def get_user_feedback():
    while True:
        try:
            exact_only = int(input("Fichas en posición correcta: "))
            color_only = int(input("Colores correctos en posición incorrecta: "))
            return exact_only, color_only
        except ValueError:
            print("Por favor ingresa números válidos.")

def modo_tiempo_real():
    myAgent = mastermindGameAgent(colors)
    print("Piensa una combinación secreta (4 colores de la lista):", ", ".join(colors))
    guess = myAgent.next_guess()

    while guess:
        print(f"Intento #{myAgent.attempts + 1}: {guess}")
        feedback = get_user_feedback()
        if feedback[0] == 4:
            break
        myAgent.update_knowledge(guess, feedback)
        guess = myAgent.next_guess()

        if guess is None:
            print("\n Error: La retroalimentación ingresada contradice la lógica del juego.")
            print(" Ya no hay combinaciones posibles. Revisa si cometiste un error al dar el feedback.\n")
            return  # salir de la función

    print("\n--------------------------------------------------------------------------")
    print(f"INTENTOS -> {myAgent.attempts}")
    print(" Combinación determinada:", guess)
    print("--------------------------------------------------------------------------")

  

menu = True
while(menu):
    print("+--------------------------------------------------------------+")
    print("|                       MASTERMIND GAME                        |")
    print("+--------------------------------------------------------------+")
    print("Selecciona el modo:")
    print("1. Modo Automático")
    print("2. Modo Tiempo Real")
    print("3. 200 runs")
    print("4. Salir")
    mode = input(" -> ").strip()

    if mode == "1":
        modo_automatico()
    elif mode == "2":
        modo_tiempo_real()
    elif mode == "3":
        modo_automatico(jugar_200_veces=True)
    elif mode == "4":
        menu = False
    else:
        print("Modo inválido.")

