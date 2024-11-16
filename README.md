TeyvaTool
==========

Description
----------

TeyvaTool is a multifunctional tool for players of Genshin Impact. The application includes three main modules:

Critical Mass Calculator for Artifacts: Helps optimize artifact stats by calculating critical chance and critical damage.

Team Builder: Automatically selects optimal teams for world exploration and Spiral Abyss runs, taking into account elemental interactions and character roles.

Artifact Drop Chance Calculator: Estimates the probability of obtaining needed artifacts during gameplay (in development).

The application is developed in Python using the PyQt library and an interface created with QtDesigner. The codebase is organized following clean architecture principles for ease of maintenance and functionality expansion.

Features
----------

- **Critical Mass Calculator**

Input Criteria: Enter critical chance and critical damage values.
Calculation: Computes critical mass using the formula: Critical Chance × 2 + Critical Damage = Critical Mass.
Evaluation: Provides assessment of results with optimization recommendations.

- **Team Builder**

Character Selection: Choose from available characters.
Team Assembly: Form teams for various purposes such as world exploration and Spiral Abyss runs.
Elemental Interactions: Takes into account elemental reactions and character roles to ensure effective team composition.

- **Artifact Drop Chance Calculator (in development)**

Probability Assessment: Estimates the likelihood of obtaining required artifacts.
Scenario Analysis: Analyzes different drop scenarios to aid in decision-making.

Installation
-----------

### Requirements
- Python 3.7+
- PyQt5

### Steps
**1. Clone the Repository**
  ```
  git clone https://github.com/your-username/ArteFactor.git
  cd ArteFactor
  ```

**2. Create and Activate a Virtual Environment (Recommended)**
  ```
  python -m venv venv
  source venv/bin/activate  # For Windows: venv\Scripts\activate
  ```
  
**3. Install Dependencies**
  ```
  pip install -r requirements.txt
  ```
  
**4. Run the Application**
  ```
  python src/main.py
  ```
  
### Usage
After launching the application, you will see the main window with available modules.
Select the desired module and follow the on-screen instructions to perform calculations or assemble teams.

Contribution
-------
We welcome any suggestions and improvements! If you would like to contribute, please follow these steps:

- Fork the Repository.

- Create a New Branch for Your Changes:
  ```
  git checkout -b feature/FeatureName
  ```
  
- Make Changes and Commit Them
  ```
  git commit -m "Added new feature ..."
  ```
  
- Push the Branch and Create a Pull Request.

Please ensure that your code adheres to the coding style and passes all tests.

License
-------
This project is licensed under the MIT License. See the LICENSE file for details.

Contacts
-------
If you have any questions or suggestions, feel free to contact me via email or through GitHub Issues.

