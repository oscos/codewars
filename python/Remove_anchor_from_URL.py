# https://www.codewars.com/kata/51f2b4448cadf20ed0000386

# Solution Submitted: 08/12/2023
def remove_url_anchor(url):
    return url.split('#')[0]


# User submitted solutions to review

def remove_url_anchor(url):
  import re
  return re.sub('#.*$','',url)

def remove_url_anchor(url):
    index = url.find('#')
    return url[:index] if index >= 0 else url