from clients.grpc.gateway.users.users_client import build_users_gateway_grpc_client

# Создаём gRPC API-клиент для взаимодействия с UsersGatewayService
users_gateway_client = build_users_gateway_grpc_client()

# Создаём пользователя с помощью клиентского метода create_user
create_user_response = users_gateway_client.create_user()
print('Create user data:', create_user_response)
print(type(create_user_response))

# Получаем пользователя по ID, используя метод get_user
get_user_response = users_gateway_client.get_user(user_id=create_user_response.user.id)
print('Get user data:', get_user_response)