class MathUtils:
    @staticmethod
    def add(a, b):
        return a + b

    @classmethod
    def description(cls):
        return f"This is {cls.__name__} class."

print(MathUtils.add(5, 7))
print(MathUtils.description())
