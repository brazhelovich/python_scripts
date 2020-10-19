file ='emails.txt'

uniqlines = set(open(file, 'r', encoding='utf-8').readlines())
gotovo = open('email_output.txt', 'w', encoding='utf-8').writelines(set(uniqlines))