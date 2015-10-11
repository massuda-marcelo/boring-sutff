#! python
#  encoding: utf-8

# Boring Stuff
# Ex 5-1 Fantasy game inventory

def display_inventory(inventory) :
    print('Inventory:')
    total = 0
    for k,v in inventory.items() :
        print(str(v) + ' ' + str(k))
        total += v
    print('Total number of items: ' + str(total))

def add_to_inventory(inventory, items_to_add) :
    for k in items_to_add :
        inventory[k] = inventory.get(k, 0) + 1
    return inventory

def test_display_inventory() :
    inventory = {
        'rope'      : 1,
        'torch'     : 6,
        'gold coin' : 42,
        'dagger'    : 1,
        'arrow'     : 12
    }
    display_inventory(inventory)

def test_add_to_inventory() :
    inventory = {
        'rope'      : 1,
        'gold coin' : 42
    }
    dragon_loot = [
        'gold coin',
        'dagger',
        'gold coin',
        'gold coin',
        'ruby'
    ]
    inventory = add_to_inventory(inventory, dragon_loot)
    display_inventory(inventory)

def main() :
    print('test_display_inventory')
    print()
    test_display_inventory()
    print()
    print('test_add_to_inventory')
    print()
    test_add_to_inventory()

if __name__ == '__main__':
    main()
