'''
COM231 - Atividade Prática 01
Nome: João Vitor de Faria
Matrícula: 2019006030
'''
from view import View
from modelM import PedidoM

class Control:
    def launch(self):
        operation = self.view.launch()
        while operation != 0:
            if operation == 1:
                order_parameters = self.view.get_order_data()
                order_products = self.view.get_order_products(order_parameters[0])
                order = PedidoM.new_order(self, order_parameters)
                status = PedidoM.insert_order(self, order, order_products)
                self.view.print_status(status) 
            if operation == 2:
                order_id = self.view.get_order_id()
                order = PedidoM.consult_order(self, order_id)
                self.view.print_order(order)
            if operation == 3:
                update_parameters = self.view.get_update_data()
                status = PedidoM.update_order(self,update_parameters)
                self.view.print_status(status)
            if operation == 4:
                order_id = self.view.get_order_id()
                status = PedidoM.delete_order(self, order_id)
                self.view.print_status(status)
            operation = self.view.menu()

    def __init__(self):
        self.view = View()

if __name__ == '__main__':
    main = Control()
    main.launch()