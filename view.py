
from decimal import *
from modelM import *
from datetime import datetime

class View():
    def launch(self):
        return self.menu()

    def menu(self):
        print("===============================MENU===============================")
        print("|(1) CADASTRAR PEDIDO                                             |")
        print("|(2) CONSULTAR PEDIDO                                             |")
        print("|(3) ALTERAR PEDIDO                                               |")
        print("|(4) APAGAR PEDIDO                                                |")
        print("|(0) SAIR                                                        |")
        print("==================================================================")
        operation = int(input("Escolha uma operação: "))
        return operation

    def get_order_id(self):
        order_id = int(input("Digite o identificador da venda: "))
        return order_id

    def get_order_data(self):
        orderid = input("Insira o identificador do pedido: ")

        # Validação customerid
        verify_customer = 0
        while verify_customer == 0:
            customerid = input(
                "Insira o identificador do cliente: ")
            verify_customer = Check.check_customer(self, customerid)

        # Validação employeeid
        verify_employee = 0
        while verify_employee == 0:
            enployerid = input("Insira o identificador do funcionario: ")
            verify_employee = Check.check_employee(self, enployerid)

        orderdate = input("Insira a data do pedido (AAAA-MM-DD): ")
        year, month, day = map(int, orderdate.split('-'))
        orderdate = datetime(year, month, day)
        requireddate = input("Insira a data do fechamento do pedido (AAAA-MM-DD): ")
        year, month, day = map(int, requireddate.split('-'))
        requireddate = datetime(year, month, day)
        shippeddate = input("Insira a data do envio do pedido (AAAA-MM-DD): ")
        year, month, day = map(int, shippeddate.split('-'))
        shippeddate = datetime(year, month, day)

        freight = input("Insira o valor do frete: ")
        shipname = input("Insira o local do envio: ")
        shipaddress = input("Insira o endereço: ")
        shipcity = input("Insira a cidade do envio: ")
        shipregion = input("Insira o região do envio: ")
        shipcountry = input("Insira o pais: ")
        shippostalcode = input("Insira o CEP: ")
        shipperid = input("Insira o id do endereço de envio: ")
        
        order = (int(orderid), customerid, int(enployerid), orderdate, requireddate, shippeddate, Decimal(freight),
                  shipname, shipaddress, shipcity, shipregion, shipcountry, shippostalcode, int(shipperid))
        return order

    def get_order_products(self, order_id):
        i = 1
        products_list = []
        while i != 0:
            print("\nInsira os dados do produto referente ao pedido:", order_id, ": ")
            product_id = input("ID do produto: ")
            unit_price = input("Valor do produto: ")
            quantity = input("Quantidade comprada: ")
            discount = input("Valor do desconto: ")
            product = Order_details(int(order_id), int(product_id), Decimal(unit_price), int(quantity), Decimal(discount))
            products_list.append(product)
            i = int(input("Deseja continuar cadastrando produtos para este pedido?\n(0)Não\n(1)Sim\n->"))
        return products_list

    def get_update_data(self):
        columns = {1: 'shipperid', 2:'customerid', 3:'employeeid', 4:'orderdate', 5:'requireddate', 6:'shippeddate', 7:'freight',8:'shipname', 9:'shipaddress', 10:'shipcity', 11:'shipregion', 12:'shippostalcode', 13:'shipcountry'}
        
        # Valida se existe registro do pedido no banco
        verify = 0
        while verify == 0:
            order_id = input("Digite o ID da ordem da venda: ")
            verify = Check.check_order(self, order_id)

        print("\nEscolha uma operação:")
        print("(1)  Alterar ID do endereço de envio ")
        print("(2)  Alterar Cliente ")
        print("(3)  Alterar Funcionario")
        print("(4)  Alterar Data do pedido")
        print("(5)  Alterar Data do fechamento")
        print("(6)  Alterar Data do envio")
        print("(7)  Alterar Valor do frete")
        print("(8)  Alterar Local de envio")
        print("(9)  Alterar Endereço")
        print("(10) Alterar Cidade")
        print("(11) Alterar Regiao")
        print("(12) Alterar CEP")
        print("(13) Alterar País")
        field_to_update = int(input())

        # Valida se existe registro do cliente no banco
        if(field_to_update == 2):
            customer_id = 0
            while customer_id == 0:
                value = input("Digite o novo identificador do cliente (identificador é string de cliente que já existe): ")
                customer_id = Check.check_customer(self, value)

        # Valida se existe registro do funcionário no banco
        elif(field_to_update == 3):
            employee_id = 0
            while employee_id == 0:
                value = input("Digite o novo identificador do funcionario: ")
                employee_id = Check.check_employee(self, value)
        else:
            value = input("Digite o novo valor para o atributo: ")
            if(field_to_update == 4 or field_to_update == 5 or field_to_update == 6):
                year, month, day = map(int, value.split('-'))
                value = datetime(year, month, day)

            elif(field_to_update == 7):
                Decimal(value)

        return (order_id, columns[field_to_update], value)

    def print_order(self, order):
        if(order is not None):
            print("\nID do pedido: ", order.orderid)
            print("Cliente: ", order.customerid)
            print("Funcionario: ", order.employeeid)
            print("Data do pedido: ", order.orderdate)
            print("Data do fechamento: ", order.requiredate)
            print("Data do envio: ", order.shippeddate)
            print("Valor do frete: ", order.freight)
            print("Local de envio: ", order.shipname)
            print("Endereço: ", order.shipaddress)
            print("Cidade: ", order.shipcity)
            print("Regiao: ", order.shipregion)
            print("País: ", order.shipcountry)
            print("CEP: ", order.shippostalcode)
            print("ID do endereço de envio: ", order.shipperid)
        else:
            print("Pedido não encontrado!")

    def print_status(self, status):
        if(status == "sucesso"):
            print("\nCOMANDO EXECUTADO NO BANCO DE DADOS!!!")
        else:
            print(status)

    
