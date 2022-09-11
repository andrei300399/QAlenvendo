import pytest
from .models import JsTestTask


class TestCase:
    @pytest.mark.API
    def test_phones(self, api_client):
        response = JsTestTask.get_phones(api_client)
        phones = JsTestTask.deserialize_array(response.json())
        for i in range(len(phones) - 1):
            assert phones[i].name <= phones[i+1].name
            assert "Alcatel" in phones[i].name





