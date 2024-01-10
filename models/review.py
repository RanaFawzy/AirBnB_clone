#!/usr/bin/python3
"""Defines rReview class."""
from models.base_model import BaseModel


class Review(BaseModel):
    """Represent review.
    Attributes:
        place_id (str): pPlace id.
        user_id (str): uUser id.
        text (str): ttext of the review.
    """

    place_id = ""
    user_id = ""
    text = ""
