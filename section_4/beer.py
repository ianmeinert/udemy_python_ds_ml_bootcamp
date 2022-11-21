def sing(num_bottles):
    song = []
    n = num_bottles
    while n <= num_bottles:
        if n == 0:
            break
        if n > 1:
            msg1 = str(n) + ' bottles of beer on the wall, ' + \
                str(n) + ' bottles of beer.'
            song.append(msg1)
        elif n == 1:
            msg1 = str(n) + ' bottle of beer on the wall, ' + \
                str(n) + ' bottle of beer.'
            song.append(msg1)

        n = n - 1
        if n > 1:
            msg2 = 'Take one down and pass it around, ' + \
                str(n) + ' bottles of beer on the wall.'
            song.append(msg2)
        elif n == 1:
            msg2 = 'Take one down and pass it around, ' + \
                str(n) + ' bottle of beer on the wall.'
            song.append(msg2)
        elif n == 0:
            msg2 = 'Take it down and pass it around, ' + \
                str(n) + ' bottles of beer on the wall.'
            song.append(msg2)
        song.append('')

    return song


print(sing(99))
