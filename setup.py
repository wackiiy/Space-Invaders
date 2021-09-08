import cx_Freeze

executables = [cx_Freeze.Executable("game.py")]

cx_Freeze.setup(
    name="Space Invaders",
    options={"build_exe": {"packages":["pygame","math","random"],
                           "include_files":["background.png","background.wav","bullet.png","enemy.png","explosion.wav","laser.wav","logo.png","player.png"]}},
    executables = executables

    )
