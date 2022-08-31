from data_structures.hashtable import Hashtable


def left_join(hash1, hash2):
    joined_list = []
    keys1 = hash1.keys()

    for key in keys1:
        if hash2.contains(key):
            joined_list.append([key, hash1.get(key), hash2.get(key)])
        else:
            joined_list.append([key, hash1.get(key), "NONE"])

    return joined_list

