from ambiente import Ambiente
from b_modelo_agente import AgenteModelo1
from reativo_agente import AgenteReativo1


# Carregar ambientes!
# Reativo
ambiente1_ag_reativo = Ambiente(3, 3, "./ambientes/ambiente.txt")
ambiente2_ag_reativo = Ambiente(4, 4, "./ambientes/ambiente2.txt")
ambiente3_ag_reativo = Ambiente(8, 8, "./ambientes/ambiente3.txt")
ambiente4_ag_reativo = Ambiente(4, 4, "./ambientes/ambiente4.txt")

# Modelo
ambiente1_ag_modelo = Ambiente(3, 3, "./ambientes/ambiente.txt")
ambiente2_ag_modelo = Ambiente(4, 4, "./ambientes/ambiente2.txt")
ambiente3_ag_modelo = Ambiente(8, 8, "./ambientes/ambiente3.txt")
ambiente4_ag_modelo = Ambiente(4, 4, "./ambientes/ambiente4.txt")

# Criar os agentes
# Reativo
ag_reativo1 = AgenteReativo1(ambiente1_ag_reativo)
ag_reativo2 = AgenteReativo1(ambiente2_ag_reativo)
ag_reativo3 = AgenteReativo1(ambiente3_ag_reativo)
ag_reativo4 = AgenteReativo1(ambiente4_ag_reativo)

# Modelo
ag_modelo1 = AgenteModelo1(ambiente1_ag_modelo)
ag_modelo2 = AgenteModelo1(ambiente2_ag_modelo)
ag_modelo3 = AgenteModelo1(ambiente3_ag_modelo)
ag_modelo4 = AgenteModelo1(ambiente4_ag_modelo)


MAX_ITERACOES = 1000

# Fazer As iterações!
# Reativo
for i in range(0, MAX_ITERACOES):
    if ag_reativo1.definir_acao() == 'HOME':
        break

for i in range(0, MAX_ITERACOES):
    if ag_reativo2.definir_acao() == 'HOME':
        break

for i in range(0, MAX_ITERACOES):
    if ag_reativo3.definir_acao() == 'HOME':
        break

for i in range(0, MAX_ITERACOES):
    if ag_reativo4.definir_acao() == 'HOME':
        break

# Modelo
for i in range(0, MAX_ITERACOES):
    if ag_modelo1.definir_acao() == 'HOME':
        break

for i in range(0, MAX_ITERACOES):
    if ag_modelo2.definir_acao() == 'HOME':
        break

for i in range(0, MAX_ITERACOES):
    if ag_modelo3.definir_acao() == 'HOME':
        break

for i in range(0, MAX_ITERACOES):
    if ag_modelo4.definir_acao() == 'HOME':
        break


# Salver histórico!

# Reativo
with open("./results/resultReativo-ambiente1.txt", "w") as r:
    i = 0
    for line in ag_reativo1.histmov:

        r.write("iteração " + str(i)+": "+str(line)+"\n")
        i = i + 1

with open("./results/resultReativo-ambiente2.txt", "w") as r:
    i = 0
    for line in ag_reativo2.histmov:

        r.write("iteração " + str(i)+": "+str(line)+"\n")
        i = i + 1

with open("./results/resultReativo-ambiente3.txt", "w") as r:
    i = 0
    for line in ag_reativo3.histmov:

        r.write("iteração " + str(i)+": "+str(line)+"\n")
        i = i + 1


with open("./results/resultReativo-ambiente4.txt", "w") as r:
    i = 0
    for line in ag_reativo4.histmov:

        r.write("iteração " + str(i)+": "+str(line)+"\n")
        i = i + 1

# Modelo
with open("./results/resultModel-ambiente1.txt", "w") as r:
    i = 0
    for line in ag_modelo1.histmov:

        r.write("iteração " + str(i)+": "+str(line)+"\n")
        i = i + 1

with open("./results/resultModel-ambiente2.txt", "w") as r:
    i = 0
    for line in ag_modelo2.histmov:

        r.write("iteração " + str(i)+": "+str(line)+"\n")
        i = i + 1

with open("./results/resultModel-ambiente3.txt", "w") as r:
    i = 0
    for line in ag_modelo3.histmov:

        r.write("iteração " + str(i)+": "+str(line)+"\n")
        i = i + 1

with open("./results/resultModel-ambiente4.txt", "w") as r:
    i = 0
    for line in ag_modelo4.histmov:

        r.write("iteração " + str(i)+": "+str(line)+"\n")
        i = i + 1
