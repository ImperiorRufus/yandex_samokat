import requests
import configuration
import data
import html

#Ахтямов Рушан, 9-ая когорта, планета Марс, Дипломный проект, Инженер по тестированию плюс
#Проверяем номер заказа
def check_the_order_track():
    new_order_track = html.create_new_order()
    return new_order_track.json()["track"]


#Убеждаемся, что код = 200
def test_check_the_order_status():
    current_track = check_the_order_track()
    act = html.get_track(current_track).status_code
    exp = 200
    assert act == exp

