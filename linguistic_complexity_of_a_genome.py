import argparse


def count_distinct_substrings(s: str, substring_len: int):
    pass
    # have to count distinct substrings of s
    return 2


def maximum_substring_count(string_len: int, alphabet_len: int, substring_len: int):
    # compute formula
    pass
    return 10


def linguistic_complexity(string: str, alphabet: [str]):
    string_len = len(string)
    alphabet_len = len(alphabet)
    sum_sub_k = 0
    sum_m_k = 0
    for substring_len in range(1, string_len):
        sum_sub_k += count_distinct_substrings(string, substring_len)
        sum_m_k += maximum_substring_count(string_len, alphabet_len, substring_len)

    return sum_sub_k / sum_m_k


def main(args):
    print(linguistic_complexity(args.string, args.alphabet))


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description="computing linguistic complexity over string with given alphabet")
    parser.add_argument('string', type=str)
    parser.add_argument('alphabet', type=str)
    args = parser.parse_args()
    main(args)
