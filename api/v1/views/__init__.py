#!/usr/bin/python3
""" Init file """
from flask import Blueprint

app_views = Blueprint('app_views', __name__, url_prefix='/api/v1')

from api.v1.views.index import index
from api.v1.views.states import get_states, get_state
from api.v1.views.cities import get_cities, get_city
from api.v1.views.amenities import get_amenities, get_amenity
from api.v1.views.users import get_users, get_user
from api.v1.views.places import get_places, get_place
from api.v1.views.places_reviews import get_place_reviews, create_place_review
from api.v1.views.places_amenities import get_place_amenities, create_place_amenity

