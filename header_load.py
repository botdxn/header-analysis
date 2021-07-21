#załadowanie pliku z parametru path i zwrócenie returnem do dalszego wykorzystania
def load_file(path):
    with open(path, 'r', encoding='utf-8') as file:
        return file.readlines()

#wycięcie fragmentu z nagłówkami i zwrócenie części linijek aż do poczatku body wiadomości
def find_headers(message):
    
    #usunięcie symboli newline
    message = [x.replace('\n','') for x in message]
    
    #przeszukanie każdego wiersza w poszukiwaniu zahardcodowanej linijki
    wiersz = 0
    for row in message:
        if 'Content-Type: text/plain;' in str(row):
            return message[0:wiersz-1] 
        else:
            wiersz += 1

#test
plik = load_file('pliki_naglowkow//test.txt')
print(find_headers(plik))