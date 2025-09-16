import sqlite3

# Conectando ao banco de dados (criará um novo se não existir)
conn = sqlite3.connect('banco.db')


def criar_tabela():
    """ cria a tabela 'tarefa' caso ela não exista """
    cursor = conn.cursor()
    conn.execute("""
    create table if not exists banco (
        conta integer primary key autoincrement,
        titular text,
        saldo float
    )
    """)


def add_conta(conta, saldo):
    """ adiciona uma nova tarefa """
    conn.execute(
        'insert into banco (titular, saldo) values (?, ?)', (conta, saldo))
    conn.commit()


def atualizar_saldo(conta, saldo):
    conn.execute('update banco set saldo = ? where conta = ? ', (saldo, conta))
    conn.commit()


def remover_saldo(saldo):
    """ remove a tarefa da tabela """
    conn.execute('delete from banco where saldo = ?', (saldo, ))
    conn.commit()


def get_contas():  # retorna um cursor
    """ retorna a lista de tarefas cadastras """
    return conn.execute("select conta, titular, saldo from banco")
