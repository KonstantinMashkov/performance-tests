from locust import task, events
from locust.env import Environment

from clients.grpc.gateway.locust import GatewayGRPCTaskSet
from seeds.scenarios.existing_user_make_purchase_operation import ExistingUserMakePurchaseOperationSeedsScenario
from seeds.schema.result import SeedUserResult
from tools.locust.user import LocustBaseUser


@events.init.add_listener
def init(environment: Environment, **kwargs):
    seeds_scenario = ExistingUserMakePurchaseOperationSeedsScenario()
    seeds_scenario.build()  # создаём пользователей, счета, карты и операции
    environment.seeds = seeds_scenario.load()


class GetOperationsTaskSet(GatewayGRPCTaskSet):
    seed_user: SeedUserResult  # Типизированная ссылка на данные из сидинга

    def on_start(self) -> None:
        super().on_start()
        self.seed_user = self.user.environment.seeds.get_random_user()

    @task(1)
    def get_account(self):
        self.accounts_gateway_client.get_accounts(user_id=self.seed_user.user_id)

    @task(2)
    def get_operations(self):
        self.operations_gateway_client.get_operations(
            account_id=self.seed_user.credit_card_accounts[0].account_id
        )

    @task(2)
    def get_statistics(self):
        self.operations_gateway_client.get_operations_summary(
            account_id=self.seed_user.credit_card_accounts[0].account_id
        )


class GetOperationsScenarioUser(LocustBaseUser):
    tasks = [GetOperationsTaskSet]