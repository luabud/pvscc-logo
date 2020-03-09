import requests

# from https://medium.com/@jorlugaqui/how-to-strip-html-tags-from-a-string-in-python-7cb81a2bbf44
def remove_html_tags(text):
    """Remove html tags from a string"""
    import re
    clean = re.compile('(<.*?>)|\\n|\\r|\\t')
    return re.sub(clean, '', text)

r = requests.get(url="https://code.visualstudio.com/docs/python/python-tutorial")
raw_content = r.content.decode("utf-8")

clean_raw_content = remove_html_tags(raw_content)
print(clean_raw_content)
