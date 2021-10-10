from bs4 import BeautifulSoup
import requests
import os

class PCMCFrom:

    def __init__(self, name, filename):
        self.name = name
        self.filename = filename

    def parseFromCMC(self):
        url = 'https://www.coinmarketcap.com/currencies/' + self.name + '/news'  # url страницы
        r = requests.get(url)
        needToDelete = False
        with open(self.filename, 'w') as output_file:
            if r.text.__contains__("price today") == False:
                print("Cryptocurrency not found!")
                needToDelete = True
            else:
                soup = BeautifulSoup(r.text, 'html.parser')
                output_file.write(soup.prettify())
                soup_parser = BeautifulSoup(r.text, 'lxml');
                for child in soup_parser.recursiveChildGenerator():
                    if child.name == 'h1' or child.name == 'h2' or child.name == 'h3' or child.name == 'p' or child.name == 'div':
                        print(child.text + '\n')
        if needToDelete:
            os.remove(output_file.name)
