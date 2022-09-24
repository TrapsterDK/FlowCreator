import re
from sys import argv
from bs4 import BeautifulSoup
import shlex


BLOCK_COMMENT = '/*'
LINE_COMMENT = '//'      
RETURN = 'return'
WHILE = 'while'
FOR = 'for'
IF = 'if'
ELSE = 'else'
OTHER = 'other'
ELIF = 'elif'
FUNCTION_CALL = 'function_call'
FUNCTION = 'function'   
DO = 'do'
WRAPPER_START = '{'
WRAPPER_END = '}'
STRING = 'string'
VARIABLE = 'variable'
PREPROCESSOR = '#'

class CParser():
    parse_arr = []

    def __init__(self, filename):
        with open(argv[1], 'r') as f: 
            data = f.read()
        self.parse(data)

    def parse(self, data):
        i = 0

        data_len = len(data)
        
        def check_item(item):
            nonlocal i, data
            l = len(item)
            s = data[i: i+l] == item

            if s:
                i+=l

            return s
        
        def check_items(*args: str):
            for item in args:
                if check_item(item):
                    return item
            return None

        def find_true_next(item):
            nonlocal i, data, data_len
            return data.find(item, i, data_len)

        def find_next(item):
            nonlocal data_len
            next = find_true_next(item)
            next = next if next != -1 else data_len
            return next

        def next_statement():
            nonlocal i, data, data_len
            first_paren = find_next('(')

            if first_paren == -1:
                raise Exception('No paren found')

            first_paren+=1

            parentheis = 1
            last_paren = first_paren

            while parentheis != 0:
                if data[last_paren] == '(':
                    parentheis+=1
                elif data[last_paren] == ')':
                    parentheis-=1
                last_paren+=1

            last_paren-=1

            return (first_paren, last_paren)
            
        def add_empty_lex_item(instruction):
            self.parse_arr.append({instruction})

        def add_lex_by_item(instruction, item):
            self.parse_arr.append({instruction: item})

        def add_lex_by_index(instruction, start_index, end_index):
            self.parse_arr.append({instruction: data[start_index:end_index]})

        def add_lex_till_next(item, instruction):
            nonlocal i
            next = find_next(item)
            add_lex_by_index(instruction, i, next)
            i = next + len(item)
            
        def add_lex_till_with_next(item, instruction):
            nonlocal i
            next = find_next(item)+1
            add_lex_by_index(instruction, i, next)
            i = next + len(item)

        def add_lex_statement(instruction):
            nonlocal i
            first_paren, last_paren = next_statement()
            add_lex_by_index(instruction, first_paren, last_paren)
            i = last_paren + 1


        look_var_end = False
        var = None
        paren = 0

        while i < len(data):
            if item := check_items('"', "'"):
                next = find_next(item) + len(item)
                add_lex_by_index(STRING, i - 1, next)
                i = next

            elif check_item(BLOCK_COMMENT):
                add_lex_till_next('*/', BLOCK_COMMENT)  

            elif item := check_items(LINE_COMMENT, PREPROCESSOR):
                add_lex_till_next('\n', item)

            elif item := check_items(WRAPPER_START, WRAPPER_END):       
                add_empty_lex_item(item)

            elif look_var_end:
                if check_item('('):
                    var += '('
                    paren+=1

                elif check_item(')'):
                    var += ')'
                    paren-=1
                    if(paren == 0):
                        add_lex_by_item(FUNCTION, var)
                        look_var_end = None
                
                elif paren:
                    var += data[i]
                    i+=1

                elif not check_items(' ', '\t', '\n'):
                    add_lex_by_item(VARIABLE, var)
                    add_lex_by_index(OTHER, look_var_end, i-1)
                    look_var_end = None

            elif data[i].isalpha():
                end = re.search('[a-zA-Z0-9_]*', data[i+1:]).end()+1
                start = i
                match = data[start:i+end]
                i+=end

                if match in [WHILE, FOR, IF]:
                    add_lex_statement(match)

                elif match in [DO, ELSE, RETURN]:
                    add_empty_lex_item(match)
                    
                else:
                    look_var_end = i
                    var = match
                
            else:
                if(OTHER in self.parse_arr[-1]):
                    self.parse_arr[-1][OTHER] += data[i]
                else:
                    add_lex_by_item(OTHER, data[i])
                i+=1

    def print_parsed(self):
        for i in self.parse_arr:
            print(i)
            
    def print_parsed_type(self, *args):
        for i in self.parse_arr:
            if(any(arg in i for arg in args)):
                print(*i)


if __name__ == '__main__':
    #argv[1] is c file name
    # argv[2] is html output file name  
    if len(argv) != 3:
        print('Usage: python3 flowcreator.py <c input file> <html output file>')
        exit(1)

    parse = CParser(argv[1])
    #parse.print_parsed_type(OTHER)
    parse.print_parsed()