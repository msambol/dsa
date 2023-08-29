import pytest
from b_tree import BTree
import random
import logging

logging.basicConfig(level=logging.DEBUG)


class TestBTree:
    def setup_method(self):
        self.tree = BTree(3)

    def test_insert(self):
        self.tree.insert(10)
        assert self.tree.search(10) is not None

    def test_search(self):
        assert self.tree.search(5) is None  # Assuming tree is initially empty
        self.tree.insert(5)
        assert self.tree.search(5) is not None

    def test_delete(self):
        self.tree.insert(20)
        # Assuming search returns the node if found, else None
        node, index = self.tree.search(20)
        self.tree.delete(node, 20)
        assert self.tree.search(20) is None

    def test_insert_multiple(self):
        values = [5, 10, 15, 20]
        for v in values:
            self.tree.insert(v)
        for v in values:
            assert self.tree.search(v) is not None

    def test_huge_insert(self):

        for _ in range(5):
            t = random.sample(range(2, 20), 1)[0]
            logging.debug(f"processing t: {t}")
            values_for_insertion = set(
                random.sample(range(1, 10 ** 6), 10 ** 5))
            non_exist_values = [i for i in range(
                1, 10**6) if i not in values_for_insertion]

            btree = BTree(t)
            count = 10 ** 5 - 1
            while count:
                value_for_insertion = values_for_insertion.pop()
                btree.insert(value_for_insertion)
                node, index = btree.search(value_for_insertion)
                assert node is not None
                non_exist_value = non_exist_values.pop()
                node = btree.search(non_exist_value)
                assert node is None
                count -= 1

    def test_huge_delete_root(self):

        for _ in range(10):
            t = random.sample(range(2, 100), 1)[0]
            logging.debug(f"processing t: {t}")
            ub = 5
            values_for_insertion = set(
                random.sample(range(1, 10 ** ub), 10 ** (ub - 1)))
            non_exist_values = [i for i in range(
                1, 10**ub) if i not in values_for_insertion]

            btree = BTree(t)
            count = 10**(ub - 1) - 1

            inserted = set()
            while count:
                value_for_insertion = values_for_insertion.pop()
                inserted.add(value_for_insertion)

                btree.insert(value_for_insertion)
                node, index = btree.search(value_for_insertion)
                assert node is not None
                non_exist_value = non_exist_values.pop()
                node = btree.search(non_exist_value)
                assert node is None
                count -= 1

            while inserted:
                root = btree.root
                for key in btree.root.keys:
                    inserted.remove(key)
                    btree.delete(btree.root, key)
                    node = btree.search(key)
                    assert node is None

    # def test_huge_insert_and_delete(self):

    #     for _ in range(5):
    #         t = random.sample(range(2, 3), 1)[0]
    #         logging.debug(f"processing t: {t}")
    #         values_for_insertion = set(
    #             random.sample(range(1, 10 ** 3), 10 ** 2))
    #         non_exist_values = [i for i in range(
    #             1, 10**3) if i not in values_for_insertion]

    #         btree = BTree(t)
    #         count = 30

    #         inserted = set()
    #         while count:
    #             value_for_insertion = values_for_insertion.pop()
    #             inserted.add(value_for_insertion)

    #             btree.insert(value_for_insertion)
    #             # node, index = btree.search(value_for_insertion)
    #             # assert node is not None
    #             # non_exist_value = non_exist_values.pop()
    #             # node = btree.search(non_exist_value)
    #             # assert node is None
    #             count -= 1

    #             delOrNot = random.sample([0, 1], 1)[0]
    #             if delOrNot:
    #                 value_for_deletion = inserted.pop()
    #                 btree.print_tree(btree.root)
    #                 print(f"Try to delete: {value_for_deletion}")
    #                 btree.delete(btree.root, value_for_deletion)
    #                 node = btree.search(value_for_deletion)

    #                 print("-=-=-=-=-=-=")
