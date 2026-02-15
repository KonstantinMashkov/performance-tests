from typing import TypedDict
from httpx import Response
from client import HTTPClient

class CardsRequestDict(TypedDict):
    """
    Структура данных для создания новой карты.
    """
    userId: str
    accountId: str
    
class CardsGatewayHTTPClient(HTTPClient):
    """
    Клиент для взаимодействия с /api/v1/cards сервиса http-gateway.
    """

    def post_issue_virtual_card(self, request: CardsRequestDict) -> Response:
        """
        Выпуск виртуальной карты.
        """
        return self.post("/api/v1/cards/issue-virtual-card", json=request)
    
    
    def post_issue_physical_card(self, request: CardsRequestDict) -> Response:
        """
        Выпуск физической карты.
        """
        return self.post("/api/v1/cards/issue-physical-card", json=request)


