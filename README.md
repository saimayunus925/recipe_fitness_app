**EpicureanExplorer: The Recipe App for Everyone!**

Are you tired of recipe apps that give you recipes loaded with the ONE ingredient (tomatoes, anchovies, whatever) you hate?

Are you done with recipe apps that just fetch content from an API and give you whatever recipe shows up, even if it's loaded with sugar, carbs, or saturated fat?

Well, today's your lucky day! As someone who's passionate about cooking, food, and fitness, I started this app in order to generate specialized recipes according to users' specific plans (gain muscle, lose weight, etc) that are still tasty and sophisticated!

TECH USED:
- Python
- MongoDB

PROJECT REQUIREMENTS:

### 1. **Introduction**
   - **Purpose:** 
      The document is meant to be a comprehensive overview of the project requirements. The project itself is a recipe app that incorporates
      fitness by generating tasty and elegant recipes that fit into users' workout and weight loss plans. The project should also filter by ingredients so that users don't need to endure food they hate to get healthy.
   - **Scope:** 
      The project will be a Flask application - HTML/CSS front-end, Flask backend, MongoDB database. Flask is a Python web-dev framework. In future updates, we may make a React front-end, but for now, we'll stick with HTML/CSS. The project will have a mechanism to get user input (e.g. does the user want more protein, more veggies, portion control, etc), which it will use to query the Spoonacular API to get the recipes best suited for the user's needs. The app will then store the correct recipes in a MongoDB database.
   - **Background:** 
      As important as weight loss plans and recipe apps are, they do not always take dietary restrictions into account. It can also be difficult to gain motivation to eat healthy with dietary restrictions, as sometimes the very foods to be avoided are front-and-center in many diet plans. E.g. during my health journey, I've noticed that protein is emphasized. However, as a Muslim, I cannot eat meat that isn't slaughtered in a *zabihah* fashion, and most meat in the West isn't slaughtered that way. Thus, I often turn to carbs for
      food, which leads to blood sugar spikes and intense cravings.

### 2. **Functional Requirements**
   1. Users shall be able to enter their preferences (dietary, taste, ingredients, religious restrictions, etc) for recipes. The system shall generate a series of recipes for the user based on those preferences.
   2. The system shall allow users to create an account with a unique username and password. 
   3. Users shall be able to log in securely using their registered credentials.
   4. Users shall be able to create, edit, and delete recipes.
   5. Users shall be able to search for recipes based on keywords, ingredients, or categories.
   6. Each recipe shall include a title, list of ingredients, step-by-step instructions, and preparation time.
   7. The system shall provide filters to sort and display recipes based on user preferences (e.g., cooking time, difficulty level).
   8. Users shall have a profile page displaying their username, profile picture, and a list of their saved and uploaded recipes.
   9. Users shall be able to update their profile information and change their profile picture.
   10. Users shall be able to add ingredients from a recipe to a shopping list.
   11. The system shall allow users to view and manage their shopping list.
   12. More requirements will be added as the need arises.
   - **Use Cases:** Describe various interactions with the system.
   - **Functional Specifications:** Detail specific functionalities the app must have.
   - **Data Handling:** Define how data will be stored, retrieved, and manipulated.

### 3. **Non-Functional Requirements**
   - **Performance:** The system should load recipes within 2 seconds of user request.
   - **Usability:** The user interface should be intuitive, following established design principles and accessibility standards.
   - **Security:** Authentication mechanisms should follow industry best practices (e.g., password hashing, multi-factor authentication).
   - **Scalability:** The application should handle a concurrent user load of at least 1000 users without significant degradation in performance.

### 4. **Constraints**
   - **Technical Constraints:** Hardware, software, and platform limitations.
   - **Regulatory:** Compliance with legal and regulatory requirements.
   - **Resource Constraints:** Limitations in budget, time, or expertise.

### 5. **Assumptions and Dependencies**
   - **Assumptions:** Things presumed true but not confirmed.
   - **Dependencies:** External factors affecting the project.

### 6. **Risks**
   - **Identification:** List potential risks that might impact the project.
   - **Mitigation Plan:** Strategies to address and mitigate these risks.

### 7. **Sign-off**
   - **Approval:** Space for stakeholders to approve the requirements document.
