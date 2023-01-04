import re 

def make_extract(html_str, number_of_words):
    clean_str = re.sub(r'<.*?>', '', html_str)
    str_list = clean_str.split(' ')[0:int(number_of_words)]
    short_str = ''
    for word in str_list:
        short_str += word + " "
    return short_str + "..."