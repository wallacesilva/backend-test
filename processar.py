import os
import csv
import io
from errors import MinItemValueNotFound
from func import formatar_dados, pegar_menor_item

"""
    - informar qual categoria cliente gastou mais
    - informar qual foi o mes que cliente mais gastou
    - quanto de dinheiro o cliente gastou
    - quanto de dinheiro o cliente recebeu
    - saldo total de movimentacoes do cliente
"""

# nome do arquivo de log
file_log = 'movimentacao.log'

# define o caminho completo para o arquivo de log, baseado na pasta atual
filepath_log = os.path.join(os.getcwd(), file_log)

# valida se existe arquivo
if not os.path.exists(filepath_log):

    print('Arquivo nao encontrado.')
    exit(0)

# pegar dados das linhas ja formatados
linhas_formatadas = ''

# abrir arquivo
with open(filepath_log) as log_file: # param: encoding='utf-8'

    log_data = log_file.readlines()

    # formata os dados para serem tratados
    linhas_formatadas = formatar_dados(log_data)

# ler as linhas limpas usando o formatador
dict_reader = csv.DictReader(io.StringIO(linhas_formatadas), delimiter='|')

# dados a serem tratados
categoria_gastou_mais = ''
gastos_por_categoria = {}
mes_gastou_mais = ''
gastos_por_mes = {}
gastos = 0.0
recebimentos = 0.0

# interar nas linhas em forma de dicionario de dados
for row in dict_reader:

    # data da movimentacao
    data = row.get('Data').strip()
    # descricao da movimentacao
    descricao = row.get('Descricao').strip().upper()
    # valor monetario pre-tratado
    valor_str = row.get('Valor').replace(' ', '').replace('.', '').replace(',', '.')
    # nome da categoria da movimentacao
    categoria_nome = row.get('Categoria').strip().upper()
    # somente nome do mes
    mes = data.split('-')[1]
    
    # valor moneterario em float
    valor = float(valor_str)

    # tiver nome de categoria incrementa valor no dicionario
    if categoria_nome:

        # add categoria que gastou mais
        gastos_por_categoria[categoria_nome] = gastos_por_categoria.get(categoria_nome, 0.0) + valor

    # add mes que gastou mais
    gastos_por_mes[mes] = gastos_por_mes.get(mes, 0.0) + valor

    # somar gastos
    if valor < 0:
        gastos = gastos + valor

    # somar recebimentos
    if valor >= 0:
        recebimentos = recebimentos + valor

try:
    
    # pega categoria que gastou mais
    categoria_gastou_mais = pegar_menor_item(gastos_por_categoria)

except MinItemValueNotFound as e:
    
    print('Erro ao pegar menor valor gasto em categorias.')
    print(e)

try:

    # pega mes que gastou mais
    mes_gastou_mais = pegar_menor_item(gastos_por_mes)

except MinItemValueNotFound as e:
    
    print('Erro ao pegar menor valor gasto no mes.')
    print(e)

# saldo total
saldo_total = recebimentos + gastos

print('Categoria que gastou mais: \t' + categoria_gastou_mais)
print('Mes com maior gasto: \t\t' + mes_gastou_mais)
print('Total de Gastos: \t\tR$ %.2f' % gastos)
print('Total de Recebimentos: \t\tR$ %.2f' % recebimentos)
print('Saldo Total: \t\t\tR$ %.2f' % saldo_total)

# print('---------')
# print('Gastos por categoria: ', gastos_por_categoria)
# print('Gastos por mes: ', gastos_por_mes)