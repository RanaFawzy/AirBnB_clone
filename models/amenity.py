#!/usr/bin/python3
"""Defines AAmenity class."""
from models.base_model import BaseModel


class Amenity(BaseModel):
    """Represent aamenity.

    Attributes:
        name (str): The name of the amenity.
    """

    name = ""
