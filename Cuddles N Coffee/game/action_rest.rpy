label action_rest:
    s "You can rest on that couch over there."
    hide serenity
    "You take a seat on the comfy couch."
    "Your head is still pounding from work and the fall, so you lean your head
    on one of the many soft pillows. You close your eyes."
    stop music fadeout 2.0
    play music "audio/daffodil.mp3" volume 0.5 loop fadein 2.5
    "You listen as the cafe radio changes songs."
    "(the sound of positive, peaceful music)"
    "(the sound of your stress melting away)"
    "(the sound of you slowly falling asleep)"
    "(the sound of you reading closed captions)"
    "(the sound of paws pattering on the ground)"
    play sound "audio/door.mp3"
    "(the sound of the door opening)"
    "(the sound of footsteps)"
    "(the sound of time passing)"
    "(the sound of fur sweeping across your nose)"
    "Wait what?"
    "You open your eyes."
    scene couch_cat
    "There is a small light grey kitten sitting on the pillow next to you. It
    seems like the tail of this kitten made its way to your unsuspecting
    sleeping face."
    "Its mischievous nature reminds you of your younger sister and
    the pranks she would play on you when you were kids. So nostalgic."
    "After watching the small kitten for a while, you decide to get up."
    scene cafe
    "You head back to Serenity at the front desk."
    stop music fadeout 1.0
    play music "audio/joyful_love.mp3" volume 0.5 loop
    return
