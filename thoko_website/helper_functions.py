import re 

def make_extract(html_str, number_of_words):
    clean_str = re.sub(r'<.*?>', '', html_str)
    str_list = clean_str.split(' ')[0:int(number_of_words)]
    short_str = ' '.join(str_list)
    #if the created sentence ends with a full stop don't add three more full stops at the end
    if short_str[len(short_str) - 1] == '.':
        return short_str
        
    return short_str + "..."