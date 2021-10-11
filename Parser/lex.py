import ply.lex as lex
import sys

reserved = {
  'START': 'START',
}

tokens = [
  'EQUALITY',
  'ID',
  'SYMBOL',
  'MULT',
  'PLUS',
  'ALT',
  'L_BRACKETS',
  'R_BRACKETS',
  'L_SQUARE',
  'R_SQUARE',
] + list(reserved.values())

def t_ID(t):
  r'[A-Za-z][A-Za-z_0-9]*'
  t.type = reserved.get(t.value, 'ID')
  return t

def t_SYMBOL(t):
  r'\'(?:[^\\\']|\\.)*\''
  t.value = t.value[1 : -1]
  t.type = reserved.get(t.value, 'SYMBOL')
  return t

t_ignore = ' \t'
t_EQUALITY = '='
t_MULT = '\*'
t_PLUS = '\+'
t_ALT = '\|'
t_L_BRACKETS = '\('
t_R_BRACKETS = '\)'
t_L_SQUARE = '\['
t_R_SQUARE = '\]'

def t_newline(t):
  r'\n+'
  t.lexer.lineno += len(t.value)

def t_error(t):
  print("Illegal character '%s'" % t.value[0])
  t.lexer.skip(1)

lexer = lex.lex()

# lexer.input(open(sys.argv[1], 'r').read())
# sys.stdout = open(sys.argv[1] + '.out', 'w')
#
# while True:
#   tok = lexer.token()
#   if not tok:
#     break
#   print(tok)