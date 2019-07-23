from errors import DataNotProvided, IsNotADictionary, MinItemValueNotFound

def formatar_dados(str_data: str):

    # se nao tem dados lanca erro
    if not str_data:

        raise DataNotProvided

    # lista com cada linha do arquivo
    log_lines = list()

    # logica simples pra validar primeira linha
    first_line = True

    # interar as linhas do arquivo e formatar/padronizar dados 
    for line_unclear in str_data:

        # remove a quebra de linha
        line = line_unclear.rstrip('\n')
        
        # TODO: melhorar essa padronizacao, talvez usar um REGEX
        # padronizar dados
        line = line.replace('\t', '|')
        line = line.replace('    ', '|')
        line = line.replace('||', '|')
        line = line.replace('||', '|')
        line = line.replace('||', '|')

        # limpar titulos
        if first_line:
        
            first_line = False

            line = line.replace(' ', '')

        # adiciona a linha na lista de linhas ja limpas
        log_lines.append(line)
    
    return '\n'.join(log_lines)

def pegar_menor_item(dicio: dict):
    
    if not isinstance(dicio, dict):

        raise IsNotADictionary
    
    menor_item = None
    
    try:

        menor_item = min(dicio, key=lambda key: dicio[key])

    except Exception as e:

        print(e)
        raise MinItemValueNotFound

    return menor_item
