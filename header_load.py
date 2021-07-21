import re

class HeaderAnalysis:
    def __init__(self, path: str, debug: bool):
        self.path = path
        self.debug = debug
        try:
            with open(self.path, 'r', encoding='utf-8') as file:
                self.message = file.readlines()
                if self.debug == True: print(f'Loaded \"{path}\"')
        except Exception as e: print(e)

    def get_headers(self, raw: bool, save: bool, output: str):
        example_headers_list = ['Delivered-To:', 'ARC-Seal:', 'ARC-Message-Signature:', 'ARC-Authentication-Results:', 'Return-Path:', 'Received-SPF:', 'Authentication-Results:', 'DKIM-Signature:', 'X-HS-Cid:', 'Date:', 'From:', 'To:', 'Message-ID:', 'Subject:', 'Content-Type:']
        example_headers_list = [list_element.lower() for list_element in example_headers_list]
    
        self.message = [x.replace('\n','') for x in self.message]
        
        for current_row, row in enumerate(self.message):
            if 'Content-Type: text/plain;' in str(row):
                if self.debug == True: print(f'Found header block in \"{self.path}\"')
                headers_block = self.message[0:current_row-1]
                headers_block = [list_element.lower() for list_element in headers_block]
            else:
                current_row += 1

        if raw == False:
            headers_list = []
            for row in headers_block:
                for list_element in example_headers_list:
                    if re.match(list_element, row) is not None:
                        headers_list.append(row)
            if save == True:
                file_name = output + self.path.split('/')[-1] + '.parsed'
                with open(file_name, 'w') as output_file:
                    for header_list_elementment in headers_list:
                        output_file.write(header_list_elementment + '\n')
                if self.debug == True: print(f'File \"{file_name}\" saved')
            return headers_list
        elif raw == True:
            return headers_block 
        
#test
test_file = HeaderAnalysis(path='pliki_naglowkow/test.txt', debug=True)
parsed_headers = test_file.get_headers(raw=False, save=True, output='')
print(parsed_headers)