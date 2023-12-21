class Creature:
    def __init__(self, life, damage, type, pos):
        self._life = life
        self._damage = damage
        self._type = type
        self._pos = pos
        dungeon.update_matrix(self._pos[0], self._pos[1], self._type)

    @property
    def damage(self):
        return self._damage
    
    @property
    def health(self):
        return self._life

    def update_pos(self):
        '''
        Updates own position in the dungeon grid.
        '''
        dungeon.update_matrix(self._pos[0], self._pos[1], self._type)

    def update_life(self, change):
        '''
        Updates own health after getting an item or getting damage.
        '''
        self._life += change
        return 0
    
    def update_damage(self, change):
        '''
        Updates own damage after getting an item.
        '''
        self._damage += change
        self._damage = max(1, self._damage)
        return 0
    
    def move_up(self):
        '''
        Moves up one position in the grid.
        '''
        self._pos[0] -= 1
        return 0

    def move_right(self):
        '''
        Moves right one position in the grid.
        '''
        self._pos[1] += 1
        return 0
    
    def move_down(self):
        '''
        Moves down one position in the grid.
        '''
        self._pos[0] += 1
        return 0
    
    def move_left(self):
        '''
        Moves left one position in the grid.
        '''
        self._pos[1] -= 1
        return 0
    
    def natural_movement(self):
        '''
        Defines the movement for every type of creature, be it a monster (U, R, D, L)
        or the hero (P).
        '''
        if self._type == "U" and self._pos[0] > 0:
            self.move_up()
        elif self._type == "R" and self._pos[1] < dungeon.max_y - 1:
            self.move_right()
        elif self._type == "D" and self._pos[0] < dungeon.max_x - 1:
            self.move_down()
        elif self._type == "L" and self._pos[1] > 0:
            self.move_left()
        elif self._type == "P":
            if self._pos[0] % 2 == 0:
                if self._pos[1] == 0:
                    self.move_up()
                else:
                    self.move_left()
            else:
                if self._pos[1] == dungeon.max_y - 1:
                    self.move_up()
                else:
                    self.move_right()
            

class Map:
    def __init__(self, size_x, size_y) -> None:
        self._size_x = size_x
        self._size_y = size_y
        self._matrix = [["."] * size_x for _ in range(size_y)]

    @property
    def max_x(self):
        return self._size_x
    
    @property
    def max_y(self):
        return self._size_y
    
    def update_matrix(self, x, y, obj):
        '''
        Updates the symbols in the matrix grid.
        '''
        self._matrix[y][x] = obj

    def print_map(self):
        '''
        Prints the dungeon grid into the console.
        '''
        for i in range(self._size_x):
            for j in range(self._size_y - 1):
                print(self._matrix[j][i], "", end="")
            print(self._matrix[self._size_y - 1][i], end="")
            print()
        print()
        return 0

class Item:
    def __init__(self, name, type, pos, status):
        self._name = name
        self._type = type
        self._pos = pos
        self._status = status
        dungeon.update_matrix(self._pos[0], self._pos[1], self._type)
    
    @property
    def name(self):
        return self._name

    @property
    def type(self):
        return self._type
    
    @property
    def stats(self):
        return self._status

    def update_pos(self):
        '''
        Updates the matrix with the item symbol.
        '''
        dungeon.update_matrix(self._pos[0], self._pos[1], self._type)

def update_positions():
    '''
    Updates all of the elements in the grid matrix to match the movements of the
    monsters and of the hero.
    '''
    dungeon._matrix = [["."] * map_sizes[0] for _ in range(map_sizes[1])]
    for j in items:
        j.update_pos()
    for i in monsters:
        i.update_pos()
    dungeon.update_matrix(exit_pos[0], exit_pos[1], "*")
    Link.update_pos()
    dungeon.print_map()
    return 0

if __name__ == "__main__":
    #Getting the initial settings for the map
    link_status = [int(x) for x in input().split()]
    map_sizes = [int(x) for x in input().split()]
    link_pos = [int(x) for x in input().split(",")]
    exit_pos = [int(x) for x in input().split(",")]
    dungeon = Map(map_sizes[0], map_sizes[1])
    Link = Creature(link_status[0], link_status[1], "P", link_pos)
    N_monsters = int(input())
    monsters = []
    for i in range(N_monsters):
        monster = input().split()
        monster_stats = []
        monster_stats.append(int(monster[0]))
        monster_stats.append(int(monster[1]))
        monster_stats.append(monster[2])
        monster_pos = [int(x) for x in monster[3].split(",")]
        monster = Creature(monster_stats[0], monster_stats[1], monster_stats[2], monster_pos)
        monsters.append(monster)
    N_items = int(input())
    items = []
    for i in range(N_items):
        item = input().split()
        item_pos =[int(x) for x in item[2].split(",")]
        item_stat = int(item[3])
        item = Item(item[0], item[1], item_pos, item_stat)
        items.append(item)
    dungeon.update_matrix(exit_pos[0], exit_pos[1], "*")
    update_positions()
    
    #Starting the game
    game_ended = 0
    Link_last_line = 0
    while game_ended != 1 and Link._type == "P":
        #Movement phase
        if Link._pos[0] == dungeon.max_x - 1:
            Link_last_line = 1
        if Link_last_line == 0:
            Link.move_down()
        else:
            Link.natural_movement()
        for i in monsters:
            i.natural_movement()
        if Link._pos == exit_pos:
                game_ended = 1

        #Items phase
        for i in list(items):
            if i._pos == Link._pos and game_ended == 0:
                if i.type == "v":
                    Link.update_life(i.stats)
                    print("[", i.type, "]Personagem adquiriu o objeto ", i.name, " com status de ", i.stats, sep="")
                    items.remove(i)
                else:
                    Link.update_damage(i.stats)
                    print("[", i.type, "]Personagem adquiriu o objeto ", i.name, " com status de ", i.stats, sep="")
                    items.remove(i)
        
        #Combat phase
        for i in list(monsters):
            if i._pos == Link._pos and Link._type == "P" and game_ended == 0:
                print("O Personagem deu ", min(i.health, Link.damage), " de dano ao monstro na posicao (", i._pos[0], ", ", i._pos[1], ")", sep="")
                i.update_life(-Link.damage)
                if i.health <= 0:
                    monsters.remove(i)
                else:
                    print("O Monstro deu ", min(Link.health, i.damage), sep="", end="")
                    Link.update_life(-i.damage)
                    print(" de dano ao Personagem. Vida restante = ", max(0, Link.health), sep="")
                if Link.health <= 0:
                    Link._type = "X"

        update_positions()
        if Link._pos == exit_pos:
                game_ended = 1
                print("Chegou ao fim!")
