# utils/cupom.py

def gerar_cupom_fiscal(produtos, venda):
    # Inicializa contadores e acumuladores
    item = 0
    valor_total = 0
    
    # Lista para armazenar as linhas do cupom fiscal
    resultado = []
    resultado.append("=" * 46)  # Linha de separação
    resultado.append("C U P O M   F I S C A L".center(46, ' '))  # Título centralizado
    resultado.append(f"{'ITEM':<5}{'CÓDIGO':<7}{'DESCRIÇÃO':<25}{'QTD.':<6}{'VL_UNIT(R$)':<10}{'ST VL':<10}")  # Cabeçalho das colunas
    resultado.append("=" * 46)  # Linha de separação
    
    # Itera sobre cada item da venda
    for indice in range(len(venda)):
        item += 1
        codigo = venda[indice][0]
        produto = produtos.get(codigo)
        quantidade = venda[indice][1]
        valor_unitario = venda[indice][2]
        subtotal = quantidade * valor_unitario
        valor_total += subtotal
        
        # Adiciona as linhas do item ao resultado
        resultado.append(f"{item:<5}{codigo:<7}{produto:<25}{quantidade:<6}{valor_unitario:<10.2f}{subtotal:<10.2f}")

    # Adiciona a linha final e o total ao resultado
    resultado.append("=" * 46)
    resultado.append(f"{'TOTAL R$':>36} {valor_total:.2f}")

    # Retorna o cupom fiscal como uma única string
    return "\n".join(resultado)
