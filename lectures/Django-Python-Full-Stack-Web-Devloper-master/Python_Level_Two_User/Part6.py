import re


patterns = ["term1", "term2"]

text = "This is a string with term1, not the other!"

for pattern in patterns:
    print("I'm searching for: " + pattern)

    if re.search(pattern, text):
        print("MATCH!")
    else:
        print("NO MATCH!")


match = re.search('term1', text)

print(type(match))
print(match.start())

split_term = "@"

email = "user@gmail.com"

print(re.split(split_term, email))

print(re.findall("match", "test phrase match in middle"))
print(re.findall("match", "test phrase match in match middle"))

def multi_re_find(patterns, phrase):
    for pat in patterns:
        print("Searching for pattern {}".format(pat))
        print(re.findall(pat, phrase))
        print("\n")

test = "sdsd..sssddd..sdddsddd...dsds...dsssssss...sddddd"

test_patterns = ["sd*"]
multi_re_find(test_patterns, test)

test_patterns = ["sd+"]
multi_re_find(test_patterns, test)

test_patterns = ["sd?"]
multi_re_find(test_patterns, test)

test_patterns = ["sd{3}"]
multi_re_find(test_patterns, test)

test_patterns = ["sd{1,3}"]
multi_re_find(test_patterns, test)

test_patterns = ["s[sd]+"]
multi_re_find(test_patterns, test)

test2 = "This is a string! But it has punctuation. How can we remove it? 123456 #hashtag"
test2_patterns = ["[^!.?]+"]
multi_re_find(test2_patterns, test2)

test2_patterns = ["[a-z]+"]
multi_re_find(test2_patterns, test2)

test2_patterns = ["[A-Z]+"]
multi_re_find(test2_patterns, test2)

test2_patterns = [r"\d+"]
multi_re_find(test2_patterns, test2)

test2_patterns = [r"\D+"]
multi_re_find(test2_patterns, test2)

test2_patterns = [r"\s+"]
multi_re_find(test2_patterns, test2)

test2_patterns = [r"\S+"]
multi_re_find(test2_patterns, test2)

test2_patterns = [r"\w+"]
multi_re_find(test2_patterns, test2)

test2_patterns = [r"\W+"]
multi_re_find(test2_patterns, test2)
