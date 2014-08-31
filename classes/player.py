import roles

class Player(object):
    def __init__(self, *args, **kwargs):
        self._role = None
        for key, value in kwargs.items():
            eval("self.{key} = {value}".format(key=key, value=value))
        super(Player, self).__init__(*args, **kwargs)

    @property
    def role(self):
        return self._role

    @role.setter
    def role(self, value):
        assert issubclass(value.__class__, roles.Role)
        self._role = value
