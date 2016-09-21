class App():
    def __init__(self):
        self.var1 = 15

    def calculate(self):
        if self.var1 < 10:
            print('foo')
        self.result = self.var1 * 4 + 2

    def retrieve(self):
        return self.result
        
    def notcalled(self):
        return 1

    def anothernotcalled(self):
        return 2

if __name__ == "__main__":
    app = App()
    app.calculate()
    print(app.retrieve)
