label nah:
    scene bg hallway1
    "You decide that has nothing to do with you and quietly leave the hall."
    menu:
        "Try to figure out more about the situation" if notdemo==1:
            jump end
        "Go back to your cabin and wait on more info":
            scene black with fade
            centered "You wander around a bit until you decide to go back to your cabin and spend some time reading there."
            centered "After a few hours the ship starts moving again, and everything goes smoothly from there."
            centered "At dinner you hear something about some kind of escaped criminal, but it seems they have already left the ship, so you dont worry too much."
            centered "NEUTRAL ENDING 1: Kept to yourself"
            jump end
        "Explore the ship and wait on more info" if notdemo==1:
            jump end
