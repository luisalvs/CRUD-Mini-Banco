import db
from db import *


def cadastrar_conta():
    titular = input('Nome: ')
    saldo = float(input('Saldo: '))
    db.add_conta(titular, saldo)


def depositar():
    conta = int(input('Numero: '))
    for contas in db.get_contas():
        if conta == contas[0]:
            deposito = float(input('Valor: '))
            saldo = contas[2] + deposito
            db.atualizar_saldo(contas[0], saldo)


def sacar():
    conta = int(input('Numero:'))
    for contas in db.get_contas():
        if conta == contas[0]:
            saque = float(input('Valor: '))
            if saque in contas[2]:
                saldo = contas[2] - saque
                db.atualizar_saldo(contas[0], saldo)


def transferir():
    conta1 = int(input('Numero: '))
    for contas in db.get_contas():
        if conta1 == contas[0]:
            saque = float(input('Valor: '))
            if saque in contas[2]:
                saldo = contas[2] - saque
                db.atualizar_saldo(contas[0], saldo)


def exibir_contas():
    for conta in db.get_contas():
        print(f'\nConta: {conta[0]} \nTitular: {conta[1]} \nSaldo: {conta[2]}')


exibir_contas()
