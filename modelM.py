'''
COM231 - Atividade Prática 01
Nome: João Vitor de Faria
Matrícula: 2019006030
'''
import psycopg2
from decimal import *
from config import Config
from psycopg2.extensions import AsIs
from datetime import datetime

class PedidoM():
    def __init__(self, orderid, customerid, employeeid, orderdate, requireddate, shippeddate, freight, shipname, shipaddress, shipcity, shipregion, shippostalcode, shipcountry, shipperid):
        self.orderid = orderid
        self.customerid = customerid
        self.employeeid = employeeid
        self.orderdate = orderdate
        self.requiredate = requireddate
        self.shippeddate = shippeddate
        self.freight = freight
        self.shipname = shipname
        self.shipaddress = shipaddress
        self.shipcity = shipcity
        self.shipregion = shipregion
        self.shippostalcode = shippostalcode
        self.shipcountry = shipcountry
        self.shipperid = shipperid

    def new_order(self, order_parameters):
        order = PedidoM(int(order_parameters[0]), str(order_parameters[1]),
                        int(order_parameters[2]), str(order_parameters[3]),
                        str(order_parameters[4]), str(order_parameters[5]),
                        Decimal(order_parameters[6]), str(order_parameters[7]),
                        str(order_parameters[8]), str(order_parameters[9]),
                        str(order_parameters[10]), str(order_parameters[11]),
                        str(order_parameters[12]), str(order_parameters[13]))
        return order

    def insert_order(self, order, product_list):
        sql_order_command = """INSERT INTO northwind.orders(orderid, customerid, employeeid, orderdate, requireddate, shippeddate, freight, shipname, shipaddress, shipcity, shipregion, shippostalcode, shipcountry, shipperid) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s);"""
        sql_product_command = """INSERT INTO northwind.order_details(orderid, productid, unitprice, quantity, discount) VALUES (%s, %s, %s, %s, %s);"""
        insert_parameters = [int(order.orderid), order.customerid, int(order.employeeid), order.orderdate, order.requiredate, order.shippeddate, Decimal(order.freight),order.shipname, order.shipaddress, order.shipcity, order.shipregion, order.shippostalcode, order.shipcountry, int(order.shipperid) ]
        status = Config.insert_database_record(Config, sql_order_command, sql_product_command, insert_parameters, product_list)
        return status

    def consult_order(self, order_id):
        string_sql = 'SELECT * FROM northwind.orders WHERE orderid = %s;'
        records = Config.consult_database_record(Config, string_sql, [order_id])
        if(len(records[1]) != 0):
            order = PedidoM.new_order(self, records[1][0])
            return order
        else:
            return None

    def update_order(self, update_parameters):
        string_sql = """UPDATE northwind.orders SET %s = '%s' WHERE orderid = %s"""
        parameters = ((AsIs(update_parameters[1])), AsIs(update_parameters[2]), int(update_parameters[0]))
        status = Config.update_database_record(Config, string_sql, parameters)
        return status

    def delete_order(self, order_id):
        string_sql = 'DELETE FROM northwind.order_details WHERE orderid = %s;'
        status = Config.delete_database_record(Config, string_sql, [order_id])
        if status == 'sucesso':
            string_sql_1 = 'DELETE FROM northwind.orders WHERE orderid = %s;'
            status = Config.delete_database_record(Config, string_sql_1, [order_id])
            return status
        else:
            return None

class Check():
    def check_order(self, order):
        string_sql = """SELECT * FROM northwind.orders WHERE orderid = %s;"""
        status = Config.check_record(Config, string_sql, [order])
        if(status == 0):
            print("Pedido não cadastrado no banco! Por favor, insira um identificador válido.")
        return status

    def check_customer(self, customerid):
        string_sql = """SELECT * FROM northwind.customers WHERE customerid = %s;"""
        status = Config.check_record(Config, string_sql, [customerid])
        if(status == 0):
            print("Cliente não cadastrado no banco! Por favor, insira um identificador válido.")
        return status

    def check_employee(self, employeeid):
        string_sql = """SELECT * FROM northwind.employees WHERE employeeid = %s;"""
        status = Config.check_record(Config, string_sql, [employeeid])
        if(status == 0):
            print("Funcionário não cadastrado no banco! Por favor, insira um identificador válido.")
        return status

class Order_details():
    def __init__(self, orderid, productid, unitprice, quantity, discount):
        self.order_id = orderid
        self.product_id = productid
        self.price = unitprice
        self.quantity = quantity
        self.discount = discount
