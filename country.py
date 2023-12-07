from countrylex import tokens
import ply.yacc as yacc


def p_start(p):
    '''start : table'''
    
    p[0] = p[1]
    print("startt")

                
def p_skiptag(p):
    '''skiptag : CONTENT skiptag
                | CLOSEHREF skiptag
                | OPENHREF skiptag
                | '''
                # | OPENSPAN skiptag
                # | CLOSESPAN skiptag
                
               
def p_handleData(p):  
    '''handleData : OPENDATA CONTENT CLOSEDATA handleData
                | OPENDATA   content   OPENHREF content CLOSEHREF CLOSEDATA handleData 
                | OPENHEADER  OPENHREF content CLOSEHREF skiptag OPENHREF content skiptag CLOSEHREF skiptag CLOSEHEADER handleData
                | OPENDATA OPENSPAN OPENSPAN content CLOSESPAN CLOSESPAN OPENSPAN skiptag OPENSPAN CLOSEDATA handleData 
                | '''
        
        
def p_handlerow(p):
    '''handlerow : OPENROW OPENHEADER OPENABBR content CLOSEABBR CLOSEHEADER handlerow
                | OPENHEADER OPENABBR content CLOSEABBR CLOSEHEADER handlerow
                | OPENHEADER content CLOSEHEADER handlerow
                | CLOSEROW
                | '''
                  
                
def p_table(p):
    '''table : BEGINAUS OPENTABLE handlerow OPENROW handleData'''
    # skiptag CLOSETABLE'''
    

def p_empty(p):
    '''empty : '''
    pass


def p_content(p):
    '''content : CONTENT
                | empty'''
    # p[0] = p[1]
    print(p[1],end='     ')
    global count
    count+=1
    if count==7:
        print('\n')

    
    
def p_error(p):
    pass

parser = yacc.yacc()

def aus():
    global count
    count=0
    file_obj1= open('Australia_data.html','r',encoding="utf-8")
    data1=file_obj1.read()
    
    parser.parse(data1)
    file_obj1.close()

def main():
    aus()

if __name__ == '__main__':
    main()
