label bridge:
    "You leave the main hall and walk somewhere in the general direction of the bridge."
    "the silence feels a bit akward"
    menu:
        "Try to talk to Tritici":
            jump smalltalk
        "Stay silent":
            jump silent
            
label smalltalk:
    y "So, why are you traveling with this ship?"
    if mean >=2:
        jump silent
    show tritici idle front
    char3 "Im on my way to a meetup with fellow biologists on planetx. Its really cool, its one of the biggest science conventions in our galaxy!"
    char3 "Its the first time ive ever gone, and Ive been invited to an exclusive meetup too!"
    y "Oh wow. What do you do for work to get invited to something like that?"
    show tritici happy 2
    char3 "Im an agriculture expert! Its always been a major interest of mine. "
    char3 "I have my own private radio station where I talk about it too! Thats how I got invited, a pretty important person listened to it and decided my research was interesting enough to allow me to attend!"
    y "Sounds really interesting!"
    show tritici happy 1
    char3 "Where are you going?"
    menu:
        "The same convention actually!":
            show tritici happy 2
            char3 "What really!? Thats so cool!"
            if jokester >=2:
                char3 "We should hang out there too!"
                show tritici idle front
                char3 "Uh- that is, if you dont have friends waiting for you there of course. You dont have to."
                char3 "But youve been really fun to talk to so far and Im honestly kind of scared to be alone there... So id be very happy if you tagged along!"
                char3 "Im not trying to force you to spend time with me, I totally understand if you dont want to. Were not friends or anything after all, we just met."
                menu:
                    "Why not? (Join him at the convention once you get there)":
                        $ scientistlikes +=1
                        show tritici happy 2
                        char3 "Yay! Thank you so much, I promise it will be fun!!"
                        jump talkbridge
                    "I dont really want to.":
                        show tritici idle 1
                        char3 "Oh, ok. Thats fine."
                        jump talkbridge
            else:
                char3 "Im sure its going to be really fun!"
                y "From what ive heard, it definitely will be!"
                jump talkbridge
        "Im visiting family.":
            show tritici happy 1
            char3 "Oh thats nice."
            char3 "Always good to visit from time to time hm?"
            jump talkbridge
        "Going on vacation!":
            show tritici happy 1
            char3 "Oh cool! Where are you going exactly?"
            menu:
                "Somewhere warm":
                    jump warm_vac
                "Somewhere cold":
                    jump cold_vac
                "Somewhere to go shopping":
                    jump shopping
                "Somewhere to go sight-seeing":
                    jump sightseeing
        "Going home after a worktrip":
            char3 "Ah how nice."
            char3 "You must be exhausted after travelling for work. Are you happy to go home again?"
            menu:
                "Yes":
                    char3 "Understandable. Fortunately I dont really travel for my work like... at all usually, it sounds very stressful."
                    jump talkbridge
                "No":
                    show tritici idle 1
                    char3 "Oh... Thats unfortunate?"
                    jump talkbridge
label cold_vac:
    y "Im traveling to an ice-planet for vacation. I like wintersports a lot, so that was the perfect vacation!"
    show tritici happy 2
    char3 "Oh, thats cool. Literally, haha. Im a fan of cold places too, I just love the snow so much!"
    $ scientistlikes +=1
    jump talkbridge
label warm_vac:
    y "Im traveling to a pretty warm planet to go on a beach vacation! I love to swim, and just like how cozy warm weather feels."
    char3 "Ah, I cant relate. I dislike even the warm seasons on my homeplanet, and thats a pretty cold world in relation to some of these vacation planets..."
    if mean <=0:
        show tritici idle 1
        char3 "What matters most is that you like it of course, its your vacation after all. I dont know why I thought it was appropriate to comment on that, im so sorry!"
    jump talkbridge
label shopping:
    y "Im going to a major city on a rich planet in the main trade regions to go on a few shopping trips! I saved up for that for a while!"
    char3 "That would be way too crowded for me."
    if mean <=0:
        char3 "But I hope you find the things youre looking for!"
    jump talkbridge
label sightseeing:
    y "I want to go sightseeing! Like going to museums and looking at cool buildings! So I decided to visit a planet with well preserved history, and a thriving economy."
    char3 "Oh that sounds super fun! Im not the biggest fan of museums, I personally just dont like the weird sterile atmosphere a lot of them have, but I always like to look at cool public art outside like statues and fountains in the city!"
    if mean <=0:
        show tritici happy 2
        char3 "I highly recommend a visit to Ahujift if youre interested in these kinds of things, thats a city on Tedow with beautiful fountains. Theyre all public and free to visit, and have a really interesting design concept!"
    jump talkbridge

label silent:
    show tritici idle 1
    "The akward silence persists..."
    "After what feels like an eternity, you finally arrive at the bridge."
    jump bridgeoutside

label talkbridge:
    if scientistlikes>=2:
        "After a very nice conversation, you arrive at the bridge!"
    else:
        "After a short conversation, you arrive at the bridge!"
    jump bridgeoutside



label bridgeoutside:
    scene bg wrenencounter with dissolve
    "Or rather outside the bridge. Your way is being blocked by a very serious looking security person."
    scene bg door2
    show tritici idle 1 at left
    show wren neutral at right
    char2 "Stop right there."
    char2 "Why are you here?"
    show wren neutral 2 at right
    char3 "We had hoped to find ship staff to ask about the quarantine."
    show tritici idle 2 at left
    char2 "Quarantine? What do you mean by that?"
    char3 "After the alarm just now, there was an announcement in the main hall about how were quarantined now for some reason."
    char3 "We dont know why, so we want to talk to someone who does. Which apparently isnt you."
    char2 "No need to be so rude."
    char3 "I wasnt trying to be, sorry!"
    char2 "Apology accepted. Sorry I couldnt help you."
    char3 "Well see, you could! Just let us talk to the captain or something."
    char2 "Im afraid youre not authorized to do that."
    char2 "And even if you were, the captain isnt here right now."
    char3 "Where are they then?"
    char2 "Im not sure if I can tell you that."
    jump convincethem

label convincethem:
    if convincesecurityfail == 2:
        char2 "Look, I dont think were getting anywhere with this."
        char2 "I have to ask you to leave. If you dont do it on your own, I will have to use force."
        char3 "Were so so sorry, of course well leave!"
        "(Because this is a demo and there is no other route right now, you get another try. Use it wisely)"
        $ convincesecurityfail = 0
        jump convincethem
    else:
        menu:
            "Its an emergency, so it should be fine.":
                char2 "Well. I guess it is..."
                char2 "Fine."
                char2 "The board computer had a malfunction, so he went to get our main technician to fix it."
                char2 "He's been gone for quite some time now, so he should get back soon."
                char3 "Alright, then we'll wait here with you."
                menu:
                    "Wait":
                        "You wait..."
                        "And wait..."
                        "And end up waiting for more than an hour."
                        char2 "That is strange..."
                        char2 "You two, can you go look for the captain?"
                        char2 "Im not allowed to leave my post, but Im very worried about him."
                        char2 "He said hed only be away for 15 minutes, normally he would have called already to tell me that it will take him longer."
                        char3 "What could have gone wrong?"
                        char2 "Im not sure."
                        char3 "I dont know if we can go look for him... What if something REALLY bad happened? Arent you more qualified to deal with that?"
                        char2 "I would, but as said, I cant leave. Also, I dont think its that bad. The worst that could have happened would be a medical emergency, and thats not a danger to you."
                        char2 "And if it was that bad, it would be even more important for you to get there as fast as possible."
                        char3 "Hm. What do you think [name]?"
                        menu:
                            "We should go look for him.":
                                char3 "If you say so... Ok."
                                char3 "Where do we need to go?"
                                char2 "The captain should be in the engine room."
                                char2 "Apparently there was a minor malfunction there, so thats where the technician and our mechanic went, and where our captain searched for them."
                                char3 "Alright, then lets go!"
                                jump waytoengineroom
                            "No, thats their job, not ours." if notdemo == 1:
                                char3 "Youre right. Im sorry, but I dont think were qualified at all!"
                                char3 "What if we mess something up?"
                                char3 "Wouldnt there be issues with insurance too? I dont want to get sued or something!"
                                char2 "Alright, yes that makes sense."
                                char2 "Then just try not to let anyone in here until the next guard is here."
                                "With that, she leaves her post."
                                "You stay there for a while longer. After a bit another security guard arrives."
                                "You dont really see what else you can do here, and walk back to the main hall."
                                char3 "We still havent found out what the quarantine was about..."
                                y "I think the bridge staff is a little uh... busy right now, so do we know about anyone else we could ask?"
                                
                                jump end
                    "Go get the captain":
                        char3 "Where do we need to go?"
                        char2 "The captain should be in the engine room."
                        char2 "Apparently there was a minor malfunction there, so thats where the technician and our mechanic went, and where our captain searched for them."
                        char3 "Alright, then lets go!"
                        jump waytoengineroom2
            "We're staff actually.":
                char2 "Then show me your ids please."
                char3 "AAAH Im so sorry, [pronoun1] [ist] just joking!"
                char3 "We're just guests!"
                char2 "How funny. Well, then I certainly cant tell you."
                $ convincesecurityfail +=1
                jump convincethem
            "I work here actually. Just me, not this guy here.":
                char2 "I would need to see your ID then."
                y "Of course... If only I hadnt lost it!"
                char2 "Lost it?"
                y "Yes, I think I forgot it in the main hall. How stupid of me."
                char2 "Then go get it...?"
                y "I will!"
                "You confidently turn around and start making your way back."
                "Tritici sprints after you."
                char3 "What do you mean lost it? You dont work here, do you?"
                y "I dont. But do they really need to know that?"
                char3 "How are you going to 'prove' that you work here then?"
                char3 "You dont have an ID!"
                if scientistlikes>=2:
                    "I dont want you to get in trouble!"
                menu:
                    #"It will be fine":
                        #jump end
                    "Youre right, what was I thinking?":
                        "You turn back and walk back to the door."
                        y "So... That was a joke."
                        char2 "What?"
                        y "I dont actually work here."
                        char2 "Ah. Very funny."
                        $ convincesecurityfail +=1
                        jump convincethem
                jump end
            "If we ask you very nicely?":
                char2 "No. Absolutely not"
                $ convincesecurityfail +=1
                jump convincethem
            "Nobody has to know...":
                char2 "I would like to keep my job, actually."
                char2 "Please leave."
                $ convincesecurityfail +=1
                jump convincethem
    
label waytoengineroom:
    "You make your way to the engine room."
    y "How do you know where we need to go?"
    char3 "Im always really anxious about getting lost, because I'd be way to scared to ask for help, so I have the layout memorized."
    char3 "And even if I didnt, I have some of these little flyers they had lying around at checkin with me, those also have a small map."
    char3 "Do you want one?"
    menu:
        "Yes":
            char3 "Ok, here you go!"
            if mean <=1:
                y "Thank you!"
            $ hasflyer = 1
            "You put the flyer in your pocket."
            $ renpy.notify("From now on, you can open the flyer using the button on the lower middle-left. This can be helpful in the epilogue, depending on which you unlocked.")
            char3 "Alright, lets continue to the engine room!"
                
            jump continuetoroom
        "No":
            char3 "Ok. Tell me if you change your mind later."
            y "I will, thanks."
            jump continuetoroom
label waytoengineroom2:
    "You make your way to the engine room."
    y "How do you know where we need to go?"
    char3 "Im always really anxious about getting lost, because I'd be way to scared to ask for help, so I have the layout memorized."
    char3 "And even if I didnt, I have some of these little flyers they had lying around at checkin with me, those also have a small map."
    char3 "Do you want one?"
    menu:
        "Yes":
            char3 "Ok, here you go!"
            if mean <=1:
                y "Thank you!"
            $ hasflyer = 1
            "You put the flyer in your pocket."
            $ renpy.notify("From now on, you can open the flyer using the button on the lower middle-left.\nThis can be helpful in the epilogue, depending on which you unlocked.")
            char3 "Alright, lets continue to the engine room!"
                
            jump engineroomearly
        "No":
            char3 "Ok. Tell me if you change your mind later."
            y "I will, thanks."
            jump engineroomearly
label continuetoroom:
    "You finally arrive at the engine room, and immediately notice that something is wrong."
    "The door is wide open, but you cant hear anything from the inside."
    "Even if the engine was silent somehow, you should at least hear the three people who should be inside the room, shouldnt you?"
    char3 "Something feels off..."
    char3 "Are you sure we should go in there...?"
    menu:
        "Go inside the engine room":
            jump engineroomafterwaiting
        "Go get the security guard for help" if notdemo == 1:
            jump end