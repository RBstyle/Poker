import re

if __name__ == '__main__':

    '''
    Принимаем данные, проверяем правильность ввода.
    '''
    list_of_cards = input('Введите знрачене карт через запятую:')
    cards = re.findall(r'\d+' , list_of_cards)

    while True:
        if len(cards) == 5:
            break
        else:
            list_of_cards = input('Не корректный ввод, попробуйте еще:')
            cards = re.findall(r'\d+' , list_of_cards)
    '''
    Вычисляем количество одинаковых значений и количество повторений каждого.
    На выходе список, где количество элементов - количество повторений,
    а значение - количество повторов соответсвтующего элемента
    '''
    def vol_of_same (self):
        result = []
        same_list = []
        for item in list(set(self)):
            if self.count(item) !=1:
                same_list.append(self.count(item))
        return same_list
    '''
    Функции по сортировке значений
    '''

    def one(self):
        if self[0] == 5:
            return 'poker'
        if self[0] == 4:
            return 'four of a kind'
        if self[0] == 3:
            return 'three of a kind'
        if self[0] == 2:
            return 'one paire'

    def two(self):
        if self.count(3):
            return 'full house'
        else:
            return 'two pair'
    '''
    Проверка количества повторений
    '''
    
    if len(vol_of_same(cards)) == 0:
        print ('all different')        
    elif len(vol_of_same(cards)) == 1:
        print (one(vol_of_same(cards)))        
    elif len(vol_of_same(cards)) == 2:
        print (two(vol_of_same(cards)))
    else:
        print ('Что-то пошло не так! Выдерните шнур питания и прыгните в окно!')


    
