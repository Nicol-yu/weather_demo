class MyErr(Exception):

    def __init__(self, code: int, description: str):
        self.description = description
        self.code = code

    def __str__(self):
        return self.description


class ParameterErr(MyErr):
    pass


class ThirdPartyServiceErr(MyErr):
    pass
