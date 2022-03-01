'''
Project  - Case Converter
In programming, there are five common cases: camelCase, snakecase, kebab-case, PascalCase and UPPER_CASE_SNAKE_CASE. For this project, you are to Write a function that takes in a sentence and a desired case as the inputs, and then converts the sentence into the desired case.

Examples:

convert("Hello, World.", "camel")
Output: helloWorld

convert("Hello, World.", "snake")
Output: hello_world

convert("Hello, World.", "kebab")
Output: hello-world

convert("Hello, World.", "pascal")
Output: HelloWorld

convert("Hello, World.", "uppercasesnake")
Output: HELLO_WORLD
'''

def convert(s,type):
    words = s.split(", ")
    res = []
    if 'camel' == type:
        res.append(words[0].lower())
        for i in range(1,len(words)):
            res.append(words[i].capitalize())

    if 'snake' == type:
        for word in words:
            res.append(word.lower())
            res.append('_')
        res.pop()

    if 'kebab' == type:
        for word in words:
            res.append(word.lower())
            res.append('-')
        res.pop()
    if 'pascal' == type:
        for word in words:
            res.append(word.capitalize())
    if 'uppercasesnake' == type:
        for word in words:
            res.append(word.upper())
            res.append('_')
        res.pop()
    return "".join(res)[:-1]

if __name__ == "__main__":
    print(convert("Hello, World.", "camel"))
    print(convert("Hello, World.", "snake"))
    print(convert("Hello, World.", "kebab"))
    print(convert("Hello, World.", "pascal"))
    print(convert("Hello, World.", "uppercasesnake"))

