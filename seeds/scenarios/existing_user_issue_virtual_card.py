from seeds.scenario import SeedsScenario
from seeds.schema.plan import SeedsPlan, SeedUsersPlan, SeedAccountsPlan, SeedCardsPlan


class ExistingUserIssueVirtualCardSeedsScenario(SeedsScenario):

    @property
    def plan(self) -> SeedsPlan:
        return SeedsPlan(
            users=SeedUsersPlan(
                count=100,
                debit_card_accounts=SeedAccountsPlan(
                    count=1,
                    physical_cards=SeedCardsPlan(count=1)
                )
            ),
        )

    @property
    def scenario(self) -> str:
        """
        Возвращает название сценария сидинга.
        Это имя будет использоваться для сохранения данных сидинга.
        """
        return "existing_user_issue_virtual_card"


if __name__ == '__main__':
    """
    Запуск сценария сидинга вручную.
    Создаём объект сценария и вызываем метод build для создания данных.
    """
    seeds_scenario = ExistingUserIssueVirtualCardSeedsScenario()
    seeds_scenario.build()  # Запуск сидинга