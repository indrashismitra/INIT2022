from random import randint
black_cards = ["What did I bring back from Mexico?", "In Michael Jackson's final moments, he thought about ________.", "Please don't put _ in your mouth.",]
white_cards = ["\"Tweeting.\"","(I am doing Kegels right now.)","10,000 Syrian refugees.","100% Pure New Zealand.","2 Girls 1 Cup.",
               "400 years of colonial atrocities.","50 mg of Zoloft daily.",
               "50,000 volts straight to the nipples.","72 virgins.",
               "8 oz. of sweet Mexican black-tar heroin.","A bag of magic beans.",
               "A balanced breakfast.","A big hoopla about nothing.","A bird that shits human turds.",
               "A bit of slap and tickle.","A bitch slap.","A bleached arsehole.","A bleached asshole.",
               "A Bop It™.","A bowl of mayonnaise and human teeth.","A brain tumor.","A brain tumour.",
               "A bucket of fish heads.","A can of whoop-ass.","A caress of the inner thigh.",
               "A cartoon camel enjoying the smooth, refreshing taste of a cigarette.",
               "A cat with... hands.","A cherry-wood spanking bench.",
               "A Chinese tourist who wants something very badly but cannot communicate it.",
               "A clandestine butt scratch.","A cooler full of organs.","A copy of Bedside Hitler.",
               "A crucifixion.","A cute, fuzzy koala, but it has chlamydia.","A death ray.",
               "A decent fucking Internet connection.","A defective condom.",
               "A despondent Maple Leafs fan sitting all alone.","A didgeridildo.","A disappointing birthday party.",
               "A drive-by shooting.","A fair go.","A falcon with a cap on its head.","A fat bald man from the internet.",
               ]
users = int(input("Enter the number of users\n"))
while True:
    print("Black card: " + black_cards[randint(0,len(black_cards)-1)])
    input()
    print("White cards:")
    for i in range(users):
        print(white_cards[randint(0,len(white_cards)-1)])
    input()