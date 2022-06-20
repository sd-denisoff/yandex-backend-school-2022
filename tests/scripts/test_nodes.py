import sys

from . import *

EXPECTED_TREE_000 = {
    "type": "CATEGORY",
    "name": "Новая категория",
    "id": "000",
    "price": 123,
    "parentId": None,
    "date": "2022-02-04",
    "children": [
        {
            "type": "OFFER",
            "name": "Единственный товар",
            "id": "100",
            "parentId": "000",
            "price": 123,
            "date": "2022-02-04",
            "children": None,
        }
    ]
}

EXPECTED_TREE_001 = {
    "type": "CATEGORY",
    "name": "Ультра мега супер категория",
    "id": "001",
    "price": None,
    "parentId": None,
    "date": "2022-02-10T15:00:00.000Z",
    "children": [
        {
            "type": "CATEGORY",
            "name": "Мега супер категория",
            "id": "002",
            "parentId": "001",
            "price": None,
            "date": "2022-02-10T15:00:00.000Z",
            "children": [
                {
                    "type": "CATEGORY",
                    "name": "Супер категория",
                    "id": "003",
                    "parentId": "002",
                    "price": None,
                    "date": "2022-02-10T15:00:00.000Z",
                    "children": []
                }
            ]
        }
    ]
}


def test_nodes():
    status, response = request(f"/nodes/000/", json_response=True)
    # print(json.dumps(response, indent=2, ensure_ascii=False))

    assert status == 200, f"Expected HTTP status code 200, got {status}"

    deep_sort_children(response)
    deep_sort_children(EXPECTED_TREE_000)
    if response != EXPECTED_TREE_000:
        print_diff(EXPECTED_TREE_000, response)
        print("Response tree doesn't match expected tree.")
        sys.exit(1)

    status, response = request(f"/nodes/001/", json_response=True)
    # print(json.dumps(response, indent=2, ensure_ascii=False))

    assert status == 200, f"Expected HTTP status code 200, got {status}"

    deep_sort_children(response)
    deep_sort_children(EXPECTED_TREE_001)
    if response != EXPECTED_TREE_001:
        print_diff(EXPECTED_TREE_001, response)
        print("Response tree doesn't match expected tree.")
        sys.exit(1)

    print("Custom test nodes passed.")


if __name__ == "__main__":
    test_nodes()
