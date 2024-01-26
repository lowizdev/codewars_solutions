#url: https://www.codewars.com/kata/526c7b931666d07889000a3c/train/python
#Carnage Heart 

import random

class BefungeInterpreter():
    def __init__(self):
        self.stack = []
        self.output = ""
        self.movement = 'r'
        self.string_mode_on = False
        self.pointer_x = 0
        self.pointer_y = 0
        self.code_table = []

    def reset(self): #TODO: RESET THE OBJECT? TEMPORAL COUPLING?
        pass

    def sum(self):
        a = self.stack.pop()
        b = self.stack.pop()
        self.stack.append(int(a) + int(b))
    
    def sub(self):
        a = self.stack.pop()
        b = self.stack.pop()
        self.stack.append(int(b) - int(a))
    
    def mult(self):
        a = self.stack.pop()
        b = self.stack.pop()
        self.stack.append(int(a) * int(b))
    
    def mod(self):
        a = self.stack.pop()
        b = self.stack.pop()
        self.stack.append(int(b) % int(a)) if int(a) != 0 else self.stack.append(0)

    def div(self):
        a = self.stack.pop()
        b = self.stack.pop()
        self.stack.append(int(b) / int(a)) if int(a) != 0 else self.stack.append(0)

    def put_call(self):
        x = self.stack.pop()
        y = self.stack.pop()
        v = self.stack.pop()
        #code_table[int(x)][int(y)] = chr(int(v))
        word = list(self.code_table[int(x)]) 
        word[int(y)] = chr(int(v))
        self.code_table[int(x)] = "".join(word)

    def get_call(self):
        x = self.stack.pop()
        y = self.stack.pop()
        self.stack.append(ord(self.code_table[int(x)][int(y)]))

    def match_symbol(self, symbol):
        if(symbol.isnumeric()):
            self.stack.append(symbol)
        elif(symbol == "+"):
            self.sum()
        elif(symbol == "-"):
            self.sub()
        elif(symbol == "*"):
            self.mult()
        elif(symbol == "/"):
            self.div()
        elif(symbol == "%"):
            self.mod()
        elif(symbol == "!"):
            a = self.stack.pop()
            if a == 0:
                self.stack.append(1)
            else:
                self.stack.append(0)
        elif(symbol == "`"):
            a = self.stack.pop()
            b = self.stack.pop()
            if int(b) > int(a):
                self.stack.append(1)
            else:
                self.stack.append(0)
        elif(symbol == '>'):
            self.movement = 'r'
        elif(symbol == '<'):
            self.movement = 'l'
        elif(symbol == '^'):
            self.movement = 'u'
        elif(symbol == 'v'):
            self.movement = 'd'
        elif(symbol == '?'):
            self.movement = random.choice("rlud")
        elif(symbol == '_'):
            a = self.stack.pop()
            if int(a) == 0:
                self.movement = 'r'  
            else:
                self.movement = 'l'
        elif(symbol == '|'):
            a = self.stack.pop()
            if int(a) == 0:
                self.movement = 'd' 
            else:
                self.movement = 'u'
        elif(symbol == ':'):
            if self.stack:
                a = self.stack.pop()
                self.stack.append(a)
                self.stack.append(a)
            else:
                self.stack.append(0)
        elif(symbol == '\\' ):
            a = self.stack.pop()
            if self.stack:
                b = self.stack.pop()
                self.stack.append(a)
                self.stack.append(b)
            else:
                self.stack.append(a)
                self.stack.append(0)
        elif(symbol == '$'):
            a = self.stack.pop()
        elif(symbol == '.'):
            a = self.stack.pop()
            print(a)
            self.output += str(a)
            print(self.output)
        elif(symbol == ','):
            a = self.stack.pop()
            print(chr(a))
            self.output += chr(a)
        elif(symbol == "p"):
            self.put_call()
        elif(symbol == "g"):
            self.get_call()
        elif(symbol == "#"):
            self.move_pointers()

    def move_pointers(self):
        if(self.movement == 'r'):
            self.pointer_x += 1
            print('right')
        elif(self.movement == 'l'):
            self.pointer_x -= 1
            print('left')
        elif(self.movement == 'u'):
            self.pointer_y -= 1
            print('up')
        elif(self.movement == 'd'):
            self.pointer_y += 1
            print('down')
        print(self.stack)
    
    def interpret(self, code):
        self.pointer_x = 0
        self.pointer_y = 0
        self.code_table = [x for x in (code.split("\n"))]
        self.movement = 'r' # resets to default
        self.string_mode_on = False

        while(True):
            symbol = self.code_table[self.pointer_y][self.pointer_x]
        
            if(symbol == "\""):
                self.string_mode_on = not self.string_mode_on
            
            if(not self.string_mode_on):
                if symbol == "@":
                    return self.output
                self.match_symbol(symbol)
            else:
                if(symbol != "\""):
                    self.stack.append(ord(symbol))

            self.move_pointers()
            

def interpret(code):
    interpreter = BefungeInterpreter()
    return interpreter.interpret(code)



'''def interpret(code):
    output = ""
    stack = []
    code_table = [x for x in (code.split("\n"))]
    pointer_x = 0
    pointer_y = 0
    movement = 'r' #rlud
    string_mode_on = False
    # TODO: Interpret the code!
    #for line in code_table:
    #for symbol in line:
    while(True):
        
        symbol = code_table[pointer_y][pointer_x]
        
        if(symbol == "\""):
            string_mode_on = not string_mode_on
        
        if(not string_mode_on):
            if symbol == "@":
                return output
            elif(symbol.isnumeric()):
                stack.append(symbol)
            elif(symbol == "+"):
                a = stack.pop()
                b = stack.pop()
                stack.append(int(a) + int(b))
            elif(symbol == "-"):
                a = stack.pop()
                b = stack.pop()
                stack.append(int(b) - int(a))
            elif(symbol == "*"):
                a = stack.pop()
                b = stack.pop()
                stack.append(int(a) * int(b))
            elif(symbol == "/"):
                a = stack.pop()
                b = stack.pop()
                stack.append(int(b) / int(a)) if int(a) != 0 else stack.append(0)
            elif(symbol == "%"):
                a = stack.pop()
                b = stack.pop()
                stack.append(int(b) % int(a)) if int(a) != 0 else stack.append(0)
            elif(symbol == "!"):
                a = stack.pop()
                if a == 0:
                    stack.append(1)
                else:
                    stack.append(0)
            elif(symbol == "`"):
                a = stack.pop()
                b = stack.pop()
                if int(b) > int(a):
                    stack.append(1)
                else:
                    stack.append(0)
            elif(symbol == '>'):
                movement = 'r'
            elif(symbol == '<'):
                movement = 'l'
            elif(symbol == '^'):
                movement = 'u'
            elif(symbol == 'v'):
                movement = 'd'
            elif(symbol == '?'):
                movement = random.choice("rlud")
            elif(symbol == '_'):
                a = stack.pop()
                if int(a) == 0:
                    movement = 'r'  
                else:
                    movement = 'l'
            elif(symbol == '|'):
                a = stack.pop()
                if int(a) == 0:
                    movement = 'd' 
                else:
                    movement = 'u'
            #elif(symbol == "\""):
            #    string_mode_on = not string_mode_on
            elif(symbol == ':'):
                if stack:
                    a = stack.pop()
                    stack.append(a)
                    stack.append(a)
                else:
                    stack.append(0)
            elif(symbol == '\\' ):
                a = stack.pop()
                if stack:
                    b = stack.pop()
                    stack.append(a)
                    stack.append(b)
                else:
                    stack.append(a)
                    stack.append(0)
            elif(symbol == '$'):
                a = stack.pop()
            elif(symbol == '.'):
                a = stack.pop()
                print(a)
                output += str(a)
            elif(symbol == ','):
                a = stack.pop()
                print(chr(a))
                output += chr(a)
            elif(symbol == "p"):
                x = stack.pop()
                y = stack.pop()
                v = stack.pop()
                #code_table[int(x)][int(y)] = chr(int(v))
                word = list(code_table[int(x)]) 
                word[int(y)] = chr(int(v))
                code_table[int(x)] = "".join(word)
                
            elif(symbol == "g"):
                x = stack.pop()
                y = stack.pop()
                stack.append(ord(code_table[int(x)][int(y)]))

            elif(symbol == "#"):
                #TODO: REFACTOR SKIPPING
                if(movement == 'r'):
                    pointer_x += 1
                    print('right')
                elif(movement == 'l'):
                    pointer_x -= 1
                    print('left')
                elif(movement == 'u'):
                    pointer_y -= 1
                    print('up')
                elif(movement == 'd'):
                    pointer_y += 1
                    print('down')
            
        else:
            if(symbol != "\""):
                stack.append(ord(symbol))
        
        #after evaluation of symbol, do the movement
        
        if(movement == 'r'):
            pointer_x += 1
            print('right')
        elif(movement == 'l'):
            pointer_x -= 1
            print('left')
        elif(movement == 'u'):
            pointer_y -= 1
            print('up')
        elif(movement == 'd'):
            pointer_y += 1
            print('down')
        print(stack)
    return output'''