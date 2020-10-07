import ply3.ply.lex as lex
import re
import codecs
import os
import sys

reservadas = ['for', 'in','distanceTo','turnTo', 'times', 'step', 'goto', 'until', 
				'near', 'if', 'else', 'and', 'or', 'not', 'return', 'cerca',
				'sleeping', 'health', 'say', 'see'
		]

tokens = reservadas+['ID', 'NUMBER', 'PLUS', 'MINUS', 'TIMES', 'DIVIDE',
		'ASSIGN', 'LT', 'GT', 'LPARENT', 'RPARENT', 'COMMA',
		'DOT', 'ARROW', 'LSQUARE', 'RSQUARE'
		]


t_ARROW = r'->'
t_LSQUARE = r'\['
t_RSQUARE = r'\]'
t_ignore = '\t '
t_PLUS = r'\+'
t_MINUS = r'\-'
t_TIMES = r'\*'
t_DIVIDE = r'/'
t_ASSIGN = r'='
t_LT = r'<'
t_GT = r'>'
t_LPARENT = r'\('
t_RPARENT = r'\)'
t_COMMA = r','
t_DOT = r'\.'

def t_ID(t):
	r'[a-z][a-zA-Z@$?]*'
	if t.value in reservadas:
		t.value = t.value
		t.type = t.value
	return t

def t_newline(t):
	r'\n+'
	t.lexer.lineno += len(t.value)

def t_COMMENT(t):
	r'\#.*'
	pass

def t_NUMBER(t):
	r'\d+'
	t.value = int(t.value)
	return t

def t_error(t):
	print ("caracter ilegal '%s'" % t.value[0])
	t.lexer.skip(1)

fp = open(r"C:\Users\David A Quesada Cald\Desktop\Progra_Pruebas\test\prueba.txt")
cadena = fp.read()
fp.close()

analizador = lex.lex()

analizador.input(cadena)

while True:
	tok = analizador.token()
	if not tok : break
	print (tok)



	
