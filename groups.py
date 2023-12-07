from p1 import tokens
import ply.yacc as yacc


#########################################################################################
def p_start(p):
    '''start : table'''
    # p[0] = p[1]


def p_skip(p):
    '''skiptag : CONTENT skiptag
                | OPENHREF skiptag
                | CLOSEHREF skiptag
                | '''


def p_skiptable(p):
    '''skiptable : OPENROW skiptable
    | CLOSEROW skiptable
                | OPENHEADER skiptable
                | CLOSEHEADER skiptable
                | OPENDATA skiptable
                | CLOSEDATA skiptable
                | CONTENT skiptable
                | OPENHREF skiptable
                | CLOSEHREF skiptable
                | '''


def p_content(p):
    '''content : CONTENT content
    |  '''

    
    
    if len(p) == 3:
        # global group
        # group
        global count,c
        if(count %12==0):
            print('\n')
            print(chr(c))
            c=c+1
        print(p[1], end='  ')
        count+=1


def p_gdata(p):
    '''gdata : OPENHEADER OPENHREF content CLOSEHREF CONTENT CLOSEHEADER gdata
    | OPENHEADER OPENHREF content CLOSEHREF CLOSEHEADER gdata
    | OPENHEADER CONTENT OPENHREF content CLOSEHREF CLOSEHEADER gdata
    | '''



def p_grow(p):
    '''grow : OPENROW gdata CLOSEROW grow
            | OPENROW OPENDATA skiptag CLOSEDATA OPENDATA skiptag CLOSEDATA OPENDATA skiptag CLOSEDATA CLOSEROW grow
            | '''



def p_matchdetails(p):
    '''details : OPENHREF CONTENT CLOSEHREF CONTENT OPENHREF CONTENT CLOSEHREF CONTENT CONTENT CONTENT CONTENT OPENHREF CONTENT skiptag 
    | '''
    print('\t\t', p[2], "\t" , p[9])  #"\t" ,p[13],



def p_matches(p):
    '''matches : grow CLOSETABLE details OPENTABLE matches
    | '''



def p_table(p):
    '''table : BEGINGROUPA skiptag OPENTABLE skiptable CLOSETABLE skiptag OPENTABLE matches
             | BEGINGROUPB skiptag OPENTABLE skiptable CLOSETABLE skiptag OPENTABLE matches
             | BEGINGROUPC skiptag OPENTABLE skiptable CLOSETABLE skiptag OPENTABLE matches
             | BEGINGROUPD skiptag OPENTABLE skiptable CLOSETABLE skiptag OPENTABLE matches
             | BEGINGROUPE skiptag OPENTABLE skiptable CLOSETABLE skiptag OPENTABLE matches
             | BEGINGROUPF skiptag OPENTABLE skiptable CLOSETABLE skiptag OPENTABLE matches
             | BEGINGROUPG skiptag OPENTABLE skiptable CLOSETABLE skiptag OPENTABLE matches
             | BEGINGROUPH skiptag OPENTABLE skiptable CLOSETABLE skiptag OPENTABLE matches
    | '''


def p_error(p):
    pass


parser = yacc.yacc()

def group():
    global count, c
    count=0
    c=65
    file_obj= open('Fifa_data.html','r',encoding="utf-8")
    data=file_obj.read()
    
    parser.parse(data)
    file_obj.close()

def main():
    group()

if __name__ == '__main__':
    main()

# file_obj= open('Fifa_data.html','r',encoding="utf-8")
# data=file_obj.read()
# parser = yacc.yacc()
# parser.parse(data)
# file_obj.close()
