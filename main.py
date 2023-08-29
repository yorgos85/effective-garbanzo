# importando Pandas

import pandas as pd

# Carregando CSV

df = pd.read_csv('/Users/usuario/Desktop/projeto_versao_final_Yorgos_Oliveira/tabela-fipe-historico-precos.csv')

print('################################################')
print('Bem vindo ao sistema de informacoes de veiculos ')
print('################################################')

# Apresentando a opcao 1 ao usuario para apresentar os dados

inf = int(input(" Digite 1: Para Informacoes descritivas sobre os veiculo \n Digite 2 : Para filtrar registros \n Digite 3: Para realizar agrupamentos:\n "))

if inf == 1:
  quant_registros = df.shape[0]
  quant_colunas = df.shape[1]
  n_colunas = df.columns[1:]
  coluna_max = df[['anoModelo', 'mesReferencia','anoReferencia','valor']]
  coluna_min = df[['anoModelo', 'mesReferencia','anoReferencia','valor']]
  coluna_media = df[['anoModelo', 'mesReferencia','anoReferencia','valor']]
  coluna_media = coluna_media.mean()
  coluna_min = coluna_min.min()
  coluna_max = coluna_max.max()
    
  print(f'Quantidade de registros total é {quant_registros} registros ')
  print(f'Quantidade de colunas total é:{quant_colunas} ')
  print(f'Nome e tipo de cada coluna é:\n {n_colunas[1:]} ')
  print(f'Os valores maximos de cada coluna é:\n {coluna_max} ')
  print(f'Os valores minimos de cada coluna é:\n {coluna_min} ')
  print(f'Os valores media de cada coluna é:\n {coluna_media} ')
  
# Apresentando a opcao 2 ao usuario para apresentar opcoes de filtros
  
if inf == 2:
    opcoes = int(input("Digite as opcoes de filtro:\n 1 - Codigo fipe\n 2 - Marca\n 3 - Modelo\n 4 - Ano Modelo\n 5 - Mes Referencia\n 6 - Ano referencia\n 7 - Valor\n "))
    if opcoes == 1:
      cod_fipe = input('Digite o código fip que deseja filtrar:')
      comp = input('Digite a comparacao:\n igual: ==\n diferente: !=\n')
      if comp == '==':
          fipe_filtrados = df[df['codigoFipe'] == cod_fipe]
          print(fipe_filtrados)
      if comp == '!=':
          fipe_filtrados = df[df['codigoFipe'] != cod_fipe]
          print(fipe_filtrados)    
      
    elif opcoes == 2:
        marca = str(input('Digite a marca que deseja filtrar: '))
        comp = input('Digite a comparacao:\n igual: ==\n diferente: !=\n')
        if comp == '==':
            marca_filtradas = df[df['marca'] == marca]
            print(marca_filtradas)
        if comp == '!=':
            marca_filtradas = df[df['marca'] != marca]
            print(marca_filtradas)
         
    elif opcoes == 3:
        modelo = input('Digite o modelo que deseja filtrar: ')
        modelo_filtradas = df[df['modelo'] == modelo]
        print(modelo_filtradas) 
    elif opcoes == 4:
        ano_modelo = int(input('Digite o ano modelo que deseja filtrar: '))
        comp = input('Digite a comparacao:\n maior: >\n menor: <\n igual: ==\n diferente: !=\n maior ou igual: >=\n menor ou igual: <=\n')
        if comp == '>':
            ano_modelo_filtradas = df.query(f"anoModelo {comp} {ano_modelo}") 
            print(ano_modelo_filtradas)
        if comp == '<':
            ano_modelo_filtradas = df.query(f"anoModelo {comp} {ano_modelo}") 
            print(ano_modelo_filtradas)
        if comp == '==':
            ano_modelo_filtradas = df.query(f"anoModelo {comp} {ano_modelo}") 
            print(ano_modelo_filtradas) 
        if comp == '!=':
            ano_modelo_filtradas = df.query(f"anoModelo {comp} {ano_modelo}") 
            print(ano_modelo_filtradas) 
        if comp == '>=':
            ano_modelo_filtradas = df.query(f"anoModelo {comp} {ano_modelo}") 
            print(ano_modelo_filtradas)
        if comp == '<=':
            ano_modelo_filtradas = df.query(f"anoModelo {comp} {ano_modelo}") 
            print(ano_modelo_filtradas)                  
        
        
        
         
    elif opcoes == 5:
        mes_referencia = int(input('Digite o mes referencia que deseja filtrar: '))
        comp = input('Digite a comparacao:\n maior: >\n menor: <\n igual: ==\n diferente: !=\n maior ou igual: >=\n menor ou igual: <=\n')
        if comp == '>':
            mes_referencia_filtradas = df.query(f"mesReferencia {comp} {mes_referencia}") 
            print(mes_referencia_filtradas)
        if comp == '<':
            mes_referencia_filtradas = df.query(f"mesReferencia {comp} {mes_referencia}") 
            print(mes_referencia_filtradas)
        if comp == '==':
            mes_referencia_filtradas = df.query(f"mesReferencia {comp} {mes_referencia}") 
            print(mes_referencia_filtradas)
        if comp == '!=':
            mes_referencia_filtradas = df.query(f"mesReferencia {comp} {mes_referencia}") 
            print(mes_referencia_filtradas) 
        if comp == '>=':
            mes_referencia_filtradas = df.query(f"mesReferencia {comp} {mes_referencia}") 
            print(mes_referencia_filtradas)
        if comp == '<=':
            mes_referencia_filtradas = df.query(f"mesReferencia {comp} {mes_referencia}") 
            print(mes_referencia_filtradas)                   
          
    elif opcoes == 6:
        ano_referencia = int(input('Digite o ano referencia que deseja filtrar: '))
        comp = input('Digite a comparacao:\n maior: >\n menor: <\n igual: ==\n diferente: !=\n maior ou igual: >=\n menor ou igual: <=\n')
        if comp == '>':
            ano_referencia_filtradas = df.query(f"anoReferencia {comp} {ano_referencia}") 
            print(ano_referencia_filtradas)
        if comp == '<':
            ano_referencia_filtradas = df.query(f"anoReferencia {comp} {ano_referencia}") 
            print(ano_referencia_filtradas)
        if comp == '==':
            ano_referencia_filtradas = df.query(f"anoReferencia {comp} {ano_referencia}") 
            print(ano_referencia_filtradas) 
        if comp == '!=':
            ano_referencia_filtradas = df.query(f"anoReferencia {comp} {ano_referencia}") 
            print(ano_referencia_filtradas)  
        if comp == '>=':
            ano_referencia_filtradas = df.query(f"anoReferencia {comp} {ano_referencia}") 
            print(ano_referencia_filtradas) 
        if comp == '<=':
            ano_referencia_filtradas = df.query(f"anoReferencia {comp} {ano_referencia}") 
            print(ano_referencia_filtradas)                
            
            
        
    elif opcoes == 7:
        valor = float(input('Digite o valor que deseja filtrar: '))
        comp = input('Digite a comparacao:\n maior: >\n menor: <\n igual: ==\n diferente: !=\n maior ou igual: >=\n menor ou igual: <=\n')
        if comp == '>':
            valor_filtrado = df.query(f"valor {comp} {valor}") 
            print(valor_filtrado)
        if comp == '<':
            valor_filtrado = df.query(f"valor {comp} {valor}") 
            print(valor_filtrado)
        if comp == '==':
            valor_filtrado = df.query(f"valor {comp} {valor}") 
            print(valor_filtrado) 
        if comp == '!=':
            valor_filtrado = df.query(f"valor {comp} {valor}") 
            print(valor_filtrado)  
        if comp == '>=':
            valor_filtrado = df.query(f"valor {comp} {valor}") 
            print(valor_filtrado) 
        if comp == '<=':
            valor_filtrado = df.query(f"valor {comp} {valor}") 
            print(valor_filtrado)                
            
        
    else:
        print('Opcao incorreta insira a opcao correta') 
if inf == 3:  
     opcoes_filtros = int(input("Digite as opcoes de filtro:\n 1 - Codigo fipe\n 2 - Marca\n 3 - Modelo\n 4 - Ano Modelo\n 5 - Mes Referencia\n 6 - Ano referencia\n 7 - Valor\n ")) 
     funcao_apli =  int(input("Digite as funcao:\n 1 - Valor maximo\n 2 - Valor minimo\n 3 - Valor da média\n 4 - Valor desvio padrao\n")) 
     if opcoes_filtros == 1 and funcao_apli == 1:
         codigo_fipe = df['codigoFipe'].max() 
         print(f'O valor maximo da tabela fip é',codigo_fipe)
     if opcoes_filtros == 1 and funcao_apli == 2:
         codigo_fipe = df['codigoFipe'].min() 
         print(f'O valor minimo da tabela fip é',codigo_fipe) 
     if opcoes_filtros == 1 and funcao_apli == 3:
         codigo_fipe = df['codigoFipe'].mean() 
         print(f'O valor média da tabela fip é',codigo_fipe) 
     if opcoes_filtros == 1 and funcao_apli == 4:
         print('Opcao indisponivel para desvio padrao')  
     if opcoes_filtros == 2 and funcao_apli == 1:
          print('Opcao indisponivel por se tratar de uma palavra')
     if opcoes_filtros == 2 and funcao_apli == 2:
          print('Opcao indisponivel por se tratar de uma palavra') 
     if opcoes_filtros == 2 and funcao_apli == 3:
          print('Opcao indisponivel por se tratar de uma palavra')
     if opcoes_filtros == 2 and funcao_apli == 4:
          print('Opcao indisponivel por se tratar de uma palavra') 
     if opcoes_filtros == 3 and funcao_apli == 1:
          print('Opcao indisponivel por se tratar de uma palavra')
     if opcoes_filtros == 3 and funcao_apli == 2:
          print('Opcao indisponivel por se tratar de uma palavra') 
     if opcoes_filtros == 3 and funcao_apli == 3:
          print('Opcao indisponivel por se tratar de uma palavra')
     if opcoes_filtros == 3 and funcao_apli == 4:
          print('Opcao indisponivel por se tratar de uma palavra')
     if opcoes_filtros == 4 and funcao_apli == 1:
         ano_modelo = df['anoModelo'].max() 
         print(f'O modelo de maior ano é',ano_modelo) 
     if opcoes_filtros == 4 and funcao_apli == 2:
         ano_modelo = df['anoModelo'].min() 
         print(f'O modelo de menor ano é',ano_modelo)
     if opcoes_filtros == 4 and funcao_apli == 3:
         ano_modelo = df['anoModelo'].mean() 
         print(f'A média de ano é',ano_modelo) 
     if opcoes_filtros == 4 and funcao_apli == 4:
         ano_modelo = df['anoModelo'].std()
         print(f'O desvio padrao é',ano_modelo)
     if opcoes_filtros == 5 and funcao_apli == 1:
         mes_modelo = df['mesReferencia'].max() 
         print(f'O mes maior é',mes_modelo) 
     if opcoes_filtros == 5 and funcao_apli == 2:
         mes_modelo = df['mesReferencia'].min() 
         print(f'O mes menor é',mes_modelo) 
     if opcoes_filtros == 5 and funcao_apli == 3:
         mes_modelo = df['mesReferencia'].mean() 
         print(f'A media de meses é',mes_modelo)  
     if opcoes_filtros == 5 and funcao_apli == 4:
         mes_modelo = df['mesReferencia'].std()
         print(f'O desvio padrao é',mes_modelo)
     if opcoes_filtros == 6 and funcao_apli == 1:
         ano_ref = df['anoReferencia'].max()
         print(f'O ano referencia maior é',ano_ref) 
     if opcoes_filtros == 6 and funcao_apli == 2:
         ano_ref = df['anoReferencia'].min()
         print(f'O ano referencia menor é',ano_ref)  
     if opcoes_filtros == 6 and funcao_apli == 3:
         ano_ref = df['anoReferencia'].mean()
         print(f'A média de ano referencia é',ano_ref) 
     if opcoes_filtros == 6 and funcao_apli == 4:
         ano_ref = df['anoReferencia'].std()
         print(f'O desvio padrao é',ano_ref) 
     if opcoes_filtros == 7 and funcao_apli == 1:
         valor = df['valor'].max()
         print(f'O valor máximo',valor)   
     if opcoes_filtros == 7 and funcao_apli == 2:
         valor = df['valor'].min()
         print(f'O valor minimo',valor) 
     if opcoes_filtros == 7 and funcao_apli == 3:
         valor = df['valor'].mean()
         print(f'O média de valores é',valor)   
     if opcoes_filtros == 7 and funcao_apli == 4:
         valor = df['valor'].std()
         print(f'O desvio padrao do valor é',valor)                                                          
                                                                    