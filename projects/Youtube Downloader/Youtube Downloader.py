from pytube import YouTube

yt = YouTube(input('Введите ссылку на нужный вам ролик: '))
stream = yt.streams.get_by_itag(22)
print('Информация о ролике: ')
print(f'Название: {yt.title}')
print(f'Автор: {yt.author}')
print(f'Описание: {yt.description}')
print(f'Длина видео: {yt.length}')
print(f'Дата публикации: {yt.publish_date}')
print(f'Количество просмотров: {yt.views}')
print(f'Размер: {stream.filesize_mb} мегабайт')
stream.download(output_path="videos")
print('Ваше видео скачано')
