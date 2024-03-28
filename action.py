import functions


def run():
    input_from_user = ''
    while input_from_user != '7':
        menu()
        input_from_user = input().strip()

        if input_from_user == '1':
            functions.add()
        if input_from_user == '2':
            functions.show('all')
            functions.id_edit_del_show('edit')
        if input_from_user == '3':
            functions.show('all')
            functions.id_edit_del_show('del')
        if input_from_user == '4':
            functions.show('all')
        if input_from_user == '5':
            functions.show('id')
            functions.id_edit_del_show('show')
        if input_from_user == '6':
            functions.show('date')
        if input_from_user == '7':
            exit()
            break



def menu():
    print("\nЭто программа 'Заметки'. Имеются следующие функции:\n\n1 - добавление заметки\n2 - редактирование заметки\n3 - удаление заметки\n4 - вывод всех заметок из файла\n5 - показать заметку по id\n6 - выборка заметок по дате\n7 - выход\n\nВведите номер функции:")

def exit():
    print("Блокнот закрыт!")