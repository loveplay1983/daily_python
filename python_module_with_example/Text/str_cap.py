# Manually accomplish the same functionality of string.capwords()
# separate text first then use a temp list add each part of the text in which each text has already been convert to captalized by for loop, then use join() to combine all together

# import string
text  = 'hello world'
def captalize(text):
    text_sep = text.split()
    text_cap = []
    str_cap = ' '
    for item in text_sep:
        each = item[0].upper() + item[1:]
        text_cap.append(each)

    return str_cap.join(text_cap)

result = captalize(text)
print(result)
