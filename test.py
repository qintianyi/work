def g():
    print('gggg')
    i = 1
    yield i
    i += 1


a = iter(g())

for i in a:
    print('for====' + str(i))

class A:
    def __init__(self) -> None:
        super().__init__()