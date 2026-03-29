AI Rule-Based Expert System
               A modern Rule-Based Expert System built using Python and Streamlit that performs intelligent diagnosis based on user input. The system applies forward chaining and also provides partial match suggestions for incomplete data.

 Features
Interactive Web UI (Streamlit)
 Rule-Based Inference System
 Forward Chaining Logic
 Partial Match Suggestions (Smart AI behavior)
 Step-by-Step Reasoning Display
 Premium UI with Cards & Dark Theme

 Technologies Used
- Python
- Streamlit

 How It Works
     The system uses predefined IF-THEN rules:

- IF fever AND cough → infection  
- IF infection AND body pain → flu  
- IF flu → visit doctor  

 Smart Behavior
     Even if full conditions are not met, the system suggests possible outcomes using partial matching.

 Example Input
 Full Match:
No full match found
Partial Match:
- fever, cough → possible infection  
- infection, body pain → possible flu  

 Final Result:
- fever  
- body pain  
 How to Run
 Install dependencies

bash
pip install -r requirements.txt

Run the app
streamlit run app.py

Open in browser
Streamlit will automatically open the app in your browser.

Project Structure

Expert-System/
│
├── app.py
├── requirements.txt
├── README.txt

Purpose

This project was developed as part of an Artificial Intelligence internship task to demonstrate practical implementation of:

Rule-Based Systems
Forward Chaining
Decision Support Systems

Author: Kinza Nazli