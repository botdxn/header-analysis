#załadowanie pliku z podanego parametru path i zwrócenie returnem do dalszego wykorzystania
def load_file(path):
    try:
        with open(path, 'r', encoding='utf-8') as file:
            return file.readlines()
    except Exception as e:
        print(e)


#wycięcie fragmentu z nagłówkami i zwrócenie części linijek aż do poczatku body wiadomości
def find_headers(message):    
    #usunięcie symboli newline
    message = [x.replace('\n','') for x in message]
    
    #przeszukanie każdego current_rowa w poszukiwaniu zahardcodowanej linijki
    current_row = 0
    for row in message:
        if 'Content-Type: text/plain;' in str(row):
            return message[0:current_row-1] 
        else:
            current_row += 1


#test
test_file = load_file('pliki_naglowkow//test.txt')
print(find_headers(test_file))