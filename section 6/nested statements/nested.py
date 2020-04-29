
name = 'THIS IS A GLOBAL STRING'

def greet(name):
    #name = 'sammy'

    def hello():
        print('hello '+ name)
    
    hello()

greet(name)