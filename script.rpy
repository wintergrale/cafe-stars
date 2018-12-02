# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.

define cm = Character("Caramel Macchiato",color = "#af3602")
define s = Character("Strawberry", color = "#d02255")
define m = Character("Mocha", color = "#9a7159")
define vl = Character("Vanilla Latte", color = "#4d3618")

default is_sabotage = False
default is_murder = False
default is_arson = False

transform sleft:
    xalign 0.07
    yalign 1.12
transform sright:
    xalign 0.93
    yalign 1.12

# The game starts here.

label start:

    # Show a background. This uses a placeholder by default, but you can
    # add a file (named either "bg room.png" or "bg room.jpg") to the
    # images directory to show it.

    scene bg floor

    # This shows a character sprite. A placeholder is used, but you can
    # replace it by adding a file named "eileen happy.png" to the images
    # directory.

    # These display lines of dialogue.

    "Stars, the most popular cafe in the world,"
    "Every year, a popularity poll is held, and it comes out today."
    "I'm Caramel Macchiato, and I'm on my way to see the rankings. Hopefully this year, I'll be able to get a high rank!"
    "Hey, it's Strawberry!"
    show strawberry smile at sright
    show caramel open at sleft
    cm "Hey Strawberry, are you going to see the postings today?"
    show caramel smile at sleft
    show strawberry open at sright
    s "If it isn't Caramel Macchiato. Everyone's going to see the rankings today right?"
    s "Do you want to go together?"
    show strawberry smile at sright

    #scene
    scene bg strawberry_card
    with fade
    "Strawberry's popular amongst the customers, so it always gets a high ranking on the popularity polls."
    "It's also a pretty cool drink. It always has its lid off. Sometimes I wonder if it's ever afraid it'll spill?"
    "Strawberry's also one of my best friends."

    #scene
    scene bg floor
    show caramel open at sleft
    show strawberry smile at sright
    cm "Sure! Do you think you'll make it into the top ten?"
    show caramel smile at sleft
    show strawberry open at sright
    s "Hmm, sure. That's how it was last year. How about you?"
    show strawberry smile at sright
    show caramel sparkle open at sleft
    cm "Haha, I thought you'd never ask."
    cm "You see, after my failure last year, I've been working a lot on my popularity. I'm sure I'll rank this year"
    show caramel sparkle at sleft
    show strawberry open at sright
    s "Is that so? Well then, let's go over to the polls to see, shall we?"

    #scene
    scene bg polls
    with fade
    "As we approach the polls, we can see a big crowd."

    show caramel shocked at sleft
    show strawberry smile at sright
    cm "Wow, the crowd's so big..."
    show strawberry open at sright
    s "It's always this big, but I guess our numbers are increasing. Did you know? We recently hit over 85,000."
    show strawberry smile at sright
    show caramel evil open at sleft
    cm "85,000... So the competition's only growing."
    show caramel worried open at sleft
    cm "Anyway, I don't know how we'll ever get to the front. We're going to wait in line forever."
    show caramel worried at sleft
    show strawberry open at sright
    s "It's simple actually. You've got me remember? Now, make sure you stick close to me."
    show strawberry smile at sright

    "Strawberry steps toward the crowd."

    show strawberry open at sright
    s "Come on! Make way please!"

    #scene
    scene bg strawberry_crowd
    "Like magic, the crowd splits in front of Strawberry."
    "Whispers start in the crowd."

    "Wow! Is that Strawberry?"
    "It's the first time I've seen it up close!"

    "Strawberry's just that popular, I guess."

    show caramel open at sleft
    show strawberry smile at sright
    cm "Your popularity's really something."
    cm "If the popularity also took the opinion of other drinks, I think you'd definitely win."

    show caramel smile at sleft
    show strawberry laugh at sright
    "Strawberry laughs"

    show strawberry open at sright
    s "But that's not what's important, now is it?"
    s "There're the polls...Seems I placed third. I guess the top three never change."
    show strawberry smile at sright

    "It was always Vanilla Latte, Mocha, and Strawberry, in that order."

    cm "Vanilla Latte, Mocha, Strawberry..."
    show caramel shocked at sleft
    cm "...Wait a second, I'm not here!"
    show strawberry worried open at sright
    s "...I'm sorry Caramel. I know what this means to you."
    show strawberry worried at sright
    show caramel open at sleft
    cm "It's okay. It's not like this is the first time, and you can't change my popularity after all."

    menu:
        cm "At times like this, the only answer is..."

        "Sabotage!":
            jump sabotage

        "Arson!":
            jump arson

        "Murder!":
            jump murder


#sabotage
label sabotage:
    $ is_sabotage = True

    show caramel evil open at sleft
    cm "Vanilla Latte! Just what do people see in it! It's basically the same thing as me and yet it is so popular!"
    cm "...Vanilla Latte must be the problem. It's sucking away my popularity!"
    cm "Strawberry, how do you think Vanilla Latte manages to be so popular compared to me?"
    show caramel smile at sleft
    show strawberry open at sright
    s "Maybe it's you deisgn? No offense to you, but it does look more modern and neat than you."
    s "Customers love that stuff these days, right?"
    show strawberry smile at sright
    show caramel evil open at sleft
    cm "You're right..."
    show caramel smile at sleft

    "Somebody calls for Strawberry. It was probably one of Strawberry's many friends."

    show strawberry open at sright
    s "I think I have to go now. See you later Caramel!"
    hide strawberry open at sright

    show caramel evil open at sleft
    cm "...Yes...If it's looks, I can definitely take care of that."
    show caramel open at sleft

    menu:
        cm "Now, where can I find it..."

        "Counters":
            jump counters

        "Tables":
            jump tables


#arson
label arson:
    $ is_arson = True;

    show caramel evil open at sleft
    cm "Vanilla Latte, bane of my existence, and my evil twin... We're basically the same thing right? Why's it so popular!"
    cm "Gah! I wish the popularity polls didn't exist. Then I wouldn't need to suffer."
    show caramel evil at sleft
    show strawberry laugh at sright
    "Strawberry laughs"

    s "You live for the popularity polls! There's no way you'd manage without it."
    show strawberry smile at sright
    show caramel evil open at sleft
    cm "No...Vanilla Latte and the polls. I'll destroy them all."
    show caramel smile at sleft
    show strawberry laugh at sright
    s "What? Are you going to burn the placedown or something?"

    "Ring, Ring"
    show strawberry smile at sright
    "Strawberry suddenly gets a call."

    show strawberry open at sright
    with moveoutright
    s "Oh, sorry, but I think I have to go. See you later Caramel!"

    hide strawberry open
    show caramel smile at sleft
    cm "Oh Strawberry..."
    cm "You know me too well..."

    menu:
        cm "Now, where do I start..."

        "Counters":
            jump arson_counters

        "Tables":
            jump tables


#murder
label murder:
    $ is_murder = True

    show caramel open at sleft
    cm "That damned Vanilla Latte! It's basically the same thing as me so why does it get so much popularity!"
    show caramel evil open at sleft
    cm "It must be drawing away my popularity..."
    show caramel smile at sleft
    show strawberry open at sright
    s "Oh well, who can stop it? It doesn't even come to the polls because it knows it's going to be first."
    show strawberry smile at sright

    "Ring, Ring"
    "Strawberry suddenly gets a call. Strawberry looks at who the caller is"

    show strawberry open at sright
    s "Hm? Oh, I think I have to go now."
    s "See you later Caramel!"
    hide strawberry open
    with moveoutright

    show caramel smile at sleft
    cm "...Yes, that's what I'll have to do. I'll just get rid of it."

    menu:
        cm "Now, where can I find it..."

        "Counters":
            jump counters

        "Tables":
            jump tables


#counters
label counters:
    #scene
    scene bg counter
    show caramel evil open at sleft
    cm "I can feel it! Vanilla Latte must be near."
    show caramel open at sleft
    cm "Hey, it's Mocha!"
    show mocha smile at sright
    m "?"

    #scene
    scene bg mocha_card
    with fade
    "Mocha's really popular. Whenever I see it, it's always hangs out with its friends."
    "Strawberry's pretty cool, but it's more of an aloof cool. Mocha, on the other hand, is a hip kind of cool."
    "But don't let the hipness fool you because it's really smart. It has the answers to everything!"

    #scene
    scene bg counter
    with fade
    show mocha open at sright
    show caramel smile at sleft
    m "Hey, CM. What's up?"
    show mocha smile at sright
    show caramel open at sleft
    cm "I'm looking for Vanilla Latte. You know where it is?"
    show caramel smile at sleft
    show mocha open at sright
    m "VL's probably at the tables talking up a storm as usual."
    show mocha question open at sright
    m "Why do you want it?"
    show mocha smile at sright

    if is_sabotage:
        show caramel open at sleft
        cm "It's taking away my popularity so I'm going to sabotage it!"

    if is_murder:
        show caramel open at sleft
        cm "It's taking away my popularity, so I have to get rid of it."

    show caramel smile at sleft
    m "..."
    show mocha laugh at sright
    m "That's nice. Well, good luck!"
    show mocha smile at sright
    show caramel open at sleft
    cm "Thanks!"
    hide caramel open at sright
    with moveoutleft

    jump tables


#tables
label tables:
    #scene
    scene bg table
    with fade

    "I make my way to the tables"

    scene bg vanilla_and_co
    with dissolve

    "There it is! My mortal enemy, Vanilla Latte."
    "Just like Mocha said, Vanilla Latte was talking to a bunch of its friends."
    "Vanilla Latte suddenly looks my way and starts walking toward me."

    #scene
    scene bg table
    with fade

    show caramel smile at sleft
    with dissolve
    show vanilla friendly open at sright
    with dissolve
    vl "Caramel! How have you been! I've heard your rank went up this year."
    vl "At this rate, you'll probably make top ten next year."
    show vanilla open at sright

    "Vanilla Latte leaned into whisper"

    vl "{size=-5}Between you and me, a lot of these drinks are on their way out.{/size}"
    show vanilla smile at sright
    show caramel evil at sleft

    if is_sabotage:
        menu:
            cm "..."

            "It's now or never":
                jump now

            "Wait":
                jump wait


    if is_murder:
        menu:
            cm "..."

            "Go for the kill":
                jump kill

            "Bide my time":
                jump bide


    if is_arson:
        show caramel evil open at sleft
        cm "And soon you'll also be on the way out."
        show caramel evil at sleft
        show vanilla question open at sright
        vl "Hm? Sorry, I didn't catch that."
        show vanilla smile at sright
        show caramel open at sleft
        cm "I asked if you knew a way to start a fire."
        show caramel smile at sleft
        show vanilla question open at sright
        vl "A fire? Why do you want to know?"
        show vanilla smile at sright
        show caramel open at sleft
        cm "It's for an experiment."
        show caramel smile at sleft
        show vanilla open at sright
        vl "I don't know, but if you manage to find Mocha, it'd probably know. It might be on the counters, but I wouldn't count on it."
        show vanilla smile at sright
        show caramel open at sleft
        cm "Okay, thanks, Vanilla Latte."
        show caramel smile at sleft
        show vanilla friendly open at sright
        vl "Come on, you can just call me Vanilla."
        show vanilla friendly at sright
        show caramel open at sleft
        cm "Right..."
        show caramel evil open at sleft
        cm "Goodbye Vanilla."
        show caramel evil at sleft
        hide vanilla friendly
        "I leave the tables and head toward the counters, leaving Vanilla Latte unaware of its impending doom."


#arson counters
label arson_counters:
    #scene
    scene bg counter
    with fade

    show caramel smile at sleft
    with dissolve
    cm "So how do I start a fire..."
    show caramel open at sleft
    cm "Hey, it's Mocha!"
    show mocha smile at sright
    with dissolve
    m "?"

    #scene
    scene bg mocha_card
    with dissolve
    "Mocha's really popular. Whenever I see it, it's always hangs out with its friends."
    "Strawberry's also pretty cool, but it's more of an aloof cool. Mocha, on the other hand, is a hip kind of cool."
    "But don't let the hipness fool you because it's really smart. It has the answers to everything!"

    #scene
    scene bg counter
    with fade

    show caramel smile at sleft
    with dissolve
    show mocha open at sright
    with dissolve
    m "Hey, CM. What's up?"
    show mocha smile at sright
    show caramel open at sleft
    cm "I'm looking for a way to start a fire. Do you know what the fastest way is?"
    show caramel smile at sleft
    show mocha question open at sright
    m "Um, I guess you can use the gas stove. Why do you ask?"
    show mocha question at sright
    show caramel open at sleft
    cm "That's a great idea! Why didn't I think of that before?"
    cm "Now, I'm going to burn the cafe down."
    show caramel smile at sleft
    m "..."
    show mocha laugh at sright
    m "That's nice. Then I'll make sure to clear out before you do that."
    m "See ya CM!"
    hide mocha open
    with moveoutright

    show caramel evil open at sleft
    cm "Thanks to Mocha, I know exactly what to do."

    #scene
    scene bg kitchen
    with fade

    scene bg stove
    with dissolve
    "I walk over to the kitchen and stand before the gas stove."
    "Not a lot of drinks came by these parts. They all stayed on the counter or the tables. Some drinks didn't know about the kitchen."
    scene bg stove2
    with dissolve
    "I turn all of the gas stoves on. The smell of gas soon fills the kitchen."
    "After double checking the gas stoves, I slip into the refrigerator."
    scene bg fridge
    with fade

    show caramel smile at sleft
    with dissolve
    "The inside of the refrigerator's dark, and it takes a moment to adjust to the new environment."
    "Then, out of the corner of my eye, is a familiar drink."

    show strawberry question open at sright
    with dissolve
    s "Caramel? What are you doing?"
    show strawberry question at sright
    show caramel open at sleft
    cm "Strawberry? Shhh. I'm trying to set the kitchen on fire. What are you doing?"
    show caramel smile at sleft
    show strawberry open at sright
    s "I was supposed to meet someone here, but they stood me up."
    pause 0.5
    show strawberry question open at sright
    s "Wait, what fire?"
    show strawberry question at sright
    show caramel open at sleft
    cm "The fire to burn down Vanilla Latte and the polls, remember?"
    show caramel smile at sleft
    show strawberry worried open at sright
    s "You were actually serious about that?"
    show strawberry worried at sright
    show caramel open at sleft
    cm "Yeah!"

    "Strawberry's about to say something, but suddenly, there's a sound from outside of the refrigerator. The sound of a door."
    "I wait with bated breath, and then"
    "Boom"
    with hpunch
    "An explosion and woosh is heard outside."

    show caramel open at sleft
    cm "Yes..."
    show caramel smile at sleft

    "After waiting for a few moments, I open the door to face a see of fire."

    #scene
    scene bg fire_and_fury
    with fade

    with dissolve
    cm "Now there's no Vanilla Latte or popularity poll!"

    "The fire flooded out of the kitchen into the counter and tables."
    "The shouts and screams of burning drinks filled the air."
    "Something opened the door and created a draft, sending a wave of fire toward the door."

    cm "Mwahahahaha. Burn, burn!"

    "I close the refrigerator door to make sure no fire makes it inside and wait for the fire to go out, the screams slightly muffled"
    scene black
    with fade

    "{b}Good Ending{/b}."
    return

#kill
label kill:
    show caramel evil open at sleft
    cm "Young fry of treachery!!!"

    hide vanilla smile
    with moveoutright
    hide caramel evil open
    with moveoutright

    "I slam into Vanilla Latte, sending it barreling off the table."
    "But at the last moment, he grabs onto me and we both plummet off the table."

    scene bg floor
    with vpunch
    "Splat"

    pause 0.5

    show caramel worried open at sleft
    cm "Ugh"
    show caramel worried at sleft

    "My insides feel all mixed up."

    show caramel open at sleft
    cm "Where's Vanilla Latte?"
    show caramel smile at sleft

    scene bg vanilla_dead_floor
    "Vanilla Latte lies lifelessly on the floor. Its lid is open, it's contents spilling all across the floor into a sticky mess."
    "I feel the liquid with my hands"

    show caramel evil open at sleft
    with dissolve
    cm "Yes, yes..."

    show caramel open at sleft

    cm "I've become the new Vanilla Latte!"
    show caramel open at sleft
    cm "We'll see who wins the popularity poll now! Hahahaha!"
    show caramel smile at sleft

    scene black with fade

    "{b}Good Ending{/b}."
    return

#bide
label bide:
    show caramel evil open at sleft
    cm "And soon you'll also be on the way out."
    show caramel evil at sleft
    show vanilla question open at sright
    vl "Hm? Sorry, I didn't catch that."
    show vanilla smile at sright
    show caramel open at sleft
    cm "I said 'Is that so, thanks Vanilla Latte'"
    show caramel smile at sleft
    show vanilla friendly open at sright
    vl "Oh, in that case, your welcome, and you can call me Vanilla, remember?"
    show vanilla friendly at sright
    show caramel open at sleft
    cm "Right..."
    show caramel evil at sleft

    "In order for a successful crime, there can't be too many witnesses. I'll have to lure it out."

    show caramel open at sleft
    cm "Hey, you wanna go to the kitchen? To get some fruit or something?"
    show caramel smile at sleft
    show vanilla question open at sright
    vl "But we're not fruit drinks. Why would we need fruit?"
    show vanilla question at sright
    show caramel open at sleft
    cm "Then how about for whipped cream."
    show caramel smile at sleft
    show vanilla open at sright
    vl "Okay then."
    show vanilla smile at sright


    "Vanilla Latte waves goodbye to its friends, and we go to the kitchen together."

    scene bg kitchen

    "Not a lot of drinks came by the kitchen. They all stayed on the counter or the tables; some drinks didn't know about the kitchen."
    "The whipped cream is on a high shelf."

    show vanilla open at sright
    vl "Boost me up. I'll grab the whipped cream."
    show vanilla smile at sright

    scene bg kitchen_w_vanilla
    "Vanilla Latte climbs onto my hands and balances on them while reaching for the cream."
    "Nobody's around."

    scene bg die_bananafish
    cm "Die bananafish!"
    with hpunch
    vl "???"

    "I throw Vanilla Latte off the kitchen counter. It yells as it plummets to the ground."

    scene bg kitchen_vanilla_dead
    with vpunch
    "Splat"
    "Vanilla Latte's cup splits open and the contents explode across the floor. The competition, eliminated."
    "The liquid that didn't initially splatter out slowly drips out of the broken cup."
    "I watch silently."

    cm "Now that you're gone, we'll see who wins the popularity poll."

    "{b}Good Ending{/b}."
    return

#now
label now:
    show caramel open at sleft
    cm "Hell hath no fury!!!"
    vl "???"

    scene bg label_run
    with hpunch
    "I rip off Vanilla Latte's label and make a break for it."

    vl "Huh? Wait! What are you doing! Come back here Caramel, I need that!"
    cm "Hahaha! Now that its charm's disappeared, nobody'll love it anymore. Mwahahaha!"
    vl "Hey!"

    "{b}Good Ending{/b}."
    return

#wait
label wait:
    show caramel evil open at sleft
    cm "And soon you'll also be on the way out."
    show caramel evil at sleft
    show vanilla question open at sright
    vl "Hm? Sorry, I didn't catch that."
    show vanilla smile at sright
    show caramel open at sleft
    cm "I said 'Is that so, thanks Vanilla Latte'"
    show caramel smile at sleft
    show vanilla friendly open at sright
    vl "Oh, in that case, your welcome, and you can call me Vanilla, remember?"
    show vanilla friendly at sright
    show caramel open at sleft
    cm "Right..."
    show caramel smile at sleft

    "Suddenly, a brilliant idea pops into my head."

    show caramel open at sleft
    cm "Wait right here, I have to go get something real quick."
    hide caramel open
    with moveoutleft

    scene bg counter
    with fade

    "I go to the counters."

    show caramel open at sleft
    with dissolve
    show mocha smile at sright
    with dissolve
    cm "Mocha! I need a permanent pen."
    show caramel smile at sleft

    show mocha look at sright
    "Mocha glances at the pencil holder filled with pens and gives me a look."

    show caramel open at sleft
    cm "Thanks!"
    show caramel smile at sleft

    "I grab a big, black, permanent marker and made my way back to the tables."

    #scene
    scene bg table
    "Vanilla Latte returned to talking with its friends, but when it saw me, it stopped talking to its friends."

    show vanilla question open at sright
    with dissolve
    show caramel evil pen at sleft
    with moveinleft
    vl "What's that Caramel?"
    show vanilla question at sright
    show caramel sparkle open at sleft

    cm "Fall, Lucifer!"
    vl "???"

    show vanilla question at sright
    "The pen swings forward, making a thick black mark on Vanilla Latte's cup. Then, I swing the pen a few more times and run."

    scene bg pen_run
    vl "Caramel? What is this?"

    "I faintly hear Vanilla Latte say something, but I keep running."

    cm "Hahaha! Now that its charm's disappeared, nobody'll love it anymore. Mwahahaha!"
    vl "Hey!"

    "{b}Good Ending{/b}."
    return

    # This ends the game.

    return
