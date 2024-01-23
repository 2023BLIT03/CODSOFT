import random
import re

class RuleBasedBot:
    negative_res = ("no","nope","nah","naw","never","not a chance","sorry")
    for_quit = ("quit","pause","exit","goodbye","bye","later")
    
    
    randomQuestions = (
        "How are you ?\n",
        "Are there many humans like you?\n",
        "what do you consume for sustence?\n",
        "Is there Intelligent life on this planet?\n",
        "what is engineer?\n"
    )
    
    def __init__(self):
        self.alienbabble = {
            'describe_planet_intent': r'.*\s*your planet.*',
            'answer_why_intent': r'why\sare.*',
            'about_intellipaat': r'.*\s*intellipaat.*'
        }
    
    def greet(self):
        self.name = input("what is your name ?\n")
        will_help = input(
            f"Hi {self.name}, I am bot.will you tell me about your self?\n")
        if will_help in self.negative_res:
            print(f"have a nice day {self.name}")
            return 
        self.chat()
        
    def make_exit(self, reply):
        for command in self.for_quit:
            if reply == command:
                print(f"have a nice day {self.name}")
                return True

    def chat(self):
        reply = input(random.choice(self.randomQuestions)).lower()
        while not self.make_exit(reply):
            reply = input(self.match_reply(reply))
            
    
    def match_reply(self, reply):
        for intent, regex_pattern in self.alienbabble.items():
            found_match = re.match(regex_pattern, reply)
            if found_match and intent == 'describe_planet_intent':
                return self.describe_planet_intent()
            elif found_match and intent == 'answer_why_intent':
                return self.answer_why_intent()
            elif found_match and intent == 'about_intellipaat':
                return self.about_intellipaat()
        
        if not found_match:
            return self.no_match_intent() 
    def describe_planet_intent(self):
        response = ("My work is to communicate with you\n",
                    "I heard the cofee is goood \n")
        return random.choice(response)
    
    def answer_why_intent(self):
        response = ("Nice to meet you \n","I am here to talk with you\n",
                      "I heard the coffe is good \n")
        return random.choice(response)
    
    def about_intellipaat(self):
        response = ("Intelligence is very useful fo all \n", " the ability to solve complex problems or make decisions\n",
                      "Intelligence is where your career and skill grows\n")
        return random.choice(response)
    

    def no_match_intent(self):
        response = ( "Please tell me more.\n","tell me more!\n","I see.Can you elaborate\n",
                        "Interesting.can you tell me more ?\n","I see.How do you think?\n","why?\n",
                         "how do you think I feel when i say that.Why?\n")
        return random.choice(response)

bot = RuleBasedBot()
bot.greet()