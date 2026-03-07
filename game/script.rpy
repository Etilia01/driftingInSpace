# Start script

define char1 = Character("PlaceholderBubblyGirl")
define char2 = Character("Wren")
define char3 = Character("Tritici")
define kit = Character ("Weirdo on a Screen")
define captain: Character ("Captain")
#define e= Character("Erzähler")
define y= Character("[name]")
default hasflyer = 0


label start:
    $ notdemo = 0
    $ config.menu_include_disabled = True
    $ convention = 0
    $ family = 0
    $ home = 0
    $ vacation = 0
    $ scientistlikes = 0
    $ scientiststable = 0
    $ mean = 0
    $ jokester = 0
    $ ist = "is"
    $ was = "was"
    $ pronoun1 = "they"
    $ pronoun1 = "them"
    $ pronoun1 = "their"
    $ name = "'You'"
    $ convincesecurityfail = 0
    scene bg hallway
    
    "A loud alarm rings all throughout the ship"
    "But its hard to pin down where exactly it came from"
    "You start looking around, trying to find out what broke this time"
    "Eventually you give up, going back to the main hall."
    #animation of giant screen thingy with kit on it
    kit "Morning."
    kit "So youre quarantined now."
    kit "Good luck fellas"
    #screen shuts off with glitch effects
    y "huh."
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
    char3 "Why would you say something like thaaaat..."
    "He's sobbing uncontrollably now"
    $scientistlikes -= 1
    $scientiststable -= 1
    $mean += 2
    jump two

label conspiracy:
    "You shocked him so much that he stopped crying."
    char3 "What do you mean by that?"
    char3 "Do you seriously think that?"
    if jokester == 1:
        y "...I was joking"
        char3 "Oh. Ok."
        "He looks relieved."
        jump two
    else:
        y "Of course I do!"
        y "Theyre trying to get you!"
        char3 "Thats so stupid."
        char3 "You are stupid if you believe that. I have nothing to do with 'the government'. Which one do you even mean??? Were not even on a planet right now???? This part of space doesnt even have a government????????????"
        $scientistlikes -= 1
        jump two
label badluck:
    char3 "I know, I know..."
    char3 "I just wanted to be a little dramatic, haha..."
    "He still seems quite upset, but he's at least trying to act fine for now."
    jump two      

label two:
    if scientiststable <= -1:
        "After a few minutes he (at least kind of) brings himself stop crying."

    "He sighs."
    char3 "Im sorry about that just now... Havent had the best day so far."
    char3 "I should probably introduce myself! Im --."
   
    
    $ name = renpy.input("Whats your name?")
    if name == "67":
        "Absolutely not."
        jump end
    else:
        if name == "Etilia":
            "Ha funny. Sure, go ahead."
            jump name
        else:
            jump name
label name:
    
    char3 "Nice to meet you [name]"
    if mean >= 1:
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
        char3 "Why are you like this!?"
        char3 "What did I do to you to deserve you saying things like that!?"
        $ scientistlikes -=1
    else:
        char3 "Thats...thats a bit mean, dont you think?"
        char3 "But no, that is definitely not why."
        $ scientistlikes -=1
label criminalidea1:
    if jokester >=2:
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
        char3 "Ah another joke? How funny-"
        y "No."
        char3 "What do you mean no?"
        y "I wasnt joking."
        char3 "Oh-"
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
