import pytest
import requests
import pytest_check as check
url= 'https://randomuser.me/api/'
#respons=request.get(url)
#print(respons.json())

def test_class_work01():
    url='https://randomuser.me/api/'
    respons = requests.get(url)
    data=respons.json()
    check.is_in ('gender',data['results'][0],'gender not key')
    check.is_in ('location',data['results'][0],'location not key')
    check.is_in ('street',data['results'][0],'street not key')
    number=data ['results'][0]['location']['street']
    print(number)


def test_class_work02():
    url='https://universities.hipolabs.com/search?country=Kazakhstan'
    response = requests.get(url)
    data=response.json()
    check.equal(data[0]['alpha_two_code'],'Kz','значение не равно Kz')


TEST_NAMES=[
    "anna",
    "dzmitry",
    "grage",
    "maria",
    "john"
]
@pytest.mark.parametrize('name',TEST_NAMES)
def test_nationalize_api(name):
    url="https://api.nationalize.io/"
    params={'name':name}
    response=requests.get(url,params=params)
    assert response.status_code==200,f"Ожидался код 200,получен{response.status_code}"
    data=response.json()
   check.is_in("name",data"Ответ не содержит ключ 'name'")
   check.is_in("country",data"Ответ не содержит ключ 'country'")
   check.equal(data['name']name)