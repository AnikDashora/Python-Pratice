def anagram(str1,str2):
    answer = True
    for i in str1:
        if i in str2:
            continue
        else:
            answer = False
            break
    if answer:
        print("It is Anagram")
    else:
        print("It is not Anagram")

anagram("listen","silent")