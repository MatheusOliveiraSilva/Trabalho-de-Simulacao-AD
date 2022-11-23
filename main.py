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

