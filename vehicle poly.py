class BMW:
    def time(self):
        print("BMW was founded on 7 March 1916")
    def founder(self):
        print("BMW was founded by an aircraft producer called Bayerische Flugzeugwerke")
    def color(self):
        print("They come in different colors")
    def type(self):
        print("A very nice car")
class Ferrari:
    def time(self):
        print("Ferrari was founded on 13 September 1939")
    def founder(self):
        print("Ferrari was founded by Enzo Ferrari")
    def color(self):
        print("They come in different colors but mostly black")
    def type(self):
        print("A very beautiful car")
obj1=BMW()
obj2=Ferrari()
for i in(obj1, obj2):
    i.time()
    i.founder()
    i.color()
    i.type()