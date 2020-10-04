from django.shortcuts import render
from django.http import HttpResponse

from pyformlang.finite_automaton import DeterministicFiniteAutomaton
from pyformlang.finite_automaton import State
from pyformlang.finite_automaton import Symbol

# Create your views here.
def home(request):
    if request.method == "POST":
        states = request.POST['States']
        ini_states = request.POST['ini_State']
        fin_states = request.POST['fin_State']
        symbols = request.POST['Symbols']
        transition_states = request.POST['tran_State']
        test_string = request.POST['test_String']
    else : 
        return render(request, 'home/home.html')

    dfa = DeterministicFiniteAutomaton()

    # Creation of the states
    input_states = states.split()
    input_states = list(map(int, input_states))
    actual_states = list(map(State, input_states))

    def convert_symb(a):
        converted_symb = []
        for i in a:
            converted_symb.append(Symbol(i))
        return converted_symb
        
    # Creation of the symbols
    input_symbs = symbols.split()
    actual_symbs = convert_symb(input_symbs)

    # Add a start state
    input_start_state = ini_states.split()
    input_start_state = list(map(int, input_start_state))
    for i in input_start_state:
        dfa.add_start_state(actual_states[i])

    # Add two final states
    input_final_state = fin_states.split()
    input_final_state = list(map(int, input_final_state))
    for i in input_final_state:
        dfa.add_final_state(actual_states[i])


    # Create transitions
    user_tran_in = transition_states.split()
    i = 0
    while(i < len(user_tran_in)):
        
        a = int(user_tran_in[i])
        i += 1
        b = int(user_tran_in[i])
        i += 1
        c = int(user_tran_in[i])
        i += 1
        dfa.add_transition(actual_states[a], actual_symbs[b], actual_states[c])

    user = test_string.split()
    user_string = convert_symb(user)
    output = dfa.accepts(user_string)

    content = {
        't1' : output
    }

    return render(request, 'home/home.html', content)