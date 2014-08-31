class Role(object):
    def __init__(self, gender=None, stamina=None, leadership=None, power=None):
        #TODO: these values need to be initialized by some historical stats
        self._stamina = stamina
        self._leadership = leadership
        self._power = power
        self._gender = gender
        self._headOfHouse = False

    @property
    def headOfHouse(self):
        return self.headOfHouse

    @property
    def gender(self):
        return self.gender

    @gender.setter
    def gender(self, value):
        assert value in ('male', 'female'), "Unknown gender {0}".format(value)
        self._gender = value

    @property
    def stamina(self):
        return self.stamina

    @stamina.setter
    def stamina(self, value):
        self._stamina = value

    @property
    def leadership(self):
        return self.leadership

    @leadership.setter
    def leadership(self, value):
        self._leadership = value

    @property
    def power(self):
        return self.power

    @power.setter
    def power(self, value):
        self._power = value


class Father(Role):
    def __init__(self, **kwargs):
        super(Role, self).__init__(**kwargs)
        self.leadership = 500
        self.stamina = 500
        self.gender = "male"
        self._priesthood = False
        self.headOfHouse = True

    @property
    def priesthood(self):
        pass

    @priesthood.setter
    def priesthood(self, value):
        self.priesthood = bool(value)
        self.power = self.power + 200


class Mother(Role):
    def __init__(self, **kwargs):
        super(Role, self).__init__(**kwargs)
        self.leadership = 500
        self.stamina = 500
        self.gender = "female"

    @headOfHouse.setter
    def headOfHouse(self, value):
        self._headOfHouse = bool(value)
        self.leadership += 200


class Son(Role):
    def __init__(self, **kwargs):
        super(Role, self).__init__(**kwargs)
        self.leadership = 200
        self.stamina = 200
        self.gender = "male"
        self._priesthood = False
        self.headOfHouse = False


class Daughter(Role):
    def __init__(self, **kwargs):
        super(Role, self).__init__(**kwargs)
        self.leadership = 250
        self.stamina = 150
        self.gender = "female"
        self._priesthood = False
        self.headOfHouse = False
