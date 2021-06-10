class test1():
    def __init__(self, str):
        self.str = str

    def p(self):
        print(f"I'm created! {self.str}")

class test2():
    def __init__(self, str):
        self.str=str
    def p(self):
        print(f"I'm created! {self.str}")


d = {"test1":test1, "test2":test2}

for v in ["test1", "test2", "test1", "test2"]:
    o = d[v]("string!")
    o.p()
