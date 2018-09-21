"""Contains character classes"""

class Character:
    """A character class
    name - character name
    battle_queue - contains information about which player will attack next
    playstyle - character has either a manual or random playstyle"""
    
    name: str
    battle_queue: 'BattleQueue'
    playstyle: 'Playstyle'
    
    def __init__(self, name: str, battle_queue: 'BattleQueue', 
                 playstyle: 'Playstyle') -> None:
        """Initializes a character with name, battle_queue, playstyle, enemy, 
        health, skill points, fighting style, animation
        
        >>> from a1_battle_queue import BattleQueue 
        >>> from a1_playstyle import ManualPlaystyle
        >>> bq = BattleQueue()
        >>> ps = ManualPlaystyle(bq)
        >>> x = Character('adam', bq, ps)
        >>> x.battle_queue == bq
        >>> True
        >>> x.skill_points == 100
        >>> True
        >>> x.health == 100
        >>> True
        """
        
        self.enemy = None
        self.health = 100
        self.skill_points = 100
        self.name = name
        self.sprite = None
        self.playstyle = playstyle
        self.battle_queue = battle_queue
        self.style = None
        self.last_animation = ('idle', 9)
        
    def get_next_sprite(self) -> str:
        """Returns the next sprite to be drawn.
        
        >>> from a1_battle_queue import BattleQueue 
        >>> from a1_playstyle import ManualPlaystyle
        >>> bq = BattleQueue()
        >>> ps = ManualPlaystyle(bq)
        >>> x = Mage('adam', bq, ps)
        >>> x.get_next_sprite()
        >>> 'mage_idle_0'
        >>> x.get_next_sprite()
        >>> 'mage_idle_1'
        >>> x.attack()
        >>> x.get_next_sprite()
        >>> 'mage_attack_0'
        >>> x.special_attack()
        >>> 'mage_special_0'
        """
        last_num = self.last_animation[1]
        if last_num != 9:
            next_num = str(last_num + 1)
            self.last_animation = (self.last_animation[0], int(next_num))
        else:
            next_num = str(0)
            self.last_animation = ('idle', int(next_num))
        return '{0}_{1}_{2}'.format(self.sprite, self.last_animation[0], 
                                    next_num)
                                    
    def get_name(self) -> str:
        """Return the name of the character
        
        >>> from a1_battle_queue import BattleQueue 
        >>> from a1_playstyle import ManualPlaystyle
        >>> bq = BattleQueue()
        >>> ps = ManualPlaystyle(bq)
        >>> x = Character('adam', bq, ps)
        >>> x.get_name()
        >>> 'adam'
        """
        return self.name
    
    def get_sp(self) -> int:
        """Return how many skill points the character has left
        
        >>> from a1_battle_queue import BattleQueue 
        >>> from a1_playstyle import ManualPlaystyle
        >>> bq = BattleQueue()
        >>> ps = ManualPlaystyle(bq)
        >>> x = Rogue('adam', bq, ps)
        >>> x.get_sp()
        >>> 100
        >>> x.attack()
        >>> x.get_sp()
        >>> 97
        >>> x.special_attack()
        >>> x.get_sp()
        >>> 87
        """
        return self.skill_points
    
    def get_hp(self) -> int:
        """Return how much health the character has left.
        
        >>> from a1_battle_queue import BattleQueue 
        >>> from a1_playstyle import ManualPlaystyle
        >>> bq = BattleQueue()
        >>> ps = ManualPlaystyle(bq)
        >>> x = Rogue('adam', bq, ps)
        >>> y = mage('mike', bq, ps)
        >>> y.get_hp()
        >>> 100
        >>> x.attack()
        >>> y.get_hp()
        >>> 93
        >>> x.special_attack()
        >>> y.get_hp()
        >>> 91"""
        return self.health       
        
    def __repr__(self) -> str:
        """Return a string representation of the character.
        
        >>> from a1_battle_queue import BattleQueue 
        >>> from a1_playstyle import ManualPlaystyle
        >>> bq = BattleQueue()
        >>> ps = ManualPlaystyle(bq)
        >>> x = Rogue('adam', bq, ps)  
        >>> x
        >>> 'adam: (Rogue) 100/100'
        >>> x.attack()
        >>> x.get_sp()
        >>> 97
        >>> 'adam: (Rogue) 100/97'
        """
        return '{0}: ({1}) {2}/{3}'.format(self.name, self.style,
                                           self.health, self.skill_points)
    
    
class Rogue(Character):
    """A rogue type character class. Inherits from character"""
    def __init__(self, name: str, battle_queue: 'BattleQueue', 
                 playstyle: 'Playstlyle') -> None:
        """Inherits from character class
        
        >>> from a1_battle_queue import BattleQueue 
        >>> from a1_playstyle import ManualPlaystyle
        >>> bq = BattleQueue()
        >>> ps = ManualPlaystyle(bq)
        >>> P1 = Rogue('Mike', bq, ps)
        >>> x.battle_queue == bq
        >>> True
        >>> x.skill_points == 100
        >>> True
        >>> x.health == 100
        >>> True"""
        
        super().__init__(name, battle_queue, playstyle)
        self.defense = 10
        self.style = 'Rogue'
        self.sprite = 'rogue'
    
    def attack(self) -> None:
        """Performs an attack. Sets animation back to the first attack 
        animation. Reduces enemy's health and it's own characters skill points
        and add's it's self to the end of the battle queue
        
        >>> from a1_battle_queue import BattleQueue 
        >>> from a1_playstyle import ManualPlaystyle
        >>> bq = BattleQueue()
        >>> ps = ManualPlaystyle(bq)
        >>> x = Rogue('adam', bq, ps)
        >>> y = mage('mike', bq, ps)
        >>> y.get_hp()
        >>> 100
        >>> x.attack()
        >>> y.get_hp()
        >>> 93
        >>> x.get_next_sprite()
        >>> 'Rogue_attack_0'
        >>> x.get_sp()
        >>> 97
        >>> bq.queue[-1]
        >>> x
        """
        
        self.last_animation = ('attack', -1)
        self.enemy.health = max(0, self.enemy.health - 15 + self.enemy.defense)
        self.skill_points = max(0, self.skill_points - 3)
        self.battle_queue.add(self)
                
    def special_attack(self) -> None:
        """Performs a special attack. Sets animation back to the first special
        attack animation. Reduces enemy's health and it's own characters skill
        points and add's it's self to the end of the battle queue twice.
        
        >>> from a1_battle_queue import BattleQueue 
        >>> from a1_playstyle import ManualPlaystyle
        >>> bq = BattleQueue()
        >>> ps = ManualPlaystyle(bq)
        >>> x = Rogue('adam', bq, ps)
        >>> y = mage('mike', bq, ps)
        >>> y.get_hp()
        >>> 100
        >>> x.special_attack()
        >>> bq.queue[-2:]
        >>> [x, x]
        >>> y.get_hp()
        >>> 82
        >>> x.get_next_sprite()
        >>> 'Rogue_special_0'
        >>> x.get_sp()
        >>> 90"""
        
        self.last_animation = ('special', -1)
        self.enemy.health = max(0, self.enemy.health - 20 + self.enemy.defense)
        self.skill_points = max(0, self.skill_points - 10)
        self.battle_queue.add(self)    
        self.battle_queue.add(self)  
        
    def get_available_actions(self) -> list:
        """Return all available attacks for the character to perform. Return 
        None if the character can not perform any attacks.
        
        >>> from a1_battle_queue import BattleQueue 
        >>> from a1_playstyle import ManualPlaystyle
        >>> bq = BattleQueue()
        >>> ps = ManualPlaystyle(bq)
        >>> x = Rogue('adam', bq, ps)
        >>> x.get_available_actions()
        >>> ['A', 'S']
        """
        if self.skill_points >= 10:
            return ['A', 'S']
        elif self.skill_points >= 3:
            return ['A']
        return []
        
    def is_valid_action(self, move: str) -> bool:
        """Return True if a character can perform the given action. Else return 
        False.
        
        >>> from a1_battle_queue import BattleQueue 
        >>> from a1_playstyle import ManualPlaystyle
        >>> bq = BattleQueue()
        >>> ps = ManualPlaystyle(bq)
        >>> x = Rogue('adam', bq, ps)
        >>> x.is_valid_action('A')
        >>> True
        >>> x.is_valid_action('S')
        >>> True
        >>> x.is_valid_action('r')
        >>> False"""
        
        if self.skill_points >= 10:
            return move in ['A', 'S']    
        elif self.skill_points >= 3:
            return move in ['A']            
        return False
        
                 
class Mage(Character):
    """A Mage type character class. Inherits from character"""
    def __init__(self, name: str, battle_queue: 'BattleQueue', 
                 playstyle: 'Playstyle') -> None:
        """Inherits from character class
        
        >>> from a1_battle_queue import BattleQueue 
        >>> from a1_playstyle import ManualPlaystyle
        >>> bq = BattleQueue()
        >>> ps = ManualPlaystyle(bq)
        >>> P1 = Mage('Mike', bq, ps)
        >>> x.battle_queue == bq
        >>> True
        >>> x.skill_points == 100
        >>> True
        >>> x.health == 100
        >>> True"""
        
        super().__init__(name, battle_queue, playstyle)
        self.defense = 8
        self.style = 'Mage'
        self.sprite = 'mage'
        
    def attack(self) -> None:
        """Performs an attack. Sets animation back to the first attack 
        animation. Reduces enemy's health and it's own characters skill points
        and add's it's self to the end of the battle queue
        
        >>> from a1_battle_queue import BattleQueue 
        >>> from a1_playstyle import ManualPlaystyle
        >>> bq = BattleQueue()
        >>> ps = ManualPlaystyle(bq)
        >>> x = mage('adam', bq, ps)
        >>> y = rogue('mike', bq, ps)
        >>> x.get_hp()
        >>> 100
        >>> x.attack()
        >>> y.get_hp()
        >>> 90
        >>> x.get_next_sprite()
        >>> 'mage_attack_0'
        >>> x.get_sp()
        >>> 95
        >>> bq.queue[-1]
        >>> x
        """        
        self.last_animation = ('attack', -1)
        self.enemy.health = max(0, self.enemy.health - 20 + self.enemy.defense)
        self.skill_points = max(0, self.skill_points - 5)
        self.battle_queue.add(self)
        
    def special_attack(self) -> None:
        """Performs a special attack. Sets animation back to the first special
        attack animation. Reduces enemy's health and it's own characters skill
        points. Add's the enemy and then it's self to the end of the battle
        queue.
        
        >>> from a1_battle_queue import BattleQueue 
        >>> from a1_playstyle import ManualPlaystyle
        >>> bq = BattleQueue()
        >>> ps = ManualPlaystyle(bq)
        >>> x = mage('adam', bq, ps)
        >>> y = rogue('mike', bq, ps)
        >>> y.get_hp()
        >>> 100
        >>> x.special_attack()
        >>> bq.queue[-2:]
        >>> [y, x]
        >>> y.get_hp()
        >>> 70
        >>> x.get_next_sprite()
        >>> 'mage_special_0'
        >>> x.get_sp()
        >>> 70
        """        
        self.last_animation = ('special', -1)
        self.enemy.health = max(0, self.enemy.health - 40 + self.enemy.defense)
        self.skill_points = max(0, self.skill_points - 30)
        self.battle_queue.add(self.enemy)    
        self.battle_queue.add(self)  
      
    def get_available_actions(self) -> list:
        """Return all available attacks for the character to perform. Return 
        None if the character can not perform any attacks.
        
        >>> from a1_battle_queue import BattleQueue 
        >>> from a1_playstyle import ManualPlaystyle
        >>> bq = BattleQueue()
        >>> ps = ManualPlaystyle(bq)
        >>> x = mage('adam', bq, ps)
        >>> x.get_available_actions()
        >>> ['A', 'S']
        """        
        if self.skill_points >= 30:
            return ['A', 'S']
        elif self.skill_points >= 5:
            return ['A']       
        return []
        
    def is_valid_action(self, move: str) -> bool:
        """Return True if a character can perform the given action. Else return 
        False.
        
        >>> from a1_battle_queue import BattleQueue 
        >>> from a1_playstyle import ManualPlaystyle
        >>> bq = BattleQueue()
        >>> ps = ManualPlaystyle(bq)
        >>> x = mage('adam', bq, ps)
        >>> x.is_valid_action('A')
        >>> True
        >>> x.is_valid_action('S')
        >>> True
        >>> x.is_valid_action('r')
        >>> False
        """        
        if self.skill_points >= 30:
            return move in ['A', 'S']        
        elif self.skill_points >= 5:
            return move in ['A']          
        return False
        
        
if __name__ == '__main__':
    import python_ta
    python_ta.check_all(config='a1_pyta.txt')

      
