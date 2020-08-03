x = {      "a": 37, "b": 42, "c": 927}


def very_important_function(
    template: str,  file: os.PathLike, debug: bool = False,
):
    """Applies `variables` to the `template` and writes to `file`."""
    with open(file, "w") as f:
        print("Hello, world!", file=f)
