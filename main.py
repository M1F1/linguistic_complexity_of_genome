import argparse
import math
import os
from pysuffixarray.core import SuffixArray


def is_valid_file(parser, arg):
    if not os.path.exists(arg):
        parser.error("The file %s does not exist!" % arg)
    else:
        return open(arg, 'r')  # return


def maximum_substring_count(string_len: int, alphabet_len: int):
    m = float(sum([string_len - k + 1
                   if k > math.log(string_len + 1) / math.log(alphabet_len)
                   else alphabet_len ** k
                   for k in range(1, string_len + 1)]))
    return m

# brute force method

# def sub_lc(string, k):
#     seet = set()
#     for i in range(len(string) - k + 1):
#         seet |= {(string[i:i+k])}
#     return seet
#
#
# def sum_sub_lc(string):
#     string_length = len(string)
#     sum = 0
#     for i in range(string_length):
#         sum += len(sub_lc(string, i + 1))
#     return sum


def linguistic_complexity(string: str, alphabet: [str]):
    string_len = len(string)
    alphabet_len = len(alphabet)
    sa = SuffixArray(string)
    sum_sub_k = len(string) * (len(string) + 1) / 2 - sum(sa.longest_common_prefix())
    sum_m_k = maximum_substring_count(string_len, alphabet_len)
    return sum_sub_k / sum_m_k


def main(args):
    print(F'lc: {linguistic_complexity(args.infile.readline(), args.alphabet)}')


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description="computing linguistic complexity over string with given alphabet")
    parser.add_argument('infile', type=argparse.FileType('r', encoding='UTF-8'))
    parser.add_argument('alphabet', type=str)
    args = parser.parse_args()
    main(args)
