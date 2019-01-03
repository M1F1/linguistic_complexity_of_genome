import argparse
import distinct_substrings

def maximum_substring_count(string_len: int, alphabet_len: int, substring_len: int):
    pass
    return 40


def linguistic_complexity(string: str, alphabet: [str]):
    string_len = len(string)
    alphabet_len = len(alphabet)
    sum_sub_k = len(distinct_substrings.create_all_distinct_substrings(string))
    sum_m_k = maximum_substring_count(string, 'ATG', 1)

    return sum_sub_k / sum_m_k


def main(args):
    print(linguistic_complexity(args.string, args.alphabet))


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description="computing linguistic complexity over string with given alphabet")
    parser.add_argument('string', type=str)
    parser.add_argument('alphabet', type=str)
    args = parser.parse_args()
    main(args)
