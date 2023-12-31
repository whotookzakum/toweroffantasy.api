
import strawberry


@strawberry.type
class Skill:
    id: str
    icon: str
    name: str
    description: str


@strawberry.type
class Skills:
    normals: list[Skill]
    dodge: list[Skill]
    skill: list[Skill]
    discharge: list[Skill]


@strawberry.type
class Stats:
    shatter: float
    charge: float


@strawberry.type
class Advancements:
    description: str | None
    stats: Stats
    need: str


@strawberry.type
class WeaponEffect:
    title: str
    description: str


@strawberry.type
class ShatterOrCharge:
    value: float
    tier: str


@strawberry.type
class WeaponAssets:
    icon: str | None 
    weaponMatrixIcon: str | None
