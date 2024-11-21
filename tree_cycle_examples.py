from collections import deque
from os import listdir
from os.path import isfile, join

filepath = '/home/rau/PYworkspace/gitRepositories/tree_algorythm'

def print_names(start_dir):
    """
    Алгоритм поиска "древо" с использованием простого цикла.
    :param start_dir: стартовая директория, внутри которой ведется поиск файлов.
    :return: выводит в консоль список файлов, найденных в каталоге.
    """
    search_queue = deque()  #Инициализируем двустороннюю очередь LILO (Lost in, Lost out)
    search_queue.append(start_dir)  #Заполняем очередь папками, в которых нужно провести поиск
    while search_queue:             #Идем по циклу, пока очередь не опустеет.
        dir = search_queue.popleft()    #Берем название директории, из начала очереди.
        for file in sorted(listdir(dir)):   #Цикл, для проверки содержимого полученной папки dir.
            fullpath = join(dir, file)      #Складываем полный путь к найденному объекту, в одну строку,
                                                # чтобы сформировать ссылку на объект.
            if isfile(fullpath):        #Если нашли файл.
                print(file)             #То, вывести название этого файла в консоль.
            else:                       #Если не файл, значит, папка
                search_queue.append(fullpath)   #Добавляем эту папку тоже, в конец очереди, для изучения.

print_names("pics")
