
import datetime as dt

import numpy as np

class Stock:
    def __init__(self):
        #self, ticker, apertura, cierre, volumen, logs
        #self.ticker = ticker
        #self.apertura = apertura
        #apertura>0
        #self.cierre = cierre
        #cierre>0
        #self.volumen = volumen
        #volumen>0
        #self.log = self.filtrar_por_ticker(logs, ticker)
        pass
        
    def obtener_tasa(self):
        return (self.cierre / self.apertura) - 1
        
    def obtener_archivo(self):
        archivo = input('Ingrese el nombre del archivo de transacciones: ')
        while archivo=="" or not archivo.endswith(".csv"):
            print("Nombre de archivo no válido")
            archivo = input('Ingrese el nombre del archivo de transacciones:')
        return archivo
    
    def cargar_historial(self, archivo):
        logs = []
        with open(archivo, 'r') as file:
            for lista in file:
                split = lista.split(",")
                logs.append(split)
                return logs
        
    def sin_repetidos(self, logs):
        list = set()
        for entry in logs:
            list.add(entry[1])
        return list
    
    def generar_lista_ticker(self, archivo):
        filtro = []
        lista = input('Ingrese los tickers que desea graficar, separados por coma: ').split(',')
        for ticker in lista:
            while ticker not in archivo[1]: 
                ticker = input('Ticker no valido, ingrese nuevamente: ')
            filtro.append(ticker)
        return filtro
    
    def filtrar_por_ticker(self, logs, archivo):
        filtered_list = []
        for entry in logs:
            if entry[1] in archivo:
                filtered_list.append(entry)
        return filtered_list
    
    def graficar_historial(self, logs, apertura, cierre): #pasarla a ejecutar
        fecha_inicio = dt.date(int(apertura[0]),int(apertura[1]),int(apertura[2]))
        fecha_fin = dt.date(int(cierre[0]),int(cierre[1]),int(cierre[2]))
        fig, ax = plot.subplots(3)
        fig.set_size_inches(18.5, 10.5)
        ax[0].set_xlin[[fecha_inicio,fecha_fin]]
        ax[1].set_xlin[[fecha_inicio, fecha_fin]]
        ax[2].set_xlin[[fecha_inicio, fecha_fin]]
        for i in self.sin_repetidos(logs):
            logs_de_ticker=self.filtrar_por_ticker(logs,[i])
            fechas=[]
            apertura=[]
            cierre=[]
            volumen=[]
            for entry in logs_de_ticker:
                fechas.append(then = dt.datetime.strptime(entry[0], '%Y-%m-%d').date())
                if entry[3] != 'None':
                    apertura.append(float(entry[3]))
                else:
                    apertura.append(None)
                if entry[4] != 'None':
                    cierre.append(float(entry[4]))
                else:
                    cierre.append(None)
                if entry[5] != 'None':
                    volumen.append(float(entry[5]))
                else:
                    volumen.append(None)
            puntos_x= np.asarray(fechas)
            d_apertura=np.asarray(apertura)
            d_cierre = np.asarray(cierre)
            d_volumen = np.asarray(volumen)

            ax[0].plot(puntos_x,d_apertura,color='b',label=i)
            ax[0].set_title("Apertura")

            ax[1].plot(puntos_x, d_cierre, color='g', label=i)
            ax[1].set_title("Cierre")

            ax[2].plot(puntos_x, d_volumen, color='r', label=i)
            ax[2].set_title("Volumen")
        ax[0].legend()
        ax[1].legend()
        ax[2].legend()
        fig.tight_layout(pad=3.0)
        plot.show()
        return apertura,cierre,volumen
    
    def ejecutar(self):
        carga = self.cargar_historial(self.obtener_archivo())
        lista = self.generar_lista_ticker(self.obtener_archivo())
        self.filtrar_por_ticker(carga, lista)
    


app = Stock()
app.ejecutar()
archivo_completo = Stock().obtener_archivo()
logs = Stock.cargar_historial(archivo_completo)
tickers = input("Ticker: ").split(',')
lista_de_tickers=tickers.split(',')
inicio= input("Fecha de inicio: ")
fin = input("Fecha de fin: ")
if not inicio:
    inicio="2019/02/05"
if not fin:
    fin="2021/06/15"
fechainicio=dt.datetime.strptime(inicio,"%Y/%m/%d")
fechafin = dt.datetime.strptime(fin, "%Y/%m/%d")
stock = Stock(tickers,fechainicio,fechafin,logs)
logs_filtrados = stock.filtrar_por_ticker(logs,lista_de_tickers)
stock.graficar_historial(logs_filtrados,inicio,fin)
print("Tasa de retorno",stock.obtener_tasa())
    

    


