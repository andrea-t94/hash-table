import pytest
from pytest_unordered import unordered
from unittest import mock

from src import HashTable

def test_should_create_hashtable():
    assert HashTable(size = 100) is not None

def test_should_return_size():
    assert len(HashTable(size = 100)) == 0

def test_should_not_create_hashtable_with_zero_size():
    with pytest.raises(ValueError):
        HashTable(size=0)

def test_should_not_create_hashtable_with_negative_size():
    with pytest.raises(ValueError):
        HashTable(size=-100)

def test_should_not_create_hashtable_with_non_int_size():
    with pytest.raises(TypeError):
        HashTable(size='100')
    with pytest.raises(TypeError):
        HashTable(size=100.5)

def test_should_report_capacity_of_empty_hash_table():
    assert HashTable(size=100).size == 100

def test_should_report_size(hash_table):
    assert hash_table.size == 100

def test_should_create_empty_value_slots():
    # Given
    expected_values = [None, None, None]
    hash_table = HashTable(size=3)

    # When
    actual_values = hash_table._items

    # Then
    assert actual_values == expected_values

# test to include key values in hash table
def test_should_insert_key_value_pairs():
    # Given
    hash_table = HashTable(size=100)
    hash_table["hola"] = "hello"
    hash_table[98.6] = 37
    hash_table[False] = True

    # When
    actual_values = hash_table.items

    # Then
    assert ("hola", "hello") in hash_table.items
    assert (98.6, 37) in hash_table.items
    assert (False, True) in hash_table.items

def test_add_key_should_not_increase_size():
    # Given
    hash_size = 100
    hash_table = HashTable(size=hash_size)
    hash_table["hola"] = "hello"
    hash_table[98.6] = 37
    hash_table[False] = True

    # When
    new_hash_size = len(hash_table)

    # Then
    assert new_hash_size == 3

def test_should_update_value(hash_table):
    assert hash_table["hola"] == "hello"

    hash_table["hola"] = "hallo"

    assert hash_table["hola"] == "hallo"
    assert hash_table[98.6] == 37
    assert hash_table[False] is True
    assert len(hash_table) == 3

def test_should_not_contain_none_value_when_created():
    # there should be no pair.value as None when table is initialized
    hash_table = HashTable(size=100)
    assert None not in hash_table.values


# happy path
def test_should_insert_none_value():
    # Given
    hash_table = HashTable(size=100)
    hash_table["key"] = None

    # Then
    assert ("key", None) in hash_table.items


@pytest.fixture
def hash_table():
    sample_data = HashTable(size=100)
    sample_data["hola"] = "hello"
    sample_data[98.6] = 37
    sample_data[False] = True
    return sample_data

# test make objects findable
def test_should_find_value_by_key(hash_table):
    assert hash_table["hola"] == "hello"
    assert hash_table[98.6] == 37
    assert hash_table[False] is True

def test_should_raise_error_on_missing_key():
    hash_table = HashTable(size=100)
    with pytest.raises(KeyError) as exception_info:
        hash_table["missing_key"]
    assert exception_info.value.args[0] == "missing_key"

def test_should_find_key(hash_table):
    assert "hola" in hash_table

def test_should_not_find_key(hash_table):
    assert "ciao" not in hash_table

# test get method
def test_should_get_value(hash_table):
    assert hash_table.get("hola") == "hello"
# handy since doesn't throw an exception
def test_should_get_none_when_missing_key(hash_table):
    assert hash_table.get("missing_key") is None

def test_should_get_default_value_when_missing_key(hash_table):
    assert hash_table.get("missing_key", "default") == "default"

def test_should_get_value_with_default(hash_table):
    assert hash_table.get("hola", "default") == "hello"

# delete key value pair
def test_should_delete_key_value_pair(hash_table):
    assert "hola" in hash_table
    assert ("hola", "hello") in hash_table.items

    del hash_table["hola"]

    assert "hola" not in hash_table
    assert ("hola", "hello") not in hash_table.items

def test_should_raise_key_error_when_deleting(hash_table):
    with pytest.raises(KeyError) as exception_info:
        del hash_table["missing_key"]
    assert exception_info.value.args[0] == "missing_key"

# test get key-value pairs (items)

def test_should_return_items(hash_table):
    assert hash_table.items == {
        ("hola", "hello"),
        (98.6, 37),
        (False, True)
    }

def test_should_get_pairs_of_empty_hash_table():
    assert HashTable(size=100).items == set()

def test_should_return_pairs(hash_table):
    # order of items shown is not important
    assert ("hola", "hello") in hash_table.items
    assert (98.6, 37) in hash_table.items
    assert (False, True) in hash_table.items


def test_should_return_copy_of_pairs(hash_table):
    # defensive copying: I don't want to return original values
    assert hash_table.items is not hash_table.items

def test_should_not_include_blank_pairs(hash_table):
    # similar to test_should_not_contain_none_value_when_created
    # now we can modify it since we have the property
    assert None not in hash_table.items

# test hash table values
def test_should_return_duplicate_values():
    # values can be duplicated
    hash_table = HashTable(size=100)
    hash_table["Alice"] = 24
    hash_table["Bob"] = 42
    hash_table["Joe"] = 42
    assert [24, 42, 42] == sorted(hash_table.values)

def test_should_get_values(hash_table):
    # test also different data types
    assert unordered(hash_table.values) == ["hello", 37, True]

def test_should_get_values_of_empty_hash_table():
    assert HashTable(size=100).values == []

def test_should_return_copy_of_values(hash_table):
    # defensive copying testing
    assert hash_table.values is not hash_table.values

# test hash table keys
def test_should_get_keys(hash_table):
    assert hash_table.keys == {"hola", 98.6, False}

def test_should_get_keys_of_empty_hash_table():
    assert HashTable(size=100).keys == set()

def test_should_return_copy_of_keys(hash_table):
    assert hash_table.keys is not hash_table.keys

# test the whole hash table
def test_should_convert_to_dict(hash_table):
    dictionary = dict(hash_table.items)
    assert set(dictionary.keys()) == hash_table.keys
    assert set(dictionary.items()) == hash_table.items
    assert list(dictionary.values()) == unordered(hash_table.values)

# test if hash table is iterable
def test_should_iterate_over_keys(hash_table):
    for key in hash_table.keys:
        assert key in ("hola", 98.6, False)

def test_should_iterate_over_values(hash_table):
    for value in hash_table.values:
        assert value in ("hello", 37, True)

def test_should_iterate_over_pairs(hash_table):
    for key, value in hash_table.items:
        assert key in hash_table.keys
        assert value in hash_table.values

def test_should_iterate_over_instance(hash_table):
    for key in hash_table:
        assert key in ("hola", 98.6, False)

# textual representation
def test_should_use_dict_literal_for_str(hash_table):
    # encoded in any combination since hash table has no ordering
    assert str(hash_table) in {
        "{'hola': 'hello', 98.6: 37, False: True}",
        "{'hola': 'hello', False: True, 98.6: 37}",
        "{98.6: 37, 'hola': 'hello', False: True}",
        "{98.6: 37, False: True, 'hola': 'hello'}",
        "{False: True, 'hola': 'hello', 98.6: 37}",
        "{False: True, 98.6: 37, 'hola': 'hello'}",
    }

# create hash table from dictionary
def test_should_create_hashtable_from_dict():
    dictionary = {"hola": "hello", 98.6: 37, False: True}

    hash_table = HashTable.from_dict(dictionary)
    # initial size same as len(dictionary)
    assert hash_table.size == len(dictionary)
    assert hash_table.keys == set(dictionary.keys())
    assert hash_table.items == set(dictionary.items())
    assert unordered(hash_table.values) == list(dictionary.values())

def test_should_have_canonical_string_representation(hash_table):
    # canonical string representation is given by custom class method from_dict
    assert repr(hash_table) in {
        "HashTable.from_dict({'hola': 'hello', 98.6: 37, False: True})",
        "HashTable.from_dict({'hola': 'hello', False: True, 98.6: 37})",
        "HashTable.from_dict({98.6: 37, 'hola': 'hello', False: True})",
        "HashTable.from_dict({98.6: 37, False: True, 'hola': 'hello'})",
        "HashTable.from_dict({False: True, 'hola': 'hello', 98.6: 37})",
        "HashTable.from_dict({False: True, 98.6: 37, 'hola': 'hello'})",
    }

def test_should_create_hashtable_from_dict_with_custom_size():
    dictionary = {"hola": "hello", 98.6: 37, False: True}

    hash_table = HashTable.from_dict(dictionary, size=100)

    assert hash_table.size == 100
    assert hash_table.keys == set(dictionary.keys())
    assert hash_table.items == set(dictionary.items())
    assert unordered(hash_table.values) == list(dictionary.values())

# test equality
def test_should_compare_equal_to_itself(hash_table):
    assert hash_table == hash_table

def test_should_compare_equal_to_copy(hash_table):
    assert hash_table is not hash_table.copy()
    assert hash_table == hash_table.copy()

def test_should_compare_equal_different_key_value_order(hash_table):
    h1 = HashTable.from_dict({"a": 1, "b": 2, "c": 3})
    h2 = HashTable.from_dict({"b": 2, "a": 1, "c": 3})
    assert h1 == h2

def test_should_compare_unequal(hash_table):
    other = HashTable.from_dict({"different": "value"})
    assert hash_table != other

def test_should_compare_unequal_another_data_type(hash_table):
    assert hash_table != 42

def test_should_compare_equal_different_capacity():
    ''' two hash table with different size can still be equal'''
    data = {"a": 1, "b": 2, "c": 3}
    h1 = HashTable.from_dict(data, size=50)
    h2 = HashTable.from_dict(data, size=100)
    assert h1 == h2

# test copy method

def test_should_copy_keys_values_pairs_capacity(hash_table):
    copy = hash_table.copy()
    assert copy is not hash_table
    assert set(hash_table.keys) == set(copy.keys)
    assert unordered(hash_table.values) == copy.values
    assert set(hash_table.items) == set(copy.items)
    assert hash_table.size == copy.size

# test update and union methods
def test_should_update_has_all_keys():
    table = HashTable.from_dict({"a": 1, "b": 2})
    table2 = HashTable.from_dict({ "c": 3})
    expected_table = HashTable.from_dict({"a": 1, "b": 2, "c": 3})
    table.update(table2)

    assert table == expected_table

def test_should_overwrite_comm_keys():
    ''' if same key, right table value should be the one kept'''
    table = HashTable.from_dict({"a": 1, "b": 2})
    table2 = HashTable.from_dict({"b": 3})
    expected_table = HashTable.from_dict({"a": 1, "b": 3})
    table.update(table2)

    assert table == expected_table

def test_should_raise_error_without_hash_table():
    ''' if table2 is not an Hashtable shoulw raise an error'''
    table = HashTable.from_dict({"a": 1, "b": 2})
    table2 = 'ciao'
    with pytest.raises(TypeError):
        table.update(table2)


def test_should_union_has_all_keys():
    table = HashTable.from_dict({"a": 1, "b": 2})
    table2 = HashTable.from_dict({ "c": 3})
    expected_table = HashTable.from_dict({"a": 1, "b": 2, "c": 3})
    new_table = table | table2

    assert new_table == expected_table

def test_should_in_place_union_has_all_keys():
    table = HashTable.from_dict({"a": 1, "b": 2})
    table2 = HashTable.from_dict({ "c": 3})
    expected_table = HashTable.from_dict({"a": 1, "b": 2, "c": 3})
    table |= table2

    assert table == expected_table

def test_should_overwrite_comm_keys():
    ''' if same key, right table value should be the one kept'''
    table = HashTable.from_dict({"a": 1, "b": 2})
    table2 = HashTable.from_dict({"b": 3})
    expected_table = HashTable.from_dict({"a": 1, "b": 3})
    new_table = table | table2

    assert new_table == expected_table

def test_should_union_creates_new_table():
    ''' union should not modify in place'''
    table = HashTable.from_dict({"a": 1, "b": 2})
    table2 = HashTable.from_dict({ "c": 3})
    new_table = table | table2

    assert new_table is not table

# test hash collisions
from unittest.mock import patch

# Patching temporarily replaces built-in hash() function with a fake one that always returns the same expected value
@patch("builtins.hash", return_value=42)
def test_should_detect_hash_collision(hash_mock):
    hash_table = HashTable(size=100)
    hash_table["easy"] = "Requires little effort"
    hash_table["difficult"] = "Needs much skill"
    assert hash_table["easy"] == "Requires little effort"
    assert hash_table["difficult"] == "Needs much skill"


def test_should_dynamically_resize():
    hash_table = HashTable(size=1)
    for i in range(10):
        hash_table[i] = i
    assert hash_table.size == 16


