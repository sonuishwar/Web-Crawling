from p1 import tokens
import ply.yacc as yacc

#########################################################################################
def p_start(p):
    '''start : table'''
    p[0] = p[1]


def p_skiptag(p):
    '''skiptag : CONTENT skiptag
                | OPENHREF skiptag
                | CLOSEHREF skiptag
                | '''
def p_handleData(p):
    '''handleData : OPENDATA OPENHREF CONTENT CLOSEHREF CLOSEDATA handleData
                    | OPENDATA CONTENT OPENHREF CONTENT CLOSEHREF CLOSEDATA handleData
                    | OPENDATA skiptag CLOSEDATA handleData
                    | '''

def p_handleHeader(p):
    '''handleHeader : OPENHEADER OPENHREF CONTENT CLOSEHREF CLOSEHEADER handleHeader
                    | OPENHEADER CONTENT CLOSEHEADER handleHeader
                    |'''

    if len(p) == 5:
        print(p[2])

    if len(p) == 7:
        print(p[3])

def p_handlerow(p):
    '''handlerow : OPENROW handleHeader CLOSEROW handlerow
            | OPENROW handleData CLOSEROW handlerow
            |''' 

def p_table(p):
    '''table : BEGINREWARD skiptag OPENTABLE handlerow'''

def p_error(p):
    pass


parser = yacc.yacc()

def award():
    global count
    count=0
    file_obj= open('Fifa_data.html','r',encoding="utf-8")
    data=file_obj.read()
    
    parser.parse(data)
    file_obj.close()

def main():
    award()

if __name__ == '__main__':
    main()
