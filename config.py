'''
COM231 - Atividade Prática 01
Nome: João Vitor de Faria
Matrícula: 2019006030
'''
import psycopg2

class Config:
    def __init__(self, connection_setup):
        self.connection_setup = connection_setup

    def set_parameters(self):
        self.connection_setup = "host='localhost' dbname='Northwind' user='postgres' password='root'"
        return self

    def insert_database_record(self, sql_order_command, sql_product_command, command_parameters, products_list):
        conn = None
        try:
            connection = psycopg2.connect(Config.set_parameters(self).connection_setup)
            session = connection.cursor()

            # Inserção do pedido na tabela orders
            session.execute(sql_order_command, command_parameters)

            # Inserção dos produtos na tabela order_details
            for i in products_list:
                session.execute(sql_product_command, (i.order_id, i.product_id, i.price, i.quantity, i.discount))
            connection.commit()
            session.close()

        except psycopg2.Error:
            return psycopg2.Error
        finally:
            if conn is not None:
                conn.close()
            return "sucesso"

    def update_database_record(self, sql_order_command, command_parameters):
        conn = None
        try:
            connection = psycopg2.connect(Config.set_parameters(self).connection_setup)
            session = connection.cursor()

            # Inserção do pedido na tabela orders
            session.execute(sql_order_command, command_parameters)

            connection.commit()
            session.close()

        except psycopg2.Error:
            return psycopg2.Error
        finally:
            if conn is not None:
                conn.close()
            return "sucesso"

    def consult_database_record(self, sql_string, valores):
        conn = None
        try:
            connection = psycopg2.connect(Config.set_parameters(self).connection_setup)
            session = connection.cursor()
            session.execute(sql_string, valores)

            # Armazenar os registros
            record = session.fetchall()
            colnames = [desc[0] for desc in session.description]

            connection.commit()
            session.close()

        except psycopg2.Error:
            return psycopg2.Error
        finally:
            if conn is not None:
                conn.close()
        return (colnames, record)

    def delete_database_record(self, sql_string, valores):
        conn = None
        try:
            connection = psycopg2.connect(Config.set_parameters(self).connection_setup)
            session = connection.cursor()
            
            # Apagar os registros
            session.execute(sql_string, valores)

            connection.commit()
            session.close()

        except psycopg2.Error:
            return psycopg2.Error
        finally:
            if conn is not None:
                conn.close()
        return "sucesso"

    def check_record(self, sql_string, valores):
        conn = None
        try:
            connection = psycopg2.connect(Config.set_parameters(self).connection_setup)
            session = connection.cursor()
            session.execute(sql_string, valores)

            # Armazenar os registros:
            record = session.fetchall()
            if(record == []):
                return_value = 0
            else:
                return_value = 1

            connection.commit()
            session.close()

        except psycopg2.Error:
            return psycopg2.Error
        finally:
            if conn is not None:
                conn.close()
        return return_value