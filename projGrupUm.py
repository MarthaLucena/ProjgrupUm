import tkinter as tk
import csv
from datetime import datetime

class Questionario:
    def __init__(self):
        self.perguntas = [
            "Qual é a sua idade?",
            "Qual gênero? (Feminino/Masculino/Outro)",
            "Qual é o seu bairro?",
            "Você tem seguro de vida atualmente? (Sim/Não/Não sei)",
            "Você já considerou adquirir um seguro de vida? (Sim/Não/Não sei)",
            "Você acredita que um seguro de vida é importante para proteger sua família em caso de sua morte ou invalidez? (Sim/Não/Não sei)",
            "Você já enfrentou dificuldades financeiras devido à perda de um ente querido sem seguro de vida? (Sim/Não/Não sei)",
            "Você considera o custo de um seguro de vida um investimento valioso para o futuro de sua família? (Sim/Não/Não sei)",
            "Você está ciente dos benefícios de um seguro de vida para cobrir despesas médicas em caso de doenças crônicas? (Sim/Não/Não sei)"
        ]
        self.conjunto_respostas = []

    def salvar_respostas(self, entries, root):
        # Obtém as respostas dos campos de entrada
        respostas = [entry.get() for entry in entries]
        # Adiciona a data e hora como última resposta
        respostas.append(datetime.now().strftime("%Y-%m-%d %H:%M:%S"))
        # Adiciona as respostas ao conjunto de respostas
        self.conjunto_respostas.append(respostas)

    def salvar_respostas(self, entries, root):
    # Obtém as respostas dos campos de entrada
        respostas = [entry.get() for entry in entries]
    
    # Verifica se a idade é "00"
        if respostas[0] == "00":
            self.salvar_arquivo_csv()  # Salva as respostas antes de finalizar o programa
            root.destroy()
        else:
            # Adiciona a data e hora como última resposta
            respostas.append(datetime.now().strftime("%Y-%m-%d %H:%M:%S"))
            # Adiciona as respostas ao conjunto de respostas
            self.conjunto_respostas.append(respostas)

            # Limpa os campos de entrada
            for entry in entries:
                entry.delete(0, tk.END)

    def salvar_arquivo_csv(self):
        # Salva as respostas em um arquivo CSV
        with open('respostas.csv', 'w', newline='') as file:
            writer = csv.writer(file)
            writer.writerow(self.perguntas + ["Data e Hora"])  # Escreve as perguntas e a coluna para data e hora
            for resposta in self.conjunto_respostas:
                writer.writerow(resposta)

        print("As respostas foram salvas em respostas.csv")

    def criar_formulario(self):
        # Criar a janela principal
        root = tk.Tk()
        root.title("Questionário")

        # Lista para armazenar os campos de entrada
        entries = []

        def verificar_idade():
            idade = entries[0].get()
            if idade == "00":
                self.salvar_arquivo_csv()  # Salva as respostas antes de finalizar o programa
                root.destroy()
            else:
                self.salvar_respostas(entries, root)

        # Adicionando as perguntas à interface
        labels = []
        for i, pergunta in enumerate(self.perguntas):
            label = tk.Label(root, text=pergunta)
            label.grid(row=i, column=0, padx=10, pady=5, sticky="w")
            entry = tk.Entry(root)
            entry.grid(row=i, column=1, padx=10, pady=5, sticky="e")
            labels.append(label)
            entries.append(entry)

        # Botão para enviar as respostas
        submit_button = tk.Button(root, text="Enviar Respostas", command=verificar_idade)
        submit_button.grid(row=len(self.perguntas), columnspan=2, padx=10, pady=10)

        # Rodar o loop principal da interface
        root.mainloop()


if __name__ == "__main__":
    questionario = Questionario()
    questionario.criar_formulario()







def salvar_respostas(self, entries, root):
    # Obtém as respostas dos campos de entrada
    respostas = [entry.get() for entry in entries]
    
    # Verifica se a idade é "00"
    if respostas[0] == "00":
        self.salvar_arquivo_csv()  # Salva as respostas antes de finalizar o programa
        root.destroy()
    else:
        # Adiciona a data e hora como última resposta
        respostas.append(datetime.now().strftime("%Y-%m-%d %H:%M:%S"))
        # Adiciona as respostas ao conjunto de respostas
        self.conjunto_respostas.append(respostas)

        # Limpa os campos de entrada
        for entry in entries:
            entry.delete(0, tk.END)
