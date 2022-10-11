from pydantic import BaseModel, validator
from typing import Optional
from datetime import datetime


class ModelSuperHero(BaseModel):
    """
    Model of a one Super Hero
    """
    id: int
    fullName: str
    birthDate: str
    city: str
    gender: str
    mainSkill: str
    phone: Optional[str]

    @validator('birthDate')
    def parse_date(cls, birth_date: str) -> str:
        """
        Check correct format of birthDate
        """
        if not datetime.strptime(birth_date, '%Y-%m-%d'):
            raise ValueError(f'birthDate - Wrong format')
        return datetime.strptime(birth_date, '%Y-%m-%d')

    @validator('gender')
    def check_gender(cls, g: str) -> str:
        """
        Check gender str - F or M
        """
        if g not in ['F', 'M']:
            raise ValueError(f'gender - Wrong format. Not "F" or "M" ---> {g} <---')
        return g

    @validator('fullName')
    def check_full_name(cls, name: str) -> str:
        """
        Check unnecessary spaces in the end or start of a fullName
        That may be critical for auth process or smthng like that
        """
        if name[0].isspace() or name[-1].isspace():
            raise ValueError(f'fullName - Unnecessary space in the end or start of string --->{name}<---')
        return name
