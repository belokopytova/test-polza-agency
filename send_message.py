import requests

TOKEN=''
CHAT_ID=''
FILE_PATH='text.txt'

def read_file():

    try:
        with open(FILE_PATH, 'r', encoding='utf-8') as f:
            text = f.read()
            return text
    except FileNotFoundError:
        print(f'Ошибка: файл {FILE_PATH} не найден!')

    except Exception as e:
        print(f'Ошибка чтения файла: {e}')

def send_text():
    url = f'https://api.telegram.org/bot{TOKEN}/sendMessage'
    text = read_file()
    data = {
        'chat_id': CHAT_ID,
        'text': text,
        'disable_web_page_preview': True
    }
    response = requests.post(url, data=data)

    if response.status_code == 200:
        print('Сообщение успешно отправлено!')
    else:
        print(f'Ошибка {response.status_code}:')
        print(response.json())

if __name__ == '__main__':
    send_text()



