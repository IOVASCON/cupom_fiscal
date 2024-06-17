# Cupom Fiscal

Este projeto gera um cupom fiscal formatado a partir de uma lista de produtos e vendas.

## Estrutura do Projeto

cupom_fiscal/
├── utils/
│ ├── init.py
│ └── cupom.py
├── main.py
├── README.md
└── test_tkinter.py

## Como Executar

1. Certifique-se de ter o Python instalado.
2. Navegue até o diretório do projeto.
3. Execute o arquivo `main.py` para iniciar a interface gráfica e gerar o cupom fiscal.

python main.py

## Dependências

Este projeto utiliza a biblioteca Tkinter, que geralmente está incluída na instalação padrão do Python.

### Explicações Detalhadas

- **`utils/cupom.py`**:

  - Define a função `gerar_cupom_fiscal` que gera e formata o cupom fiscal a partir de uma lista de produtos e vendas.

- **`main.py`**:

  - Define os produtos e vendas.
  - Define funções para mostrar o cupom fiscal e adicionar novas vendas usando diálogos de entrada.
  - Configura a interface gráfica com Tkinter, incluindo botões para mostrar o cupom fiscal e adicionar vendas.

- **`README.md`**:

  - Fornece instruções sobre a estrutura do projeto, como executá-lo e as dependências necessárias.
