from sly import Lexer

class LexicalAnalysis(Lexer):
    tokens = { NAME, NUMBER, STRING, TURN, LEFT, RIGHT, STEP }
    ignore = '\t '

    literals = { '=', '+', '-', '/', '*', '(', ')', ',', ';' }

    # Define tokens
    TURN = r'turn'
    LEFT = r'left'
    RIGHT = r'right'
    STEP = r'step'
    NAME = r'[a-z][a-zA-Z0-9@$?]*'
    STRING = r'\".*?\"'

    @_(r'\d+')
    def NUMBER(self, t):
        t.value = int(t.value)
        return t

    @_(r'#.*')
    def COMMENT(self, t):
        pass

    @_(r'\n+')
    def newline(self,t ):
        self.lineno = t.value.count('\n')