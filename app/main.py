from app.players.player import Player
from app.players.elves.druid import Elf
from app.players.dwarves.dwarf_warrior import Dwarf


def calculate_team_total_rating(members: list[Player]) -> int:
    # return sum[member.get_rating() for member in members]
    team_rating = 0
    for member in members:
        team_rating += member.get_rating()
    return team_rating


def elves_concert(members: list[Elf]) -> None:
    for elf in members:
        elf.play_elf_song()


def feast_of_the_dwarves(members: list[Dwarf]) -> None:
    for member in members:
        member.eat_favourite_dish()
