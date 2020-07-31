stopwords = input("Enter words to be ignored seperated by commas: ").split(", ")
text = input("Enter a title to generate its acronym: ").split()
#
print("The acronym is:/n")
acronym = []
for i in text:
        if i.lower() not in stopwords:
                acronym.append(i[0])
print(''.join(acronym))