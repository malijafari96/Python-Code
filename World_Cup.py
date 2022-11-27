win_iran = win_spain = win_portugal = win_morocco = 0
draw_iran = draw_spain = draw_portugal = draw_morocco = 0
lost_iran = lost_spain = lost_portugal = lost_morocco = 0

iran_spain = input().split('-')
if int(iran_spain[0]) > int(iran_spain[1]):
    win_iran += 1
    lost_spain += 1
if int(iran_spain[0]) < int(iran_spain[1]):
    win_spain += 1
    lost_iran += 1
if int(iran_spain[0]) == int(iran_spain[1]):
    draw_iran += 1
    draw_spain += 1

iran_portugal = input().split('-')
if int(iran_portugal[0]) > int(iran_portugal[1]):
    win_iran += 1
    lost_portugal += 1
if int(iran_portugal[0]) < int(iran_portugal[1]):
    win_portugal += 1
    lost_iran += 1
if int(iran_portugal[0]) == int(iran_portugal[1]):
    draw_iran += 1
    draw_portugal += 1

iran_morocco = input().split('-')
if int(iran_morocco[0]) > int(iran_morocco[1]):
    win_iran += 1
    lost_morocco += 1
if int(iran_morocco[0]) < int(iran_morocco[1]):
    win_morocco += 1
    lost_iran += 1
if int(iran_morocco[0]) == int(iran_morocco[1]):
    draw_iran += 1
    draw_morocco += 1

spain_portugal = input().split('-')
if int(spain_portugal[0]) > int(spain_portugal[1]):
    win_spain += 1
    lost_portugal += 1
if int(spain_portugal[0]) < int(spain_portugal[1]):
    win_portugal += 1
    lost_spain += 1
if int(spain_portugal[0]) == int(spain_portugal[1]):
    draw_spain += 1
    draw_portugal += 1

spain_morocco = input().split('-')
if int(spain_morocco[0]) > int(spain_morocco[1]):
    win_spain += 1
    lost_morocco += 1
if int(spain_morocco[0]) < int(spain_morocco[1]):
    win_morocco += 1
    lost_spain += 1
if int(spain_morocco[0]) == int(spain_morocco[1]):
    draw_spain += 1
    draw_morocco += 1

portugal_morocco = input().split('-')
if int(portugal_morocco[0]) > int(portugal_morocco[1]):
    win_portugal += 1
    lost_morocco += 1
if int(portugal_morocco[0]) < int(portugal_morocco[1]):
    win_morocco += 1
    lost_portugal += 1
if int(portugal_morocco[0]) == int(portugal_morocco[1]):
    draw_portugal += 1
    draw_morocco += 1

iran_points = win_iran*3 + draw_iran*1
spain_points = win_spain*3 + draw_spain*1
portugal_points = win_portugal*3 + draw_portugal*1
morocco_points = win_morocco*3 + draw_morocco*1

iran_scored = int(iran_spain[0]) + int(iran_portugal[0]) + int(iran_morocco[0])
iran_concede = int(iran_spain[1]) + \
    int(iran_portugal[1]) + int(iran_morocco[1])
iran_differ = iran_scored - iran_concede

spain_scored = int(iran_spain[1]) + \
    int(spain_portugal[0]) + int(spain_morocco[0])
spain_concede = int(iran_spain[0]) + \
    int(spain_portugal[1]) + int(spain_morocco[1])
spain_differ = spain_scored - spain_concede

portugal_scored = int(
    iran_portugal[1]) + int(spain_portugal[1]) + int(portugal_morocco[0])
portugal_concede = int(
    iran_portugal[0]) + int(spain_portugal[0]) + int(portugal_morocco[1])
portugal_differ = portugal_scored - portugal_concede

morocco_scored = int(iran_morocco[1]) + \
    int(spain_morocco[1]) + int(portugal_morocco[1])
morocco_concede = int(iran_morocco[0]) + \
    int(spain_morocco[0]) + int(portugal_morocco[0])
morocco_differ = morocco_scored - morocco_concede

total = [('Iran', win_iran, lost_iran, draw_iran, iran_differ, iran_points),
         ('Spain', win_spain, lost_spain, draw_spain, spain_differ, spain_points),
         ('Portugal', win_portugal, lost_portugal,
          draw_portugal, portugal_differ, portugal_points),
         ('Morocco', win_morocco, lost_morocco, draw_morocco, morocco_differ, morocco_points)]

sorted_total = sorted(total, key=lambda x: (-x[5], x[1], x[0]))

for i in range(0, 4):
    result = ' '.join(map(str, sorted_total[i]))
    result = result.split()
    print('%s  wins:%s , loses:%s , draws:%s , goal difference:%s , points:%s' % (
        result[0], result[1], result[2], result[3], result[4], result[5]))
