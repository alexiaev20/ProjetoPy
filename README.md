# ProjetoPy

O **ProjetoPy** é uma aplicação desenvolvida em **Python** para a gestão de dados bancários. O projeto demonstra como manipular e processar informações financeiras de forma eficiente, utilizando técnicas e bibliotecas do Python para análise e gerenciamento de dados.

## Funcionalidades:
- **Gestão de Contas**: Criação, atualização e exclusão de contas bancárias.
- **Transações**: Registro e monitoramento de transações financeiras entre contas.
- **Relatórios**: Geração de relatórios sobre saldos de contas e histórico de transações.

## Tecnologias Utilizadas:
- **Linguagem**: Python

## Estrutura do Projeto:
O projeto está organizado da seguinte forma:
- **banco.py**: Contém a lógica principal do sistema bancário
    ├── Classe ContaBancaria: Manipula uma conta individual (depósito, saque, extrato)
    └── Classe Banco: Gerencia várias contas e facilita as operações
- **main.py**: Menu principal para interagir com o sistema bancário
    └── Função executar_sistema: Apresenta o menu ao usuário e lida com as entradas

## Como Executar:
1. Clone o repositório:
    ```bash
    git clone https://github.com/alexiaev20/ProjetoPy
    ```

2. Navegue até o diretório do projeto:
    ```bash
    cd ProjetoPy
    ```

3. Crie e ative um ambiente virtual (opcional, mas recomendado):
    ```bash
    python -m venv venv
    source venv/bin/activate  # Para Windows use: venv\Scripts\activate
    ```

4. Instale as dependências:
    ```bash
    pip install -r requirements.txt
    ```

5. Execute o script principal:
    ```bash
    python main.py
    ```

---

Para mais informações ou contribuições, sinta-se à vontade para explorar o código ou abrir uma issue no repositório.
