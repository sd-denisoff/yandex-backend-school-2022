from . import *

IMPORT_BATCHES = [
    {
        "items": [
            {
                "type": "CATEGORY",
                "name": "Новая скидочная категория",
                "id": "1000",
                "parentId": None
            }
        ],
        "updateDate": "2022-02-01T12:00:00.000Z"
    },
    {
        "items": [
            {
                "type": "OFFER",
                "name": "Супер горячий товар",
                "id": "1005",
                "price": 6,
                "parentId": "1000"
            },
            {
                "type": "OFFER",
                "name": "Супер горячий товар 2",
                "id": "1006",
                "price": 8,
                "parentId": "1000"
            }
        ],
        "updateDate": "2022-04-07T12:00:00.000Z"
    },
    {
        "items": [
            {
                "type": "OFFER",
                "name": "Супер горячий товар",
                "id": "1005",
                "price": 6,
                "parentId": "1000"
            },
            {
                "type": "OFFER",
                "name": "Супер горячий товар -1",
                "id": "1006",
                "price": 10,
                "parentId": "1000"
            }
        ],
        "updateDate": "2022-04-09T12:00:00.000Z"
    },
]


def test_sales():
    for index, batch in enumerate(IMPORT_BATCHES):
        status, _ = request("/imports/", method="POST", data=batch)
        assert status == 200, f"Expected HTTP status code 200, got {status}"

    # item = Item.objects.filter(id="1000").first()
    # assert item.price_last_update is None, f"Expected CATEGORY last price update NONE, " \
    #                                        f"got {item.price_last_update}"
    #
    # item = Item.objects.filter(id="1005").first()
    # assert item.price_last_update == "2022-04-09T12:00:00.000Z", \
    #     f"Expected OFFER last price update 2022-04-09T12:00:00.000Z, " \
    #     f"got {item.price_last_update}"
    #
    # item = Item.objects.filter(id="1006").first()
    # assert item.price_last_update == "2022-04-09T12:00:00.000Z", \
    #     f"Expected OFFER last price update 2022-04-09T12:00:00.000Z, " \
    #     f"got {item.price_last_update}"

    params = urllib.parse.urlencode({
        "date": "2022-04-09T12:00:00.000Z"
    })
    status, response = request(f"/sales/?{params}", json_response=True)
    assert status == 200, f"Expected HTTP status code 200, got {status}"

    items = response['items']
    assert len(items) == 2, "Too many or too less objects in response"

    ids = sorted([items[0]['id'], items[1]['id']])
    assert ids == ["1005", "1006"]

    status, _ = request(f"/delete/1000/", method="DELETE")
    assert status == 200, f"Expected HTTP status code 200, got {status}"

    status, _ = request(f"/nodes/1000/", json_response=True)
    assert status == 404, f"Expected HTTP status code 404, got {status}"

    print("Test sales passed.")


if __name__ == "__main__":
    test_sales()
