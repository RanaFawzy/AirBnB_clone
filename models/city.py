#!/usr/bin/python3
"""Defines cCity class."""
from models.base_model import BaseModel


class City(BaseModel):
    """Represent ccity.

    Attributes:
        state_id (str): The state id.
        name (str): The name of the city.
    """

    state_id = ""
    name = ""
