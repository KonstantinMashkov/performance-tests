import time
from clients.http.gateway.users.user_client import build_users_gateway_http_client


# user_client = build_users_gateway_http_client()
#
# new_user = CreateUserRequestDict(
#     email=f"user.{time.time()}@example.com",
#     lastName="Иванов",
#     firstName="Иван",
#     middleName="Иванович",
#     phoneNumber="+79999999999",
# )
#
# create_user_response = user_client.create_user_api(new_user)
# create_user_response_data = create_user_response.json()
# print(f"Status code: {create_user_response.status_code}")
# print(f"Create user response: {create_user_response_data}")
#
# get_user_response = user_client.get_user_api(create_user_response_data["user"]["id"])
# get_user_response_data = get_user_response.json()
# print(f"Status code: {get_user_response.status_code}")
# print(f"Get user response: {get_user_response_data}")


users_gateway_client = build_users_gateway_http_client()

# Используем метод create_user
create_user_response = users_gateway_client.create_user()
print('Create user data:', create_user_response)

# Используем метод get_user
get_user_response = users_gateway_client.get_user(create_user_response['user']['id'])
print('Get user data:', get_user_response)