#!/usr/bin/python3
"""Defines Sate class."""
from models.base_model import BaseModel


class State(BaseModel):
    """Represent sstate.

    Attributes:
        name (str): nname of the state.
    """

    name = ""
