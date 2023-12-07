import ply.lex as lex

#################token list##################

tokens = ('OPENTABLE', 'CLOSETABLE', 'OPENROW', 'CLOSEROW',
'OPENHEADER', 'CLOSEHEADER', 'OPENHREF', 'CLOSEHREF',
'CONTENT', 'OPENDATA', 'CLOSEDATA' ,'OPENSPAN',
'CLOSESPAN', 'OPENDIV', 'CLOSEDIV', 'OPENSTYLE', 'CLOSESTYLE','GARBAGE',
'BEGINTABLE1','BEGINTEAM', 'ENDTEAM','BEGINGROUPA','BEGINGROUPB','BEGINGROUPC','BEGINGROUPD','BEGINGROUPE','BEGINGROUPF',
'BEGINGROUPG','BEGINGROUPH', 'BEGINREWARD')

###############tokenizer rules################

t_ignore = '\t'



def t_BEGINTABLE1(t):
    '''<h3><span\sclass="mw-headline"\sid="Stadiums">Stadiums</span></h3>'''
    return t


def t_ENDTEAM(t):
    '''<h2><span\sclass="mw-headline"\sid="Teams">Teams</span></h2>'''
    return t

def t_BEGINGROUPA(t):
    '''<h3><span\sclass="mw-headline"\sid="Group_A">Group\sA</span></h3>'''
    return t

def t_BEGINGROUPB(t):
    '''<h3><span\sclass="mw-headline"\sid="Group_B">Group\sB</span></h3>'''
    return t

def t_BEGINGROUPC(t):
    '''<h3><span\sclass="mw-headline"\sid="Group_C">Group\sC</span></h3>'''
    return t

def t_BEGINGROUPD(t):
    '''<h3><span\sclass="mw-headline"\sid="Group_D">Group\sD</span></h3>'''
    return t

def t_BEGINGROUPE(t):
    '''<h3><span\sclass="mw-headline"\sid="Group_E">Group\sE</span></h3>'''
    return t

def t_BEGINGROUPF(t):
    '''<h3><span\sclass="mw-headline"\sid="Group_F">Group\sF</span></h3>'''
    return t

def t_BEGINGROUPG(t):
    '''<h3><span\sclass="mw-headline"\sid="Group_G">Group\sG</span></h3>'''
    return t    

def t_BEGINGROUPH(t):
    '''<h3><span\sclass="mw-headline"\sid="Group_H">Group\sH</span></h3>'''
    return t

def t_BEGINREWARD(t):
    '''<table\sclass="wikitable"\sstyle="text-align:center">'''
    return t


def t_OPENTABLE(t):
    '''<tbody[^>]*>'''
    return t

def t_CLOSETABLE(t):
    '''</tbody[^>]*>'''
    return t

def t_OPENROW(t):
    '''<tr[^>]*>'''
    return t

def t_CLOSEROW(t):
    '''</tr[^>]*>'''
    return t

def t_OPENHEADER(t):
    '''<th[^>]*>'''
    return t

def t_CLOSEHEADER(t):
    '''</th[^>]*>'''
    return t

def t_OPENHREF(t):
    '''<a[^>]*>'''
    return t

def t_CLOSEHREF(t):
    '''</a[^>]*>'''
    return t

def t_OPENDATA(t):
    '''<td[^>]*>'''
    return t

def t_CLOSEDATA(t):
    '''</td[^>]*>'''
    return t

def t_OPENDIV(t):
    '''<div[^>]*>'''

def t_CLOSEDIV(t):
    '''</div[^>]*>'''

def t_OPENSTYLE(t):
    '''<style[^>]*>'''

def t_CLOSESTYLE(t):
    '''</style[^>]*>'''

def t_OPENSPAN(t):
    '''<span[^>]*>'''

def t_CLOSESPAN(t):
    '''</span[^>]*>'''


def t_CONTENT(t):
    '''[A-Za-z0-9, ]+'''
    return t

def t_GARBAGE(t):
    r'<[^>]*>'

def t_error(t):
    t.lexer.skip(1)


# precedence = (
#     ('left', 'PLUS', 'MINUS'),
#     ('left', 'MULTIPLY', 'DIVIDE', 'MODULO'),
#      ('right','EXPONENT'),
# )

#########DRIVER FUNCTION#######

file_obj= open('Fifa_data.html','r',encoding="utf-8")
data=file_obj.read()
lexer = lex.lex()
lexer.input(data)

# for tok in lexer:print(tok)