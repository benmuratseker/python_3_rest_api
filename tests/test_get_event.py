from unittest.mock import patch
from fastapi import HTTPException

import pytest

from globoticket.api import get_event
from globoticket.models import DBEvent

@patch(target="globoticket.api.get_dbevent", return_value=DBEvent(product_code="Test"))
def test_get_event(mock_get_dbevent):
    """Return the event found in the database."""
    assert get_event(id=25, db="Fake db") is mock_get_dbevent.return_value
    mock_get_dbevent.assert_called_with(25, "Fake db")

@patch(target="globoticket.api.get_dbevent", return_value=None)
def test_get_event_404(_):
    """Raise HTTPException when no event is found."""
    with pytest.raises(HTTPException):
        get_event(id=0, db=None)