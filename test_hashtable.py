import pytest

from src import HashTable

def test_should_create_hashtable():
    assert HashTable(size = 100) is not None

def test_should_return_size():
    assert len(HashTable(size = 100)) == 100

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
    assert new_hash_size == hash_size

def test_should_update_value(hash_table):
    assert hash_table["hola"] == "hello"

    hash_table["hola"] = "hallo"

    assert hash_table["hola"] == "hallo"
    assert hash_table[98.6] == 37
    assert hash_table[False] is True
    assert len(hash_table) == 100

def test_should_not_contain_none_value_when_created():
    # there should be no pair.value as None when table is initialized
    hash_table = HashTable(size=100)
    values = [pair.value for pair in hash_table.items if pair]
    assert None not in values


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

def test_delete_should_not_shrink_size(hash_table):
    assert len(hash_table) == 100

    del hash_table["hola"]

    assert len(hash_table) == 100

def test_should_raise_key_error_when_deleting(hash_table):
    with pytest.raises(KeyError) as exception_info:
        del hash_table["missing_key"]
    assert exception_info.value.args[0] == "missing_key"

# test get key-value pairs

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