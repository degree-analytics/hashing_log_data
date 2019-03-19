# Copyright 2019 MF Genius, Corp d/b/a Degree Analytics
#
# Licensed under the MIT License

import re
import os
from uuid import UUID, uuid3
from os.path import isfile
import fileinput
import sys

# replace with secret namespace uuid. This will try and see if there is a NAMESPACE available as an environmental variable
NAMESPACE = os.getenv("NAMESPACE", UUID('00000000-0000-0000-0000-000000000000'))


# this is the regix to identify the particular data that should be replaced it is based on the sample below as well as in the testfile where User[EncryptThisUsername] is how the identity is coded
class REGEX_MATCHES(object):
    MERAKI = [r"(?<=identity\=')[^'\s]*"]
    ARUBA = [r"(?<=username\=)[^\s]*", r"(?<=\sName\:)[^\s]*"]
    EXTREME = [r"(?<=User\[)[^]]*"]

    @classmethod
    def all(cls):
        return cls.EXTREME + cls.MERAKI + cls.ARUBA


SELECTED_REGEX = REGEX_MATCHES.all()


regex = "|".join(SELECTED_REGEX)

if len(sys.argv) != 2:
    raise Exception("Must provide filename")
filename = sys.argv[1]

if not isfile(filename):
    raise Exception("Must provide valid filename")

subst = lambda x: str(uuid3(NAMESPACE, str(x)))

# If you want to replace in original file, use this line below and remove print statement. This currently stores the original in a backup aka '.bak'
# with fileinput.FileInput(filename, inplace=True, backup='.bak') as file:

with fileinput.FileInput(filename, inplace=False) as file:
    for line in file:
        print(re.sub(regex, subst, line), end='')
