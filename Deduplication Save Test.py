import glob
import os
import json


def jacquard_similarity(set1, set2):
    intersection = len(set1.intersection(set2))
    union = len(set1.union(set2))
    similarity = intersection / union
    return similarity


def hmd_distance(hash1, hash2):
    num = 0
    assert len(hash1) == len(hash2)
    for i in range(len(hash1)):
        if hash1[i] != hash2[i]:
            num += 1
    return num


def list_to_str(_list: list) -> str:
    h_s = ''
    for i in _list:
        h_s += str(i)
    return h_s


def list_to_set(_list: list) -> set:
    return set(_list)


def contrast(json_dict: dict, thr):
    dep_set: set = set()
    keys = list(json_dict.keys())
    for i, k1 in enumerate(keys[0:]):
        for k2 in keys[i + 1:]:
            v1 = json_dict.get(k1)
            v2 = json_dict.get(k2)
            if isinstance(v1, list):
                v1 = list_to_str(v1)
            if isinstance(v2, list):
                v2 = list_to_str(v2)
            if hmd_distance(v1, v2) < thr:
                dep_set.add(k1)
    return dep_set


def contrast_jacb(json_dict: dict, thr):
    dep_set: set = set()
    keys = list(json_dict.keys())
    for i, k1 in enumerate(keys[0:]):
        for k2 in keys[i + 1:]:
            v1 = json_dict.get(k1)
            v2 = json_dict.get(k2)
            if isinstance(v1, list):
                v1 = list_to_set(v1)
            if isinstance(v2, list):
                v2 = list_to_set(v2)
            sim = jacquard_similarity(v1, v2)
            if sim > thr:
                dep_set.add(k1)
    return dep_set


if __name__ == '__main__':
    root = r"H:\ColorDe_Code\JsonFile"
    _all_json = glob.glob(os.path.join(root, "TZH_*.json"))
    print("当前所有使用数据集个数: {}".format(len(_all_json)))

    for json_path in _all_json:
        with open(json_path, 'r+') as f:
            ded_size = 0
            org_size = 0
            j_dict = json.load(f)
            deduplication_set = contrast(j_dict, thr=3)
            for p in list(j_dict.keys()):
                org_size += os.stat(p).st_size
            for d_path in deduplication_set:
                ded_size += os.stat(d_path).st_size

            print("{} => 节约空间比例: {}%".format(json_path.split("\\")[-1], (ded_size / org_size) * 100))
