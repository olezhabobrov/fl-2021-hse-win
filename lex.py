import ply.lex as lex
import sys

reserved = {
  'setAlphabet': 'ALPHABET',
  'setStatesAmount': 'STATES_AMOUNT',
  'setStart': 'START',
  'makeTerminate': 'TERMINATE',
  'addEdge': 'EDGE'
}

tokens = [
  'NUM',
  'SYMB',
  'COLON',
  'WRONG_ID'
] + list(reserved.values())

t_COLON = r':'

symbols=[]

def t_WRONG_ID(t):
  r'[a-z_][a-z_A-Z0-9]*'
  t.type = reserved.get(t.value, 'WRONG_ID')
  return t

def t_NUM(t):
  r'[0-9]+'
  t.value = int(t.value)
  return t

def t_SYMB(t):
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
sys.stdout = open(sys.argv[1] + '.out', 'w')

while True:
  tok = lexer.token()
  if not tok:
    break
  print(tok)
