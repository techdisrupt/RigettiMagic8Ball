""" magic8ball.py: Quantum based Magic 8 Ball using the Rigetti PyQuill Framework"""

__author__ = "Brett Donovan"
__copyright__ = "Copyright 2018"
__license__ = "MIT"
__version__ = "1.0.1"
__maintainer__ = "Rob Knight"
__status__ = "Production"


import math
from pyquil.quil import Program
from pyquil.api import QVMConnection
quantum_simulator = QVMConnection()
from pyquil.gates import I, X, Y, Z, H, CNOT


def MagicNBall(N):

    """ Takes N, number of options and creates required number of Qubits into a super position and returns an integer out of the number of possible combinations of N. Example N=5, returns a number {0, 1, 2, 3, 4}. """

    # We can only deal with 2^nQubits possibilities, so this places limits on N.

    r = math.log(N) / math.log(2)
    nQubits = int(r)
    if r > int(r):
        nQubits+= 1
    
    # Now create the required number of qubits in the correct initial Hadamard State using the H gate. Each qubit is specified by i up to the nQubits.

    p = Program()
    for i in range(0, nQubits):
        p += Program(H(i))
    p.measure_all()
    result = quantum_simulator.run(p)
    option = sum([result[0][i] * 2**i for i in range(0, nQubits)])

    # Deal with the addition options over specified N

    print("Number of Qubits: ", nQubits)
    print("Number of Quantum possibilities: ", 2**nQubits)
    print("Number of possibilities you chose: ", N)
    return option % N




if __name__ == "__main__":
    # Magic 8 Ball options
    options = [
    "It is certain.",
    "It is decidedly so.",
    "Without a doubt.",
    "Yes - definitely.",
    "You may rely on it.",
    "As I see it, yes.",
    "Most likely.",
    "Outlook good.",
    "Yes.",
    "Signs point to yes.",
    "Reply hazy, try again.",
    "Ask again later.",
    "Better not tell you now.",
    "Cannot predict now.",
    "Concentrate and ask again.",
    "Don't count on it.",
    "My reply is no.",
    "My sources say no.",
    "Outlook not so good.",
    "Very doubtful."
    ]


    select = MagicNBall(len(options))
    print("Magic 8 ball response: ", options[select], select)
    

