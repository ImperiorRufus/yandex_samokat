import requests
import configuration
import data


#Создаем новый набор
def create_new_order():
    return requests.post(configuration.URL_SERVICE + configuration.ORDERS, json=data.order)


#Получаем номер заказа
def get_track(new_order_track):
    track_number = configuration.GET_ORDER + "?t=" + str(new_order_track)
    return requests.get(configuration.URL_SERVICE + track_number)


