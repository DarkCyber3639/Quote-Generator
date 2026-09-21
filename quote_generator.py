import random

class QuoteGenerator:
    """A simple random quote generator with a collection of 100+ quotes."""
    
    quotes = [
        "The only way to do great work is to love what you do. – Steve Jobs",
        "Innovation distinguishes between a leader and a follower. – Steve Jobs",
        "Life is what happens when you're busy making other plans. – John Lennon",
        "The future belongs to those who believe in the beauty of their dreams. – Eleanor Roosevelt",
        "It is during our darkest moments that we must focus to see the light. – Aristotle",
        "The only impossible journey is the one you never begin. – Tony Robbins",
        "Success is not final, failure is not fatal: it is the courage to continue that counts. – Winston Churchill",
        "Believe you can and you're halfway there. – Theodore Roosevelt",
        "The best time to plant a tree was 20 years ago. The second best time is now. – Chinese Proverb",
        "Your time is limited, don't waste it living someone else's life. – Steve Jobs",
        "The way to get started is to quit talking and begin doing. – Walt Disney",
        "Don't let yesterday take up too much of today. – Will Rogers",
        "You learn more from failure than from success. – Unknown",
        "It's not whether you get knocked down, it's whether you get up. – Vince Lombardi",
        "Do something today that your future self will thank you for. – Sean Patrick Flanery",
        "Little things make big days. – Unknown",
        "It's going to be hard, but hard does not mean impossible. – Unknown",
        "Don't stop when you're tired, stop when you're done. – Unknown",
        "Wake up with determination. Go to bed with satisfaction. – Unknown",
        "Do something now; your future self will be thankful. – Unknown",
        "Great things never come from comfort zones. – Unknown",
        "Dream it. Wish it. Do it. – Unknown",
        "Success doesn't just find you. You have to go out and get it. – Unknown",
        "The harder you work for something, the greater you'll feel when you achieve it. – Unknown",
        "Dream bigger. Do bigger. – Unknown",
        "Don't wait for opportunity. Create it. – Unknown",
        "Sometimes we're tested not to show our weaknesses, but to discover our strengths. – Unknown",
        "The key to success is to focus on goals, not obstacles. – Unknown",
        "Dream it. Believe it. Build it. – Unknown",
        "What lies behind us and what lies before us are tiny matters compared to what lies within us. – Ralph Waldo Emerson",
        "Failure is simply the opportunity to begin again, this time more intelligently. – Henry Ford",
        "You are never too old to set another goal or to dream a new dream. – C.S. Lewis",
        "The only limit to our realization of tomorrow is our doubts of today. – Franklin D. Roosevelt",
        "The future is created by what you do today, not tomorrow. – Unknown",
        "Challenges are what make life interesting. Overcoming them is what makes life meaningful. – Joshua J. Marine",
        "What we think, we become. – Buddha",
        "All progress takes place outside the comfort zone. – Michael John Bobak",
        "Success is not how high you have climbed, but how you make a positive difference to the world. – Roy T. Bennett",
        "Believe in yourself. You are braver than you think, more talented than you know, and capable of more than you imagine. – Roy T. Bennett",
        "The only way to achieve the impossible is to believe it is possible. – Charles Kingsleigh",
        "Motivation is what gets you started. Habit is what keeps you going. – Jim Ryun",
        "Life is either a daring adventure or nothing at all. – Helen Keller",
        "Success is the sum of small efforts repeated day in and day out. – Robert Collier",
        "Your limitation—it's only your imagination. – Unknown",
        "Great things never came from comfort zones. – Unknown",
        "Success doesn't require luck. – Unknown",
        "The way to get started is to quit talking. – Walt Disney",
        "Don't stop believing. – Unknown",
        "Push yourself, because no one else is going to do it for you. – Unknown",
        "Sometimes we're tested not to show our weaknesses, but to discover our strengths. – Unknown",
        "Dream bigger than your fears. – Unknown",
        "I am not a product of my circumstances. I am a product of my decisions. – Stephen Covey",
        "Your limitation—it's only your imagination. – Unknown",
        "Great things never came from comfort zones. – Unknown",
        "Don't be afraid to give up the good to go for the great. – John D. Rockefeller",
        "Don't watch the clock; do what it does. Keep going. – Sam Levenson",
        "Believe in yourself and all that you are. – Unknown",
        "The best version of yourself is just a few decisions away. – Unknown",
        "Success is no accident. It is hard work, perseverance, learning, studying, sacrifice and most of all, love of what you are doing. – Pelé",
        "Don't let your struggle become your identity. – Unknown",
        "You don't need to be perfect to be worthy. – Unknown",
        "Strive for greatness. – Unknown",
        "Great minds discuss ideas; average minds discuss events; small minds discuss people. – Eleanor Roosevelt",
        "You are the sum of your choices. – Unknown",
        "The only thing stopping you is you. – Unknown",
        "Success is walking from failure to failure with no loss of enthusiasm. – Winston Churchill",
        "Keep your eyes on the prize. – Unknown",
        "It does not matter how slowly you go as long as you do not stop. – Confucius",
        "You are capable of amazing things. – Unknown",
        "Don't stop until you're proud. – Unknown",
        "The key to success is to quit talking and begin doing. – Walt Disney",
        "Dream it. Wish it. Do it. – Unknown",
        "One day or day one. You decide. – Unknown",
        "Excellence is not a skill, it's an attitude. – Ralph Marston",
        "You don't have to be great to start, but you have to start to be great. – Zig Ziglar",
        "Don't be a backup plan, be the main event. – Unknown",
        "Your limitation—it's only your imagination. – Unknown",
        "The success of an individual is measured by their concentration of effort. – Unknown",
        "Success is a journey, not a destination. – Unknown",
        "Every accomplishment starts with the decision to try. – Unknown",
        "Motivation is what gets you started. Habit is what keeps you going. – Jim Ryun",
        "The future depends on what you do today. – Mahatma Gandhi",
        "Don't wait for the perfect moment. Take the moment and make it perfect. – Unknown",
        "Great things take time. – Unknown",
        "Stay focused and extra hard. – Unknown",
        "Dream bigger. – Unknown",
        "Greatness is not a destination, it's a journey. – Unknown",
        "Never stop growing. – Unknown",
        "You've got this. – Unknown",
        "The only impossible journey is the one you never begin. – Tony Robbins",
        "Challenges make you discover things about yourself that you never really knew. – Cicely Tyson",
        "What lies behind you and what lies before you pales in comparison to what lies within you. – Ralph Waldo Emerson",
        "Believe in yourself, take on your challenges, dig deep within yourself to conquer fears. – Chantal Sutherland",
        "The only way to do great work is to love what you do. – Steve Jobs",
        "Success is getting what you want, happiness is wanting what you get. – Unknown",
        "Don't be afraid to be your authentic self. – Unknown",
        "The only time you fail is when you fall down and don't get back up. – Stephen Colbert",
        "Master the basics and the rest will follow. – Unknown",
        "No one can tell you how to be successful, you must find your own way. – Unknown",
        "I have not failed. I've just found 10,000 ways that won't work. – Thomas Edison",
        "Even the darkest night will end and the sun will rise. – Victor Hugo",
        "The best time to plant a tree was 20 years ago. The second best time is now. – Chinese Proverb",
        "Just breathe, you've got this. – Unknown",
    ]
    
    @classmethod
    def get_random_quote(cls):
        return random.choice(cls.quotes)
    
    @classmethod
    def get_n_quotes(cls, n):
        if n > len(cls.quotes):
            print(f"Warning: Requested {n} quotes but only {len(cls.quotes)} available.")
            n = len(cls.quotes)
        return random.sample(cls.quotes, n)
    
    @classmethod
    def display_random_quote(cls):
        quote = cls.get_random_quote()
        print("\n" + "="*60)
        print(quote)
        print("="*60 + "\n")


def main():
    """Main function to run the quote generator.If you fork this do NOT edit this unless you know what youre doing."""
    print("Welcome to the Random Quote Generator!")
    
    while True:
        print("\nOptions:")
        print("1. Get a random quote")
        print("2. Get multiple random quotes")
        print("3. Exit")
        
        choice = input("\nEnter your choice (1-3): ").strip()
        
        if choice == "1":
            QuoteGenerator.display_random_quote()
        elif choice == "2":
            try:
                n = int(input("How many quotes do you want? "))
                quotes = QuoteGenerator.get_n_quotes(n)
                print("\n" + "="*60)
                for i, quote in enumerate(quotes, 1):
                    print(f"\n{i}. {quote}")
                print("\n" + "="*60 + "\n")
            except ValueError:
                print("Please enter a valid number.")
        elif choice == "3":
            print("Thanks for using the Quote Generator <3. Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")


if __name__ == "__main__":
    main()
