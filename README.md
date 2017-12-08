DroneSim

A simulation for playing with drone based mesh networks. 

Requirements / Usage
===

python 2.*
pygame

Run example.py for an example.

To do / Ideas
===
High Priority
* New Classes
    - World: Class that contains information about world
    - Perspective: Class that holds rules, when applied to world it creates what the Drone sees
    - Drone: Class that is the drones
* Proper class structure for Drone class.
   - Things like x and y coordinates should be untouchable by subclasses.
   - Things that are marked for the user to control should be public.
   - Would help distinguish what's available for you to "use".

Low Priority
* Easy way to draw lines between drones.
* Simple example drones
    - Move towards others
    - Move away from others
* De/acceleration for drone movement.
    - Would make it more of a challenge/more realistic.

* Re-write in lisp ;)
