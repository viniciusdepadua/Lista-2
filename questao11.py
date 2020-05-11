def speak_formation_futsal(*arguments, **keywords):
    for args in arguments:
        print(args)
    print("-" * 40)
    keys = sorted(keywords.keys())
    for key in keys:
        print(key + ":" + keywords[key])


speak_formation_futsal("There will be 5 player.", "The coach chooses them.", "The team has to win.",
                       "Best formation is:", GK='A tall guy', ZB="Two big guys",
                       CM="A clever guy", LF="Two skilled guys")
