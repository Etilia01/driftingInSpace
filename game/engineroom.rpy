label engineroomafterwaiting:
    "You enter the engine room."
    y "What-!?"
    "In front of you, on the ground, lies a man in an important looking uniform."
    "The captain, you assume."
    "And lets just say he doesnt look very healthy right now."
    "As you look up at the rest of the room, you can see that there seems to be loose cables hanging out of a corner at the ceiling, and the engine controls in the middle of the room look strangely damaged."
    "It looks almost as if they exploded, pieces shattered all around the room."
    "Its also getting harder to breathe, altough there is barely any visible smoke."
    char3 "Why are you just standing there!?"
    "Scienceguyplaceholder rushes towards the man lying on the floor, frantically trying to check his pulse."
    char3 "Shit how do I do this???"
    "You decide to go help after all."
    "As you hold your fingers to his wrist you can feel the faintest pulse."
    "He seems to be breathing as well."
    y "He's alive, its ok."
    y "How about we try to get him out of this room, inhaling whatever gas is in the air here cant be good for either of us."
    char3 "That- thats a good idea."
    "He looks like he's about to cry. Understandable. You yourself feel very uncomfortable with this situation."
    "You manage to drag the mans body out of the engine room together. Well, you did most of the work in the end."
    if mean <=1:
        "But you cant really hold it against scienceguyplaceholder. He doesnt seem very physically strong anyway, and he's not in the best mental state right now."
    "You take a deep breath trying to focus and figure out what to do now."
    captain "Wren...?"
    "The captain seems to be awake."
    char3 "Good afternoon sir, I am scienceguy. [name] and me found you passed out in the engine room, do you know what happened?"
    captain "Passed out...? OH NO!"
    "He jolts upright, grabbing scienceguys arm."
    captain "Theres a saboteur on board, they attacked Amelia and Parker! You have to tell Wren, they need to know! Have her get the passengers to the escape pods, and I'll go after the saboteur!"
    "He tries to get up, but doubles over in pain almost immediately."
    char3 "This might be bad timing... But who are these people youre talking about...?"
    "It takes the captain a minute to be able to talk again."
    captain "Ah... Youre passengers, right? Of course you cant know that..."
    captain "My apologies."
    captain "The people that I was looking for here, Amelia and Parker, are our technician and mechanic. Wren is our head of security, they should be guarding the bridge right now."
    captain "She's a good friend of mine, as such I dont want them to endanger themselves. But I am afraid I am currently unable to act as needed to get the situation under control myself."
    captain "So plan change - inform Wren of what happened, and let her decide how to handle it. But do warn them, the saboteur is armed with some sort of ranged weapon."
    menu:
        "We can go after the saboteur!":
            captain "You would do that...?"
            captain "Under normal circumstances I wouldnt allow it, but we cant lose any more time."
            captain "Sure, go after them. I suspect theyre trying to get to the power generator. Since they attacked the engine their goal must be to incapacitate the ship."
            "Tritici helps him get up, and the Captain starts walking towards the bridge."
            "He turns around once more."
            captain "What are you waiting for? Go!"
            "You start running towards the power generator room, or rather Tritici starts doing that, and you follow him, trusting him to know the right way."
            "The ship is relatively quiet, except for some of the lone passengers slowly coming out of their rooms again."
            "You arrive at the generator room. The door is closed."
            char3 "Its very calm here... Maybe they havent arrived yet?"
            y "Its probably been aboout an hour since what happened in the engine room, considering thats when the captain went there."
            y "They should already be here."
            jump end
        "We can go tell Wren!" if notdemo == 1:
            jump end
        "We dont even work here..." if notdemo == 1:
            jump end

label afterpowergen:
    
    y "Maybe there's a clue in what happened in the engine room..."
    "You walk back there to look at it."
    y "Hm... I know! Its..."
    menu:
        "...the engine":
            y "No, that cant be it..."
            jump end
        "...the blood":
            y "No, that cant be it..."
            jump end
        "...the cables":
            y "See those ripped out cables in the corner?"
            y "I bet that was a security camera!"
            y "Theyre all over the ship! We can use them to find the saboteurs location!"
            char3 "But why didnt the broken camera here for example alert Wren to the situation sooner?"
            y "The board computer is broken, remember? That was why the captain went looking for the technician in the first place."
            char3 "That makes sense. But then how are we going to access the cameras? The technician was kidnapped, she cant help us repair the computer."
            y "Arent you some sciency guy, cant you do it?"
            char3 "Im an agriculture expert."
            y "Oh."
            char3 "Oh indeed. Lets just go back to the bridge and see if theyve found a solution there."
            "The both of you rush back to the bridge, where you find an exhausted captain sitting inside the room."
            captain "Ah, hello. It turns out Ive sent you to the wrong place."
            "He gestures to the now (kind of) working screen next to him."
            captain "All cameras but these two are sending a signal."
            "He points towards one of them."
            captain "The engine room,"
            "He points towards the other."
            captain "the escape pods."
            char3 "That means?"
            captain "That means I have sent Wren and her colleagues there. We can do nothing but wait now."
            "You wait. After less than five minutes, one of the monitoring screens starts blinking red."
            "The captain sighs."
            "After about 40 minutes, an exhausted security guard enters the bridge."
            "Its Wren."
            jump end
           