# The script of the game goes in this file.

define p = Character("[player]", color="#c8c8ff")
define c = Character("Co-worker")
define m = Character("[employee]", color="#ffffd3")
define s = Character(_("Serenity"), color="#c8ffc8")
define l = Character(_("[cat]"), color="#966fd6")

image coffee = im.Scale("bg coffee.jpeg", 1300, 1000)
image black = im.Scale("bg black.jpeg", 1300, 1000)
image mascot = im.Scale("bg street.jpeg", 1300, 800)
image outside_entrance = im.Scale("bg storefront.jpeg", 1300, 780)
image cafe = im.Scale("bg cafe.jpg", 1300, 1000)
image latte = im.Scale("bg latte.jpg", 1300, 800)
image serenity = im.Scale("Hana/Maid/Hana_maid_smile.png", 400, 700)
image serenity_upset = im.Scale("Hana/Maid/Hana_maid_upset.png", 400, 700)
image luna = im.Scale("bg cat.jpeg", 1300, 750)
image couch_cat = im.Scale("bg rest cat.jpeg", 1300, 750)


# The game starts here.

init python:
    actions = []
    class Action(object):
        """
        Represents a label that we can jump to.
        """

        def __init__(self, label, title):
            self.kind = "action"
            self.label = label
            self.title = title

            actions.append(self)

    Action("action_cat", _("Play with a cat"))
    Action("action_rest", _("Rest on the couch"))
    Action("action_latte", _("Drink a latte"))

screen actions(adj):

    frame:
        xsize 640
        xalign .5
        ysize 485
        ypos 30

        has side "c r b"

        viewport:
            yadjustment adj
            mousewheel True

            vbox:
                for i in actions:

                    if i.kind == "action":

                        textbutton i.title:
                            action Return(i)
                            left_padding 20
                            xfill True

                    else:

                        null height 10
                        text i.title alt ""
                        null height 5




        bar adjustment adj style "vscrollbar"

        textbutton _("Head Home"):
            xfill True
            action Return(False)
            top_margin 10


default options_first_time = True
default actions_adjustment = ui.adjustment()

label start:
    window show
    scene coffee


    $ player = renpy.input("What is your name?")
    $ player = player.strip()

    if not player:
         $player = "Average Joe"
    # $ employee = "Cafe Employee"
    $ cat = "???"

    "Welcome to \"Cuddles N Coffee\" [player]!"
    "This is an iyashi visual novel centered around a cat cafe.
    We hope that this is a healing experience!"
    "We shall now proceed with the game."

    scene bg busy street
    play music "audio/joyful_love.mp3" volume 0.5 loop

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
    "It seems like you bumped into something incredibly fuzzy and then fell to the floor."
    $ employee = "???"
    m "Are you alright!?"

    scene mascot
    play music "audio/joyful_love.mp3" volume 0.5 loop

    "You open your eyes to a startled person in a cat costume.
    They are wearing a big sign advertising a cat cafe.
    After getting up and regaining your senses you answer the concerned employee."

    $ employee = "Cafe Employee"

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

    "What a homely place!"
    "The cafe is nice and quiet. Immediately, you can spot a few cats roaming about."
    "You can smell a light, sweet scent from the back of the cafe.
    There are all kinds of cushions and comfort items that remind you of home."
    "The place is a bit messy for a cafe, but this strikes you as a suprisingly plesant feature."
    "Having stuff around makes you feel at ease compared to the usual prim and perfect
    restaurants your company sends you to for meetings."
    "Perhaps, it's the imperfection of the place that makes it seem more comfortable."

    show serenity
    s "Welcome to Cuddles N Coffee, home of the most cuddly cats and cutest
    latte art! My name is Serenity. How may I help y-"
    show serenity_upset
    s "Tran? Why are you inside? Tran Anne Quility please tell me you
    need more pamphlets and didn't pressure this customer to our cafe."

    $ employee = "Cafe Employee (Tran)"
    m "Serenity! I accidently bumped into this person and since they seemed
    hurt I invited them inside."
    s "*sigh*"
    hide serenity_upset
    show serenity
    s "You are always so clumsy."
    s "I apologize for our employees clumsiness. There's some dirt on your arms.
    Let's get you cleaned up. Tran, you can head out I'll take care of this."

    play sound "audio/door.mp3"

    "The cafe employee known as \"Tran\" heads out. Although they were bickering,
    it seems like they are good friends. Serenity heads to the back
    of the cafe and brings you a clean, hot towel. You wipe off the dirt and
    hand it back. "

    s "Although this must have been a rough evening for you, I hope you enjoy
    your time at Cuddles N Coffee. Have you ever been to a cat cafe before?"

    menu:
        "Yes":
            "That's great! I'm sure the cats will be happy to meet you."
        "No":
            "Serenity proceeds to explain the nature of cat cafes. She
            instructs you to be careful around the cats and avoid disturbing
            the ones that are sleeping."
    s "Let me show you what the cafe has to offer."
    "Serenity hands you some hand sanitizer and then presents you a pamphlet
    with different options of what to do."
    s "Please feel free to explore the cafe and use the place as you would like!"
    hide serenity
    jump options

label options:
    scene cafe
    show serenity
    show serenity at left
    with move

    if options_first_time:
        $ s(_("What would you like to do?"), interact=False)
    else:
        $ s(_("Is there anything else you'd like to do?"), interact=False)

    $ options_first_time = False
    $ renpy.choice_for_skipping()

    call screen actions(adj=actions_adjustment)

    $ action = _return

    if not action:
        jump end

    call expression action.label from _call_expression

    jump options


label end:
    "You tell Serenity you need to leave. She takes a commemorative photo of you
    and the cats. After saying goodbye to the cats you take your leave."
    play sound "audio/door.mp3"
    scene bg busy street
    stop music fadeout 1.0
    "As you walk back home, you feel a lot more energetic. Maybe you should go
    back again tomorrow."

    return
