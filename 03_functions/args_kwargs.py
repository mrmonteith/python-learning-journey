def show_args(*args, **kwargs):
    print("Positional args:", args)
    print("Keyword args:", kwargs)

show_args(1, 2, 3, name="Michael", age=42)
