class Bangladesh():
    def capital(self):
        print("Dhaka")
    
    def language(self):
        print("Bangle")
        
    def type(self):
        print("Developing Country")

class USA(object):
    def capital(self):
        print('Washington')
    
    def language(self):
        print("English")
    
    def type(self):
        print("Developed Country")
        
        
bangla = Bangladesh()
usa = USA()

for country in (bangla, usa):
    country.capital()
    country.language()
    country.type()