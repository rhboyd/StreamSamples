class SharkProps(object):
    def __init__(self, baby_name: str, mama_name: str, daddy_name: str):
        self._baby_name = baby_name
        self._mama_name = mama_name
        self._daddy_name = daddy_name

    @property
    def baby_name(self) -> str:
        return self._baby_name

    @property
    def mama_name(self) -> str:
        return self._mama_name

    @property
    def daddy_name(self) -> str:
        return self._daddy_name
