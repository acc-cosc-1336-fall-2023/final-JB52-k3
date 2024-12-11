#write functions here, don't add input('') statements here!
def get_most_likely_ancestor_consensus(dna_string1, dna_string2):
    s1_len = len(dna_string1)
    s2_len = len(dna_string2)

    unittest_list = []

    if s2_len < s1_len:
        for indx in range(s1_len - (s2_len + 1)):
            if dna_string1[indx : (indx + s2_len)] == dna_string2:
                unittest_list.append(indx + 1)
                print(indx + 1)
    return unittest_list