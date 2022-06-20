from scripts.baseline import baseline_test_all
from scripts.test_delete import test_delete
from scripts.test_imports import test_import
from scripts.test_nodes import test_nodes
from scripts.test_sales import test_sales


def test_all():
    # baseline tests
    baseline_test_all()

    # custom tests
    test_import()
    test_nodes()
    test_delete()
    test_sales()


if __name__ == "__main__":
    test_all()
