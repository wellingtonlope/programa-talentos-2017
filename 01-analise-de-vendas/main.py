import pandas

dados = pandas.read_csv('dados.csv', delimiter=',')

codigos = dados.drop_duplicates('codigo')
dias = dados.drop_duplicates('data')

for dia in dias['data']:
	for codigo in codigos['codigo']:
		print("{} no {} = {:.2f}".format(dados[dados['codigo'] == codigo]['nome'].iloc[0], dados[dados['data'] == dia]['data'].iloc[0], dados[(dados['codigo'] == codigo) & (dados['data'] == dia)]['preco'].sum()))
	print('Total dia {}: {:.2f}'.format(dados[dados['data'] == dia]['data'].iloc[0], dados[dados['data'] == dia]['preco'].sum()))
	print('')
print('Total vendido: {:.2f}'.format(dados['preco'].sum()))