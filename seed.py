#!/usr/bin/env python3

from app import app
from models import db, Hero, Power, HeroPower

with app.app_context():

    # Delete existing data
    HeroPower.query.delete()
    Hero.query.delete()
    Power.query.delete()

    # Seed data for heroes
    hero1 = Hero(
        name="Superman",
        super_name="Clark Kent"
    )

    hero2 = Hero(
        name="Batman",
        super_name="Bruce Wayne"
    )

    db.session.add_all([hero1, hero2])

    # Seed data for powers
    power1 = Power(
        name="Flight",
        description="Ability to fly"
    )

    power2 = Power(
        name="Super Strength",
        description="Incredible physical strength"
    )

    power3 = Power(
        name="Balance Unlimited",
        description="Super rich "
    )    

    db.session.add_all([power1, power2, power3])

    # Seed data for hero powers
    hero_power1 = HeroPower(
        strength="Weak",
        hero_id=1,  # Superman
        power_id=1   # Flight
    )

    hero_power2 = HeroPower(
        strength="Strong",
        hero_id=1,  # Superman
        power_id=2   # Super Strength
    )

    hero_power3 = HeroPower(
        strength="Average",
        hero_id=2,  # Batman
        power_id=3   # Moneeeeeeeeeeeeeeeeeeeeeeeeeeeeey
    )

    db.session.add_all([hero_power1, hero_power2, hero_power3])

    db.session.commit()
