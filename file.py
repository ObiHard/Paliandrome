def is_palindrome(text):
    cleaned = ''
    for char in text:
        if char.isalnum():
            cleaned += char.lower()

    reversed_text = ''
    for i in range(len(cleaned) - 1, -1, -1):
        reversed_text += cleaned[i]

    if cleaned == reversed_text:
        return True
    else:
        return False

assert is_palindrome('A man, a plan, a canal: Panama') == True, 'Test1'
assert is_palindrome('0P') == False, 'Test2'
assert is_palindrome('a.') == True, 'Test3'
assert is_palindrome('aurora') == False, 'Test4'
print("ОК")
