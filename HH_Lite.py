import pprint
import requests

def count_salary_json(result_json):
    sum_sal = 0
    sum_vac = 0
    for item in result_json['items']:
        if item['salary'] == None:
            continue
        sal = item['salary']['to']
        if sal:
            sum_sal += float(sal)
            sum_vac += 1
    return sum_sal, sum_vac

url = 'https://api.hh.ru/vacancies'

params = {'text': 'NAME:Python',
          'area': 1,
          'page': 0}

result = requests.get(url, params = params).json()

# всего найдено
found_vac = result['found']
qnt_page = result['pages']

# print('Найдено:', found_vac)
# print('Нужно обработать (страниц):', qnt_page)

# pprint.pprint(result['items'])

sum_sal, sum_vac = count_salary_json(result)
for i in range(1, qnt_page + 1):
    params['page'] = i
    result = requests.get(url, params=params).json()
    p_sum_sal, p_sum_vac = count_salary_json(result)
    sum_sal += p_sum_sal
    sum_vac += p_sum_vac

mean_sal = 0
# print('sum_sal', sum_sal)
# print('sum_vaac', sum_vac)


if sum_vac != 0:
    mean_sal = round(sum_sal / sum_vac, 0)

print('Средняя зарплата Python программиста в Москве: ', mean_sal, 'рублей')
