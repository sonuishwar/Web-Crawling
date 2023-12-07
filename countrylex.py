import ply.lex as lex

#################token list##################

tokens = ('OPENTABLE', 'CLOSETABLE', 'OPENROW', 'CLOSEROW',
'OPENHEADER', 'CLOSEHEADER', 'OPENHREF', 'CLOSEHREF',
'CONTENT', 'OPENDATA', 'CLOSEDATA' ,'OPENSPAN',
'CLOSESPAN', 'OPENDIV', 'CLOSEDIV', 'OPENSTYLE', 'CLOSESTYLE','GARBAGE',
'BEGINAUS','ENDAUS','OPENABBR','CLOSEABBR')

###############tokenizer rules################

t_ignore = '\t'

def t_BEGINAUS(t):
    '''<table\sclass="sortable\swikitable\splainrowheaders"\sstyle="font-size:100%;\swidth:\s98%">'''
    # '''fgfg'''
    return t

def t_OPENABBR(t):
    '''<abbr[^>]*>'''
    return t

def t_CLOSEABBR(t):
    '''</abbr[^>]*>'''
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
    '''[A-Za-z0-9,.()\- ]+'''
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
