def get_user_input(prompt):
    answer = input(prompt+" ").strip().lower()
    print()
    return answer


answer = get_user_input("Do you want to play? [yes] or [no]")
end_greet = "\n\nYour journey ends here. Thank you for playing."

if answer == "yes":
    answer = get_user_input("you think of exploring today. where would you go [mountain] or [woods]")
    if answer == "mountain":
        answer = get_user_input("You reached the foot of the mountain. Do you want to [climb] or [trek]")
        if(answer == "climb"):
            answer = get_user_input("you tried to climb the mountain, but now your rope is stuck half way. what would you do ? [call for help] or [help yourself] ")
            if answer == "call for help":
                answer = get_user_input("There is no service. you should do something now, the rope won't hold much longer... call again] or [help yourself]")
                if answer == "call again" or "help yourself":
                    print("Too late. The rope broke and you fell down." + end_greet)
            elif answer == "help yourself":
                answer = get_user_input("You see a ledge where you could jump by cutting the rope or try to free the rope. [jump to ledge] or [free rope]")
                if answer == "free rope":
                    print("you lost your foot and fell down while trying to free the rope." + end_greet)
    elif answer == "woods":
        answer = get_user_input("You went to woods and you meet a stranger with a strange appearence with a strange liquid which has a strange smell. Do yo accecpt it? [yes] or [no]")
        if answer == "yes":
            print("You drink and it Gave you Captain America Powers. You've won the quest!")
        else: 
            print("You didn't drink and the stranger killed you because he thought that was strange." + end_greet)
else: 
    print("Goodbye")
    exit()