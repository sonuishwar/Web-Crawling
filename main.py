from p1 import tokens
import ply.yacc as yacc
from groups import group
from awards import award
# from country import aus


def p_start(p): 
    '''start : table'''
    p[0] = p[1]


def p_skiptag(p):
    '''skiptag : CONTENT skiptag
                | OPENHREF skiptag
                | CLOSEHREF skiptag
                | '''

############################### 2 #######################     // main grammar for teams

def p_data(p):
    '''data : data OPENDATA CONTENT OPENHREF CONTENT CLOSEHREF CLOSEDATA
    | data OPENDATA skiptag CLOSEDATA
    |'''
    if len(p) == 8 and f==2:
        print(p[5])
        global count
        count=count+1


def p_row(p):
    '''row : OPENROW data CLOSEROW
                | '''

############################### 2 #######################        // main grammar for stadiums

def p_handleData(p):
    '''handleData : OPENDATA OPENHREF CONTENT CLOSEHREF CLOSEDATA handleData
                | OPENDATA CONTENT skiptag CLOSEDATA handleData 
                | '''     

    if (len(p) == 6 and f==1):
        global capacity
        capacity =p[2]

    if (len(p) == 7 and f==1):
        # global s
        print(p[3], "   " ,capacity)
        global count
        count=count+1

        
def p_handlerow(p):
    '''handlerow : OPENROW OPENHEADER skiptag CLOSEHEADER OPENHEADER skiptag CLOSEHEADER OPENHEADER skiptag CLOSEHEADER CLOSEROW handlerow
                | OPENROW OPENHEADER OPENHREF CONTENT CLOSEHREF CLOSEHEADER handleData CLOSEROW handlerow
                | OPENROW handleData CLOSEROW handlerow
                | '''

#################################################

def p_table(p):
    '''table : BEGINTABLE1 skiptag OPENTABLE handlerow
             | row CLOSETABLE ENDTEAM'''
  
def p_empty(p):
    '''empty : '''
    pass

def p_content(p):
    '''content : CONTENT
                | empty'''
    p[0] = p[1]


def p_error(p):
    pass

parser = yacc.yacc()

while(True):
    file_obj= open('Fifa_data.html','r',encoding="utf-8")
    data=file_obj.read()
    global f,count
    count=0
    print("\nChoice List (teams, stadiums, awards, groups, exit)")
    s=input("Enter a choice: ")
    if(s=="exit"):
        break
    elif(s=="teams"):
        f=2
    elif(s=="stadiums"):
        f=1
    elif(s=="groups"):
        group()
        continue
    elif(s=="awards"):
        award()
        continue
    # elif(s=="country"):
    #     # from country import aus
    #     aus()
    #     continue
    else:
        print("Invalid Input  ")
        continue
    parser.parse(data)
    print("Total ",count)

# def main():
#     global f
#     f=2
#     f=input("Enter choice:  ")
#     parser = yacc.yacc()
#     parser.parse()
    

# if __name__ == '__main__':
#     main()

