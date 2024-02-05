def gs_dreieck(a, b, c):

    if a == b != c or a == c != b or b == c != a:

        if a + b > c and a + c > b and b + c > a:
            return True
    return False


print(gs_dreieck(3, 3, 10))  # False
print(gs_dreieck(3, 3, 5))   # True

