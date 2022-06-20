from . import *


def test_delete():
    status, _ = request(f"/delete/000/", method="DELETE")
    assert status == 200, f"Expected HTTP status code 200, got {status}"

    status, _ = request(f"/nodes/000/", json_response=True)
    assert status == 404, f"Expected HTTP status code 404, got {status}"

    status, _ = request(f"/delete/001/", method="DELETE")
    assert status == 200, f"Expected HTTP status code 200, got {status}"

    status, _ = request(f"/nodes/001/", json_response=True)
    assert status == 404, f"Expected HTTP status code 404, got {status}"

    print("Custom test delete passed.")


if __name__ == "__main__":
    test_delete()
