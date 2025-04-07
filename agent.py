import itertools
import random

class mastermindGameAgent:
    def __init__(self, colors):
        self.colors = colors
        self.spaces = 4
        self.attempts = 0
        self.possible_combinations = list(itertools.product(colors, repeat=self.spaces)) # modelo
        self.history = []

    def feedback(self, guess, solution):
        # verificar cuantas fichas coinciden en posiciones exactas
        # AND
        exact = 0
        for g,s in zip(guess, solution):
            if g == s:
                exact += 1
                # print(exact)

        # contar cuantos colores coinciden, pero en posiciones equivocadas
        # OR
        color_matches = 0
        for color in set(guess):
            color_matches += min(guess.count(color), solution.count(color))
        color_only = color_matches - exact  # restar las que ya estaban en posición correcta
        
        return exact, color_only

    def update_knowledge(self, guess, feedback):
        # print(f"  Actualizando conocimiento con ... {guess} y {feedback}")
        new_space = []
        # model_check
        for actual_combination in self.possible_combinations:
            if self.feedback(guess, actual_combination) == feedback:
                # consigo todas las combinaciones que tengan el mismo feedback que el guess ingresado                
                # print(f"  Nuevo conocimiento - {actual_combination}")
                new_space.append(actual_combination)
        self.possible_combinations = new_space # cambia el modelo por posibles respuestas restantes
        print(f"  - Posibles combinaciones - {len(new_space)}")
        self.history.append(len(new_space))
        self.attempts += 1

    def next_guess(self):
        # model_check 2
        if self.possible_combinations:
            return self.possible_combinations[0]
        else:
            return None # cuando ya no haya mas opciones, encontro la combinacion o no estaba en el modelo