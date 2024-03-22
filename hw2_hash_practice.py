word_output = {}

with open("./hw2_data.txt","r",encoding="utf-8") as file:
    for line in file:
        one_word = str(line).replace("\n","")
        if one_word not in word_output:
            word_output[one_word] = 1
        else:
            word_output[one_word] = word_output[one_word] + 1
file.close()

print(f"Hash內容: {word_output}\n")
print(f"總共有{len(word_output)}種不重複的字彙\n")
for word in word_output:
    print(f"{word}共出現了{word_output[word]}次")