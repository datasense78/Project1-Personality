import time

print("🧠 Welcome to the 'Know Your Personality' Quiz 2.0!")
print("✨ Let's discover who you truly are!")
print("=" * 60)

# Collecting basic info
name = input("👋 What's your name? ").strip()
age = int(input("🎂 How old are you? "))
city = input("🏙️ Which city do you live in? ").strip()
food = input("🍕 What's your favorite food? ").strip()
color = input("🎨 Your favorite color? ").strip()
animal = input("🐾 If you could be any animal, what would it be? ").strip()
hobby = input("🎮 What's one thing you LOVE doing in free time? ").strip()

# Convert name and color for formatting
name_clean = name.title()
color_upper = color.upper()

# Type and length checks
print("\n🔍 Doing some analysis...")
time.sleep(1.5)
print(f"📏 Your name has {len(name)} characters.")
print(f"📏 Your city has {len(city)} characters.")
print(f"🧬 Data type of age is: {type(age)}")
print(f"🧬 Data type of food is: {type(food)}")

# Age-based fun logic
if age < 18:
    age_tag = "Young Explorer"
elif age <= 30:
    age_tag = "Adventurer"
else:
    age_tag = "Wise Owl"

# Calculate age in months + personality code
age_months = age * 12
personality_code = name[:2].upper() + str(age)[-1] + animal[:1].upper() + color[:1].lower()

# Optional Boolean flag
is_fun = True

print("\n🎭 Finalizing your personality file...")
time.sleep(2)
print("=" * 60)

# Final Result
print(f"🎉 Hey {name_clean}, here's your fun personality report!")
print(f"🌆 You're from {city.title()}, a place of dreams!")
print(f"🍿 You love {food.lower()} and spend your time doing {hobby.lower()}.")
print(f"🎨 You vibe with the color {color_upper} and your spirit animal is the {animal.lower()}.")
print(f"📅 You’ve lived approximately {age_months} months.")
print(f"🧩 You belong to the '{age_tag}' tribe.")
print(f"🔐 Your secret personality code is: {personality_code} 🤖")

# Fun suggestion based on hobby length
if len(hobby) > 8:
    print("✨ You seem deeply passionate — that hobby says a lot about your vibe!")
else:
    print("💡 Time to explore more hobbies? You’ve got potential!")

if is_fun:
    print("🌈 You are officially certified as: FUNKY AND FABULOUS!")
print("=" * 60)
print("💬 Share this quiz with a friend and compare your vibes!")

