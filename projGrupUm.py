import csv
import datetime

# Definindo as perguntas
perguntas = [
    "Qual é a sua idade?",
    "Qual gênero? (Feminino/Masculino/Outro)",
    "Qual é o seu bairro?",
    "Você tem seguro de vida atualmente? (Sim/Não/Não sei)",
    "Você já considerou adquirir um seguro de vida? (Sim/Não/Não sei)",
    "Você acredita que um seguro de vida é importante para proteger sua família em caso de sua morte ou invalidez? (Sim/Não/Não sei)",
    "Você já enfrentou dificuldades financeiras devido à perda de um ente querido sem seguro de vida? (Sim/Não/Não sei)",
    "Você considera o custo de um seguro de vida um investimento valioso para o futuro de sua família? (Sim/Não/Não sei)",
    "Você está ciente dos benefícios de um seguro de vida para cobrir despesas médicas em caso de doenças crônicas? (Sim/Não/Não sei)",
    "Data: ",
    "Hora: "
]

# Lista para armazenar as respostas
respostas = []


# Loop principal para solicitar respostas
while True:
    for i, pergunta in enumerate(perguntas):
        resposta = input(pergunta + " ")
        if i == 0 and resposta == '00':
            break  # Se a primeira resposta for '00', encerra o loop
        respostas.append(resposta)
    else:
        continue  # Continue se o loop for concluído sem interrupção
    break  # Interrompe o loop principal se a primeira resposta for '00'



#Obtendo a data e hora atuais
data_hora_atual = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

# Escrevendo as perguntas como colunas no arquivo CSV
nome_arquivo = 'respostas.csv'
with open(nome_arquivo, 'w', newline='') as file:
    writer = csv.writer(file)
    writer.writerow(["Data e Hora"] + [data_hora_atual])  # Escreve a data e hora atual
    writer.writerow(["Pergunta"] + perguntas)  # Escreve as perguntas como cabeçalho
    writer.writerow(["Resposta", *respostas])  # Escreve as respostas como segunda linha

print("As respostas foram salvas em", nome_arquivo)