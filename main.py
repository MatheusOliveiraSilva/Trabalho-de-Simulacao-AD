# Funções de cálculo das estatísticas 

# Média de uma rodada 
def media(rodada):
    return sum(rodada)/len(rodada)

# Média das amostras
def media_amostras(amostras):
    return sum(amostras)/len(amostras)

# acima poderia usar a mesma função para as duas coisas, mas procuro adicionar semântica no código, para que ele seja mais legível.

# Variancia de uma rodada
def variancia(rodada):
    m = media(rodada)
    return sum([(x-m)**2 for x in rodada])/len(rodada-1)

# Desvio padrão de uma rodada ( Vai ser útil para o cálculo da confiança ) 
def desvio_padrao(rodada):
    return variancia(rodada)**(1/2)

# --------------------------------------------------------------------------------------------------------------------------------

# Usaremos random para gerar os números pseudo-aleatórios
import random as rd

# --------------------------------------------------------------------------------------------------------------------------------

# definindo número de euler para uso posterior:
e = 2.71828182845904523536028747135266249775724709369995

taxa_de_entrada = 1/10
taxa_de_servico = 1/2

# CDF do tempo entre chegadas:
def A(t):
    return 1 - e**(-(taxa_de_entrada*t))

# pdf do tempo entre chegadas:
def a(t):
    return taxa_de_entrada*e**(-(taxa_de_entrada*t))


# CDF do tempo de serviço:
def B(t):
    return 1 - e**(-(taxa_de_servico)*t)

# pdf do tempo de serviço:
def b(t):
    return taxa_de_servico*e**(-(taxa_de_servico)*t)

#--------------------------------------------------------------------------------------------------------------------------------

# o lambda = rho nesse caso ( taxa de serviço (mu) = 1  )  

rhos = [0.2, 0.4, 0.6, 0.8, 0.9]

# --------------------------------------------------------------------------------------------------------------------------------

"""
Vamos tentar definir os valores que já temos, para solução analítica. 

Cenario: temos uma fila 1 com prioridade preemptiva sobre a fila 2. E ambas as filas tem tempo de atendimento exponencialmente distribuido com pdf e cdf já
descritas acima. 

"""

X1_MEAN = 1         # Avg. processing time in minutes of queu 1
X2_MEAN = 1         # Avg. processing time in minutes of queu 2

W1_MEANs = [(rhos[i]/2 + X1_MEAN)/(1-rhos[i]/2) for i in range(len(rhos))]       # Avg. interarrival time in minutes of queu 1

T1_MEANs = [X1_MEAN + W1_MEANs[i] for i in range(len(W1_MEANs))]       # Avg. time in queu 1

W2_MEANs = [(W1_MEANs[i] + (rhos[i]/2) * T1_MEANs[i])/(1-rhos[i]) for i in range(len(rhos))]       # Avg. interarrival time in minutes of queu 2

T2_MEANs = [X2_MEAN + W2_MEANs[i] for i in range(len(W2_MEANs))]       # Avg. time in queu 2

N1 = [T1_MEANs[i]*rhos[i] for i in range(len(rhos))] # número de clientes na fila de espera 1

N2 = [T2_MEANs[i]*rhos[i] for i in range(len(rhos))] # número de clientes na fila de espera 1

Nq1 = [W1_MEANs[i]*rhos[i] for i in range(len(rhos))] # número de clientes na fila de espera 1

Nq2 = [W2_MEANs[i]*rhos[i] for i in range(len(rhos))] # número de clientes na fila de espera 2

# --------------------------------------------------------------------------------------------------------------------------------

# printando para ver os valores analíticos.
for i in range(len(rhos)):
    print("Para rho = ", rhos[i], " temos que o tempo que se passa no sistema da fila 1 é: ", T1_MEANs[i], " segundos e o tempo que se passa no sistema da fila 2 é: ", T2_MEANs[i], " segundos. \n")
    print("E o tempo de espera na fila 1 é: ", W1_MEANs[i], " segundos e o tempo de espera na fila 2 é: ", W2_MEANs[i], " segundos. \n")
    print("O número de clientes no sistema da fila 1 é: ", N1[i], " e o número de clientes no sistema da fila 2 é: ", N2[i], " . \n")
    print("O número de clientes na fila de espera da fila 1 é: ", Nq1[i], " e o número de clientes na fila de espera da fila 2 é: ", Nq2[i], " . \n")
    print("E o tempo passado no sistema inteiro é : ", T1_MEANs[i] + T2_MEANs[i], " segundos. \n")
    
# --------------------------------------------------------------------------------------------------------------------------------

