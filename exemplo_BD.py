import customtkinter
import sqlite3

def criar_banco():
    conexao = sqlite3.connect("dados_cadastro.db")
    terminal_sql = conexao.cursor()
    terminal_sql.execute("CREATE TABLE IF NOT EXISTS pessoas (nome text)")
    conexao.commit()
    conexao.close()


def salvar_dados():
    conexao = sqlite3.connect("dados_cadastro.db")
    terminal_sql = conexao.cursor()
    terminal_sql.execute(f"INSERT INTO pessoas (nome) VALUES ('{entradanome.get()}')")
    conexao.commit()
    conexao.close()


def ler_dados():
    conexao = sqlite3.connect("dados_cadastro.db")
    terminal_sql = conexao.cursor()
    terminal_sql.execute(f"SELECT * FROM pessoas")
    recebe_dados = terminal_sql.fetchall()
    for i in recebe_dados:
        nomes = "\n" + str(i[0])

aba = customtkinter.CTk()
aba.title('BD')
aba.geometry("300x300")

criar_banco()

titulo = customtkinter.CTkLabel(aba, text="Sistema \n Salva Nome", font=("comic sans", 20, "bold"))
titulo.pack(pady=10)

entradanome = customtkinter.CTkEntry(aba, placeholder_text="insira um nome")
entradanome.pack(pady=10)

botaosalvar = customtkinter.CTkButton(aba, text="Salvar", command=salvar_dados())
botaosalvar.pack(pady=5)

botaolistar = customtkinter.CTkButton(aba, text="listar")
botaolistar.pack(pady=5)

aba.mainloop()