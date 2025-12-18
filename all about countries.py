class Nigeria:
    def capital(self):
        print("Abuja is the capital of Nigeria")
    def language(self):
        print("Yoruba is the most widely spoken country in Nigeria")
    def type(self):
        print("Nigeria is developing very slowly.")
class China:
    def capital(self):
        print("Beijing is the capital of China")
    def language(self):
        print("Standard Chinese is the most widely spoken language in China")
    def type(self):
        print("China is a very developed country")
obj1=Nigeria()
obj2=China()
for i in (obj1, obj2):
    i.capital()
    i.language()
    i.type()