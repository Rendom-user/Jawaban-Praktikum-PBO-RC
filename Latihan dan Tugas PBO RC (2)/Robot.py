import random

class Robot:
    def __init__(self, name, attack, defense, power, hp, accuracy):
        self.name = name
        self.attack = attack
        self.defense = defense
        self.power = power
        self.hp = hp
        self.accuracy = accuracy
        self.is_defending = False  
    
    def attack_enemy(self, enemy):
        if random.random() <= self.accuracy:  
            damage = max(0, self.attack - (enemy.defense * (1/2 if enemy.is_defending else 1)))  
            enemy.hp -= damage  
            print(f"{self.name} menyerang {enemy.name} dan memberikan {damage} damage!")
        else:
            print(f"{self.name} menyerang {enemy.name} tapi meleset!")
    
    def defend(self):
        self.is_defending = True
        print(f"{self.name} bersiap bertahan, pertahanan meningkat!")
    
    def reset_defense(self):
        self.is_defending = False  
    
    def is_alive(self):
        return self.hp > 0

class Game:
    def __init__(self, robot1, robot2):
        self.robot1 = robot1
        self.robot2 = robot2
        self.game_over = False  
    
    def start(self):
        round_number = 1
        while self.robot1.is_alive() and self.robot2.is_alive() and not self.game_over:
            print(f"\nRound-{round_number} ==========================================================")
            print(f"{self.robot1.name} [{self.robot1.hp} HP | Defense: {self.robot1.defense}]")
            print(f"{self.robot2.name} [{self.robot2.hp} HP | Defense: {self.robot2.defense}]")
            
            self.take_turn(self.robot1, self.robot2)
            if self.game_over or not self.robot2.is_alive():
                break  
            
            self.take_turn(self.robot2, self.robot1)
            if self.game_over or not self.robot1.is_alive():
                break  
            
            self.robot1.reset_defense()
            self.robot2.reset_defense()
            round_number += 1
        
        self.declare_winner()

    def take_turn(self, robot, enemy):
        print("\n1. Attack     2. Defense     3. Giveup")
        action = input(f"{robot.name}, pilih aksi : ")
        if action == "1":
            robot.attack_enemy(enemy)
        elif action == "2":
            robot.defend()
        elif action == "3":
            print(f"{robot.name} menyerah! {enemy.name} menang!")
            self.game_over = True  
        else:
            print("Pilihan tidak valid, default ke Attack.")
            robot.attack_enemy(enemy)

    def declare_winner(self):
        if self.game_over:
            return  
        
        if not self.robot1.is_alive():
            print(f"\n{self.robot2.name} menang!")
        elif not self.robot2.is_alive():
            print(f"\n{self.robot1.name} menang!")
        else:
            print("Tidak ada pemenang.")


robotA = Robot("Cypher", attack = 100, defense = 10, power = 10, hp = 450, accuracy = random.uniform(0.5, 1))
robotB = Robot("Sova", attack = 80, defense = 8, power = 8, hp = 500, accuracy = random.uniform(0.5, 1))

game = Game(robotA, robotB)
game.start()
