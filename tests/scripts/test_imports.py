# encoding=utf8

from . import *

IMPORT_GOOD_BATCHES = [
    {
        "items": [
            {
                "type": "CATEGORY",
                "name": "Новая категория",
                "id": "000",
                "parentId": None
            }
        ],
        "updateDate": "2022-02-01T12:00:00.000Z"
    },
    {
        "items": [
            {
                "type": "OFFER",
                "name": "Единственный товар",
                "id": "100",
                "price": 123,
                "parentId": "000"
            }
        ],
        "updateDate": "2022-02-04"
    },
    {
        "items": [
            {
                "type": "CATEGORY",
                "name": "Ультра мега супер категория",
                "id": "001",
                "parentId": None
            },
            {
                "type": "CATEGORY",
                "name": "Мега супер категория",
                "id": "002",
                "parentId": "001"
            },
            {
                "type": "CATEGORY",
                "name": "Супер категория",
                "id": "003",
                "parentId": "002"
            },
        ],
        "updateDate": "2022-02-10T15:00:00.000Z"
    }
]

IMPORT_BAD_BATCHES = [
    {
        # without price
        "items": [
            {
                "type": "OFFER",
                "name": "Какой-то товар",
                "id": "209",
                "parentId": None
            },
        ],
        "updateDate": "2022-02-01T12:00:00.000Z"
    },
    {
        # parent does not exist
        "items": [
            {
                "type": "OFFER",
                "name": "Какой-то товар 2",
                "id": "202",
                "parentId": "1564378193767186918648879"
            },
        ],
        "updateDate": "2022-02-01T12:00:00.000Z"
    },
    {
        # the same id
        "items": [
            {
                "type": "OFFER",
                "name": "Какой-то товар 3",
                "id": "202",
                "parentId": "200"
            },
        ],
        "updateDate": "2022-02-01T12:00:00.000Z"
    },
    {
        # incorrect data
        "items": [
            {
                "type": "OFFER",
                "name": "Какой-то товар 4",
                "id": "202",
                "parentId": "002"
            },
        ],
        "updateDate": "2022-02-00T12:00:00.000Z"
    },
    {
        # price for category
        "items": [
            {
                "type": "CATEGORY",
                "name": "Что за категория?",
                "price": 777,
                "id": "205",
                "parentId": None
            },
        ],
        "updateDate": "2022-02-02T12:00:00.000Z"
    },
    # {
    #     # extra field
    #     "items": [
    #         {
    #             "type": "OFFER",
    #             "name": "Какой-то товар N",
    #             "price": 777,
    #             "id": "207",
    #             "parentId": None,
    #             "some_strange": "some_strange"
    #         },
    #     ],
    #     "updateDate": "2022-02-02T12:00:00.000Z"
    # },
    {
        # without name
        "items": [
            {
                "type": "OFFER",
                "name": None,
                "price": 777,
                "id": "208",
                "parentId": None,
            },
        ],
        "updateDate": "2022-02-02T12:00:00.000Z"
    },
    {
        # incorrect price
        "items": [
            {
                "type": "OFFER",
                "name": "New OfFER!!!",
                "price": -2,
                "id": "212",
                "parentId": None,
            },
        ],
        "updateDate": "2022-02-02T12:00:00.000Z"
    },
]


def test_import():
    for index, batch in enumerate(IMPORT_GOOD_BATCHES):
        print(f"Importing good batch {index}")
        status, _ = request("/imports/", method="POST", data=batch)

        assert status == 200, f"Expected HTTP status code 200, got {status}"

    for index, batch in enumerate(IMPORT_BAD_BATCHES):
        print(f"Importing bad batch {index}")
        status, _ = request("/imports/", method="POST", data=batch)

        assert status == 400, f"Expected HTTP status code 400, got {status}"

    print("Custom test import passed.")


if __name__ == "__main__":
    test_import()
