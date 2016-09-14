def say(num_beer, end):
    print(num_beer or '0','bottle'+('s' if num_beer-1 else ''), end)

for i in range(99, 0, -1):
    say(i, 'of beer on the wall,')
    say(i, 'of beer,')
    print('if one of those bottles should happen to fall')
    say(i-1, 'of beer on the wall.\n')
