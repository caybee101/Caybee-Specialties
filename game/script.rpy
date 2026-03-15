# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.


# The game starts here.
define a= Character("Cate")
define c= Character("Christin")
define s= Character("Sebastian")
define n= Character("Narrator")
define h= Character("Hooded figure")

image 1= "argue.png"
image 2= "baby.jpeg"
image 3= "bblue.jpg"
image 4= "bdown1.png"
image 5= "bdown2.png"
image 6= "bdown3.png"
image 7= "bleo.jpg"
image 8= "blue.jpeg"
image 9= "bobb.jpg"
image 10= "bobl.jpg"
image 11= "bobs.jpg"
image 12= "bobsuit.jpg"
image 13= "bobw.jpg"
image 14= "bsuit.jpg"
image 15= "bsweater.jpg"
image 16= "bwhite.jpg"
image 17= "cblue.bmp"
image 18= "closet.jpeg"
image 19= "csuit.png"
image 20= "curlyleo.png"
image a= "curlysweater.png"
image b= "cwhite.png"
image c= "face.png"
image d= "hood.png"
image e= "hood1.jpeg"
image f= "leo.jpeg"
image g= "pblue.png"
image h= "pleo.png"
image i= "psuit.png"
image j= "psweat.png"
image k= "pwhite.png"
image l= "reco.png"
image m= "sblue.jpeg"
image n= "sleo.jpeg"
image o= "ssuit.jpeg"
image p= "ssweat.jpeg"
image q= "suit.jpeg"
image r= "sweater.jpeg"
image s= "swhite.jpeg"
image t= "bye.png"
image u= "white.jpeg"
image v= "wreco.png"
image w= "argue2.png"
image x= "bath.png"
image y= "in.png"
image z= "storm.jpeg"
image 1a= "out1.png"
image 1b= "out2.png"
image 1c= "out3.png"
image 1d= "out4.png"
image 1e= "reco2.png"
image 1f= "reco3.bmp"
image 1g= "storm1.png"
image 1h= "hood3.webp"
image 1i= "hood2.webp"
image 1j= "bye.png"
image 1k= "drive.png"
image 1m= "outc1.png"
image 1n= "outcb.png"    
image 1o= "ex.png"
image 1p= "call.png"   
#Setting up money bar

label main_menu:

default money=1500

screen money_bar:
    frame:
        xalign 0.0
        yalign 0.0
        text "💶Money: [money]"
show screen money_bar


#Setting up gem bar

default gems=300
screen gem_bar:
    frame:
        xalign 1.0
        yalign 0.0
        text "💎Gems:[gems]"
show screen gem_bar


# Setting up start-up interface

scene black
show text "My Game" at truecenter with dissolve
menu:
    "Start Game":
        jump begin
    "Quit":
        $ renpy.quit()




label begin:    
    play sound "Bg audio.mp3"
    show 1
    c "You know what, Sebastian? I'm done playing cool with all your cheating scandals!"
    show w
    s "Christy, please calm down. Lets-"
    show 1
    c "Don't try to interject when i'm speaking, Sebastian!" 
    c "Hadn't we agreed on surrogacy, huh?! So what's all this Amanda crap I'm seeing in your phone?!"
    show w
    s "My love, can we just-"
    scene black
show 4
menu:
    "Listen          💎10":
        if gems >=10:
            $ gems -=10
            "You listen"
            jump listen
        
    "Ignore him":
     jump ignore
    
label listen:
    "+1 love❤️"
    scene black
    show 5
    n "Christin sits on the edge of the bed and puts her head in her hands"
    s "I'm really sorry, my love"
    s "It was never my intention, not at all, to hurt you"
    n "Christin shakes her head and sniffles"
    scene black
    show 1
    s "I swear, if you'll have me, to cut all ties with her. To be a better husband. For you. No more cheating"
    scene black
    show l
    c "What makes you think i'll trust you?"
    n "Sebastian looks sad and guilty"
    c "You have 1 last chance to prove yourself"
    scene black
    show 1e
    s "I promise i won't disappoint you, my love"
    c "I have a meeting. I have to go now"
    s "Ok. I have to leave soon too. Let me take a shower. Bye"
    c "Wait. I need to fix myself first"
    scene black
    show c
    n "She goes to the bathroom and washes her face then fixes her appearance"
    n "She returns to their room, takes her handbag and phone"
    scene black
    show v
    n "He kisses her forehead and goes to the bathroom"
    n "She then takes her phone and purse and leaves. Little does she know..."
   
    jump next_scene

    
label ignore:
    "+1 self-respect🫡"
    scene black
    show 1g
    c "You know what? I don't have the time and energy for this. I have a meeting"
    s "Ok then. I'll go take my shower, madam furious"
    scene black
    show z
    n "Christin clicks her tongue, takes her phone and purse and leaves. Little does she know..."
    jump next_scene
    
label next_scene:
    scene black
    show e    
    n "A few minutes ago..."
    h "I'm sorry but I think it's best i leave you, for your own good, child. I'll always love you and I will never forgive myself for this. I'll leave you here"
    h "This place looks creepy though. I want the best for you. I'll look for another place"
    scene black
    show d
    n "The hooded figure looks around and their eyes land on the mansion behind their current location"
    h "That looks perfect. I'll leave you there"
    scene black
    show 1h
    scene black
    show 1i
    n "Places the baby on the outside porch"
    scene black
    show 2
    n "The baby cries from the cold"
    scene black
    show x
    s "Who's crying outside?"
    scene black
    show s
    c "I don't know. It's probably our new neighbours' child"
    n "Back to initial scene..."
    scene black
    show 1a
    n "Christin is leaving. She opens the front door and to her surprise, there's a crying baby on the porch"
    
    n "Christin looks around for the owner who's nowhere to be seen"
    n "What will she do?"
menu:
    "Pick up baby":
        jump pick_up_baby
    "Leave the baby there":
        jump leave_baby
label pick_up_baby:
    scene black
    show 1b
    "..."
    scene black
    show 1c
    "..."

    scene black
    show 1d
    n "Christin picks up baby and cradles it in her arms"
    
    jump next_scene2

label leave_baby:
    "+1 cruelty😡"
    "+1 guilt😞"
    scene black
    show 1n
    n "Christin hesitates then decides to leave the baby"
    scene black
    show 1k
    n "She drives away but the guilt eats her away so much she returns"
    show 1m
    n "The poor baby is still there, alone, crying on the cold porch. The Early hours tend to be chilly"
    scene black
    show 1b
    scene black
    show 1c
    scene black
    show 1d
    n "She picks the baby"
    scene black
    jump next_scene2
label next_scene2:
    scene black
    show 1p
    c "Seb!"
    n "No response"
    n "Christin sets her things down and goes to look for Seb with the baby in her arms"
    c "Sebastian!"
    scene black
    show x
    s "I'm in the shower! You forgot anything?"
    c "No. Finish up"

# Selecting outfit

label start: 
    show 18
    "Select Your desired outfit"
    scene black
menu:
    "Homely outfit":
        jump of3
    "blue bodycon dress":
        jump outfit_1
    "white bodycon dress":
        jump of1
    "suit":
        jump of2
    "leopard print dress 💶100":
       jump outfit_2
   
label outfit_1:
    show 8
    "This is your new look. Are you sure you want it?"
menu:
    "Yes":
        scene black
        jump hairb
    "No":
        scene black
        jump start
label outfit_2:
    if money >=100:
        $ money -=100
        show f
        "This is your new look. Are you sure you want it?"
menu:
    "Yes":
        scene black
        jump hairl
    "No":
        scene black
        $ money += 100
        jump start

label of3:
    show r
    "This is your new look. Are you sure you want it?"
menu:
    "Yes":
        scene black
        jump hairh
    "No":
        scene black
        jump start

label of1:
    show u
    "This is your new look. Are you sure you want it?"
menu:
    "Yes":
        scene black
        jump hairw
    "No":
        scene black
        jump start
label of2:
    show q
    "This is your new look. Are you sure you want it?"
menu:
    "Yes":
        scene black
        jump hairs
    "No":
        scene black
        jump start
  

label hairh:
    scene black    
    
menu:
    
    "Hairstyle 1":
        jump hih
    


    "Hairstyle 2": 
        jump h2h

 
    "Hairstyle 3 💎10":
        jump h3h
        
    "Hairstyle 4 💎15":
        jump h4h

    "Hairstyle 5 💎15":
        jump h5h

label h5h:
    show j
    if gems >=15:
        $ gems -=15
    "This is your new look. Are you sure you want it?"
menu:
    "Yes":
        jump baby
    "No":
        scene black
        $ gems +=15
        jump hairh

label h4h:
    show a
    if gems >=15:
        $ gems -=15
    "This is your new look. Are you sure you want it?"
menu:
    "Yes":
        jump baby
    "No":
        scene black
        $ gems +=15
        jump hairh

label hih:
    show p
    "This is your new look. Are you sure you want it?"
menu:
    "Yes":
        jump baby
    "No":
        scene black
        jump hairh
label h2h:
    show 11
    "This is your new look. Are you sure you want it?"
menu:
    "Yes":
        jump baby
    "No":
        scene black
        jump hairh

label h3h:
    show 15
    if gems >=10:
        $ gems -=10
    "This is your new look. Are you sure you want it?"
menu:
    "Yes":
        jump baby
    "No":
        scene black
        $ gems +=10
        jump hairh

label hairb:
    scene black    
    
menu:
    
    "Hairstyle 1":
        jump hib
    


    "Hairstyle 2": 
        jump h2b

 
    "Hairstyle 3 💎10":
        jump h3b
        
    "Hairstyle 4 💎15":
        jump h4b

    "Hairstyle 5 💎15":
        jump h5b

label h5b:
    show g
    if gems >=15:
        $ gems -=15
    "This is your new look. Are you sure you want it?"
menu:
    "Yes":
        jump baby
    "No":
        scene black
        $ gems +=15
        jump hairb



label h4b:
    show 17
    if gems >=15:
        $ gems -=15
    "This is your new look. Are you sure you want it?"
menu:
    "Yes":
        jump baby
    "No":
        scene black
        $ gems +=15
        jump hairb

label hib:
    show m
    "This is your new look. Are you sure you want it?"
menu:
    "Yes":
        jump baby
    "No":
        scene black
        jump hairb
label h2b:
    show 9
    "This is your new look. Are you sure you want it?"
menu:
    "Yes":
        jump baby
    "No":
        scene black
        jump hairb

label h3b:
    show 3
    if gems >=10:
        $ gems -=10
    "This is your new look. Are you sure you want it?"
menu:
    "Yes":
        jump baby
    "No":
        scene black
        $ gems +=10
        jump hairb

label hairw:
    scene black    
    
menu:
    
    "Hairstyle 1":
        jump hiw
    


    "Hairstyle 2": 
        jump h2w

 
    "Hairstyle 3 💎10":
        jump h3w
        
    "Hairstyle 4 💎15":
        jump h4w

    "Hairstyle 5 💎15":
        jump h5w

label h5w:
    show k
    if gems >=15:
        $ gems -=15
    "This is your new look. Are you sure you want it?"
menu:
    "Yes":
        jump baby
    "No":
        scene black
        $ gems +=15
        jump hairw



label h4w:
    show b
    if gems >=15:
        $ gems -=15
    "This is your new look. Are you sure you want it?"
menu:
    "Yes":
        jump baby
    "No":
        scene black
        $ gems +=15
        jump hairw

label hiw:
    show 5
    "This is your new look. Are you sure you want it?"
menu:
    "Yes":
        jump baby
    "No":
        scene black
        jump hairw
label h2w:
    show 13
    "This is your new look. Are you sure you want it?"
menu:
    "Yes":
        jump baby
    "No":
        scene black
        jump hairw

label h3w:
    show 16
    if gems >=10:
        $ gems -=10
    "This is your new look. Are you sure you want it?"
menu:
    "Yes":
        jump baby
    "No":
        scene black
        $ gems +=10
        jump hairw

label hairs:
    scene black    
    
menu:
    
    "Hairstyle 1":
        jump his
    


    "Hairstyle 2": 
        jump h2s

 
    "Hairstyle 3 💎10":
        jump h3s
        
    "Hairstyle 4 💎15":
        jump h4s

    "Hairstyle 5 💎15":
        jump h5s

label h5s:
    show i
    if gems >=15:
        $ gems -=15
    "This is your new look. Are you sure you want it?"
menu:
    "Yes":
        jump baby
    "No":
        scene black
        $ gems +=15
        jump hairs



label h4s:
    show 19
    if gems >=15:
        $ gems -=15
    "This is your new look. Are you sure you want it?"
menu:
    "Yes":
        jump baby
    "No":
        scene black
        $ gems +=15
        jump hairs

label his:
    show o
    "This is your new look. Are you sure you want it?"
menu:
    "Yes":
        jump baby
    "No":
        scene black
        jump hairs
label h2s:
    show 12
    "This is your new look. Are you sure you want it?"
menu:
    "Yes":
        jump baby
    "No":
        scene black
        jump hairs

label h3s:
    show 14
    if gems >=10:
        $ gems -=10
    "This is your new look. Are you sure you want it?"
menu:
    "Yes":
        jump baby
    "No":
        scene black
        $ gems +=10
        jump hairs

label hairl:
    scene black    
    
menu:
    
    "Hairstyle 1":
        jump hil
    


    "Hairstyle 2": 
        jump h2l

 
    "Hairstyle 3 💎10":
        jump h3l
        
    "Hairstyle 4 💎15":
        jump h4l

    "Hairstyle 5 💎15":
        jump h5l

label h5l:
    show h
    if gems >=15:
        $ gems -=15
    "This is your new look. Are you sure you want it?"
menu:
    "Yes":
        jump baby
    "No":
        scene black
        $ gems +=15
        jump hairl


label h4l:
    show 20
    if gems >=15:
        $ gems -=15
    "This is your new look. Are you sure you want it?"
menu:
    "Yes":
        jump baby
    "No":
        scene black
        $ gems +=15
        jump hairl


label hil:
    show n
    "This is your new look. Are you sure you want it?"
menu:
    "Yes":
        jump baby
    "No":
        scene black
        jump hairl
label h2l:
    show 10
    "This is your new look. Are you sure you want it?"
menu:
    "Yes":
        jump baby
    "No":
        scene black
        jump hairl

label h3l:
    show 7
    if gems >=10:
        $ gems -=10
    "This is your new look. Are you sure you want it?"
menu:
    "Yes":
        jump baby
    "No":
        scene black
        $ gems +=10
        jump hairl



label baby:
    scene black
    
    show text "The game is still under development. More graphics will be added. Check back soon!" at truecenter with dissolve
    show text "Dialogue continues though" at truecenter with dissolve
    show text "" at truecenter with dissolve

    n "A few minutes later..."
    s "I'm done. What's wrong? Wait, who's that?"
    c "I found her on the porch on my way out"
    n "She looks up at him"
    c "There was no one around, no contact or anything. I guess she was abandoned..."
    s "So what's the way forward?"
    c "Let's take her in. I mean... we don't have any children and all... We can take her as our own... Hopefully it will also solve the Amanda problems too"
    n "She looks up at him"
    n "He lets out a humourless chuckle"
    s "Where'd you say you found this baby again?"
    c "The porch"
    s "You didn't steal the child just because of the Amanda thing?"
    c "You know I'm better than that, Sebastian!"
    s "Hey, Hey. Easy. I'm just messing with you. But we have to take her in legally."
    s "Like actually involve the cops, maybe child services and all... Just in case we are not found on the wrong side if the parents come to take her back"
    c "Ok then. Let me cancel my meeting so we can do so"
    n "She calls Justin, Her PA, to cancel all her agendas for today. Seb does the same and sits next to her"
    n "The baby starts crying"
    c "Hush, little one"
    c "What should we call her for now?"
    s "Sarah"
    c "Nope. That's too common"
    n "Christin looks down at the crying baby in her arms."
    c "You're so innocent, so pure, little one. I wonder why your parents did it."
    c "Wait. That's it! Pure!. Let's call her Pure!"
    n "Sebastian bursts out laughing at the ridicule of the name"
    s "Of all the names, Pure? At this point, Sarah is a whole league better"
    n "Christin scowls"
    c "Fine then. We'll look for alternatives to the name Pure"
    n "She takes out her phone and searches as she hushes the baby"
    c "There's Clara, Safiya, Katherine, ooh Caitlyn. How does that sound?"
    s "Perfect. It's unique and nice. And fits her perfectly"
    c "Great"
    c "Now we really need to get started on the arrangements of taking her in legally. But I think she's hungry. Let's pass through the grocery store and buy some formula"
    s "Alright. Let me take the keys"
    c "Let me quickly boil some water for the formula. Please hold her"
    n "They get their things then leave"
    n "They arrive at the grocery store"
    "Should she go in with him?"

menu:

    "Yes  💎10":
         if gems >=10:
            $ gems -=10
            "You go with him"

            jump yes

    "No":
        jump no

label yes:
    "+1 love ❤️"
    c "Let me come with you, Seb"
    n "Sebastian looks back at her"
    s "Will you be able to walk around with the baby?"
menu:
    "Yes":
        jump yes1
    "No":
        "Nevermind then"
        jump no

label yes1:
    "+1 love ❤️"
    s "Ok. Let me rush to the baby store to get you something to carry her in. Will be back in a bit. Here are the keys. You can open the windows if it gets too hot"
    n "He reaches over and kisses her cheek"
    n "He comes back after a while and opens the door for her"
    s "I found this. It should work just fine"
    n "He takes her hand and helps her out"
    n "He takes Caitlyn from her arms and helps Christin with the baby carrier"
    n "Together they leave hand in hand to the store"
    s "We need to get Caitlyn a sun hat. Its burning ouside."
    c "Yes. Sure"
    n "They get into the bustling store. Christin picks a basket which is immediately taken out of her hands by [s]"
    s "Let me carry it, love. You just make sure the baby is ok."
    c "Thank you"
    c "We need formula. There"
    n "She points and he picks it up."
    c "Diapers, a hat and some spare clothes. I think that will suffice for now. Let's go"
    s "Here's my card. You can proceed to the checkout. I need to grab a few things"
    c "The pin?"
    s "Our annivessary"
    n "[c] smiles"

label no:
    c "Can you please leave the windows open"
    s "You can open them. Here are the keys"
    n "Christin watches as her husband leaves. She notices the tension beginning to form between them"
jump main_menu
