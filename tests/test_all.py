from scripts.baseline import baseline_test_delete, baseline_test_import, baseline_test_nodes
from scripts.test_delete import test_delete
from scripts.test_imports import test_import
from scripts.test_nodes import test_nodes


def test_all():
    # baseline tests
    baseline_test_import()
    baseline_test_nodes()
    # baseline_test_sales()
    # baseline_test_stats()
    baseline_test_delete()

    # custom tests
    test_import()
    test_nodes()
    test_delete()


if __name__ == "__main__":
    test_all()
