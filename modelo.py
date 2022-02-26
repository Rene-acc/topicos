import numpy as np
import pandas as pd
from nltk.corpus import stopwords
from wordcloud import ImageColorGenerator, WordCloud
import matplotlib.pyplot as plt
from matplotlib.widgets import Slider
from PIL import Image


class modelo():
    
    def __init__(self):
        self._archivo = None
        self._texto = None
        self._archivoHead = None
        self._encabezado = None
        self._datos = None
        self._x = None
        self._y = None
        self._slider = []
        self._stopwords = set(stopwords.words('spanish'))
        self._stopwords.update(stopwords.words('english'))
        self._stopwords.update({'https','merida', 'yucatan','yuc','mérida','así','va','co','día','dio','da','voy','hoy','si','yucatán','mas',
        'dia','im', 'en', 'la', 'del', 'ñeñe','es', 'para', 'los', 'de', 'a', 'me','ese', 'que', 'o', 'un', 'este', 'las', 'pero', 'el', 'al', 'con', 'no', 'hasta',
        'por', 'lo', 'te', 'y','mexico', 'asi','gracias','dias','hace','tan','vez'})

    def get_archivo(self):
        return self._archivo

    def set_archivo(self, direccion):
        self._archivo = pd.read_csv(direccion, encoding = "UTF-8")
        self.updateArchivo(self._archivo)

    def updateArchivo(self, archivo):
        self._archivo = archivo
        self._texto = self._archivo.Texto.str.lower()
        self._archivoHead = self._archivo.head(50)
        self._encabezado = list(self._archivoHead.columns)
        self._datos = self._archivoHead.to_numpy().tolist()
        self._x = len(self._encabezado)
        self._y = len(self._datos)
    
    def limpiarTexto(self):
        self._texto = self._texto.str.replace(r'[^\w\s]+', '', regex=True)
        self._texto = self._texto.str.replace(r'^[a-zA-Z]+$', '', regex=True)
        self._texto = self._texto.str.replace(r'[0-9]+', '', regex=True)
        self._texto = self._texto.str.normalize("NFD")
        self._texto = self._texto.str.replace(r"([^n\u0300-\u036f]|n(?!\u0303(?![\u0300-\u036f])))[\u0300-\u036f]+", r"\1", regex=True)
        self._texto = self._texto.str.normalize("NFC")
        self._texto = self._texto.str.replace(r"\bhttps\w+", '', regex=True)
        self._texto = self._texto.str.replace(r'\bjaja.*', '', regex=True)
        self._texto = self._texto.str.replace(r'\bajaj.*', '', regex=True)
        self._texto = self._texto.str.replace(r"[\u0600-\u06ff]|[\u0750-\u077f]|[\ufb50-\ufbc1]|[\ufbd3-\ufd3f]|[\ufd50-\ufd8f]|[\ufd92-\ufdc7]|[\ufe70-\ufefc]|[\uFDF0-\uFDFD]", '', regex=True)

    def get_encabezado(self):
        return self._encabezado
    
    def get_datos(self):
        return self._datos

    def get_x(self):
        return self._x

    def get_y(self):
        return self._y

    def filtrarCSV(self, texto, sentimiento, idioma):
        texto = list(texto.split(" "))
        sentimiento = list(sentimiento.split(" "))
        idioma = list(idioma.split(" "))
        if len(texto) > 0:
            self._archivo = self._archivo.loc[self._archivo['Texto'].str.contains('|'.join(texto), case=False)]
        if len(sentimiento) > 0:
            self._archivo = self._archivo.loc[self._archivo['Sentimiento'].str.contains('|'.join(sentimiento), case=False)]
        if len(idioma) > 0:
            self._archivo = self._archivo.loc[self._archivo['Idioma'].str.contains('|'.join(idioma), case=False)]
        self.updateArchivo(self._archivo)
    
    def nubePalabras(self):
        self.limpiarTexto()
        mascara = np.array(Image.open('circl.png'))
        ColorImagen = ImageColorGenerator(mascara)
        palabras = " ".join(mensaje for mensaje in self._texto)
        nubeDePalabras = WordCloud( mask=mascara,
                                    stopwords=self._stopwords,
                                    min_font_size=7, 
                                    width=1280,
                                    height=720,
                                    relative_scaling=0.1, 
                                    max_words=500, 
                                    contour_color='#A430F0',
                                    random_state=42,
                                    color_func= ColorImagen, 
                                    background_color="black",
                                    contour_width = 3).generate(palabras)
        #colormap='cool'
        nubeDePalabras.to_file('bleh01.png')
        plt.figure( figsize=(15,10), facecolor='k' )
        plt.tight_layout(pad=0)
        plt.imshow(nubeDePalabras)
        plt.axis("off")
        plt.show()

    def histograma(self):
        self.limpiarTexto()
        frecuenciaDePalabras = self._texto.str.split(expand=True).stack().value_counts()
        frecuenciaDePalabras  = frecuenciaDePalabras.drop(list(self._stopwords), axis=0, errors='ignore')
        labels = np.array(frecuenciaDePalabras.index.values)
        values = np.array(frecuenciaDePalabras.to_numpy())
        indSort = np.argsort(values)[::-1]

        labels = np.array(labels)[indSort]
        values = np.array(values)[indSort]
        indexes = np.arange(len(labels))
        plot, axis = plt.subplots(figsize=(20,10))
        N=15

        def bar(val):
            nonlocal indexes, values, labels, plot, axis
            pos = int(slider.val)
            axis.clear()
            if pos+N > len(indexes): 
                n=len(indexes)-pos
            else:
                n=N
            x=indexes[pos:pos+n]
            y=values[pos:pos+n]
            etiquetas = labels[pos:pos+n]
            axis.bar(x,y,width=0.7,align='edge',color='#5A68C6',ecolor='black')
            for i, text in enumerate(etiquetas):
                axis.annotate(text, (x[i]+0.2,values[0]/100), rotation=90, fontsize='16')
                axis.annotate(y[i], (x[i]+0.5,values[0]/100), rotation=90, fontsize='10')

            axis.xaxis.set_ticks([])
            axis.axis([pos, pos+15, 0, values[0]])
            
        barpos = plt.axes([0.18, 0.05, 0.55, 0.03])

        slider = Slider(barpos, 'Posición', 0, len(values)-N, valinit=0)
        slider.on_changed(bar)
        self._slider.append(slider)

        bar(0)
        plt.show()
    
    def archivoCompleto(self):
        self._datos = self._archivo.to_numpy().tolist()
        self._y = len(self._datos)