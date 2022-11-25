# módulos e definições de variáveis dadas pelo professor
import simpy
import random
import math

rhos = [0.2, 0.4, 0.6, 0.8, 0.9]
lambdas = rhos 

#---------------------------------------------------------------------------------------------------------------------

# funções das variáveis aleatórias

# CDF do tempo entre chegadas 
def A(t, lambdas):
    return 1 - math.exp(-(lambdas * t))

# pdf do tempo entre chegadas
def a(t, lambdas):
    return lambdas * math.exp(-lambdas * t)

# como temos mu = 1
# CDF do tempo de serviço
def B(t, rhos):
    return 1 - math.exp(-(t))

def b(t, rhos):
    return lambdas * math.exp(-t)

#---------------------------------------------------------------------------------------------------------------------

RANDOM_SEED = 42
random.seed(RANDOM_SEED)

# nosso tempo médio de serviço é 1 
X_mean = 1
X1_mean = X_mean
X2_mean = X_mean

# Entra na fila 1
def fila1(env, name, servidor, lambdas):
     yield env.timeout(random.expovariate(lambdas)) # chegada Poisson aleatória exponencialmente distribuída na fila 1
     print('%s chegou na fila 1 no segundo  %f' % (name, env.now)) # chegada na fila 1 no momento do timout aleatório acima

     # Faz request pelo serviço, aqui dentro vai ser checado se está ocupado ou não, etc. 
     with servidor.request() as req:
         yield req # espera até que o servidor esteja livre

         # Começa o serviço
         print('%s começou o serviço da fila 1 no segundo %f' % (name, env.now))
         yield env.timeout(random.expovariate(1)) # serviço com duração aleatória mas exponencialmente distribuída com tempo médio X1 = mu = 1 
         print('%s terminou o serviço da fila 1 no segundo %f' % (name, env.now))
         # cria um cliente 2 que vai entrar na fila 2
         env.process(fila2(env, name, servidor, env.now)) 


# Entra na fila 2
def fila2(env, name, servidor, tempo_de_chegada):

    print('%s chegou na fila 2 no segundo %f' % (name, tempo_de_chegada))

    with servidor.request() as req:
        yield req

        print('%s começou o serviço da fila 2 no segundo %f' % (name, env.now))
        yield env.timeout(random.expovariate(1)) # serviço com duração aleatória mas exponencialmente distribuída com tempo médio X2 = mu = 1
        print('%s terminou o serviço da fila 2 no segundo %f' % (name, env.now))
        

# nosso servidor atende um cliente por vez, vou alocar ele no nosso ambiente "env"
env = simpy.Environment()
servidor = simpy.Resource(env, capacity=1)

for i in range(20):
    env.process(fila1(env, 'Cliente %d' % i, servidor, 0.9))

env.run()


