class Automaton:
    def __init__(self):
        self.states = [0, 1, 2, 3, 4]
        self.final_states = [1, 2, 3, 4]
        self.alphabet = ['R', 'U', 'G', 'J', 'r', 'u', 'g', 'j']
        self.transition_table = {
            (0, 'R'): 1, (0, 'r'): 1,
            (1, 'U'): 2, (1, 'u'): 2,
            (2, 'G'): 3, (2, 'g'): 3,
            (3, 'J'): 4, (3, 'j'): 4
        }
        self.current_state = 0

    def transition_to_state_with_input(self, input_value):
        if (self.current_state, input_value) not in self.transition_table:
            self.current_state = None
        else:
            self.current_state = self.transition_table[(self.current_state, input_value)]

    def in_accept_state(self):
        return self.current_state in self.final_states

    def go_to_initial_state(self):
        self.current_state = 0

    def run_with_input_list(self, input_list):
        self.go_to_initial_state()
        for inp in input_list:
            self.transition_to_state_with_input(inp)
            if self.current_state is None:
                return False
        return self.in_accept_state()

dfa = Automaton()

user_input = input("Inserte la cadena: ")

is_valid = dfa.run_with_input_list(user_input)

if is_valid:
    print(f"La cadena '{user_input}' es correcto deacuerdo al DFA.")
else:
    print(f"La cadena '{user_input}' es incorrecta.")
