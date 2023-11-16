import json
import requests


mas_of_req = ['''{"form_email": "darkenrisen@yandex.ru","form_phone": "+7 987 876 12 34","form_text": "ccc"}''',
              '''{"form_email": "ruslban@pstu.ru","form_phone": "+7 987 876 12 34", "additional_param1": 
              "+7 123 456 78 90", "additional_param2": "21.03.2002"}''',
              '''{"param1": "darkenrisen@tandex.ru","param2": "+7 983 123 56 78","param3": "21.03.2002","param4": 
              "2002-03-21"}''',
              '''{"form3_text": "42","form3_phone": "+7 123 654 12 32","form3_date": "2048-12-22"}''',
              '''{"form2_email": "dplk@gmail.com","form2_date": "2048-12-22","form2_phone": "+7 123 654 12 32"}''']


for i in range(len(mas_of_req)):
    body = mas_of_req[i]
    response = requests.post("http://127.0.0.1:8000/get_form", data=body)

    print(f'Request #{i + 1}\n{json.dumps(json.loads(body), indent=4)}\n'
          f'Response\n{json.dumps(response.json(), indent=4)}')
    print("+" * 50)