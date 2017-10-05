# Perceptron modelo;

# aplicativo para verificar se o caractere é J ou H;
# J = 1, H = -1

# J = [1, 1, 1, 1, 1, -1, -1, 1, -1, -1, -1, -1, 1, -1, -1, 1, -1, 1, -1, -1, 1, 1, 1, -1, -1] | resposta = 1
# H = [1, -1, -1, -1, 1, 1, -1, -1, -1, 1, 1, 1, 1, 1, 1, 1, -1, -1, -1, 1, 1, -1, -1, -1, 1] | resposta = -1


# pesos (sinapses)
w = [0,0]

# entradas
x = [[1, 1, 1, 1, 1, -1, -1, 1, -1, -1, -1, -1, 1, -1, -1, 1, -1, 1, -1, -1, 1, 1, 1, -1, -1],
     [1, -1, -1, -1, 1, 1, -1, -1, -1, 1, 1, 1, 1, 1, 1, 1, -1, -1, -1, 1, 1, -1, -1, -1, 1]]

# respostas esperadas
t = [1,-1]

# bias (ajuste fino)
b = 0

#saida
y = 0

# numero maximo de iteracoes
max_int = 10

# taxa de aprendizado
taxa_aprendizado = 0.0000015

#theshold
threshold = 1

# Caracter
letra = ""

# resposta = acerto ou falha
resposta = ""

# dicionario de dados
d = {'1,1,1,1,1,-1,-1,1,-1,-1,-1,-1,1,-1,-1,1,-1,1,-1,-1,1,1,1,-1,-1' : 'Letra J',
     '1,-1,-1,-1,1,1,-1,-1,-1,1,1,1,1,1,1,1,-1,-1,-1,1,1,-1,-1,-1,1' : 'Letra H' }

print("Treinando")

# funcao para converter listas em strings
def listToString(list):
    s = str(list).strip('[]')
    s = s.replace(' ', '')
    return s

# inicio do algoritmo
for k in range(1,100):
    acertos = 0    
    print("ITERACAO "+str(k)+"--------------------------------------------------")
    for i in range(0,len(x)):
        soma = 0
        # pega o caracter no dicionário
        if (listToString(x[i])) in d:
            letra = d[listToString(x[i])]
        else:
            letra = ""

        # para calcular a saida do perceptron, cada entrada de x eh multiplicada
        # pelo seu peso w correspondente
        for j in range(0,2):
            soma += x[i][j] * w[j]

        # a saida eh igual a adicao do bias com a soma anterior
        y_in = b + soma
        
        #print("y_in = ",str(y_in))

        # funcao de saida eh determinada pelo threshold
        if y_in > threshold:
            y = 1
        elif y_in >= -threshold and y_in <= threshold:
            y = 0
        else:
            y = -1        

        # atualiza os pesos caso a saida nao corresponda ao valor esperado
        if y == t[i]:
            acertos+=1
            resposta = "Acerto"
        else:
            for j in range (0,len(w)):                
                w[j] = w[j] + (taxa_aprendizado * t[i] * x[i][j])
            b = b + taxa_aprendizado * t[i]
            resposta = "Falha - Peso atualizado"

        #imprime a resposta
        if y == 1:
            print(letra +" = J = "+resposta)
        elif y == 0:
            print(letra +" = padrao nao identificado = "+resposta)
        elif y == -1:
            print(letra +" = H = "+resposta)

    if acertos == len(x):
        print("Funcionalidade aprendida com "+str(k)+" iteracoes")
        break;
    print("")
print("------------------------------------------------------------")
print("Finalizado")
print("------------------------------------------------------------")

#Agora fazendo testes com 8% de Erro
#Entradas
xnovo = [[1, 1, 1, 1, 1, -1, -1, 1, -1, -1, -1, -1, 1, -1, -1, 1, -1, 1, -1, -1, 1, 1, 1, -1, 1],
        [1, -1, -1, -1, 1, 1, -1, -1, -1, 1, 1, 1, 1, 1, 1, 1, -1, -1, -1, 1, 1, -1, 1, -1, 1]]

#Saida
ynovo = 0
print("Para x%")

# para calcular a saida do perceptron, cada entrada de x eh multiplicada
# pelo seu peso w correspondente
#for treino in 
for a in range(0,len(xnovo)):
    for b in range(0,2):
        soma += xnovo[a][b] * w[b]
        print(w)

    # a saida eh igual a adicao do bias com a soma anterior
    y_novo = b + soma

    # funcao de saida eh determinada pelo threshold
    if y_novo > threshold:
        ynovo = 1
    elif y_novo >= -threshold and y_in <= threshold:
        ynovo = 0
    else:
        ynovo = -1

    #imprime a resposta
    if ynovo == 1:
        print("J, "+"Acertou")
    elif ynovo == 0:
        print("Padrão nao identificado")
    elif ynovo == -1:
        print("H, "+"Acertou")
print("------------------------------------------------------------")


