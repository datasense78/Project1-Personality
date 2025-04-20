import streamlit as st
import time

st.set_page_config(page_title="Know Your Personality Quiz", page_icon="🧠")

# Header
st.title("🧠 Know Your Personality ")
st.markdown("✨ Let's discover who you really are with some fun data magic!")
st.markdown("---")

# Sidebar for user details
st.sidebar.title("📝 Enter Your Details")

# Input fields
name = st.sidebar.text_input("👤 Your Name")
age = st.sidebar.number_input("🎂 Your Age", min_value=1, max_value=120, step=1)
city = st.sidebar.text_input("🏙️ City You Live In")
food = st.sidebar.text_input("🍕 Your Favorite Food")
color = st.sidebar.text_input("🎨 Your Favorite Color")
animal = st.sidebar.text_input("🐾 Your Spirit Animal")
hobby = st.sidebar.text_input("🎮 One Thing You LOVE Doing")

# Submit Button
submitted = st.sidebar.button("🔍 Generate My Personality")

# Main Output Area
if submitted:
    with st.spinner("🧪 Brewing your unique vibe..."):
        time.sleep(1.5)

    st.info("🔍 Scanning colors, foods, and animal energies...")
    time.sleep(1)

    st.info("💫 Calculating your personality type using complex non-scientific logic...")
    time.sleep(1.2)

    # Process Inputs
    name_clean = name.title()
    color_upper = color.upper()
    city_title = city.title()
    age_months = age * 12
    personality_code = name[:2].upper() + str(age)[-1] + animal[:1].upper() + color[:1].lower()

    # Age-based Tag
    if age < 18:
        age_tag = "Young Explorer"
    elif age <= 30:
        age_tag = "Adventurer"
    else:
        age_tag = "Wise Owl"

    # Display Output
    st.success(f"🎉 Hey **{name_clean}**, here's your fun personality report!")
    st.markdown("---")
    st.write(f"🌆 You're from **{city_title}**, a place of dreams!")
    st.write(f"🍿 You love **{food.lower()}** and enjoy doing **{hobby.lower()}**.")
    st.write(f"🎨 You vibe with the color **{color_upper}** and your spirit animal is the **{animal.lower()}**.")
    st.write(f"📅 You've lived approximately **{age_months} months** already.")
    st.write(f"🧩 You belong to the '**{age_tag}**' tribe.")
    st.write(f"🔐 Your **Secret Personality Code** is: `💡 {personality_code}`")
    st.markdown("---")

    # Extra Fun Logic
    if len(hobby) > 8:
        st.info("✨ You seem deeply passionate — that hobby says a lot about your vibe!")
    else:
        st.info("💡 Time to explore more hobbies? You’ve got hidden sparks waiting!")

    st.success("🌈 You are officially certified as: FUNKY AND FABULOUS! 😎")
    st.balloons()
    st.markdown("---")

    # 👇 Explanation Note (Educational)
    with st.expander("📘 How did we generate your Personality Code & Title?"):
        st.markdown("""
        - The **Personality Code** is made using parts of your name, favorite color, age, and animal:
          > `name[:2].upper() + last digit of age + animal initial + color initial`  
        - The **Title (Young Explorer / Adventurer / Wise Owl)** is based on:
          - `If age < 18 → Young Explorer`
          - `18 ≤ age ≤ 30 → Adventurer`
          - `age > 30 → Wise Owl`
        - The **hobby comment** is chosen based on how long your hobby string is using `len()`.
        - We used `f-strings`, `.title()`, `.upper()`, `.lower()`, and some fun logic to build your profile.

        This is how Python turns your data into a *personalized experience*! 💻✨
        """)
    
    st.caption("💬 Share this app with a friend and compare your results!")

