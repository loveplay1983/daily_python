# string_capwords.py
import string

text = 'The quick brown fox jumped over the lazy dog.'
text_cap = string.capwords(text)
print(text_cap)


# string_template.py  (substitute, values and format)
values = {'var': 'foo'}

t = string.Template("""
Variable        : $var
Escape          : $$
Variable in text: ${var}iable
""")
print('TEMPLATE:', t.substitute(values))
print('\n')

s = """
Variable : %(var)s
Escape : %%
Variable in text : %(var)siable
"""
print('INTERPOLATION: ', s % values)
# TEMPLATE AND INTERPOLATION, interpolation needs to consider the type of args
print('\n')

s = """
Variable        : {var}
Escape          : {{}}
Variable in text: {var}iable
"""
print('FORMAT:', s.format(**values))  #

# save_substitute
import string```````````````````````````````````````````````````
values = {'var': 'foo'}
t = string.Template("$var is here but $missing is not provided")
try:
    print('substitute()     :', t.substitute(values))
except KeyError as err:
    print('ERROR:', str(err))
print('safe_substitute():', t.safe_substitute(values))  # substitute the existed $ object

##### string_template advanced for regular expression

class MyTemplate(string.Template):
    delimiter = '^'
    idpattern = '[a-z]+_[a-z]+'

template_text = '''
    Delimiter: ^^
    Replaced: ^replaced_text
    Ignored: ^ignored_text
'''

dict_text = {
    'replaced_text': 'Hello world',
    'ignored_text': 'Python is bad',
}

t = MyTemplate(template_text)
print('replacing text by tempalte')
print(t.safe_substitute(dict_text))
