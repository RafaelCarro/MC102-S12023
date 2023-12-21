def damage_done(fx, fy, cx, cy, max_monster_dmg, monster_weakness, arrow_type) -> int:
    '''
    Gets the damage done by Aloy on the monster based on their type and crit spots.
    '''
    if monster_weakness == "todas" or monster_weakness == arrow_type:
        return max(0, max_monster_dmg - (abs(cx -fx) + abs(cy-fy)))
    else:
        return max(0, (max_monster_dmg - (abs(cx -fx) + abs(cy-fy)))//2)


if __name__ == "__main__":
    #Inputs
    aloy_hp = int(input())
    aloy_max_hp = aloy_hp
    arrows = input().split()
    arrows_keys = []
    arrows_qtd = []
    qtd_arrows = 0
    for i in range(len(arrows)):
        if i % 2 == 0:
            arrows_keys.append(arrows[i])
        else:
            arrows_qtd.append(int(arrows[i]))
            qtd_arrows += int(arrows[i])
    aloy_arrows = dict(zip(arrows_keys, arrows_qtd))
    qtd_enemies = int(input())
    n_battle = 0
    while qtd_enemies > 0:
        qtd_enemies_in_battle = int(input())
        enemies_in_battle = []
        for i in range(qtd_enemies_in_battle):
            enemy = {}
            enemy_string = input().split()
            enemy["hp"] = int(enemy_string[0])
            enemy["atk"] = int(enemy_string[1])
            enemy_qtd_parts = int(enemy_string[2])
            enemy_parts = {}
            for j in range(enemy_qtd_parts):
                part_string = input().split(", ")
                part = {}
                part["weakness"] = part_string[1]
                part["max_dmg"] = int(part_string[2])
                part["cx"] = int(part_string[3])
                part["cy"] = int(part_string[4])
                enemy_parts[part_string[0]] = part
            enemy["parts"] = enemy_parts
            enemies_in_battle.append(enemy)
        
        #Combat Phase
        while len(enemies_in_battle) > 0:
            print("Combate ", n_battle, ", vida = ", aloy_hp, sep= "")
            used_arrows = dict.fromkeys(aloy_arrows, 0)
            crits = []
            for i in range(len(enemies_in_battle)):
                crits.append({})
                for j in enemies_in_battle[i]["parts"]:
                    crit_pos = (enemies_in_battle[i]["parts"][j]["cx"], enemies_in_battle[i]["parts"][j]["cy"])
                    crits[i][crit_pos] = 0
            arrow_count = 0
            dead_enemies = 0
            defeated_enemies = []
            while len(enemies_in_battle) > 0:
                enemies_numbers = len(enemies_in_battle)
                try:
                    attack = input().split(", ")
                except:
                    pass
                attack[0] = int(attack[0])
                attack[3] = int(attack[3])
                attack[4] = int(attack[4])
                current_attack = damage_done(attack[3],
                                            attack[4],
                                            enemies_in_battle[attack[0]]["parts"][attack[1]]["cx"],
                                            enemies_in_battle[attack[0]]["parts"][attack[1]]["cy"],
                                            enemies_in_battle[attack[0]]["parts"][attack[1]]["max_dmg"],
                                            enemies_in_battle[attack[0]]["parts"][attack[1]]["weakness"],
                                            attack[2])
                enemies_in_battle[attack[0]]["hp"] -= current_attack
                used_arrows[attack[2]] += 1
                arrow_count += 1
                if (attack[3] == enemies_in_battle[attack[0]]["parts"][attack[1]]["cx"]
                    and attack[4] == enemies_in_battle[attack[0]]["parts"][attack[1]]["cy"]):
                    crit_pos = (attack[3], attack[4])
                    crits[attack[0]][crit_pos] += 1
                if enemies_in_battle[attack[0]]["hp"] <= 0:
                    print("Máquina", attack[0], "derrotada")
                    qtd_enemies -= 1
                    dead_enemies += 1
                    defeated_enemies.append(enemies_in_battle[attack[0]])
                    if dead_enemies == enemies_numbers:
                        enemies_in_battle.clear()
                if arrow_count == 3:
                    for j in range(len(enemies_in_battle)):
                        if enemies_in_battle[j] not in defeated_enemies:
                            aloy_hp -= enemies_in_battle[j]["atk"]
                    arrow_count = 0
                if aloy_hp <= 0:
                    print("Vida após o combate =", max(aloy_hp, 0))
                    print("Aloy foi derrotada em combate e não retornará a tribo.")
                    exit()
                if used_arrows == aloy_arrows:
                    print("Vida após o combate =", max(aloy_hp, 0))
                    print("Aloy ficou sem flechas e recomeçará sua missão mais preparada.")
                    exit()
            print("Vida após o combate =", max(aloy_hp, 0))
            print("Flechas utilizadas:")
            for i in used_arrows:
                if used_arrows[i] != 0:
                    print("- ", i, ": ", used_arrows[i], "/", aloy_arrows[i], sep= "")
            crit_flag = 0
            for i in range(len(crits)):
                for j in crits[i]:
                    if crits[i][j] != 0:
                        crit_flag = 1
            if crit_flag == 1:
                print("Críticos acertados:")
            for i in range(len(crits)):
                crits_printed = 0
                for j in crits[i]:
                    if crits[i][j] != 0 and crits_printed == 0:
                        print("Máquina ", i, ":", sep= "")
                        crits_printed = 1
                for j in crits[i]:
                    if crits[i][j] != 0:
                        print("- ", j, ": ", crits[i][j], "x", sep= "")
            aloy_hp = min(aloy_max_hp, int(0.5 * aloy_max_hp + aloy_hp))
            n_battle += 1
    print("Aloy provou seu valor e voltou para sua tribo.")