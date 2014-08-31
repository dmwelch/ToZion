import doctest
import nose

import player
import roles

father = player.Player()
role = roles.Father()
father.role = role
print role
assert issubclass(father.role.__class__, roles.Role)
role.gender = 'female'
assert role.gender == 'male'
assert role.leadership == 500
role.leadership = 0
assert role.stamina == 500
role.stamina = 0
assert role.headOfHouse
role.headOfHouse = False
role.power = 100
print role
assert not role.priesthood
role.priesthood = True
print role

mother = player.Player()
mother.role = roles.Mother()
assert issubclass(mother.role.__class__, roles.Role)

son = player.Player()
son.role = roles.Son()
assert issubclass(son.role.__class__, roles.Role)

daughter = player.Player()
daughter.role = roles.Daughter()
assert issubclass(daughter.role.__class__, roles.Role)
