import random
from typing import List, Any
ids=[]

class Pizzeria:
  def __init__(self, name:str, clientes:List["Cliente"]=[], items:List["Item"]=[], pedidos:List["Pedido"]=[])->None:
    self.__name = name
    self.__clientes = clientes
    self.__items = items
    self.__pedidos = pedidos

  def add_item(self, item:"Item")->bool:
    self.__items.append(item)
    return True

  def add_cliente(self, cliente: "Cliente")->bool:
    self.__clientes.append(cliente)
    return True

  def add_pedido(self, pedido: "Pedido")->bool:
    self.__pedidos.append(pedido)
    return True

  def get_cliente(self, index:int)->"Cliente":
    if index  < len(self.__clientes):
      newcliente=self.__clientes[index]
      return newcliente
    return False

  def get_item(self, index:int)->"Item":
    l=len(self.__items)
    if index < l:
      newitem=self.__items[index]
      return newitem
    return False

  def get_items(self):
      return self.__items

  def calc_prod_mas_vendido_cliente(self, num_cliente:int)->int:
    items=[]
    if num_cliente<len(self.__clientes):
      cliente = self.__clientes[num_cliente]
      for pedido in cliente.get_pedidos():
        for item in pedido.get_items():
          items.append(item.get_name())
        
    mayor=0
    mayoritem=None
    for item in items:
      rep=int(items.count(item))
      if rep > mayor:
        mayor = rep
        mayoritem=item

    return mayoritem
  
class Item:
  def __init__(self, name:str, price:int)->None:
    id = random.randint(0,10000)
    while id in ids:
        id = random.randint(0,10000)
    self.__id=id
    self.__name = name
    self.__price = price
  
  def get_id(self)->int:
    return self.__id
  
  def get_name(self)->str:
    return self.__name

  def get_price(self)->int:
    return self.__price
  

class Cliente:
  def __init__(self, name:str, pedidos:List["Pedido"]=None)->None:
    self.__name = name 
    self.__pedidos = [] if pedidos is None else pedidos
  
  def get_pedidos(self)->List["Pedido"]:
    return self.__pedidos

  def get_name(self)->str:
    return self.__name

  def add_pedido(self, pedido:"Pedido")->bool:
    self.__pedidos.append(pedido)
    return True
  

  
from abc import ABC
class Pedido(ABC):
  def __init__(self, cliente:Cliente, items:List["Item"]=[])->None:
    self._cliente = cliente
    self._items = items
    self._cliente.add_pedido(self)

  def get_cliente(self)->"Cliente":
    return self._cliente

  def get_items(self)->List["Item"]:
    return self._items


class PedidoOnLine(Pedido):
  def __init__(self, email:str, **kwargs: Any):
    self.__email = email
    super().__init__(**kwargs)

  def get_email(self)->str:
    return self.__email
  


class PedidoTelefono(Pedido):
  def __init__(self, telefono:str, **kwargs:Any):
    self.__telefono = telefono
    super().__init__(**kwargs)

  def get_telefono(self)->str:
    return self.__telefono