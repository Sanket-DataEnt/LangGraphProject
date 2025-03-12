from typing_extensions import TypedDict

class BlogGeneratorState(TypedDict):
    """Represents the structure of the state used in the Blog Generator Application

    Args:
        TypedDict (_type_): _description_
    """
    topic: str
    title: str
    blog: str
    finalblog: str