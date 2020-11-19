## capa de livro custa 24,95, as livrarias recebem 40% de desconto. transporte custa 3,00 para o primeiro exemplar e 0,75 para os adicionais,
## qual custo para 60 copias

capa = 24.95 - (24.95*0.4)

transporte1 = 3.00

transporte2 = 0.75

livro1 = capa + transporte1

demais_livros = (capa + transporte2) * 59

total = livro1 + demais_livros

print("valor total do custo dos livros: ", total)

