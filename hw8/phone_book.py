phone_book = []


def get_phone_book():
    global phone_book
    return phone_book


def set_phone_book(new_phone_book):
    global phone_book
    phone_book = new_phone_book


def add_contact(contact: list):
    global phone_book
    phone_book.append(contact)


def remove_contact(id):
    global phone_book
    name = phone_book[id - 1][0]
    confirm = input(f'Вы действительно хотите удалить контакт {name}? (y/n) ')
    if confirm.lower() == 'y':
        phone_book.pop(id - 1)
        return True
    return False


def change_contact_confirm(id):
    global phone_book
    name = phone_book[id - 1][0]
    confirm = input(f'Вы действительно хотите изменить контакт {name}? (y/n) ')
    if confirm.lower() == 'y':
        return True
    return False


def change_contact(id: int, contact: list):
    global phone_book
    phone_book[id - 1] = contact


def find_contact(text: str):
    global phone_book
    find_ids = []
    txt = text.lower()
    for idx, contact in enumerate(phone_book):
        for i in contact:
            j = i.lower()
            if txt in j:
                find_ids.append(idx)
    find_ids = list(set(find_ids))
    result = [phone_book[i] for i in find_ids]
    return result
