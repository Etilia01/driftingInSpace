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
    "Tritici rushes towards the man lying on the floor, frantically trying to check his pulse."
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
        "But you cant really hold it against Tritici. He doesnt seem very physically strong anyway, and he's not in the best mental state right now."
    "You take a deep breath trying to focus and figure out what to do now."
    captain "Wren...?"
    "The captain seems to be awake."
    char3 "Hi- Uh I mean good afternoon sir, I am Tritici. [name] and me found you passed out in the engine room, do you know maybe happen to know what happened?"
    captain "Passed out...? OH NO!"
    "He jolts upright, grabbing Triticis arm."
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
            char3 "Alright, then lets go in there!"
            "You open the door and step inside."
            "The room is empty. Except for the generator and various controlpanels of course."
            "Theres nobody inside, and everything seems like its running well."
            char3 "Thats weird."
            menu:
                "Maybe the captain was wrong?":
                    y "It could be that just rendering the ship unable to move wasnt their goal."
                    y "Can we guess where they went? Im assuming they went in this general direction, which is why the captain thought the power generator was where they were headed."
                    $ placeinput = renpy.input("Just where could they have gone...?").strip()
                    if placeinput == place:
                        jump end
                    else:
                        y "I have no idea..."
                        jump afterpowergen
                "Maybe theyre actually not here yet..." if notdemo == 1:
                    jump end
        "We can go tell Wren!" if notdemo == 1:
            jump end
        "We dont even work here...":
            char3 "...What?"
            y "Come on, dont pretend you actually want to play the hero here."
            y "Theres no way this will end well."
            if mean >=2:
                "This is so stupid. What do we care what happens to these people? We dont even know them. Honestly, for all I care they could suffocate in space."
                char3 "Thats- I dont think you should say things like that..."
            y "Either way, Im not helping."
            captain "That is your choice."
            captain "You are right, you have nothing to do with this. I sincerly apologise for trying to drag you into this debacle."
            captain "I have to admit that it is a bit disappointing how you dont want to help with something as harmless as delivering a message, but I understand where you are coming from with this decision."
            "Tritici helps him get up, and the captain slowly limps to the bridge."
            y "Well, I will be going back to my cabin."
            char3 "Good for you I guess. But Im going to try my best to help the captain."
            char3 "...Even if my best isnt a lot."
            "He walks over to the captain to help him. Thats the last you see of the two before you turn around and go to your cabin, where you spent the rest of the day, reading your favorite book."
            if mean <=0:
                "You feel a bit bad about not helping out, but quickly shake off that feeling. You probably werent even qualified to handle that kind of situation!"
            "After a few hours the ship starts moving again, and everything goes as planned from there on."
            "At dinner you hear something about the criminal who had sabotaged the engine escaping, but you dont pay much mind to it, and forget about it soon after."
            "You leave the ship at your planned stop a few days later, and never think back to this incident."
            "NEUTRAL ENDING 2: The best choice (for yourself)"
            jump end

label afterpowergen:
    y "Maybe there's a clue to what theyre trying to do in what happened in the engine room..."
    "You walk back there to look at the engine room again."
    y "Hm... I know! Its..."
    menu:
        "...the engine":
            y "No, that cant be it..."
            menu:
                "...the blood":
                    y "No, that cant be it..."
                    menu:
                        "...the cables":
                            jump cables
                "...the cables":
                    jump cables
        "...the blood":
            y "No, that cant be it..."
            menu:
                "...the engine":
                    y "No, that cant be it..."
                    menu:
                        "...the cables":
                            jump cables
                "...the cables":
                    jump cables
        "...the cables":
            jump cables
            
label cables:
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
    captain "Wren tried kicking it. Surprisingly, that worked."
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
    char2 "Both Amelia and Parker are doing well- or as well as possible in this situation."
    captain "Thats good to hear. But I assume the saboteur got away?"
    char2 "They did, Im sorry."
    captain "Its fine. The most important thing is that everyone is safe now. Please go to the medical station and get yourself checked. While youre there, tell Amelia to come here once she's feeling good enough."
    char3 "So what now?"
    captain "Now Amelia will try to fix the boardcomputer so that we can ask ground to send help. You two can go back to whatever you were doing before. Thank you for trying to help though."
    "Tritici and you go back to the sections of the ship accessible to passengers."
    "The rest of your travels go relatively uneventful, and you arrive safely at your destination."
    "NEUTRAL ENDING 3: What great help you were."
    "Epilogue coming soon!"
    jump end
    
    


label engineroomearly:
    "You arrive at the engine room."
    "Through the closed door you can hear a loud noise. It almost sounds like an explosion."
    char3 "Whats going on here!?"
    "He rushes towards the door, and hits the button to open it."
    "You go after him."
    unknown "Dont come closer!"
    "And come face to face with the barrel of a gun."
    "Taking a quick look around the room you notice a man in uniform lying on the ground, presumably the captain."
    "In the corner of the room you see two people in quite similar get-up, just lacking some decorations on their uniforms. Likely the technician and mechanic."
    "One of the two gestures in your direction, maybe trying to get you to talk to the person in the middle of the room threatening you?"
    menu:
        "Try to talk to them":
            y "What are you trying to do here?"
            unknown "I just want to leave. Just follow my instructions and you'll be fine."
            "The woman that gestured to you now slowly moves behind the (heavily damaged) engine and slowly works on removing a steel pipe thats attached to it."
            menu:
                "Keep talking to distract them":
                    y "May I ask who you are?"
                    unknown "I suppose you can think of me as Erika Mustermann."
                    y "And why are you threatening us?"
                    muster "You three-"
                    "She points to the captain, Tritici and you."
                    muster "Bad time, wrong place. These guys behind me, I need their help starting the escape pods. Theyre locked for some reason."
                    "You nod."
                    y "The quarantine."
                    muster "The what now?"
                    y "Thats what the alarm was for, were quarantined for some reason. Of course we cant leave then."
                    muster "Ah... That was not what I assumed it was. Either way, I NEED to leave right now."
                    muster "So if you'd let me and these technology people through now..."
                    y "Alright, but tell me first, why do you need to leave?"
                    muster "How's that any of your business?"
                    y "Im just curious."
                    muster "I may not be that popular with authoritys. And when i heard the alarm I assumed that I was why it rang."
                    muster "Satisfied with the answer or not, MOVE!"
                    "And right as she says that, she's hit on the head with a steel pipe"
                    "And falls over, dropping the gun."
                    "Tritici reacts quickly, seizing the gun and pointing it at her just in case she gets up again, while the young woman that knocked her out ties her to whats left of the engine."
                    "After she's done with that, she introduces herself."
                    tech "Hi, Im Amelia, the ships head technician. Thank you for distracting her. Would you mind standing guard here while Parker, our mechanic, and I bring the captain to the medical station?"
                    char3 "Sure, were happy to help. But could you please send over some security personell as well?"
                    char3 "Im a bit concerned about her waking up..."
                    tech "That was the plan."
                    "She smiles warmly."
                    tech "But we cant leave her alone while we wait for them to arrive, so it would be nice of you to keep an eye on her until then."
                    tech "See you later."
                    "She picks up the captain by his arms, and Parker comes over to lift his legs. Together they haul him out the door."
                    "You wait, occasionally glancing nervously at Mustermann, but she doesnt seem to be waking up anytime soon."
                    "After a while the security guard you met at the bridge enters the room with a small team, introducing herself as Wren, and telling you to go walk to the medical station to get a checkup, sice you werent needed here anymore."
                    "You did just that. As expected, both of you were fine, altough Tritici was still a bit shaken, and you were sent back to your cabins."
                    "It took less then a day for the interdimensional police to arrive and arrest the criminal. Apparently they had been looking for her for quite a while, since she had ties to various illegal weapon smuggling operations, and had been illegally working as a well known mercenary for years."
                    "They had suspected she was on the ship, hoping a quarantine would prompt her to drop her disguise, but didnt expect to lose contact to the ship and their internal agent before they could inform the crew of this plan."
                    "Both Tritici and you were interviewed as witnesses and awarded a small monetary prize for the role you played in capturing her."
                    "They left again, and you dont expect to hear any more of this case."
                    "GOOD ENDING 1: SUCESSFUL ARREST"
                    "Epilogue coming soon."
                    jump end
                "Try to disarm the person threatening you":
                    "You move closer and reach for their gun."
                    "They move back a little, panicking and pulling the trigger."
                    "The people around you watch in shock as you fall over on your back, and the light leaves your eyes."
                    "BAD ENDING 1: Not an action movie hero"
                    jump end
                "Seek cover" if notdemo == 1:
                    jump cover
                "Try to signal that youre harmless and are going to surrender & cooperate" if notdemo == 1:
                    jump end

            jump end
        "Try to get closer and disarm them":
            "You move closer and reach for their gun."
            "They move back a little, panicking and pulling the trigger."
            "The people around you watch in shock as you fall over on your back, and the light leaves your eyes."
            "BAD ENDING 1: Not an action movie hero"
            jump end
        "Try to move out of the room and seek cover" if notdemo == 1:
            jump cover

label cover:
    "You slowly walk backwards and turn around the corner, seeking cover behind the doorframe."
    muster "What do you think youre doing!?"
    y "Not getting shot?"
    muster "Ah..."
    muster "Well-"
    muster "Well come back here!"
    muster "I need to see what youre doing!"
    menu:
        "Try to call help":
            jump end
        "Leave to get help":
            jump end
        "Look for a weapon":
            jump end