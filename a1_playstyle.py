"""
The Playstyle classes for A1.
Docstring examples are not required for Playstyles.

The Playstyle classes represent ways for us to choose attacks. 
They are initialized with 2 attibutes: whether they're a Manual mode or not, 
and the battle queue for it. When it's called to perform an action, it'll try 
to decide an action for the first person in th at BattleQueue.

The Manual Playstyle has been provided for you.
It simply takes the key that is pressed and calls perform_action, passing in
that key if it's a valid key ("A" or "S").

You are tasked with implementing the Random Playstyle, which returns a key 
for a move that can be used by the player (e.g. if the character has enough SP 
for only a normal attack, it should return 'A'. If they have enough SP for 
either a normal or a special attack, it should return either 'A' or 
'S') at random.
"""
from typing import Any
from random import choice


class Playstyle:
    """
    The Playstyle superclass.
    
    is_manual - Whether the class is a manual Playstyle or not.
    battle_queue - The BattleQueue corresponding to the game this Playstyle is
                   being used in.
    """
    is_manual: bool
    battle_queue: 'BattleQueue'
    
    def __init__(self, battle_queue: 'BattleQueue') -> None:
        """
        Initialize this Playstyle with BattleQueue as its battle queue.
        """
        self.battle_queue = battle_queue
        self.is_manual = True
    
    def select_attack(self, parameter: Any = None) -> str:
        """
        Return the attack for the next character in this Playstyle's
        battle_queue to perform.
        
        Return 'X' if a valid move cannot be found.
        """
        raise NotImplementedError

class ManualPlaystyle(Playstyle):
    """
    The ManualPlaystyle. Inherits from Playstyle.
    """
    
    def select_attack(self, parameter: Any = None) -> str:
        """
        Return the attack for the next character in this Playstyle's
        battle_queue to perform.
        
        parameter represents a key pressed by a player.

        Return 'X' if a valid move cannot be found.
        """
      
        if parameter in ['A', 'S']:
            return parameter

        return 'X'

# Implement a random playstyle that selects an attack at random.
# Importing random and using random.choice might be helpful.

class RandomPlaystyle(Playstyle):
    """
    The RandomPlaystyle. Inherits from Playstyle.
    """
   
    def __init__(self, battle_queue: 'BattleQueue') -> None:
        """
        Initialize this Playstyle with BattleQueue as its battle queue.
        """
        self.battle_queue = battle_queue
        self.is_manual = False
    
        
    def select_attack(self, parameter: Any = None) -> str:
        """
        Return a random attack for the next character in this Playstyle's
        battle_queue to perform.
        
        parameter will always be None. 

        Return 'X' if a valid move cannot be found.
        """
        player = self.battle_queue.first_player_with_action()
        
        if player.style == 'Rogue':
            if player.skill_points >= 10:
                return choice(['A', 'S']) 
            return 'A'
        
        elif player.style == 'Mage':
            if player.skill_points >= 30:
                return choice(['A', 'S']) 
            return 'A'        
        return 'X'


if __name__ == '__main__':
    import python_ta
    python_ta.check_all(config='a1_pyta.txt')
