from sly import Parser
from lexicalAnalysis import *

class SyntacticAnalyzer(Parser):
    tokens = LexicalAnalysis.tokens

    precedence = (
        ('right', 'UMINUS'),
        )

    def __init__(self):
        self.env = { }

    @_('')
    def statement(self, p):
        pass

    @_('var_assign')
    def statement(self, p):
        return p.var_assign

    @_('NAME "=" expr')
    def var_assign(self, p):
        return ('var_assign', p.NAME, p.expr)

    @_('NAME "=" STRING')
    def var_assign(self, p):
        return ('var_assign', p.NAME, p.STRING)

    @_('STEP expr')
    def var_assign(self, p):
        return ('step_', p.STEP, p.expr)

    @_('expr')
    def statement(self, p):
        return (p.expr)

    @_('"-" expr %prec UMINUS')
    def expr(self, p):
        return p.expr

    @_('NAME')
    def expr(self, p):
        return ('var', p.NAME)

    @_('NUMBER')
    def expr(self, p):
        return ('num', p.NUMBER)