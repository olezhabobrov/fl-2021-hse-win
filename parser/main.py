import ply.lex as lex
import sys
import re

reserved = {
  'setAlphabet': 'ALPHABET',
  'setStates': 'STATES',
  'setStart': 'START',
  'makeTerminate': 'TERMINATE',
  'addEdge': 'EDGE'
}

tokens = [
  'STR',
  'COLON',
  'WRONG_ID'
] + list(reserved.values())

t_COLON = r':'

def t_WRONG_ID(t):
  r'[a-z_][a-z_A-Z0-9]*'
  t.type = reserved.get(t.value, 'WRONG_ID')
  return t

def t_STR(t):
  r'".*"'
  return t

t_ignore = ' \t'

def t_newline(t):
  r'\n+'
  t.lexer.lineno += len(t.value)

def t_error(t):
  print("Illegal character '%s'" % t.value[0])
  t.lexer.skip(1)

lexer = lex.lex()

lexer.input(open(sys.argv[1], 'r').read())
sys.stdout = open(sys.argv[1] + ".out", 'w')

resulted_tokens = []

while True:
  tok = lexer.token()
  if not tok:
    break
  resulted_tokens.append(tok)

class Automata:
  alphabet = []
  states = []
  starting = None
  edges = {}
  terminateStates = []

  def fromStringToList(self, str):
    str = re.sub(r'"* *\t*', "", str)
    return str.split(',')

  def addSymbols(self, str):
    if self.alphabet:
      print("Error: alphabet is set more than once!")
      exit(1)
    self.alphabet = self.fromStringToList(str)

  def addStates(self, str):
    if self.states:
      print("Error: states are set more than once!")
      exit(1)
    self.states = self.fromStringToList(str)
    for st in self.states:
      self.edges[st] = []

  def setStarting(self, str):
    if self.starting != None:
      print("Error: starting state was declared before!")
      exit(1)
    str = self.fromStringToList(str)
    if len(str) > 1:
      print("Error: starting state should be unique")
      exit(1)
    if len(str) == 0:
      print("Error: starting state isn't declared")
      exit(1)
    if str[0] not in self.states:
      print("Error: starting state is invalid")
      exit(1)
    self.starting = str[0]

  def addTerminate(self, str):
    str = self.fromStringToList(str)
    for st in str:
      if st not in self.states:
        print("Error: state is invalid")
        exit(1)
      if st not in self.terminateStates:
        self.terminateStates.append(st)

  def addEdge(self, str):
    str = self.fromStringToList(str)
    if len(str) != 3:
      print("Error: wrong amount of parameters")
      exit(1)
    efrom = str[0]
    eto = str[1]
    symb = str[2]
    if efrom not in self.states or eto not in self.states:
      print("Error: invalid state")
      exit(1)
    if symb not in self.alphabet:
      print("Error: invalid symbol")
      exit(1)
    self.edges[efrom].append([eto, symb])

  def print(self):
    print("Alphabet is:")
    print(*self.alphabet, sep=', ')
    print("===============================")
    print("States are:")
    print(*self.states, sep=', ')
    print("Initial state is " + self.starting)
    print("===============================")
    print("Edges:")
    for st in self.states:
      print("from " + st + " :")
      for edge in self.edges[st]:
        print("to " + edge[0] + " with " + edge[1])

      if st in self.terminateStates:
        print(st + " is terminate")

  def check(self):
    if len(set(self.alphabet)) != len(self.alphabet):
      print("Error: symbols in alphabet should be unique!")
      exit(1)
    if len(set(self.states)) != len(self.states):
      print("Error: states should be unique")
      exit(1)
    for st in self.states:
      if len(self.edges[st]) != len(self.alphabet):
        print("Error: automata is not full!")
        exit(1)

  def __init__(self):
    for i in range(0, len(resulted_tokens), 3):
      if resulted_tokens[i + 1].type != "COLON":
        print("Error: Missed colon!")
        exit(1)
      if resulted_tokens[i + 2].type != "STR":
        print("Error: Missed arguments for function!")
        exit(1)

      str = resulted_tokens[i + 2].value

      if resulted_tokens[i].type == "ALPHABET":
        self.addSymbols(str)

      if resulted_tokens[i].type == "STATES":
        self.addStates(str)

      if resulted_tokens[i].type == "START":
        self.setStarting(str)

      if resulted_tokens[i].type == "TERMINATE":
        self.addTerminate(str)

      if resulted_tokens[i].type == "EDGE":
        self.addEdge(str)

automata = Automata()
automata.check()
automata.print()
