import notepad

number = 4  # сколько знаков МИНИМУМ может быть в тексте заметки


def add():
    note = create_note(number)
    array = read_file()
    for notebook in array:
        if notepad.Note.get_id(note) == notepad.Note.get_id(notebook):
            notepad.Note.set_id(note)
    array.append(note)
    write_file(array, 'a')
    print('Заметка добавлена !!!')


def show(text):
    logic = True
    array = read_file()
    if text == 'date':
        date = input('Введите дату в формате dd.mm.yyyy: ')
    for notebook in array:
        if text == 'all':
            logic = False
            print(notepad.Note.map_note(notebook))
        if text == 'id':
            logic = False
            print('ID: ' + notepad.Note.get_id(notebook))
        if text == 'date':
            logic = False
            if date in notepad.Note.get_date(notebook):
                print(notepad.Note.map_note(notebook))
    if logic == True:
        print('Нет ни одной заметки...')


def id_edit_del_show(text):
    id = input('Введите id необходимой заметки: ')
    array = read_file()
    logic = True
    for notebook in array:
        if id == notepad.Note.get_id(notebook):
            logic = False
            if text == 'edit':
                note = create_note(number)
                notepad.Note.set_title(notebook, note.get_title())
                notepad.Note.set_body(notebook, note.get_body())
                notepad.Note.set_date(notebook)
                print('Заметка изменена !')
            if text == 'del':
                array.remove(notebook)
                print('Заметка удалена !')
            if text == 'show':
                print(notepad.Note.map_note(notebook))
    if logic == True:
        print('Такой заметки нет, вы ввели неверный id')
    write_file(array, 'a')

def read_file():
    try:
        array = []
        file = open("notebook.txt", "r", encoding='utf-8')
        notebook = file.read().strip().split("\n")
        for n in notebook:
            split_n = n.split(';')
            note = notepad.Note(
                id=split_n[0], title=split_n[1], body=split_n[2], date=split_n[3])
            array.append(note)
    except Exception:
        print('Нет сохраненных заметок')
    finally:
        return array

def write_file(array, mode):
    file = open("notebook.txt", mode='w', encoding='utf-8')
    file.seek(0)
    file.close()
    file = open("notebook.txt", mode=mode, encoding='utf-8')
    for notebook in array:
        file.write(notepad.Note.to_string(notebook))
        file.write('\n')
    file.close


def create_note(number):
    title = check_len_text_input(
        input('Введите Название заметки: '), number)
    body = check_len_text_input(
        input('Введите Описание заметки: '), number)
    return notepad.Note(title=title, body=body)

def check_len_text_input(text, n):
    while len(text) <= n:
        print(f'Текст должен быть больше {n} символов\n')
        text = input('Введите тескт: ')
    else:
        return text