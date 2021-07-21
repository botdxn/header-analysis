class HeaderAnalysis:
    def __init__(self, path, debug):
        self.path = path
        self.debug = debug
        try:
            with open(self.path, 'r', encoding='utf-8') as file:
                self.message = file.readlines()
                if self.debug == True:
                    print(f'Loaded \"{path}\"')
        except Exception as e:
            print(e)


    #wycięcie fragmentu z nagłówkami i zwrócenie części linijek aż do poczatku body wiadomości
    def find_headers(self):    
        #usunięcie symboli newline
        self.message = [x.replace('\n','') for x in self.message]
        
        #przeszukanie każdego current_rowa w poszukiwaniu zahardcodowanej linijki
        current_row = 0
        for row in self.message:
            if 'Content-Type: text/plain;' in str(row):
                if self.debug == True:
                   print(f'Found header block in \"{self.path}\"') 
                return self.message[0:current_row-1] 
            else:
                current_row += 1


#test
test_file = HeaderAnalysis('pliki_naglowkow/test.txt', debug=True)
test_file.find_headers()