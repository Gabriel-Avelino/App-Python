import requests
from tkinter import *
from tkinter import ttk


def coleta_cotacoes():
    global text
    if not text:
        requisicao = requests.get('https://economia.awesomeapi.com.br/json/last/USD-BRL,EUR-BRL,BTC-BRL')
        requisicao_dic = requisicao.json()

        cotacao_dolar = requisicao_dic['USDBRL']['bid']
        cotacao_euro = requisicao_dic['EURBRL']['bid']
        cotacao_btc = requisicao_dic['BTCBRL']['bid']

        text = f'''
Dólar: {cotacao_dolar}
Euro: {cotacao_euro}
BTC: {cotacao_btc}
        '''
    else:
        text = ''

    txt_cotacoes['text'] = text
    botao.config(background='#4E97D1')


janela = Tk()  # Cria Janela
janela.title('Cotações Atuais das Moedas')
janela.geometry('400x400')
janela.config(background='#242424')

text = ''

txt_orientacao = Label(janela, text='Para mostrar as cotações, clique no botão.', background='#242424', foreground='#ddd')
txt_orientacao.pack(padx=40, pady=40)

s = ttk.Style()
s.configure('Custom.TButton', background='#4E97D1', borderwidth=0, bordercolor='#4E97D1', focusthickness=0, focuscolor='#4E97D1')
botao = ttk.Button(janela, text='Buscar Cotações \nDólar, Euro e BTC', command=coleta_cotacoes, style='Custom.TButton', width=20)
botao.pack()

txt_cotacoes = Label(janela, text='', foreground='#ddd')
txt_cotacoes.config(background='#242424')
txt_cotacoes.pack()

janela.mainloop()  # Mantém a janela em funcionamento
