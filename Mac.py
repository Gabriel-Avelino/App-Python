import requests
from tkinter import *
from tkmacosx import Button


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
        txt_cotacoes['text'] = text
    else:
        text = ''
        txt_cotacoes['text'] = text


janela = Tk()  # Cria Janela
janela.title('Cotações Atuais das Moedas')
janela.geometry('400x400')
janela.config(background='#242424')

text = ''

txt_orientacao = Label(janela, text='Para mostrar as cotações, clique no botão.', background='#242424', foreground='#ddd')
txt_orientacao.pack(padx=40, pady=40)

botao = Button(janela, text='Buscar Cotações \nDólar, Euro e BTC', command=coleta_cotacoes, bg='#4E97D1', fg='white', activebackground='#AEB6BF', borderless=1, width=200, height=50)
botao.pack()

txt_cotacoes = Label(janela, text='', foreground='#ddd', background='#242424')
txt_cotacoes.pack()

janela.mainloop()  # Mantém a janela em funcionamento
