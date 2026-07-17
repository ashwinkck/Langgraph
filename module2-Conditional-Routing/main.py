from typing import TypedDict
class State(TypedDict):
    number:int # with only one var
def router(state: State):
    return state