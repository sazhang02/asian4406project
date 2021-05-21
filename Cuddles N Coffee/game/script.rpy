# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.

define p = Character("[player]", color="#c8c8ff")
define c = Character("Co-worker")
define m = Character("Cafe Employee")

image coffee = im.Scale("bg coffee.jpeg", 1300, 1000)
image black = im.Scale("bg black.jpeg", 1300, 1000)
image mascot = im.Scale("bg street.jpeg", 1300, 800)
image outside_entrance = im.Scale("bg storefront.jpeg", 1300, 780)
image cafe = im.Scale("bg cafe.jpg", 1300, 1000)
image latte = im.Scale("bg latte.jpg", 1300, 800)


# The game starts here.

label start:

    scene coffee

    $ player = renpy.input("What is your name?")
    $ player = player.strip()

    if not player:
         $player = "Average Joe"

    # show eileen happy

    "Welcome to \"Cuddles N Coffee\" [player]!"
    "This is an iyashi visual novel centered around a cat cafe.
    We hope that this is a healing experience!"
    "We shall now proceed with the game."

    scene bg busy street
    play music "audio/daffodil.mp3" volume 0.5 loop

    "9 P.M."
    "Another day of working overtime."
    "Exhausted from a long day of work, you walk slowly down your normal
    route home. The busy streets make you feel lonely."
    "How long has it been since you have seen your family? Actually, how long
    has it been since you have seen anyone?"
    "You let out a sigh. It's hard to visit your family these days due to your
    endless work. Not to mention, your younger sister just got married and the
    couple makes you feel awkward in your family home."
    "Thinking of family, you recall a conversation you had at work today with
    a co-worker."

    c "Look at this kitty! I took this picture at the new cat cafe that opened
    up on 92th avenue. My niece has been incredibly stressed recently with
    college applications so I took her there to relax."
    c "You should go, it was such a healing experience. It was
    so cute when the cat ju-"

    stop music
    scene black
    play sound "audio/bump.mp3"
    "BANG"
    stop sound
    "It seems like you bumped into something incredibly fuzzy."
    "???" "Are you alright!?"

    scene mascot
    play music "audio/daffodil.mp3" volume 0.5 loop

    "You open your eyes to a startled person in a cat costume.
    They are wearing a big sign advertising a cat cafe.
    After regaining your senses you answer the concerned employee."

    p "I'm alright."
    "As you respond, you feel yourself tipping over. Luckily you were able
    to catch yourself. You feel a bit dizzy from the collision. All those
    long nights in the office must have weakened your physical state."

    m "Oh no! You don't seem alright. I work at the Cuddles N Coffee down 92th
     avenue. It's just right around the corner. If you would like, you can rest
     up for a bit there. Free of charge, as an apology for bumping into you."

    menu:
        "Go to cafe":
            p "Sure! That would be great, thanks."
        "Go home":
            p "Unfortunately, I have somewhere to go but thanks for the offer!"
            scene bg busy street
            stop music fadeout 1.0
            "You continue back home, still exhausted from this long day. Will
            tomorrow be just the same?"
            return
            #ENDING HOME


    "You and the employee head off to Cuddles N Coffee. You remember that this
    is the place your co-worker wouldn't stop talking about."

    scene outside_entrance

    m "Here we are!"

    "As it is a new store, the front of the cafe features a simple look.
    If the employee didn't bring you to the entrance, you would have never
    noticed this place."
    "This seems like a rare space that doesn't get too many
    customers. Its hiddenness reminds you of the Midnight Diner restaurant
    you saw on Netflix."

    "You enter the cafe."

    play sound "audio/door.mp3"
    scene cafe

    "What a homely place"
    scene latte
    "nice"




    # This ends the game.
    return
