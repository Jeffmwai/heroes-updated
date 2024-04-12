from app import db
from app.models import Hero, Power, HeroPower

def seed_data():
    fire = Power(name='Fire', description='Ability to manipulate fire')
    ice = Power(name='Ice', description='Ability to control ice and cold temperatures')
    super_strength = Power(name='Super Strength', description='Enhanced physical strength')
    flight = Power(name='Flight', description='Ability to fly at supersonic speed')

    superman = Hero(name='Clark Kent', super_name='Superman')
    batman = Hero(name='Bruce Wayne', super_name='Batman')
    flash = Hero(name='Barry Allen', super_name='Flash')

    superman_powers = [HeroPower(strength='Strong', hero=superman, power=super_strength)]
    batman_powers = [HeroPower(strength='Average', hero=batman, power=super_strength)]
    flash_powers = [HeroPower(strength='Weak', hero=flash, power=super_strength), 
                    HeroPower(strength='Strong', hero=flash, power=flight)]

    db.session.add_all([fire, ice, super_strength, flight, superman, batman, flash] + superman_powers + batman_powers + flash_powers)
    db.session.commit()

if __name__ == '__main__':
    seed_data()
