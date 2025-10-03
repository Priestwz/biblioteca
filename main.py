import sqlite3

conexao = sqlite3.connect("Biblioteca.db")

cursor = conexao.cursor()

cursor.execute("""
CREATE TABLE IF NOT EXISTS livros (
    id  INTEGER PRIMARY KEY AUTOINCREMENT,
    Titulo TEXT NOT NULL,
    Autor TEXT NOT NULL,                              
    Ano INTERGER,            
    Disponivel TEXT NOT NULL           
)
""")


def inserir_livros():
    try:
        conexao = sqlite3.connect("Biblioteca.db")
        cursor = conexao.cursor()
        Titulo = input("Digitar o Titulo do livro: ").lower()
        Autor = input("Digitar o Autor do livro: ").lower()
        Ano = int(input("Digite o Ano do livro: "))
        cursor.execute("""
        INSERT INTO livros (Titulo,Autor,Ano,Disponivel)
        VALUES (?,?,?,?)
        """,
        (Titulo,Autor,Ano,"sim")
        )
        conexao.commit()
    except Exception as erro:
        print(f"erro ao inserir o livro {erro}")
    finally:
        if conexao:
            conexao.close()


def listar_livros():
    try:
        conexao = sqlite3.connect("Biblioteca.db")
        cursor = conexao.cursor()
        cursor.execute("SELECT * FROM livros")
        for linha in cursor.fetchall():
            print(f"id:{[0]} | Titulo: {linha[1]} |Autor:{linha[2]} |Ano:{linha[3]} |Dispsonivel:{linha[4]}")

    except Expection as erro:
        print(f"erro ao inserir o livro {erro}")
    finally:

        if conexao:
            conexao.close()


def atualizar_disponibilidade():
    try:
        conexao = sqlite3.connect("biblioteca.db")
        cursor = conexao.cursor()

        id_livro = int(input("Digite o ID do livro que deseja atualizar a disponibilidade: ").strip())
        nova_disponibilidade = input("Digite a nova disponibilidade (sim/não): ").lower().strip()

        cursor.execute("""
        UPDATE livros  
        SET disponivel = ? 
        WHERE id = ?""", (nova_disponibilidade, id_livro))

        conexao.commit()
        if cursor.rowcount > 0:
            print("Disponibilidade atualizada com sucesso!")
        else:
            print("Nenhum livro encontrado com o ID fornecido. ")
        
    except sqlite3.Error as error:
        print("Erro ao atualizar disponibilidade:", erro)
    finally:
        if conexao:
            conexao.close()


def deletar_livro():
    try:
        conexao = sqlite3.connect("biblioteca.db")
        cursor = conexao.cursor()
        deletar= int(input("Digite o id do livro que deseja deletar: "))
        cursor.execute("DELETE FROM livros WHERE id = ?", (deletar,))

        conexao.commit()

        if cursor.rowcount > 0:
            print("Livro foi removido com sucesso ")
        else:
            print("Nenhum livro encontrado")
    except Exception as erro:
        print(f"erro ao tentar excluir livro {erro} ")
    finally:
        if conexao:
            conexao.close()

def menu():
    try:
        while True:
            print("\nMenu:")
            print("1.Cadastra livro")
            print("2.listar livro")
            print("3.Atualizar disponiblidade")
            print("4.Deletar livro")
            print("5.Sair")
            opcao = input("Escolha uma opção: ")
            match opcao :
                case "1": inserir_livros()
                case "2": listar_livros()
                case "3": atualizar_disponibilidade()
                case "4": deletar_livro()

    except sqlite3.Error as error:
        print("Erro na operação do menu", error)
    finally:
        if conexao:
            conexao.close()
menu()
