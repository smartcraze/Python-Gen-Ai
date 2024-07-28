# Regex is a pattern-matching language that allows you to search, validate, and extract text.


'''
\d - digit
\w - word character (alphanumeric + underscore)
\s - whitespace
. - any character
^ - start of string
$ - end of string
| - OR operator
* - zero or more occurrences
+ - one or more occurrences
? - zero or one occurrence
{n} - exactly n occurrences
'''


'''
import re
re.search(pattern, text) - search for pattern in text
re.match(pattern, text) - match pattern at start of text
re.findall(pattern, text) - find all occurrences of pattern in text
re.sub(pattern, replacement, text) - replace pattern with replacement in text
'''







