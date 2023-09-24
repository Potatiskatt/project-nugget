# Character names
define d = Character('DEX', color="#ffffff")
define j = Character('JASPER', color="#ffffff")
define lb = Character('LADY BELLA', color="#ffffff")
define ll = Character('LADY LUNA', color="#ffffff")
define n = Character('NUGGET', color="#ffffff")
define p = Character('PEANUT', color="#ffffff")
define s = Character('SABINE', color="#ffffff")
define z = Character('ZMEYA', color="#ffffff")

# Character variables
default dex = False
default jasper = False
default ladies = False
default peanut = False
default sabine = False
default zmeya = False

# Peanut choices
default cupcakes = False
default caramel = False
default pie = False

# Dex choices
default fireworks = False
default pyro = False
default film = False

# Zmeya choices
default brew = False
default poison = False
default punch = False

# Character pictures

#   image d ... = "dex/filename.png"

#   image j ... = "jasper/filename.png"

#   image lb ... = "lady bella/filename.png"

#   image ll ... = "lady luna/filename.png"

image n closed eyes = "nugget/n_closed_eyes.png"
image n open eyes = "nugget/n_open_eyes.png"
image n worried = "nugget/n_worried.png"

image p closed eyes = "peanut/p_closed_eyes.png"
image p open eyes = "peanut/p_open_eyes.png"
image p worried = "peanut/p_worried.png"

#   image s ... = "sabine/filename.png"

#   image z ... = "zmeya/filename.png"

# Background pictures
image bg test = "background/test.png"
#   image bg main menu = "background/main_menu.png"
#   image bg pause menu = "background/pause_menu.png"
#   image bg town = "background/town.png"
#   image bg dex = "background/dex.png"
#   image bg jasper = "background/jasper.png"
#   image bg ladies = "background/ladies.png"
#   image bg peanut = "background/peanut.png"
#   image bg sabine = "background/sabine.png"
#   image bg zmeya = "background/zmeya.png"
#   image bg party = "background/party.png"

# The game starts here.

label start:

    scene bg test
    with fade
    show n open eyes at center

    n "Today is finally the day, October the 31st, also known as HALLOWEEN!"
    
    hide n open eyes
    show n closed eyes at center

    n "There are only a few hours until it's party time, so everything must get done before that."

    hide n closed eyes with dissolve
    
    "You need to check in on everyone to make sure they are ready. It's an all-hands-on-deck situation."

    jump talk

label talk:

    menu:

        #"Check in on:"
        
        "Talk to Peanut":
            if peanut == False:
                jump PeanutDialogue

            elif cupcakes == True:
                jump CupcakesChoice
            
            elif caramel == True:
                jump CaramelChoice

            elif pie == True:
                jump PieChoice

        "Talk to Dex":
            if dex == False:
                jump DexDialogue

            elif fireworks == True:
                jump FireworkChoice

            elif pyro == True:
                jump PyroChoice

            elif film == True:
                jump FilmChoice
    
        "Talk to Zmeya":
            if zmeya == False:
                jump ZmeyaDialogue

            elif brew == True:
                jump BrewChoice

            elif poison == True:
                jump PoisonChoice

            elif punch == True:
                jump PunchChoice
        
        "Talk to Lady Bella and Lady Luna":
            jump LadiesDialogue
        
        "Talk to Sabine":
            jump SabineDialogue
        
        "Talk to Jasper":
            jump JasperDialogue
        
        "Get yourself ready for the Halloween party":
            jump HalloweenParty

label PeanutDialogue:

    $ peanut = True

    "You walk through the door to the town's bakery and are met with the smell of sweet baked goods. In the displays, you can see many types of cupcakes with different designs and decorations. Your mouth starts to water, and then you hear someone running down from the upper level, panting and with a great smile on his face."
    
    show p open eyes at right with vpunch

    p "HELLO NUGGIE!!!"

    hide p open eyes
    show n closed eyes at left

    n "HELLO!"

    hide n closed eyes
    show p closed eyes at right
    
    p "HOW CAN I HELP YOU???"

    hide p closed eyes
    show n open eyes at left
    
    n "It's time to start preparation for the Halloween party, so we need your amazing baked goods!"

    hide n open eyes
    show p open eyes at right
    
    p "YES, AND IT'S GONNA BE SO FUN!!! WHAT DO YOU WANT ME TO MAKE?"

    hide p open eyes

    menu:

        "Halloween themed cupcakes.":
            jump CupcakesChoice

        "Caramel apples.":
            jump CaramelChoice

        "Pumpkin pie.":
            jump PieChoice

label CupcakesChoice:

    if cupcakes == False:
    
        $ cupcakes = True

        show p open eyes at right
    
        p "OOOOH!!! I LOVE MAKING CUPCAKES, AND MAKING THEM HALLOWEEN THEMED WILL BE SO FUN!!!"

        hide p closed eyes
        show n open eyes at left

        n "Yey!"

        hide n open eyes

        "Peanut starts rummaging around in the kitchen, throwing things all over the place."

        show n worried at left

        n "Anyway, GOODBYE!"

        hide n worried
        show p closed eyes at right
        
        p "GOODBYE!!!"

        hide p closed eyes
    
        jump talk

    else:

        "You walk through the door to the town's bakery and are met with the same, sweet smell of baked goods. In the displays you see many types of cupcakes and around the shop you see your best friend Peanut run around with cupcake tins, piping bags, flour bags and more. Best not to disrupt his work."
    
        jump talk

label CaramelChoice:

    if caramel == False:
        
        $ caramel = True

        show p worried at right
    
        p "OKAY, IT'S NOT ANYTHING LIKE CUPCAKES, BUT CARAMEL APPLES ARE DELICIOUS!!!"

        hide p worried
        show n worried at left
        
        n "Great!"

        hide n worried

        "Peanut starts rummaging around in the kitchen, throwing things all over the place."

        show n closed eyes at left

        n "So anyway, GOODBYE!"

        hide n closed eyes
        show p closed eyes at right
        
        p "GOODBYE!!!"

        hide p closed eyes
    
        jump talk

    else:

        "You walk through the door to the town's bakery and are met with the same, sweet smell of baked goods. In the displays you see many types of cupcakes and around the shop you see your best friend Peanut run around with sticks, apples, brown sugar and whatnots. Best not to disrupt his work."
        
        jump talk

label PieChoice:

    if pie == False:
        
        $ pie = True

        show p open eyes at right
    
        p "PIES ARE ALMOST LIKE CUPCAKES, AND THAT IS AMAZING!!!"

        hide p open eyes
        show n open eyes at left
        
        n "Wonderful!"

        hide n open eyes

        "Peanut starts rummaging around in the kitchen, throwing things all over the place."

        show n worried at left

        n "Anyhow, GOODBYE!"

        hide n worried
        show p closed eyes at right
        
        p "GOODBYE!!!"

        hide p closed eyes
    
        jump talk

    else:

        "You walk through the door to the town's bakery and are met with the same, sweet smell of baked goods. In the displays you see many types of cupcakes and around the shop you see your best friend Peanut run around with pie dishes, cans of puréed pumpkins, various spices, and other stuff. Best not to disrupt his work."
    
        jump talk

label DexDialogue:

    $ dex = True

    "You open the door to the EXPLOSIVE Lights shop and are met with a small explosion. Knowing Dex, there is an equal chance that it was meant to explode, or not."

    n "Hello, Dex!"
    d "My Liege! What can I do for you?"
    n "I've come to make a reminder about tonight's festivities and the entertainment you are supposed to provide."
    d "Ahh, yes! YES! I need you to help me make up my mind on what will be the best sort of entertainment."
    d "Fireworks, a pyrotechnic show, or maybe just a film on a big screen"

    menu:

        "Firework show.":
            jump FireworkChoice
        
        "Pyrotechnic show.":
            jump PyroChoice
        
        "Halloween film on a big screen.":
            jump FilmChoice

label FireworkChoice:

    if fireworks == False:

        $ fireworks = True

        d "I will NEVER say no to a good, massive firework show!"
        n "What… What was that about massive fireworks???"
        d "Ah! Nothing that will go wrong."
        n "Okay, that's go-"
        d "Probably."
        n "Probably?"
        d "Do not worry, my Liege, everything will go as planned! Now, go! I have work to do."

        jump talk
    
    else:
    
        "You get close to the door of Dex's shop, and smell something burning. Best not disturb them right now."

        jump talk

label PyroChoice:

    if pyro == False:

        $ pyro = True

        d "I can't wait for the whole town to see a close-up pyrotechnic show!"
        n "Close-up???"
        d "Oh, but it's nothing that would go wrong."
        n "Okay, that's go-"
        d "Probably."
        n "Probably?"
        d "Do not worry, my Liege, everything will go as planned! Now, go! I have work to do."

        jump talk
    
    else:
    
        "You get close to the door of Dex's shop, and smell something burning. Best not disturb them right now."

        jump talk

label FilmChoice:

    if film == False:

        $ film = True

        d "I guess a film night can't go wrong…"
        n "It would be impressive if something would go wrong."
        d "Maybe if we add-"
        n "Just a film! Please, Dex."
        d "Just a film it is, my Liege."

        jump talk
    
    else:
    
        "You get close to the door of Dex's shop, and smell something burning. Best not disturb them right now."

        jump talk

label ZmeyaDialogue:

    if zmeya == False:

        $ zmeya = True

        "After taking a boat to the swamp, you have reached the cabin. The door takes a little force to open, but that door is no match for your strength."

        n "HELLO!"
        z "..."
        z "Hello?"
        z "..."
        n "..."
        z "What do you need of me, little Wizard?"

        menu:

            "Witches' brew.":
                jump BrewChoice

            "Poisoned apple cider.":
                jump PoisonChoice

            "Harvest punch.":
                jump PunchChoice

    else:

        "After taking a boat to the swamp, you have reached the cabin. From inside the cabin, you hear Zmeya hum a melody. This time, it takes less force to open the door. You look at her and she looks back."

        if brew == True:
            
            z "..."
            n "..."
            n "I was j-"
            z "Witches' brew, yes…"
            n "Yes, exactly... GOODBYE!"
                
            jump talk

        elif poison == True:
            
            z "..."
            n "..."
            n "I was j-"
            z "Poisoned apple cider, yes…"
            n "Yes, exactly… GOODBYE!"
                
            jump talk

        elif punch == True:
            
            z "..."
            n "..."
            n "I was j-"
            z "Harvest punch, yes…"
            n "Yes, exactly… GOODBYE!"
                
            jump talk

label BrewChoice:

    $ brew = True

    z "Yes, that will do nicely..."
    n "Oh, good!"
    z "..."
    n "..."
    n "Well, GOODBYE!"

    jump talk

label PoisonChoice:
    
    $ poison = True

    z "Yes, that will do nicely..."
    n "Oh, good!"
    z "..."
    n "..."
    n "Well, GOODBYE!"

    jump talk

label PunchChoice:
    
    $ punch = True

    z "Yes, that will do nicely..."
    n "Oh, good!"
    z "..."
    n "..."
    n "Well, GOODBYE!"

    jump talk

label LadiesDialogue:

    if ladies == False:

        $ ladies = True
    
        "You walk into the farmhouse, like you have done many times before, and are met with a warm feeling. It's nice, and warm inside the house. From the kitchen, you hear two of your favourite dogs talking, and laughing."

        lb "Oh, hello honey!"
        ll "Hi, little one!"
        n "Hey! How are you both?"
        ll "Oh, we are just fine. How about you?"
        n "I'm all good!"
        lb "I'm guessing you are going around, checking if everyone is ready, or are getting ready for this evening's festivities?"
        n "Yes I am!"
        ll "And, I'm guessing that you are excited for tonight?"
        n "As always!"
        ll "Don't worry about the food, we are going to make food to feed the town twice!"
        n "Of course you will. Well, I'll see you both later!"
        ll "Goodbye, little one!"
        lb "Bye, Sweetie!"
    
        jump talk

    else:

        "You walk into the farmhouse again, like many times before, and earlier today. As before, the house is nice, and toasty. You hear Lady Bella, and Lady Luna from the kitchen. It already smells of all kinds of apples, spices and other foods."

        ll "Welcome back, little one."
        n "Hey! I just wanted to check in on you."
        ll "We are doing fine, and are getting everything ready."
        lb "We are making sure that we have enough of all ingredients for the feast, or if we need to go out to gather anything more."
        ll "I think we got everything covered."
        lb "But it never hurts to be extra sure, isn't that right?"
        n "Better be safe, than sorry!"
        lb "I know we raised you well!"
        ll "We did, but if we want to make sure to have everything ready in time, we best get on with the cooking."
        n "I'll leave you to it, see you later!"
    
        jump talk

label SabineDialogue:

    if sabine == False:

        $ sabine = True
    
        "You're getting close to a smaller, dark dog with yellow eyes, that is also covered in mummy rags. She looks excitedly, tail wagging, as she sees Nugget, but stays where she is."

        s "Heya, Nuggie."
        n "Heya Sabine!"
        s "..."
        n "Are you excited about the Halloween party tonight?"
        s "Yes! Very much! I have almost got all the decorations ready."
        n "That's amazing, Sabine!"
        s "Ooh, thank you."
        n "I'll let you get on with your work then, and I'm excited to see what you have created later!"
        s "Yes, I hope everyone will be pleased."
        n "I'm sure we'll all be! Goodbye, Sabine!"
        s "Bye Nuggie."
    
        jump talk

    else:

        "As you walk closer to Sabine again, she reacts the same way. Looks excitedly at Nugget, wagging her tail, but staying where she is."

        n "Heya again, Sabine!"
        s "Heya again, Nuggie."
        n "How's it going?"
        s "It's going well, thank you."
        n "That's great, I'll let you get on with it! Goodbye!"
        s "Bye."
    
        jump talk

label JasperDialogue:

    if jasper == False:

        $jasper = True
    
        "You approach Jasper, the Dalmatian dog, who seems to have a pumpkin on his head. You could say that some dogs have their heads in the clouds, this one has got its head in a pumpkin."

        n "Hey Jasper!"
        j "Oh, Nugget, is that you? I can't see you… due to the pumpkin on my head."
        n "Yes, what happened Jasper?"
        j "I got my head stuck, and I can't get out."
        n "Well, that could happen to anyone, I guess."
        j "I guess so… Anyway, can I do anything for you?"
        n "Not really, I just wanted to check in on you!"
        j "Thanks!"
        n "Anyway, I'll see you later at the Halloween party!"
        j "Oh wait, that's today? I really should get my head out of this pumpkin bef-"
        
        jump talk

    else:

        "You approach Jasper, the Dalmatian dog, whose head still seems to be stuck in the pumpkin. This time there are eyes carved out in the pumpkin."

        n "Still stuck in the pumpkin?"
        j "Yes, but Peanut came and helped me carve out eye holes so I can see you now!"
        n "Why didn't he help you get the pumpkin off your head?"
        j "..."
        n "Neither of you thought about getting the pumpkin off?"
        j "No..."
        n "Weeeeeeeell, goodbye Jasper!"
        j "Goodbye..."
        
        jump talk

label HalloweenParty:

    if peanut == False and dex == False and zmeya == False:

        show n worried

        n "I still haven't checked in on Peanut about the baked goods, Zmeya about drinks, and Dex about the entertainment, and I need to get those things done before I can get ready myself."

        hide n worried
    
        jump talk
    
    elif peanut == False and dex == False and zmeya == True:

        show n worried

        n "I still haven't checked in on Peanut about the baked goods, and Dex about the entertainment, and I need to get those things done before I can get ready myself."

        hide n worried
    
        jump talk

    elif peanut == False and dex == True and zmeya == False:

        show n worried

        n "I still haven't checked in on Peanut about the baked goods, and Zmeya about drinks, and I need to get those things done before I can get ready myself."

        hide n worried
    
        jump talk
    
    elif peanut == False and dex == True and zmeya == True:

        show n worried

        n "I still haven't checked in on Peanut about the baked goods, and I need to get those things done before I can get ready myself."

        hide n worried
    
        jump talk
    
    elif peanut == True and dex == False and zmeya == False:

        show n worried

        n "I still haven't checked in on Zmeya about drinks, and Dex about the entertainment, and I need to get those things done before I can get ready myself."

        hide n worried

        jump talk
    
    elif peanut == True and dex == True and zmeya == False:

        show n worried

        n "I still haven't checked in on Zmeya about drinks, and I need to get those things done before I can get ready myself."

        hide n worried
    
        jump talk
    
    elif peanut == True and dex == False and zmeya == True:

        show n worried

        n "I still haven't checked in on Dex about the entertainment, and I need to get those things done before I can get ready myself."

        hide n worried
    
        jump talk

    elif peanut == True or dex == True or zmeya == True:

        show n closed eyes

        n "I have made sure the baked goods, entertainment and drinks are all ready for the party. Now I just have to get myself ready for it!"

        "As you walk out from your home, you see the town square looking amazing! Every dog in town is there, and seem to be enjoying themselves, including Zmeya. You see that the baked goods are quickly being eaten, the drinks being slurped up, and Dex setting up the entertainment..."

        hide n closed eyes

        # show EN BAKGRUNDS BILD SOM VISAR ALLA PÅ FESTEN

        jump credits

label credits:

    "Sam Lövstad - Narrative, Writing, Design, Programming"
    "~ samlovstad.itch.io ~"

    "Jonna Persson - Art (character, backgrounds)"
    "~ link to something ~"

    # music credits

    return