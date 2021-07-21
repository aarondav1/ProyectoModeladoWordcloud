'''
PROGRAMA
'''
import sys
from bs4 import BeautifulSoup
import requests
from wordcloud import  WordCloud
import matplotlib.pyplot as plt


class Usuario():
    '''
    Esta clase ewiofjw fwoj fwoifwjefoije foiwjfwoifj.
    '''
    def __init__(self, id_usuario):
        '''
        Metodo constructor de la clase usuario, recibe el id de usuario.
        '''
        self.id_usuario = id_usuario
        self.url = 'https://es.stackoverflow.com/users/' + self.id_usuario + '?tab=tags'
        self.nombre = ""

    def mostrar_id(self):
        '''
        kjfekjfekrelj
        '''
        print(self.id_usuario)

    def mostrar_url(self):
        '''
        kjfekjfekrelj
        '''
        print(self.url)

class WebScrapping():
    '''
    Clase que contendra los metodos de extraccion y manejo de los datos html
    '''
    def __init__(self, id_usuario):
        '''
        efwfiwefiuwehfiweufhweuifhwef uwihfewiufhwefuih
        '''
        self.usuario = Usuario(id_usuario)
        #self.url = 'https://es.stackoverflow.com/users/'
        #·self.url = self.url + self.usuario.id_usuario +"?tab=tags"
        self.url = self.usuario.url
        response = requests.get(self.url)
        self.soup = BeautifulSoup(response.content, 'html.parser')
        self.codigo = self.soup.find("div", {"class":"user-tab-content"})
        self.datos = list
        self.etiquetas = list

    def extraer_datos(self):
        '''
        x
        '''
        try:
            self.datos = self.codigo.find_all('div', class_='answer-votes')
        except AttributeError:
            print("El id es incorrecto.\n")
            sys.exit()
        self.etiquetas = self.codigo.find_all('a', class_='post-tag')
        paginacion = self.soup.find("div", {"class":"s-pagination pager fr"})
        try:
            paginas = paginacion.find_all('a', class_='s-pagination--item js-pagination-item')
        except AttributeError:
            print("El usuario no tiene etiquetas.\n")
            sys.exit()
        numero_paginas = len(paginas)
        if numero_paginas > 1:
            for index in range(2, numero_paginas+1):
                new_url = self.url + "&sort=votes&page=" + str(index)
                response = requests.get(new_url)
                soup = BeautifulSoup(response.content, 'html.parser')
                codigo= soup.find("div", {"class":"user-tab-content"})
                mas_datos = codigo.find_all('div', class_='answer-votes')
                mas_tags = codigo.find_all('a', class_='post-tag')
                self.datos = self.datos + mas_datos
                self.etiquetas = self.etiquetas + mas_tags
    def generar_txt(self):
        '''
        x
        '''
        #self.archivo = open("Datos.txt", "w")
        with open("Datos.txt", "w") as arhivotxt:
            for longitud, data in enumerate(self.datos):
                if int(data.text) != 0:
                    rep = int(data.text)
                    while rep > 0:
                        #self.archivo.write(self.etiquetas[longitud].text)
                        #self.archivo.write('\n')
                        arhivotxt.write(self.etiquetas[longitud].text)
                        arhivotxt.write('\n')
                        rep -= 1
        #self.archivo.close()

    def generar_wordcloud(self):
        '''
        x
        '''
        self.usuario.url = self.url
        textdata = ""
        #nube = open('Datos.txt', 'r+')
        with open("Datos.txt", "r+") as nube:
            textdata = nube.read().replace('-', '')
        wordcloud = WordCloud(background_color='white', max_words=900,
        width=1200, height=750, regexp = r"(.+)", collocations = False).generate(textdata)
        plt.figure(figsize = (12, 10), facecolor = None)
        plt.imshow(wordcloud)
        plt.axis("off")
        plt.tight_layout(pad = 0)
        plt.show()

def main():
    '''
    kjfekjfekrelj
    '''
    nube = WebScrapping("32292")
    nube.extraer_datos()
    nube.generar_txt()
    nube.generar_wordcloud()

if __name__ == '__main__':
    main()
