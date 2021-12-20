import requests

get_key_headers = {
    "email": "maksaevi4@mail.ru",
    "password": "5CyckrX23"
}
get_key_params = get_key_headers
api_key_link = "https://petfriends1.herokuapp.com/api/key"
def get_api_key(link, params, headers):
    response = requests.get(link,
                            params=params,
                            headers=headers
                            )
    if response.status_code == 200:
        print("OK")
    if response.ok:
        print("OK")
get_headers_my_pets = {
    "auth_key ": "a9e1abf07ed7c7ef76d4ea65990d355a51e17c0b9aa9b7561a89ffaa",
    "filter": "my_pets"
}
get_params_my_pets = get_headers_my_pets
my_pets_link = "https://petfriends1.herokuapp.com/api/pets?filter=my_pets"
def get_pet_list(link, params, headers):
    response = requests.get(link,
                            params=params,
                            headers=headers
                            )
    if response.status_code == 200:
        print("OK")
    if response.ok:
        print("OK")
    return response.text
print(get_pet_list(my_pets_link, get_params_my_pets, get_headers_my_pets))
post_new_pet_headers = {
    "auth_key": "a9e1abf07ed7c7ef76d4ea65990d355a51e17c0b9aa9b7561a89ffaa",
    "name": "Jimmy Neitron",
    "animal_type": "Gorilla",
    "age": '12',
    "pet_photo": ""
}
post_new_pet_params = post_new_pet_headers
new_pet_POST_link = "https://petfriends1.herokuapp.com/api/pets"
def create_new_pet(link, post_params, post_headers):
    response = requests.post(link,
                             params=post_params,
                             headers=post_headers,
                             files={"pet_photo": open('fortniter.jpg', 'rb')}
                             )
    if response.status_code == 200:
        print("OK")
    if response.ok:
        print("OK")
print(create_new_pet(new_pet_POST_link, post_new_pet_params, post_new_pet_headers))
post_set_photo_headers = {
    "auth_key": "a9e1abf07ed7c7ef76d4ea65990d355a51e17c0b9aa9b7561a89ffaa",
    "pet_id": "3fb97833-dc3a-4c90-b6ae-687238b7bea4"
}
post_set_photo_params = post_set_photo_headers
set_photo_POST_link = "https://petfriends1.herokuapp.com/api/pets/set_photo/" + "3fb97833-dc3a-4c90-b6ae-687238b7bea4"
def post_photo(link, post_params, post_headers):
    response = requests.post(link,
                             params=post_params,
                             headers=post_headers,
                             files={"pet_photo": open('poro2.jpg', 'rb')}
                             )
    if response.status_code == 200:
        print("OK")
    if response.ok:
        print("OK")
print(post_photo(set_photo_POST_link, post_set_photo_params, post_set_photo_headers))
delete_pet_headers = {
    "auth_key": "a9e1abf07ed7c7ef76d4ea65990d355a51e17c0b9aa9b7561a89ffaa",
    "pet_id": "3fb97833-dc3a-4c90-b6ae-687238b7bea4"
}
delete_pet_params = delete_pet_headers
DELETE_pet_link = "https://petfriends1.herokuapp.com/api/pets/" + "3fb97833-dc3a-4c90-b6ae-687238b7bea4"
def delete(link, del_params, del_headers):
    response = requests.delete(link,
                               params=del_params,
                               headers=del_headers
                               )
    if response.status_code == 200:
        print("OK")
    if response.ok:
        print("OK")
    return response.text
print(delete(DELETE_pet_link, delete_pet_params, delete_pet_headers))
put_info_headers = {
    "auth_key": "a9e1abf07ed7c7ef76d4ea65990d355a51e17c0b9aa9b7561a89ffaa",
    "pet_id": "6a1520d5-b93f-4ed6-80d4-15d823394ecb"
}
put_info_params = put_info_headers
put_info_link = "https://petfriends1.herokuapp.com/api/pets/" + "6a1520d5-b93f-4ed6-80d4-15d823394ecb"
def put_pet(link, p_params, p_headers):
    response = requests.put(link,
                            params=p_params,
                            headers=p_headers
                            )
    if response.status_code == 200:
        print("OK")
    if response.ok:
        print("OK")
    return response.text
print(put_pet(put_info_link, put_info_params, put_info_headers))
