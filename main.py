from tkinter import *  
from tkinter import ttk 
from lexicalAnalysis import *
from syntacticAnalysis import *

# Main class
class Aplication:
    def __init__(self):
        
        self.root=Tk()
        self.root.title("CodeMonkey!") 
        self.root.resizable(0,0)

        #Create Panedwindow 
        self.panedwindow=ttk.Panedwindow(self.root, orient=HORIZONTAL)  
        self.panedwindow.pack(fill=BOTH, expand=True)  

        #Create fram1  
        self.fram1 = ttk.Frame(self.root, width=550, height=500, relief=SUNKEN)  
        self.fram2 = ttk.Frame(self.root, width=250, height=500, relief=SUNKEN)

        # Elements fram2
        self.textBox1 = Text(self.fram2, height=10, width=40)
        self.textBox1.pack()
        self.button1 = Button(self.fram2, text ="Interpretar", command = self.run_interpreter)
        self.button1.pack()

        self.img = PhotoImage(file="resources/monkey.png")

        # Elements fram1
        self.canvas = Canvas(self.fram1, bg="white", height=550, width=500)
        self.canvas.create_image(100, 100, anchor=CENTER, image=self.img, tags="img")
        self.canvas.pack()

        # Add fram1 and fram2 to the panedwindoe
        self.panedwindow.add(self.fram1, weight=1)  
        self.panedwindow.add(self.fram2, weight=4)  

        self.root.mainloop()
    
    def run_interpreter(self):
        self.text = self.textBox1.get("1.0","end-1c")

        lexer = LexicalAnalysis()
        parser = SyntacticAnalyzer()
        env = {}
        if self.text:   
            lex = lexer.tokenize(self.text)
            print("Lexical results: ")
            for token in lex:
                print(token)

            tree = parser.parse(lexer.tokenize(self.text))
            print("Syntatic results: ")
            print(tree)
            self.interpreter(tree, env)         
    
    def move_monkey(self, steps):
        self.canvas.move(ALL, 0, -steps)

    def interpreter(self, tree, env):
        self.env = env
        result = self.walkTree(tree)
        if result is not None and isinstance(result, int):
            print(result)
        if isinstance(result, str) and result[0] == '"':
            print(result)

    def walkTree(self, node):

        # "isinstance" shows the type of the variable
        if isinstance(node, int):
            return node
        if isinstance(node, str):
            return node

        if node is None:
            return None

        if node[0] == 'num':
            return node[1]

        if node[0] == 'str':
            return node[1]

        if node[0] == 'var_assign':
            self.env[node[1]] = self.walkTree(node[2])
            return node[1]

        if node[0] == 'var':
            try:
                return self.env[node[1]]
            except LookupError:
                print("Undefined variable '"+node[1]+"' found!")
                return 0

        if node[0] == 'step_':
            steps = self.walkTree(node[2])
            self.move_monkey(steps)

aplication=Aplication() 