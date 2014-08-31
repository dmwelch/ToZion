class Role(object):
    def __init__(self, **kwargs):
        #TODO: these values need to be initialized by some historical stats
        super(Role, self).__init__()
        self._stamina = kwargs.pop('stamina', 0)
        self._leadership = kwargs.pop('leadership', 0)
        self._power = kwargs.pop('power', 0)
        self._gender = kwargs.pop('gender', '')
        self._hasBeenHead = False
        self._headOfHouse = kwargs.pop('headOfHouse', False)
        self._priesthood = kwargs.pop('priesthood', False)
        self._age = 0

    def __str__(self):
        retval = '\n'.join(['-' * 20,
                            'Gender: {0}'.format(self._gender),
                            'Priesthood: {0}'.format(self._priesthood),
                            'Power: {0}'.format(self._power),
                            'Leadership: {0}'.format(self._leadership),
                            'Stamina: {0}'.format(self._stamina),
                            'Age: {0}'.format(self._age),
                            'Head of house: {0}'.format(self._headOfHouse),
                            '-' * 20,
                            ])
        return retval

    @property
    def headOfHouse(self):
        return self._headOfHouse

    @headOfHouse.setter
    def headOfHouse(self, value):
        """
        Case: first time as head of house
        if value and not hasBeenHead:
            headOfHouse = value
            hasBeenHead = True
        Case: was head but not anymore
        if not value and hasBeenHead:
            headOfHouse = value
        Case: again head of house
        if value and hasBeenHead:
            headOfHouse = value
        """
        value = bool(value)
        if value == self._headOfHouse:
            return  # Do nothing
        self._headOfHouse = value
        if self._headOfHouse and not self._hasBeenHead:
            self._hasBeenHead = True  # This should only be able to be set once!
            self.firstTimeHead()

    @property
    def gender(self):
        return self._gender

    @gender.setter
    def gender(self, value):
        assert value in ('male', 'female'), "Unknown gender {0}".format(value)
        if self._gender is not None:
            return # Don't allow sex changes!
        else:
            self._gender = value

    @property
    def stamina(self):
        return self._stamina

    @stamina.setter
    def stamina(self, value):
        self._stamina = value

    @property
    def leadership(self):
        return self._leadership

    @leadership.setter
    def leadership(self, value):
        self._leadership = value

    @property
    def power(self):
        return self._power

    @power.setter
    def power(self, value):
        self._power = value

    def firstTimeHead(self):
        pass


class Male(Role):
    priesthoodPowerBoost = 200
    leaderPowerBoost = 100
    leaderStaminaBoost = 20

    def __init__(self, **kwargs):
        super(Male, self).__init__(**kwargs)
        self._gender = 'male'
        kwargs.pop('gender', None)

    @property
    def priesthood(self):
        return self._priesthood

    @priesthood.setter
    def priesthood(self, value):
        value = bool(value)
        if value == self._priesthood:  # prevent multiple resets to boost power
            print "HERE"
            return  # Do nothing
        if self._age > 11:
            self._priesthood = value
            self.gainThePriesthood()
        else:
            print "Here now"

    def gainThePriesthood(self):
        if self.priesthood:
            self._power += self.priesthoodPowerBoost
        else:
            self._power -= self.priesthoodPowerBoost

    def firstTimeHead(self):
        self._power += self.leaderPowerBoost
        self._stamina += self.leaderStaminaBoost


class Female(Role):
    leaderStrengthBoost = 50
    leaderStaminaBoost = 200
    leaderPowerBoost = 300

    def __init__(self, **kwargs):
        super(Female, self).__init__(**kwargs)
        self._gender = 'female'
        self._priesthood = False

    @property
    def headOfHouse(self):
        return super(Female, self).headOfHouse

    @property
    def priesthood(self):
        assert self._priesthood == False
        return self._priesthood

    @priesthood.setter
    def priesthood(self, value):
        return  # Do nothing

    @headOfHouse.setter
    def headOfHouse(self, value):
        super(Female, self).headOfHouse(value)

    def firstTimeHead(self):
        self.strength += self.leaderStrengthBoost
        self.stamina += self.leaderStaminaBoost
        self.power += self.leaderPowerBoost


class Son(Male):
    def __init__(self, **kwargs):
        super(Son, self).__init__(**kwargs)
        self._leadership = kwargs.pop('leadership', 200)
        self._stamina = kwargs.pop('stamina', 200)
        self._age = kwargs.pop('age', 0)
        self._headOfHouse = kwargs.pop('headOfHouse', False)


class Daughter(Female):
    def __init__(self, **kwargs):
        super(Daughter, self).__init__(**kwargs)
        self.leadership = 250
        self.stamina = 150


class Father(Son):
    def __init__(self, **kwargs):
        super(Father, self).__init__(**kwargs)
        self._leadership = kwargs.pop('leadership', 500)
        self._stamina = kwargs.pop('stamina', 500)
        self._age = kwargs.pop('age', 30)
        self._headOfHouse = kwargs.pop('headOfHouse', True)
        self._priesthood = kwargs.pop('priesthood', False)


class Mother(Daughter):
    def __init__(self, **kwargs):
        super(Mother, self).__init__(**kwargs)
        self._gender = 'female'
        self.kwargs = kwargs.pop('leadership', 500)
        self.stamina = kwargs.pop('stamina', 500)
