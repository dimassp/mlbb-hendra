import json
import time
from character.hero.hero import Hero_3Skill, Hero_4Skill
from utils import heroes_json_dict
heroes_dict = dict()

def generate_heroes():
    heroes = None
    with open(heroes_json_dict) as json_file:
        data = json.load(json_file)
    heroes = data
    for hero in heroes:
        total_skill = heroes[hero].get('skills')
        damage_type = heroes[hero].get('damage_type')
        basic_attack_damage = heroes[hero].get('basic_attack_damage')
        
        skill1_name = heroes[hero].get('skill1_name')
        skill1_damage = heroes[hero].get('skill1_damage')
        skill1_duration = heroes[hero].get('skill1_duration')
        
        skill2_name = heroes[hero].get('skill2_name')
        skill2_damage = heroes[hero].get('skill2_damage')
        skill2_duration = heroes[hero].get('skill3_duration')
        
        skill3_name = heroes[hero].get('skill3_name')
        skill3_damage = heroes[hero].get('skill3_damage')
        skill3_duration = heroes[hero].get('skill3_duration')
        
        if total_skill == 3:
            new_hero = Hero_3Skill(
                hero_name=hero,
                damage_type=damage_type,
                basic_attack_damage=basic_attack_damage,
                skill1_name=skill1_name,
                skill1_damage=skill1_damage,
                skill1_duration=skill1_duration,
                
                skill2_name=skill2_name,
                skill2_damage=skill2_damage,
                skill2_duration=skill2_duration,
                skill3_name=skill3_name,
                skill3_damage=skill3_damage,
                skill3_duration=skill3_duration,
            )
        elif total_skill == 4:
            skill4_name = heroes[hero].get('skill4_name')
            skill4_damage = heroes[hero].get('skill4_damage')
            skill4_duration = heroes[hero].get('skill4_duration')
            new_hero = Hero_4Skill(
                hero_name=hero,
                damage_type=damage_type,
                basic_attack_damage=basic_attack_damage,
                
                skill1_name=skill1_name,
                skill1_damage=skill1_damage,
                skill1_duration=skill1_duration,
                
                skill2_name=skill2_name,
                skill2_damage=skill2_damage,
                skill2_duration=skill2_duration,
                
                skill3_name=skill3_name,
                skill3_damage=skill3_damage,
                skill3_duration=skill3_duration,
                
                skill4_name=skill4_name,
                skill4_damage=skill4_damage,
                skill4_duration=skill4_duration,
            )
        heroes_dict.update({hero :new_hero})
        
def add_heroes_to_player():
    pass