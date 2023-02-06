#Chapter-3 Number and Strings

# Initialize the string “abc” on a variable named “s”:
# 1. Use a function to get the length of the string.
# 2. Write the necessary sequence of operations to transform the string “abc” in
# “aaabbbccc”. Suggestion: Use string concatenation and string indexes.

# s = "abc"
# def len_str(s):
#     get_len = len(s)
#     print("Seqence of string: ",get_len)

#     seq_s = s[0] * 3 + s[1] * 3 + s[2] * 3
#     print(seq_s)


# len_str(s)

# 2. Initialize the string “aaabbbccc” on a variable named “s”:
# 1. Use a function that allows you to find the first occurence of “b” in the string,
# and the first occurence of “ccc”.


# s = "aaabbbcc"

# def first_occ(s):
#     for i,c in enumerate(s):
#         if c == 'b':                                                      ####unable to solve
#             return i,c

            
#     print("First occurrence of 'b' is at position: ",i)

# print(first_occ(s))

# 2. Use a function that allows you to replace all occurences of “a” to “X”, and
# then use the same function to change only the first occurence of “a” to “X”.

# s = "aaabbbcc"
# def rep_occ(s):
#     #replace all occurrence of 'a' to 'X'
#     new_rep = s.replace("a","X")
#     # first_occ = s.replace("a","X",1)#replace(old_char, new_char, number)->third parameter is the max number of occurrences that you want to replace

#     # return first_occ
#     return new_rep


# print(rep_occ(s))

# 3. Starting from the string “aaa bbb ccc”, what sequences of operations do you need
# to arrive at the following strings? You can use the “replace” function.
# 1. “AAA BBB CCC”
# 2. “AAA bbb CCC”

# s = "aaa bbb ccc"
# new_seq = s.replace("aaa bbb ccc", "AAA BBB CCC")
# another_seq = s.replace("aaa bbb ccc", "AAA bbb CCC")
# print(another_seq)
# print(new_seq)



