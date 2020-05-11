def function_works(f):
    def decorated(*args, **kwargs):
        print('This call of the function works')
        return f(*args, **kwargs)

    return decorated


@function_works
def test_function(x1, x2):
    print(x1 + x2)


@function_works
def test_function2():
    print("Hope this is a good example")


test_function(1, 1)
test_function2()
