import glob
import os
import time
import json


def hmd_distance(hash1, hash2):
    num = 0
    assert len(hash1) == len(hash2)
    for i in range(len(hash1)):
        if hash1[i] != hash2[i]:
            num += 1
    return num


def jaccard_similarity(set1: set, set2: set):
    intersection = len(set1.intersection(set2))
    union = len(set1.union(set2))
    similarity = intersection / union
    return similarity


def list_to_str(_list: list) -> str:
    h_s = ''
    for i in _list:
        h_s += str(i)
    return h_s


def list_to_set(_list: list) -> set:
    return set(_list)


def contrast(json_dict: dict, period):
    values = list(json_dict.values())
    for i, v1 in enumerate(values[0:period]):
        for v2 in values[i:period]:
            if isinstance(v1, list):
                v1 = list_to_str(v1)
            if isinstance(v2, list):
                v2 = list_to_str(v2)
            hmd_distance(v1, v2)


def contrast_jacb(json_dict: dict, period):
    values = list(json_dict.values())
    for i, v1 in enumerate(values[0:period]):
        for v2 in values[i:period]:
            if isinstance(v1, list):
                v1 = list_to_set(v1)
            if isinstance(v2, list):
                v2 = list_to_set(v2)
            jaccard_similarity(v1, v2)


root = r"H:\ColorDe_Code\JsonFile"
_all_json = glob.glob(os.path.join(root, "SHA_*.json"))
print("当前所有使用数据集个数: {}".format(len(_all_json)))

for json_path in _all_json:
    with open(json_path, 'r+') as f:
        j_dict = json.load(f)
        for p in range(100, 1100, 100):
            start_time = time.time()
            # contrast(j_dict, p)
            contrast_jacb(j_dict, p)
            end_time = time.time()
            print("{}-{}-time: {}".format(json_path.split("\\")[-1], p, end_time - start_time))
