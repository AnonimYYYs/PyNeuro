import neuro_lib_load

my_World = neuro_lib_load.World()
my_World.create_random_world(2, 3, 0.1)
my_World.print_ions()