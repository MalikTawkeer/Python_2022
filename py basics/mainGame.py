
import gamePackege.game_rules
# importing sub-package of package -> module ->py file
from gamePackege.weaponPkg.scarl import scarlWeapon

print(scarlWeapon())

from gamePackege.characterPkg import emeny as EMEMY
print(EMEMY.peterEnemy())
