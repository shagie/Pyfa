# shipBonusTorpedoMissileThermDmgMB
#
# Used by:
# Ship: Typhoon Fleet Issue
type = "passive"
def handler(fit, ship, context):
    fit.modules.filteredChargeBoost(lambda mod: mod.charge.requiresSkill("Torpedoes"),
                                    "thermalDamage", ship.getModifiedItemAttr("shipBonusMB"), skill="Minmatar Battleship")
