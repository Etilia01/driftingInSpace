#effects and stuff idfk
define slowdissolve = Dissolve(1.0)
default lowered = False
# this adjusts sprite sizes because i drew them horribly small :,)
#tritici
image tritici idle 1:
    "Tritici/tritici idle 1.png"
    zoom 1.8
image tritici idle 2:
    "Tritici/tritici idle 2.png"
    zoom 1.8
image tritici idle front:
    "Tritici/tritici idle front.png"
    zoom 1.8
image tritici slight sad:
    "Tritici/tritici slight sad.png"
    zoom 1.8
image tritici sad:
    "Tritici/tritici sad.png"
    zoom 1.8
image tritici very sad:
    "Tritici/tritici very sad.png"
    zoom 1.8
image tritici shocked:
    "Tritici/tritici shocked.png"
    zoom 1.8
image tritici happy 1:
    "Tritici/tritici happy 1.png"
    zoom 1.8
image tritici happy 2:
    "Tritici/tritici happy 2.png"
    zoom 1.8

#wren
image wren neutral:
    "wren/wren neutral.png"
    zoom 1.8
image wren neutral 2:
    "wren/wren neutral 2.png"
    zoom 1.8
image wren angry:
    "wren/wren angry.png"
    zoom 1.8
image wren happy:
    "wren/wren happy.png"
    zoom 1.8
image wren sus:
    "wren/wren sus.png"
    zoom 1.8
image wren unsure:
    "wren/wren unsure.png"
    zoom 1.8

#captain
image captain concerned:
    "captain/captain concerned.png"
    zoom 1.8
image captain happy:
    "captain/captain happy.png"
    zoom 1.8
image captain neutral1:
    "captain/captain neutral1.png"
    zoom 1.8
image captain neutral2:
    "captain/captain neutral2.png"
    zoom 1.8
image captain sad:
    "captain/captain sad.png"
    zoom 1.8
image captain shocked:
    "captain/captain shocked.png"
    zoom 1.8

# bubbly
image bubbly happy:
    "Bubbly/bubbly happy.png"
    zoom 1.8
image bubbly idle:
    "Bubbly/bubbly idle.png"
    zoom 1.8
image bubbly sad:
    "Bubbly/bubbly sad.png"
    zoom 1.8
image bubbly shocked:
    "Bubbly/bubbly shocked.png"
    zoom 1.8

#this adjusts background sizes
image bg glitchscreen:
    "bg glitchscreen.png"
    zoom 0.5
image bg bluescreen:
    "bg bluescreen.png"
    zoom 0.5
image bg hallway1:
    "bg hallway1.png"
    zoom 0.5
image bg kit1:
    "bg kit1.png"
    zoom 0.5
image bg kit2:
    "bg kit2.png"
    zoom 0.5
image bg kit3:
    "bg kit3.png"
    zoom 0.5
image bg mainhall 1:
    "bg mainhall 1.png"
    zoom 0.5
image bg door1:
    "bg door1.png"
    zoom 0.5
image bg door2:
    "bg door2.png"
    zoom 0.5
image bg doortobridge:
    "bg doortobridge.png"
    zoom 0.5
image bg wrenencounter:
    "bg wrenencounter.png"
    zoom 0.5
image bg engineroom1:
    "bg wrenencounter.png"
    zoom 0.5
image bg engineroom2:
    "bg wrenencounter.png"
    zoom 0.5
image bg engineroom3:
    "bg wrenencounter.png"
    zoom 0.5
image bg dooropen:
    "bg wrenencounter.png"
    zoom 0.5
#voices
define tritici_voice= ['audio/voice/sound.wav', 'audio/voice/sound2.wav', 'audio/voice/voice4.wav', 'audio/voice/sound3.wav']
define wren_voice= ['audio/voice/wren1.wav', 'audio/voice/wren2.wav', 'audio/voice/wren3.wav', 'audio/voice/wren4.wav']
define captain_voice= ['audio/voice/sound.wav', 'audio/voice/sound2.wav', 'audio/voice/voice4.wav', 'audio/voice/sound3.wav']
define kit_voice= ['audio/voice/kitvoice1.wav', 'audio/voice/kitvoice2.wav', 'audio/voice/kitvoice3.wav', 'audio/voice/kitvoice4.wav']
define muster_voice= ['audio/voice/sound.wav', 'audio/voice/sound2.wav', 'audio/voice/voice4.wav', 'audio/voice/sound3.wav']
define amelia_voice= ['audio/voice/sound.wav', 'audio/voice/sound2.wav', 'audio/voice/voice4.wav', 'audio/voice/sound3.wav']
#there has to be a better/more efficient way to handle this (ᵕ—ᴗ—)
init python: 
    def tritici_voicefunc(event, interact=True, **kwargs):

        if not interact: 
            return 
        if event == "show_done": 
            
            for _ in range(30):
                renpy.sound.queue(renpy.random.choice(tritici_voice))
        elif event == "slow_done":
            renpy.sound.stop()
    def wren_voicefunc(event, interact=True, **kwargs):

        if not interact: 
            return 
        if event == "show_done": 
            
            for _ in range(30):
                renpy.sound.queue(renpy.random.choice(wren_voice))
        elif event == "slow_done":
            renpy.sound.stop()
    def kit_voicefunc(event, interact=True, **kwargs):

        if not interact: 
            return 
        if event == "show_done": 
            
            for _ in range(30):
                renpy.sound.queue(renpy.random.choice(kit_voice))
        elif event == "slow_done":
            renpy.sound.stop()
    def captain_voicefunc(event, interact=True, **kwargs):

        if not interact: 
            return 
        if event == "show_done": 
            
            for _ in range(30):
                renpy.sound.queue(renpy.random.choice(captain_voice))
        elif event == "slow_done":
            renpy.sound.stop() 
    def muster_voicefunc(event, interact=True, **kwargs):

        if not interact: 
            return 
        if event == "show_done": 
            
            for _ in range(30):
                renpy.sound.queue(renpy.random.choice(muster_voice))
        elif event == "slow_done":
            renpy.sound.stop() 
    def amelia_voicefunc(event, interact=True, **kwargs):

        if not interact: 
            return 
        if event == "show_done": 
            
            for _ in range(30):
                renpy.sound.queue(renpy.random.choice(amelia_voice))
        elif event == "slow_done":
            renpy.sound.stop()  



#characters
define char1 = Character("PlaceholderBubblyGirl")
define char2unknown = Character("Security Guard",callback=wren_voicefunc)
define char2 = Character("Wren",callback=wren_voicefunc)
define char3 = Character("Tritici",callback=tritici_voicefunc)
define kit = Character ("Weirdo on a Screen", callback=kit_voicefunc)
define captain= Character ("Captain",callback=captain_voicefunc)
define unknown = Character("???",callback=muster_voicefunc)
define muster = Character ("Mustermann",callback=muster_voicefunc)
define tech = Character ("Amelia",callback=amelia_voicefunc)
#define e= Character("Erzähler")
define y= Character("[name]")

#variables that need to be preloaded for the game to work apparently. Basically input stuff for riddles and stuff that determines if things like certain menus can be accessed.
default hasflyer = 0
default place = "Escape Pods"


#game starts here
label start:
    $ config.menu_include_disabled = True
    $ notdemo = 0
    # a bunch more variables that only get important later in the game, which is why they can be declared within start. The two above are how i do greyed out choices. Prob not the best way but oh well.
    $ convention = 0
    $ family = 0
    $ home = 0
    $ vacation = 0
    $ scientistlikes = 0
    $ scientiststable = 0
    $ mean = 0
    $ jokester = 0
    $ convincesecurityfail = 0

    #these are for dialogue changes depending on player input
    $ ist = "is"
    $ was = "was"
    $ pronoun1 = "they"
    $ pronoun1 = "them"
    $ pronoun1 = "their"
    $ name = "'You'"
    
    stop music
    play music 'audio/music/mainthememoreeditedidk.wav'
    $ lowered = True
    show text  _("{size=50}Which version of the story would you like to play?"): 
        xalign 0.5 
        yalign 0.3 
    with slowdissolve
    menu:
        "Passenger":
            hide text
            $ lowered = False
            jump passenger
        "Staff" if notdemo == 1:
            $ lowered = False
            hide text
            jump end
    
label staff:
    scene bg hallway1
    "A loud alarm rings all throughout the ship"
    "But its hard to pin down where exactly it came from"
    "You start looking around, trying to find out what broke this time"
    jump end
label passenger:

    # starts a new scene, meaning it hides all sprites and backgrounds and loads hallway
    "A loud alarm rings all throughout the ship"
    y "What could that mean? More turbulences?"
    "You wait for the announcement that should inevitably follow after."
    "..."
    "Nothing."
    y "Huh. Thats weird."
    "You decide to go to the main hall, since thats likely the place where youll find an explanation."
    scene bg hallway1
    "So you leave your room and walk over there."
    "Its not that far from the passenger cabins, so even though you almost get lost navigating the grey, repetitive hallways, it doesnt take you long to get there."
    scene bg door2
    $ renpy.pause(0.5)
    scene bg mainhall 1 with dissolve
    "As you arrive in the main hall, the alarm has already stopped again."
    "Some other passengers apparently had the same idea. Yet theres no staff to be found."
    "Slowly the other people in the hall leave again, murmuring about this strange situation."
    "But its not much different than what youre already used from this ship."
    "The public transit system really needs an overhaul, there have been constant malfunctions and delays throughout all of your travels with this line."
    scene bg glitchscreen
    "Suddenly the huge screen in the back of the hall lights up"
    #animation of giant screen thingy with kit on it
    scene bg kit1
    
    $ renpy.pause(0.5)
    scene bg kit2
    with slowdissolve
    $ renpy.pause(0.5)
    kit "Morning."
    scene bg kit3
    kit "So youre quarantined now."
    
    kit "Good luck fellas"
    scene bg glitchscreen
    $ renpy.pause(0.2)
    scene bg bluescreen
    pause
    #screen shuts off with glitch effects
    y "huh."
    scene bg mainhall 1
    show tritici shocked
    char3 "WHAT WHAT WHAT WHAT WHAT WHAT WHAT WHAT WHAT WHAT WHAT WHAT WHAT WHA-"
    "You only now notice the guy standing in the corner of the hall."
    #camera pans to scientist guy
    "He seems kind of... nervous"

label choice_no1:
    "Maybe you want to do something?"
    menu:
        "Go over to him and try to comfort him":
            $mean -= 1
            jump comforttheweirdguy
        "Nah." if notdemo == 1:
            jump end
label comforttheweirdguy:
    show tritici sad
    "You approach the guy in the corner."
    "Hes crying now."
    char3 "Why me... waaahhh"
    menu:
        "Mayhaps you did something really bad in a previous life?":
            jump mean
        "Bad luck I suppose.":
            jump badluck
        "Government conspiracy. Definitely. (Joking)":
            $jokester += 1
            jump conspiracy
        "Government conspiracy. Definitely. (Serious)":
            jump conspiracy
        "Because I dont like you.":
            jump mean
label mean:
    show tritici very sad
    char3 "Why would you say something like thaaaat..."
    "He's sobbing uncontrollably now"
    $scientistlikes -= 1
    $scientiststable -= 1
    $mean += 2
    jump two

label conspiracy:
    show tritici idle 2
    "You shocked him so much that he stopped crying."
    char3 "What do you mean by that?"
    show tritici idle 1
    char3 "Do you seriously think that?"
    if jokester == 1:
        y "...I was joking"
        show tritici happy 1
        char3 "Oh. Ok."
        "He looks relieved."
        jump two
    else:
        y "Of course I do!"
        y "Theyre trying to get you!"
        show tritici idle 1
        char3 "Thats so stupid."
        char3 "You are stupid if you believe that. I have nothing to do with 'the government'. Which one do you even mean??? Were not even on a planet right now???? This part of space doesnt even have a government????????????"
        $scientistlikes -= 1
        jump two
label badluck:
    char3 "I know, I know..."
    char3 "I just wanted to be a little dramatic, haha..."
    show tritici slight sad
    "He still seems quite upset, but he's at least trying to act fine for now."
    jump two      

label two:
    if scientiststable <= -1:
        show tritici slight sad
        "After a few minutes he (at least kind of) brings himself stop crying."

    "He sighs."
    char3 "Im sorry about that just now... Havent had the best day so far."
    show tritici idle 2
    char3 "I should probably introduce myself! Im Tritici."
   
    
    $ name = renpy.input("Whats your name?")
    if name == "67":
        "Absolutely not."
        jump end
    else:
        if name == "Etilia":
            "Ha funny. Sure, go ahead."
            jump name
        else:
            if name == "Deez Nuts":
                "Wow youre either very old and unfunny or a toddler. And also unfunny."
                "But I suppose it could be worse. Go ahead."
                jump name
            else:
                jump name
label name:
    if mean <=0 and scientistlikes >=1:
        show tritici happy 1
    
    char3 "Nice to meet you [name]"
    if mean >= 1:
        show tritici idle 1
        "It sounds forced."
    char3 "And what pronouns should I refer to you as?"
    menu:
        "They/Them/Theirs":
            $ pronoun1 = "they"
            $ pronoun2 = "them"
            $ pronoun3 = "their"
            $ ist = "are"
            $ was = "were"
            jump storyagain
        "It/It/Its":
            $ pronoun1 = "it"
            $ pronoun2 = "it"
            $ pronoun3 = "its"
            jump storyagain
        "She/Her/Her":
            $ pronoun1 = "she"
            $ pronoun2 = "her"
            $ pronoun3 = "her"
            jump storyagain
        "He/Him/His":
            $ pronoun1 = "he"
            $ pronoun2 = "him"
            $ pronoun3 = "his"
            jump storyagain
        "Something else":
            jump pronounselect
label pronounselect:
    $ pronoun1 = renpy.input("General (As in 'They went for a walk.')")
    $ pronoun2 = renpy.input("Referred to by (As in 'I met him yesterday!')")
    $ pronoun3 = renpy.input("Posessive (As in 'Thats her book.')")
    char3 "[pronoun1]/[pronoun2]/[pronoun3], is that right?"
    menu:
        "Yes":
            show tritici idle 2
            char3 "Oh, and does that work like for example they/them, that i would refer to you in plural? Like [pronoun1] are an interesting person?"
            menu:
                "Yes":
                    $ ist = "are"
                    $ was = "were"
                    char3 "Good to know!"
                    jump storyagain
                "No":
                    char3 "Good to know!"
                    jump storyagain   
            
        "No":
            jump pronounselect
label storyagain:
    char3 "So what do you think quarantine means here?"
    char3 "Like a viral outbreak or something? As far as Im aware there isnt any major illness going around currently, at least none concerning enough to warrant these measures..."
    char3 "Im not sure. Maybe political reasons? Ive heard we have a diplomat on board, maybe thats why? But quarantine is certainly strange wording if thats truly the case."
    menu:
        "A virus sounds reasonable.":
            jump reasonable
        "Politics would make sense.":
            jump reasonable
        "Maybe we have a dangerous criminal onboard! (Joking)":
            $ jokester += 1
            jump criminalidea1
        "Maybe we have a dangerous criminal onboard! (Serious)":
            jump criminalidea2
        "Maybe youre just that gross, they need time to prepare for your arrival with enough disinfectant.":
            $ mean += 1
            jump mean2
label reasonable:
    char3 "It does, right?"
    char3 "But thats still just a guess, we cant know for sure..."
    jump story2
label mean2:
    if mean >=2:
        show tritici shocked
        char3 "Why are you like this!?"
        show tritici sad
        char3 "What did I do to you to deserve you saying things like that!?"
        $ scientistlikes -=1
    else:
        show tritici slight sad
        char3 "Thats...thats a bit mean, dont you think?"
        char3 "But no, that is definitely not why."
        $ scientistlikes -=1
label criminalidea1:
    if jokester >=2:
        show tritici happy 1
        char3 "Ah another joke? How funny!"
        char3 "Of course we have a dangerous criminal onboard - Me Mr.Villanguy! I do very evil things, like jaywalking!"
        char3 "That was sarcasm, in case you didnt notice."
        y "It was quite obvious."  
        $ scientistlikes += 1
        jump story2
    else:
        char3 "I highly doubt that."
        y "Same, I was just joking."
        char3 "Oh ok. Haha...? How...funny."
        jump story2
label criminalidea2:
    if jokester >=1:
        show tritici happy 1
        char3 "Ah another joke? How funny-"
        y "No."
        show tritici idle 2
        char3 "What do you mean no?"
        y "I wasnt joking."
        char3 "Oh-"
        show tritici idle 1
        char3 "Well, I think thats highly unlikely to be the case."
        y "If you say so..."
        jump story2 
    else:
        char3 "I highly doubt that."
        y "Why? How are any of your ideas more likely than mine?"
        char3 "I-"
        char3 "You know what, sure, go ahead and think that."
        char3 "Just know that i think its stupid."
        jump story2 

label story2:
    if mean >= 2:
        show tritici idle 1
        "He sighs, clearly annoyed."
    char3 "Well, maybe someone else knows more than us. Lets look for some other passengers and ask them about it."
    menu:
        "Sounds good!":
            jump soundsgood
        "Id rather not do that." if notdemo == 1:
            jump end 
label soundsgood:
    if mean ==1:
        char3 "Alright. Id say we look on the ships bridge first. The captain likely knows whats going on."
        jump bridge
    if mean ==2:
        char3 "Ok. We'll look for the captain, they should be on the bridge."
        jump bridge
    else:
        show tritici happy 1
        char3 "Alright! Where should we look first?"
        menu:
            "You choose.":
                char3 "Why dont we go to the bridge? The staff there probably knows more than us."
                menu:
                    "Sure":
                        jump bridge
                    "What are the other options?" if notdemo == 1:
                        char3 "Lets have a look at the floor plan."
                        char3 "Does anything here look like a good choice to you?"
                        jump end
            "Let me have a look at the floorplan." if notdemo == 1:
                jump end
        
#after sounds good:
# look around the ship, depending on where meet different character, ask them about it. they have no idea. bridge captain not there, you leave, meet security person at entrance security person says to call back, you go to commando room, signal cut off, scientist guy says he can fix it, you go out to see who did it, meet bubbly girl, she helps you look around, you find someone working on electricity supply, they say theyre the janitor. if you dont believe they attack (gun) 
label end:
    return
