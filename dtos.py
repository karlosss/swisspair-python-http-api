from functools import partial

from pydantic import BaseModel
from swisspair import create_matches, Player, Match


class PlayerDto(BaseModel):
    id: str
    points: int
    rank: int
    can_get_bye: bool
    cannot_be_paired_against_ids: list[str]


class MatchDto(BaseModel):
    p1_id: str
    p2_id: str | None
    is_bye: bool


class RequestDto(BaseModel):
    players: list[PlayerDto]
    power_pairing: bool

    def to_swisspair_callable(self) -> callable:
        swisspair_players = [Player(p.id, p.points, p.rank, p.can_get_bye, set(p.cannot_be_paired_against_ids)) for p in self.players]
        return partial(create_matches, swisspair_players, self.power_pairing)


class ResponseDto(BaseModel):
    matches: list[MatchDto]

    @staticmethod
    def from_swisspair(swisspair_matches: list[Match]) -> "ResponseDto":
        return ResponseDto(matches=[MatchDto(p1_id=m.p1.id, p2_id=m.p2.id if m.p2 else None, is_bye=m.is_bye) for m in swisspair_matches])
