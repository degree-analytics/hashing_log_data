# Hashing Student IDs/Protected Information - Simple Python Example

This simple script is designed to identify data that should be protected, and create a unique hash UUID identifier. 

One of the simplest ways to hash a student id is to use Version 3/5 of a UUID (other encrypting techniques may be used (like SHA-256), but should be used with caution for this particular example as to not overly inflate the size of the data files)

UUID3 hashes for example, begin with a namespace, and will then uniquely create an ID given some input.

Per example, we might have a namespace (just some random UUID): 
```
>>> namesspace = uuid1()
>>> print(namespace)
UUID('308c5806-47c2-11e8-a664-4a0006cb7710')
Then we can generate a unique hash on some student id/username, say for "billyjoe"
>>> uuid3(namespace, 'billjoe')
UUID('18dac545-a288-3486-ac10-dc54e35c48d9')
```

Per this case `118dac545-a288-3486-ac10-dc54e35c48d91` effectively becomes the random "identity" for "billyjoe". As this is a one-way md5 hash, it is not practically possible to re-identify "billyjoe" without having access to the protected `namespace`

These functions can easily be applied over `.csv` files or the like to randomize data. 

To run this, execute `./run.sh` - data from `testfile.txt` will be de-identified and written to `outputfile.txt`

**NOTE**: in order to consistently produce the same unique "random" identity every time for every student, you must use the same `namespace`. Essentially that means that anytime it is necessary to de-identify a student with a random UUID identifier, you should use the same `namespace` and hash mechanism (ie, uuid3 in this example)

**NOTE**: Depending on the source of the log file (Aruba, Meraki, Cisco, Extreme, etc...), the regex will need to be replaced appropriately. We have included a few here, but feel free to contact us with any quesitons or for assistance

---------

Degree Analytics

support@degreeanalytics.com

