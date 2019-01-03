
def create_substrings_idxs(substring: str, string: str) -> [str]:
    new_substrings_idxs = []
    substring_len = len(substring)
    string_len = len(string)
    for i in range(string_len - substring_len + 1):
        compared_substring = string[i: i + substring_len]
        if compared_substring == substring:
            new_substrings_idxs.append((i, i + substring_len))
    return new_substrings_idxs


def create_new_substrings(substrings_idxs:[(int, int)], string: str) -> [(int, int)]:
    new_substrings_idxs = []
    for substring_idxs in substrings_idxs:
        next_char_idx = substring_idxs[1] + 1
        if next_char_idx <= len(string):
            new_substrings_idxs.append(create_substrings_idxs(string[substring_idxs[0]: next_char_idx], string))
    return flatten_list(new_substrings_idxs)


def create_string_from_idxs(start_idx: int, end_idx: int, string: str) -> str:
    return string[start_idx: end_idx]


def flatten_list(list_of_lists: [[]]) -> []:
    return [item for sublist in list_of_lists for item in sublist]


def create_all_distinct_substrings(string):
    all_substrings_idxs = []
    new_substrings_idxs = []
    for c in list(set(string)):
        new_substrings_idxs.append(create_substrings_idxs(c, string))
    new_substrings_idxs = flatten_list(new_substrings_idxs)

    all_substrings_idxs.append(new_substrings_idxs)

    while len(new_substrings_idxs):
        new_substrings_idxs = create_new_substrings(substrings_idxs=new_substrings_idxs,
                                                    string=string)
        all_substrings_idxs.append(new_substrings_idxs)

    substrings = [create_string_from_idxs(idxs[0], idxs[1], string) for idxs in flatten_list(all_substrings_idxs)]
    return set(substrings)


def main():
    string = 'ATTTGGATT'
    distinct_substrings = create_all_distinct_substrings(string)
    print(distinct_substrings)
    print(len(distinct_substrings))


if __name__ == '__main__':
    main()
