# Завдання 1
# Маємо певний словник з назвами країн і столиць. Назва
# країни використовується як ключ, назва столиці — як значення.
# Реалізуйте: додавання, видалення, пошук, редагування,
# збереження та завантаження даних (використовуючи стиснення та розпакування).
import pickle
import gzip


def save_data(data, filename):
    with gzip.open(filename, 'wb') as file:
        pickle.dump(data, file)


def load_data(filename):
    try:
        with gzip.open(filename, 'rb') as file:
            return pickle.load(file)
    except FileNotFoundError:
        return {}


def add_data(data, country, capital):
    data[country] = capital


def delete_data(data, country):
    if country in data:
        data.pop(country, None)


def search_by_capital(data, capital):
    for country, cap in data.items():
        if cap == capital:
            return country
    return None


def edit_data(data, country, new_capital):
    if country in data:
        data[country] = new_capital


countries = {}
save_data(countries, 'countries.gz')
add_data(countries, 'Ukraine', 'Kiev')
add_data(countries, 'Spain', 'Madrid')
print(load_data('countries.gz'))
delete_data(countries, 'Ukraine')
print(search_by_capital(countries, 'Madrid'))
edit_data(countries, 'Spain', 'Paris')
print(countries)
save_data(countries, 'countries.gz')

# Завдання 2
# Маємо певний словник з назвами музичних груп (виконавців) та альбомів.
# Назва групи використовується як ключ,
# назва альбомів — як значення. Реалізуйте: додавання, видалення, пошук,
# редагування, збереження та завантаження
# даних (використовуючи стиснення та розпакування).
import pickle
import gzip


def save_data(data, filename):
    with gzip.open(filename, 'wb') as file:
        pickle.dump(data, file)


def load_data(filename):
    try:
        with gzip.open(filename, 'rb') as file:
            return pickle.load(file)
    except FileNotFoundError:
        return {}


def add_album(data, group, album):
    if group in data:
        data[group].append(album)
    else:
        data[group] = [album]


def delete_album(data, group, album):
    if group in data and album in data[group]:
        data[group].remove(album)


def search_album(data, group, album):
    return group in data and album in data[group]


def edit_album(data, group, old_album, new_album):
    if group in data:
        albums = data[group]
        for i, album in enumerate(albums):
            if album == old_album:
                albums[i] = new_album
                break


music_groups = {}
save_data(music_groups, 'music_groups.gz')

add_album(music_groups, 'Billie Eilish', 'Happier Than Ever')
add_album(music_groups, 'Jungle', 'Loving In Stereo')
add_album(music_groups, 'Kanye West', 'DONDA')

print(load_data('music_groups.gz'))

delete_album(music_groups, 'Jungle', 'Loving In Stereo')
print(search_album(music_groups, 'Kanye West', 'DONDA'))

edit_album(music_groups, 'Kanye West', 'DONDA', 'Vultures 1')
save_data(music_groups, 'music_groups.gz')
