'''
Порядок запуска сервера
1) создаете виртуальную среду через терминал:
virtualenv -p python2.7 --no-site-packages --clear --distribute venv
2) активируете виртуальную среду:
source venv/bin/activate
3) устанавливаете зависимости:
pip install -r requirements.txt
4) запускаете сервер:
python api.py
'''


import requests
import pprint

SERVER = 'http://127.0.0.1:5000/'
DIR = 'example'


# ЗАПРОС-ТЕСТ
result = requests.get(SERVER)
print(result.status_code, result.text)


# # POST
# headers = {'Content-Type': 'application/json'}
#
# (key, val) = ('mode', 2)
# result = requests.post(f'{SERVER}api/{DIR}',
#     headers=headers,
#     data='{"%s":"%s"}' % (key, val)
# )
# print(result.status_code)

# GET
#
# result = requests.get(f'{SERVER}api/{DIR}')
# print(result.status_code,result.text )

# DELETE

key = 'test'
result = requests.delete(f'{SERVER}api/{DIR}/{key}')

# GET

result = requests.get(f'{SERVER}api/{DIR}')
print(result.status_code,result.text )
