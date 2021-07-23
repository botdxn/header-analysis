from header_load import HeaderAnalysis

#test
test_file = HeaderAnalysis(path='pliki_naglowkow/test.txt', debug=True)
parsed_headers = test_file.get_headers(return_raw=False)

for elem in parsed_headers:
    print(elem)