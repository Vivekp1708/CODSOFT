import random

class HealthChatbot:
    def __init__(self):
        self.responses = {
            "greetings": ["Hey there! How's your day going? Ready to chat about health and fitness?",
                          "Hi! How are you feeling today? Let's talk about staying healthy!",
                          "Hello! What's on your mind? Let's dive into some health tips!"],
            "farewells": ["Take care! Keep up the good work on your health journey!",
                          "See you later! Stay healthy and happy!",
                          "Goodbye! Remember, your well-being matters!"],
            "exercise": ["Adding some movement to your day can do wonders! How about a walk or some stretching?",
                         "Strength training exercises can help you feel strong and energized!",
                         "Don't forget to stay active throughout the day, even if it's just a short walk or some dancing!"],
            "diet": ["Eating balanced meals with plenty of fruits, veggies, and lean proteins is key!",
                     "Stay hydrated by drinking water throughout the day.",
                     "Opt for whole foods and try to avoid processed snacks and sugary drinks for better nutrition."],
            "water": ["Remember to drink at least 8 glasses of water daily to stay hydrated and energized!",
                      "Carry a reusable water bottle with you to make it easier to stay hydrated throughout the day!"],
            "sleep": ["Aim for 7-9 hours of quality sleep each night to feel refreshed and rejuvenated!",
                      "Make your sleep environment as cozy as possible by keeping your bedroom cool, dark, and quiet!"],
            "stress": ["Practice deep breathing or mindfulness meditation to help reduce stress and promote relaxation.",
                       "Engage in activities you enjoy, whether it's reading, spending time outdoors, or pursuing a hobby, to unwind and recharge."],
            "what_to_eat": ["Focus on nourishing your body with a variety of colorful fruits, vegetables, and whole grains.",
                            "Healthy fats from sources like avocado, nuts, and olive oil can support heart health and keep you feeling satisfied!"],
            "what_not_to_eat": ["Avoid sugary snacks and beverages for better health.",
                                "Limit fast food and fried foods for a healthier diet.",
                                "Watch your portion sizes to avoid overeating."],
            "daily_water_goal": "Remember to drink at least 8 glasses of water each day.",
            "daily_calorie_goal": "Aim for around 2000-2500 calories per day for most adults."
        }

    def get_response(self, user_input):
        for key, values in self.responses.items():
            if key in user_input:
                if isinstance(values, list):
                    return random.choice(values)
                else:
                    return values
        return "I'm sorry, I didn't understand that. Can you please ask again?"

if __name__ == "__main__":
    chatbot = HealthChatbot()
    print("Welcome to the Health Chatbot!")
    print("I'm here to help you stay healthy and fit. Ask me anything!")

    while True:
        user_input = input("You: ").lower()
        response = chatbot.get_response(user_input)
        print("HealthBot:", response)
