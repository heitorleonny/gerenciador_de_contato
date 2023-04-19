import PySimpleGUI as sg


class Contato:
    def __init__(self, nome, endereco, numero, email):
        self.nome = nome 
        self.endereco = endereco
        self.numero = numero
        self.email = email
        



#layout 
class Tela:
    def __init__(self):
        layout = [
            [sg.Text('GERENCIADOR DE CONTATOS', size=(15,0))],
            [sg.Text('Adicione um novo contato:')],
            [sg.Text('Nome:', size=(5,0)), sg.Input('', size=(8,0), key='nome'), sg.Text('Endereço:', size=(7, 0)), sg.Input('', size=(8, 0), key='endereco')],
            [sg.Text('Número:', size=(6,0)), sg.Input('', size=(10,0), key='numero'), sg.Text('E-mail:', size=(6, 0)), sg.Input('', size=(10, 0), key='email')],
            [sg.Button('Salvar', size=(7,0), key='salvar'), sg.Button('Mostrar', size=(7,0), key='mostrar')],
            [sg.Output(size=(40,20))],
                
        ]
        self.lista_contatos = []
        
        #janela
        self.janela = sg.Window('GERENCIADOR DE CONTATOS').layout(layout)
        
       
        
        
    def adicionar_contato(self, contato):
        self.lista_contatos.append(contato)
        
    def mostrar_contatos(self):
        for contato in self.lista_contatos:
            print(contato.nome)
            print(contato.endereco)
            print(contato.numero)
            print(contato.email)
            print()
            
        
        
    def iniciar(self):
        while True:
            event, values = self.janela.Read()
            if event == sg.WINDOW_CLOSED:
                break
            if event == 'salvar':
                novo_contato = Contato(values['nome'], values['endereco'], values['numero'], values['email'])
                self.adicionar_contato(novo_contato)
            elif event == 'mostrar':
                self.mostrar_contatos()






tela = Tela()
tela.iniciar()