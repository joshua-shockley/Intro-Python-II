

# this is to setup a layout that will show up in the terminal

layouts = ['outside', 'foyer', 'overlook', 'narrow', 'treasure']


def the_layout(layouts):

    if layouts == "Outside Cave Entrance":
        fmt = '{:<3}{:<3}{:<3}{:<3}{:<3}'
        print(fmt.format('     ', '----', '|   |', '----', '     '))
        print(fmt.format('|----', '    ', '     ', '    ', '----|'))
        print(fmt.format('|    ', '    ', ' -8- ', '    ', '    |'))
        print(fmt.format('|    ', '    ', '     ', '    ', '    |'))
        print(fmt.format('|    ', '    ', '     ', '    ', '    |'))
        print(fmt.format('|    ', '    ', '     ', '    ', '    |'))
        print(fmt.format('|    ', '    ', '     ', '    ', '    |'))
        print(fmt.format('|    ', '    ', '     ', '    ', '    |'))

        return layouts


# below is my little local test to see how it shows up on the term
# print(the_layout('Outside Cave Entrance'))
