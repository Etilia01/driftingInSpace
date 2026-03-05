label bridge:
    "You leave the main hall and walk somewhere in the general direction of the bridge."
    "the silence feels a bit akward"
    menu:
        "Try to talk to ScienceGuyPlaceholder":
            jump smalltalk
        "Stay silent":
            jump silent
            
label smalltalk:
    y "So, why are you traveling with this ship?"
    if mean >=2:
        jump silent
    char3 "Im on my way to a meetup with fellow biologists on planetx. Its really cool, its one of the biggest science conventions in our galaxy!"
    char3 "Its the first time ive ever gone, and Ive been invited to an exclusive meetup too!"
    y "Oh wow. What do you do for work to get invited to something like that?"
    char3 "Im an agriculture expert! Its always been a major interest of mine. "
    char3 "I have my own private radio station where I talk about it too! Thats how I got invited, a pretty important person listened to it and decided my research was interesting enough to allow me to attend!"
    y "Sounds really interesting!"
    char3 "Where are you going?"
    menu:
        "The same convention actually!":
            char3 "What really!? Thats so cool!"
            if jokester >=2:
                char3 "We should hang out there too!"
                char3 "Uh- that is, if you dont have friends waiting for you there of course. You dont have to."
                char3 "But youve been really fun to talk to so far and Im honestly kind of scared to be alone there... So id be very happy if you tagged along!"
                char3 "Im not trying to force you to spend time with me, I totally understand if you dont want to. Were not friends or anything after all, we just met."
                menu:
                    "Why not? (Join him at the convention once you get there)":
                        $ scientistlikes +=1
                        char3 "Yay! Thank you so much, I promise it will be fun!!"
                        jump talkbridge
                    "I dont really want to.":
                        char3 "Oh, ok. Thats fine."
                        jump talkbridge
            else:
                char3 "Im sure its going to be really fun!"
                y "From what ive heard, it definitely will be!"
        "Im visiting family.":
            char3 "Oh thats nice."
            char3 "Always good to visit from time to time hm?"
            jump end
        "Going on vacation!":
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
                    char3 "Oh... Thats unfortunate?"
                    jump talkbridge
label cold_vac:
    y "Im traveling to an ice-planet for vacation. I like wintersports a lot, so that was the perfect vacation!"
    char3 "Oh, thats cool. Literally, haha. Im a fan of cold places too, I just love the snow so much!"
    $ scientistlikes +=1
    jump talkbridge
label warm_vac:
    y "Im traveling to a pretty warm planet to go on a beach vacation! I love to swim, and just like how cozy warm weather feels."
    char3 "Ah, I cant relate. I dislike even the warm seasons on my homeplanet, and thats a pretty cold world in relation to some of these vacation planets..."
    if mean <=0:
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
        char3 "I highly recommend a visit to Ahujift if youre interested in these kinds of things, thats a city on Tedow with beautiful fountains. Theyre all public and free to visit, and have a really interesting design concept!"
    jump talkbridge

label silent:
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
    "Or rather outside the bridge. Your way is being blocked by a very serious looking security person."
    char2 "Stop right there."
    char2 "Why are you here?"
    char3 "We had hoped to find ship staff to ask about the quarantine."
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
        jump end
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
                        jump end
                    "Go get the captain":
                        jump end
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
                "Scienceguy sprints after you."
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