# hash-table
I want to replicate built-in Python hash table to better understand its functioning. Moreover I apply TDD framework to make sure it's working as expected. mplementing a well-known data structure such as a hash table is a perfect application of this software development methodology. You have clear expectations that are straightforward to codify as test cases.  
The hash table is mainly comprised of two components
- hash function
- linked list

### hash table key features

| requirement                                      | included |  
|--------------------------------------------------|----------|
| Create an empty hash table                       | ✅        |
| Insert a key-value pair                          | ✅        | 
| Accept arbitrary key type                        | ✅        |
| Get a key-value pair                             | ✅         |
| Delete a key-value pair                          |     ✅     |
| Update the value associated with an existing key |          |
| Hash table is iterable                           |          |
| Possible to compare to hash tables               |          |
| Possible to convert python dictionary            | ✅         |
| String representation                            | ✅         |


### custom hash function requirements

Those requirements have been tested

| requirement             | included |  
|-------------------------|----------|
| deterministic           |          |
| universal input         |          | 
| fixed-size output       |          |
| uniformely distributed  |          |
| fast to compute         |          |




## TO DO

1. create a package
3. prepare custom hash function requirements