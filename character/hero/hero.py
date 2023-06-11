import json
from character.character import Character
from abc import ABC, abstractmethod

class HeroAbstract(ABC):
    @abstractmethod
    def use_skill_1(self):
        pass
    
    @abstractmethod
    def use_skill_2(self):
        pass
    
    @abstractmethod
    def use_skill_3(self):
        pass
    
    @abstractmethod
    def recall(self):
        pass
    
    @abstractmethod
    def heal(self):
        pass
    
    @abstractmethod
    def use_spell(self):
        pass
    
    @abstractmethod
    def my_own_hero_encoder(self):
        pass
    

class Hero(HeroAbstract):
    def __init__(self, 
                 hero_name: str, damage_type: str, basic_attack_damage: int, role: list, hero_image_selected_for_slot: str, select_hero_icon:str,
                 skill1_damage: int, skill1_name: str, skill1_duration: float,
                 skill2_damage: int, skill2_name: str, skill2_duration: float,
                 skill3_damage: int, skill3_name: str, skill3_duration: float,
                 ):
        self.__hero_name = hero_name
        self.__damage_type = damage_type
        self.__role = role
        self.__hero_image_selected_for_slot=hero_image_selected_for_slot
        self.__select_hero_icon = select_hero_icon
        self.__is_picked = False
        self.__is_banned = False
        self.__basic_attack_damage = basic_attack_damage
        
        self.__skill1_damage = skill1_damage
        self.__skill1_name = skill1_name
        self.__skill1_duration = skill1_duration
        
        self.__skill2_damage = skill2_damage
        self.__skill2_name = skill2_name
        self.__skill2_duration = skill2_duration
        
        self.__skill3_damage = skill3_damage
        self.__skill3_name = skill3_name
        self.__skill3_duration = skill3_duration
    
    #GET HERO NAME
    def get_hero_name(self):
        return self.__hero_name
    
    #GET DAMAGE TYPE
    def get_damage_type(self):
        return self.__damage_type
    
    #GET HERO SELECTED IMAGE FOR SLOT
    def get_hero_image_selected_for_slot(self):
        return self.__hero_image_selected_for_slot
    
    #GET HERO TYPE (EX: MARKSMAN)
    def get_role(self):
        return self.__role
    
    #GET HERO IMAGE PATH
    def get_select_hero_icon(self):
        return self.__select_hero_icon
    
    #GET STATUS IS HERO PICKED
    def get_is_picked(self):
        return self.__is_picked
    
    #GET STATUS IS HERO BANNED
    def get_is_banned(self):
        return self.__is_banned
    
    #GET BASICK ATTACK DAMAGE
    def get_basic_attack_damage(self):
        return self.__basic_attack_damage
    
    ## GET SKILL DAMAGE
    def get_skill1_damage(self):
        return self.__skill1_damage
    
    def get_skill2_damage(self):
        return self.__skill2_damage
    
    def get_skill3_damage(self):
        return self.__skill3_damage
    
    ## GET SKILL NAME
    def get_skill1_name(self):
        return self.__skill1_name
    
    def get_skill2_name(self):
        return self.__skill2_name
    
    def get_skill3_name(self):
        return self.__skill3_name
    
    ## GET SKILL DURATION
    
    def get_skill1_duration(self):
        return self.__skill1_duration
    
    def get_skill2_duration(self):
        return self.__skill2_duration
    
    def get_skill3_duration(self):
        return self.__skill3_duration
    
    #SET STATUS IS HERO PICKED
    def set_is_picked(self, value: bool):
        self.__is_picked = value
    
    #GET STATUS IS HERO BANNED
    def set_is_banned(self, value: bool):
        self.__is_banned = value
        
    def use_skill_1(self):
        print("Skill 1 used")
    
    def use_skill_2(self):
        print("Skill 2 used")
    
    def use_skill_3(self):
        print("Skill 3 used")
    
        
    def heal(self):
        print("Heal used")
    
    def recall(self):
        print("Recall used")
    
    def use_spell(self):
        print("Spell used")
    
        
            
class Hero_3Skill(Hero):
    def __init__(self, hero_name: str, damage_type: str, basic_attack_damage: int, role: list, hero_image_selected_for_slot: str, 
                 select_hero_icon: str, skill1_damage: int, skill1_name: str, skill1_duration: float, 
                 skill2_damage: int, skill2_name: str, skill2_duration: float, 
                 skill3_damage: int, skill3_name: str, skill3_duration: float):
        super().__init__(hero_name, damage_type, basic_attack_damage, role, hero_image_selected_for_slot, select_hero_icon, skill1_damage, skill1_name, skill1_duration, skill2_damage, skill2_name, skill2_duration, skill3_damage, skill3_name, skill3_duration)
    # def __init__(self, hero_name: str, damage_type: str, basic_attack_damage: int, role: list, 
    #              select_hero_icon: str, skill1_damage: int, skill1_name: str, skill1_duration: float, 
    #              skill2_damage: int, skill2_name: str, skill2_duration: float, 
    #              skill3_damage: int, skill3_name: str, skill3_duration: float):
        # super().__init__(hero_name, damage_type, basic_attack_damage, role, select_hero_icon, skill1_damage, skill1_name, skill1_duration, skill2_damage, skill2_name, skill2_duration, skill3_damage, skill3_name, skill3_duration)
    
    def my_own_hero_encoder(self):
        dictionary = {
            "skills": 4,
            "damage_type": self.get_damage_type(),
            "basic_attack_damage": self.get_basic_attack_damage(),
            "role": self.get_role(),
            "hero_image_selected_for_slot": self.get_hero_image_selected_for_slot(),
            "select_hero_icon": self.get_select_hero_icon(),
            
            "skill1_name": self.get_skill1_name(),
            "skill1_damage": self.get_skill1_damage(),
            "skill1_duration": self.get_skill1_duration(),
            
            "skill2_name": self.get_skill2_name(),
            "skill2_damage": self.get_skill1_damage(),
            "skill2_duration": self.get_skill2_duration(),
            
            "skill3_name": self.get_skill3_name(),
            "skill3_damage": self.get_skill3_damage(),
            "skill3_duration": self.get_skill3_duration(),
        }
        return dictionary
        
class Hero_4Skill(Hero):
    def __init__(self, 
                 hero_name: str, damage_type: str, basic_attack_damage: int, 
                 role: list, hero_image_selected_for_slot: str, select_hero_icon: str, 
                 skill1_damage: int, skill1_name: str, skill1_duration: float, 
                 skill2_damage: int, skill2_name: str, skill2_duration: float, 
                 skill3_damage: int, skill3_name: str, skill3_duration: float,
                 skill4_damage: int, skill4_name: str, skill4_duration: float):
        super().__init__(hero_name, damage_type, basic_attack_damage, role, hero_image_selected_for_slot, select_hero_icon, skill1_damage, skill1_name, skill1_duration, skill2_damage, skill2_name, skill2_duration, skill3_damage, skill3_name, skill3_duration)
    # def __init__(self, 
    #              hero_name: str, damage_type: str, basic_attack_damage: int, role: list, 
    #              select_hero_icon: str, skill1_damage: int, skill1_name: str, skill1_duration: float, 
    #              skill2_damage: int, skill2_name: str, skill2_duration: float, 
    #              skill3_damage: int, skill3_name: str, skill3_duration: float,
    #              ):
    #     super().__init__(hero_name, damage_type, basic_attack_damage, role, select_hero_icon, skill1_damage, skill1_name, skill1_duration, skill2_damage, skill2_name, skill2_duration, skill3_damage, skill3_name, skill3_duration)
        self.__skill4_damage = skill4_damage
        self.__skill4_name = skill4_name
        self.__skill4_duration = skill4_duration
    ##GET SKILL NAME
    def get_skill4_name(self):
        return self.__skill4_name
    
    ##GET SKILL DAMAGE
    def get_skill4_damage(self):
        return self.__skill4_damage
    
    ##GET SKILL DURATION
    def get_skill4_duration(self):
        return self.__skill4_duration
    
    def my_own_hero_encoder(self):
        dictionary = {
            "skills": 4,
            "damage_type": self.get_damage_type(),
            "basic_attack_damage": self.get_basic_attack_damage(),
            "role": self.get_role(),
            "hero_image_selected_for_slot": self.get_hero_image_selected_for_slot(),
            "select_hero_icon": self.get_select_hero_icon(),
            
            "skill1_name": self.get_skill1_name(),
            "skill1_damage": self.get_skill1_damage(),
            "skill1_duration": self.get_skill1_duration(),
            
            "skill2_name": self.get_skill2_name(),
            "skill2_damage": self.get_skill1_damage(),
            "skill2_duration": self.get_skill2_duration(),
            
            "skill3_name": self.get_skill3_name(),
            "skill3_damage": self.get_skill3_damage(),
            "skill3_duration": self.get_skill3_duration(),
            
            "skill4_name": self.get_skill4_name(),
            "skill4_damage": self.get_skill4_damage(),
            "skill4_duration": self.get_skill4_duration(),
        }
        return dictionary