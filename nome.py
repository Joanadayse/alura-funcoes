# Você recebeu uma demanda para tratar 2 
# listas com os nomes e sobrenomes de cada 
# estudante concatenando-as para apresentar 
# seus nomes completos na forma Nome Sobrenome.
# As listas são:

nomes = ["joão", "MaRia", "JOSÉ"]
sobrenomes = ["SILVA", "souza", "Tavares"]

# O texto exibido ao fim deve ser parecido com:
# "Nome completo: Ana Silva"

nome_completo= map(lambda nome , sobrenome: f"{nome.title()} {sobrenome.title()}" , nomes,sobrenomes)

for n in nome_completo:
    print(f"Nome completo:{n}")