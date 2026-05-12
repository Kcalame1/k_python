# Reflection

## What part of the project was hardest?
The hardest part was building the purchase order system and making sure inventory updates correctly when a shipment is received. Organizing the program into multiple files was also challenging at first.

## What bug took the longest to solve?
The longest bug was duplicate receiving of purchase orders. Inventory was increasing more than once, so I fixed it by checking if the purchase order was already marked as RECEIVED before updating inventory.

## How did you organize your code across multiple files?
I separated the program by purpose. main.py handles menus, models.py has the classes, inventory_manager.py has main functions, file_manager.py handles saving/loading JSON, and reports.py handles reports.

## How does your save/load system work?
The program saves data by converting objects into dictionaries and writing them to JSON files. When loading, it reads the JSON files and recreates the objects.

## What would you improve if you had another week?
I would improve the menu design, add automatic purchase order numbers, and add more detailed reports.
