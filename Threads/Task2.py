"""
Создайте функцию напоминалку в отдельном потоке от основном программы.
Функция должна запрашивать о чем напомнить и через сколько секунд.
В основной части программы запустите поток с функцией и выполните задержку в 10 секунд.
После выполнения программа должна написать "программа завершается"
"""
import threading
import time

def remember():
    user_note = input('О чем напомнить?:\n')
    user_time = int(input('Через сколько напомнить?'))
    time.sleep(user_time)
    print(user_note)

th = threading.Thread(target=remember())
th.start()
th.join()
time.sleep(2)
print('прога завершается')