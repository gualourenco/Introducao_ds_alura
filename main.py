import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

pd.read_csv('ratings.csv')
notas = pd.read_csv('ratings.csv')

print(notas)

# imprime as 5 primeiras notas do arquivo
print(notas.head())

# imprime o formato dessa tabela (linhas, colunas)
print(notas.shape)

notas.columns = ['usuarioId', 'filmeId', 'nota', 'momento']


print(notas['nota'])

# imprime os valores que existem na coluna nota
print(notas['nota'].unique())

# imprime o quanto existe de cada nota, na coluna nota
print(notas['nota'].value_counts())

# imprime a média das notas da coluna nota
print(notas['nota'].mean())

# imprime o valor mediano da coluna
print(notas.nota.median())

# também imprime as primeiras linhas da coluna nota sem uso de chaves
print(notas.nota.head())

# após instalar a matplotlib, podemos retornar em gráficos
# retorna uma tabela geral referente a coluna
print(notas.nota.plot())

# retorna uma tabela do tipo histograma
print(notas.nota.plot(kind='hist'))

# retorna descricao da tabela em consulta, como: qtd de dados, média,
# quantos valores mostram por quarto
print(notas.nota.describe())

# apos instalar o seaborn:
print(sns.boxplot(notas.nota))

# abrindo arquivo movies.csv e colocando em uma variavel
pd.read_csv('movies.csv')
filmes = pd.read_csv('movies.csv')
print(filmes.head())
filmes.columns = ['filmeId', 'titulo', 'genero']

# busco no arquivo em notas somento o referente a coluna do "filmeId"
print(notas.query('filmeId==1'))

# busco todas as colunas "nota" referente o "filmeId==1"
# e tiro uma média das notas em nota
print(notas.query('filmeId==1').nota.mean())

# agrupa todas as notas referente a cada "filmeId"
notas.groupby('filmeId')

# tira a média de cada coluna de cada "filmeId"
notas.groupby('filmeId').mean()

# tira a media somente da coluna "nota" para cada "filmeId"
print(notas.groupby('filmeId').mean()['nota'])

# guardando essa media em uma variavel
medias_por_filme = notas.groupby('filmeId').mean().nota

# Somente os 5 primeiros do filtro de medias por filme
print(medias_por_filme.head())

# plotando um grafico de histograma referente a media das notas
print(medias_por_filme.plot(kind='hist'))

# plotando grafico pelo seaborn
print(sns.boxplot(medias_por_filme))

# plotando um grafico descritivo com ondulacoes, do seaborn
print(sns.distplot(medias_por_filme))

# regula o quanto de linhas o grafico ira especificar nos intervalos
print(sns.distplot(medias_por_filme, bins=10))

# plota um histograma de mais baixo nivel com bibliotecas normais no python
print(plt.hist(medias_por_filme))

# adciona titulo ao histograma do pyplot
plt.title('Histograma das medias dos filmes')

plt.figure(figsize=(5, 8))

# plota o grafico de caixa pelo eixo Y
print(sns.boxplot(y=medias_por_filme))
