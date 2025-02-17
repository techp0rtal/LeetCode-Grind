
def isAnagram(s: str, t: str) -> bool:
    # Not sure if this is needed, but I like the thought so I'll keep it here for reference
    # string_1 = s.lower()
    # string_2 = t.lower()

    # not too sure if this is worth having but maybe it can save some work
    # Update according to leetcode it makes it slower. just get rid of it (went from 15ms beating 43% to 7, and beats 90%
    for letter in t:
        if letter not in s:
            print(False)
            return False

    string_1_dic = {}
    string_2_dic = {}

    for key in s:
        if key not in string_1_dic:
            string_1_dic[key] = 1
        else:
            string_1_dic[key] = string_1_dic[key] + 1
    for key in t:
        if key not in string_2_dic:
            string_2_dic[key] = 1
        else:
            string_2_dic[key] = string_2_dic[key] + 1
    print(string_1_dic, string_2_dic)
    print(string_1_dic == string_2_dic)
    return string_1_dic == string_2_dic



isAnagram("rat", "rcar")
