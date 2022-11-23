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

