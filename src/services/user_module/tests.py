from django.test import TestCase

# Create your tests here.
import pytest
from rest_framework.test import APIRequestFactory
from rest_framework import status
from unittest.mock import patch
from bson.objectid import ObjectId
from services.user_module.views import get_items


# Setup for all tests
@pytest.fixture
def mock_mongo_collection():
    with patch("services.user_module.views.mongo_db_collection") as mock:
        yield mock


@pytest.fixture
def api_request_factory():
    return APIRequestFactory()


# Parametrized test for happy path scenarios
@pytest.mark.parametrize(
    "username, expected_items, test_id",
    [
        (
            "user1",
            [
                {
                    "_id": ObjectId("507f1f77bcf86cd799439011"),
                    "user_name": "user1",
                    "item": "book",
                }
            ],
            "HP-1",
        ),
        ("user2", [], "HP-2"),
        (
            "user3",
            [
                {
                    "_id": ObjectId("507f1f77bcf86cd799439012"),
                    "user_name": "user3",
                    "item": "pen",
                }
            ],
            "HP-3",
        ),
    ],
    ids=lambda x: x[-1],
)
def test_get_items_happy_path(
    api_request_factory, mock_mongo_collection, username, expected_items, test_id
):
    # Arrange
    request = api_request_factory.get(f"/items/{username}")
    mock_mongo_collection.find.return_value = expected_items

    # Act
    response = get_items(request, username)

    # Assert
    assert response.status_code == status.HTTP_200_OK
    assert response.data == [
        {"_id": str(item["_id"]), "user_name": item["user_name"], "item": item["item"]}
        for item in expected_items
    ]


# Parametrized test for edge cases
@pytest.mark.parametrize(
    "username, expected_items, test_id",
    [("", [], "EC-1"), ("1234567890" * 10, [], "EC-2")],
    ids=lambda x: x[-1],
)
def test_get_items_edge_cases(
    api_request_factory, mock_mongo_collection, username, expected_items, test_id
):
    # Arrange
    request = api_request_factory.get(f"/items/{username}")
    mock_mongo_collection.find.return_value = expected_items

    # Act
    response = get_items(request, username)

    # Assert
    assert response.status_code == status.HTTP_200_OK
    assert response.data == []


# Parametrized test for error cases
@pytest.mark.parametrize(
    "username, exception, test_id",
    [
        ("user1", Exception("Database error"), "ER-1"),
        ("user2", Exception("Timeout error"), "ER-2"),
    ],
    ids=lambda x: x[-1],
)
def test_get_items_error_cases(
    api_request_factory, mock_mongo_collection, username, exception, test_id
):
    # Arrange
    request = api_request_factory.get(f"/items/{username}")
    mock_mongo_collection.find.side_effect = exception

    # Act and Assert
    with pytest.raises(Exception) as exc_info:
        get_items(request, username)
    assert str(exc_info.value) == str(exception)
