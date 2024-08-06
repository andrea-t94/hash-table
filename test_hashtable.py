import pytest

from src import HashTable, Blank

def test_should_create_hashtable():
    assert HashTable(size = 100) is not None

def test_should_return_size():
    assert len(HashTable(size = 100)) == 100

def test_should_create_empty_value_slots():
    # Given
    expected_values = [Blank, Blank, Blank]
    hash_table = HashTable(size=3)

    # When
    actual_values = hash_table.values

    # Then
    assert actual_values == expected_values

def test_should_insert_key_value_pairs():
    # Given
    hash_table = HashTable(size=100)
    hash_table["hola"] = "hello"
    hash_table[98.6] = 37
    hash_table[False] = True

    # When
    actual_values = hash_table.values

    # Then
    assert "hello" in actual_values
    assert 37 in actual_values
    assert True in actual_values

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


@pytest.mark.skip
def test_delete_should_not_shrink_size():
    pass

def test_should_not_contain_none_value_when_created():
    assert None not in HashTable(size=100).values

# happy path
def test_should_insert_none_value():
    # Given
    hash_table = HashTable(size=100)
    hash_table[None] = None

    # When
    actual_values = hash_table.values

    # Then
    None in actual_values