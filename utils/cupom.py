# utils/cupom.py

def gerar_cupom_fiscal(produtos, venda):
    # Inicializa contadores e acumuladores
    item = 0
    valor_total = 0
    
    # Lista para armazenar as linhas do cupom fiscal
    resultado = []
    resultado.append("=" * 46)  # Linha de separação
    resultado.append("C U P O M   F I S C A L".center(46, ' '))  # Título centralizado
    resultado.append("ITEM CÓDIGO DESCRIÇÃO".ljust(23) + "QTD.UN.VL_UNIT(R$) ST VL")  # Cabeçalho das colunas
    resultado.append("=" * 46)  # Linha de separação
    
    # Itera sobre cada item da venda
    for indice in range(len(venda)):
        subtotal = 0
        item += 1
        produto = produtos.get(venda[indice][0])  # Obtém a descrição do produto pelo código
        quantidade = venda[indice][1]  # Quantidade vendida
        valor = venda[indice][2]  # Valor unitário
        subtotal += quantidade * valor  # Calcula o subtotal
        valor_total += subtotal  # Acumula o valor total
        
        # Adiciona as linhas do item ao resultado
        resultado.append(f'{str(item).ljust(4)} {str(venda[indice][0]).ljust(4)} {produto.ljust(37)}')
        resultado.append(f'{str(quantidade).rjust(11)}UN X {str(valor).rjust(6)} {str(subtotal).rjust(23)}')

    # Adiciona a linha final e o total ao resultado
    resultado.append("=" * 46)
    resultado.append('TOTAL R$'.rjust(37))
    resultado.append(f'{str(valor_total).rjust(37)}')

    # Retorna o cupom fiscal como uma única string
    return "\n".join(resultado)
