import sqlite3

def conectar_banco():
    # cria a conexão com o banco de dados
    conn = sqlite3.connect('despesas.db')
    return conn

def criar_tabela_despesas(conn):
    # cria a tabela de despesas
    conn.execute('''CREATE TABLE IF NOT EXISTS despesas
                (id INTEGER PRIMARY KEY AUTOINCREMENT,
                 data DATE,
                 descricao TEXT,
                 valor REAL)''')
    print("Tabela de despesas criada com sucesso.")

def cadastrar_despesa(conn):
    # solicita as informações da despesa ao usuário
    data = input("Data (AAAA-MM-DD): ")
    descricao = input("Descrição: ")
    valor = float(input("Valor: "))

    # insere a despesa na tabela de despesas
    conn.execute("INSERT INTO despesas (data, descricao, valor) VALUES (?, ?, ?)", (data, descricao, valor))
    conn.commit()
    print("Despesa cadastrada com sucesso.")

def visualizar_despesas(conn):
    # solicita o mês e ano para filtrar as despesas
    mes = int(input("Mês (1-12): "))
    ano = int(input("Ano (AAAA): "))

    # consulta as despesas na tabela de despesas para o mês e ano informados
    cursor = conn.execute("SELECT id, data, descricao, valor FROM despesas WHERE strftime('%m', data) = ? AND strftime('%Y', data) = ?", (f'{mes:02d}', str(ano)))

    # exibe as despesas na tela
    print()
    print(f"Despesas cadastradas em {mes}/{ano}:")
    total = 0
    for row in cursor:
        print(f"Data = {row[1]}, Descrição = {row[2]}, Valor = {row[3]}")
        total += row[3]
    print(f"Total de despesas: {total:.2f}")





def exibir_menu():
    print("\n----- MENU -----")
    print("1. Cadastrar despesa")
    print("2. Visualizar todas as despesas")
   
    print("3. Sair")

def main():
    # abre a conexão com o banco de dados
    conn = sqlite3.connect("despesas.db")

    # cria a tabela de despesas se ela ainda não existir
    criar_tabela_despesas(conn)

    while True:
        exibir_menu()
        opcao = input("Escolha uma opção: ")

        if opcao == "1":
            cadastrar_despesa(conn)
        elif opcao == "2":
            visualizar_despesas(conn)
        elif opcao == "3":
            break
        else:
            print("Opção inválida. Tente novamente.")


if __name__ == '__main__':
    main()
