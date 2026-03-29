import streamlit as st

# Page config
st.set_page_config(page_title="Expert System", layout="centered")

# 🎨 PREMIUM CSS
st.markdown("""
<style>

.stApp {
    background: linear-gradient(135deg, #0f2027, #203a43, #2c5364);
    color: white;
}

h1 {
    text-align: center;
    font-weight: bold;
}

.card {
    background: #1e2a38;
    padding: 15px;
    border-radius: 12px;
    margin-bottom: 15px;
    box-shadow: 0px 4px 15px rgba(0,0,0,0.4);
}

.success-card {
    border-left: 5px solid #00ff9f;
}

.warning-card {
    border-left: 5px solid #ffc107;
}

.result-card {
    border-left: 5px solid #00c6ff;
}

input {
    background-color: #1e2a38 !important;
    color: white !important;
}

button {
    border-radius: 10px !important;
}

</style>
""", unsafe_allow_html=True)

# 🧠 HEADER
st.title("🧠 AI Expert System")
st.markdown("### ⚡ Smart Diagnosis Interface")
st.markdown("---")

# RULES
rules = [
    {"if": ["fever", "cough"], "then": "infection"},
    {"if": ["infection", "body pain"], "then": "flu"},
    {"if": ["sneezing", "runny nose"], "then": "cold"},
    {"if": ["itchy eyes", "sneezing"], "then": "allergy"},
    {"if": ["flu"], "then": "visit doctor"},
]

# LOGIC
def forward_chaining(facts, rules):
    inferred = set(facts)
    steps = []
    suggestions = []

    # FULL MATCH
    while True:
        new_added = False
        for rule in rules:
            if all(cond in inferred for cond in rule["if"]):
                if rule["then"] not in inferred:
                    inferred.add(rule["then"])
                    steps.append(f"{', '.join(rule['if'])} → {rule['then']}")
                    new_added = True
        if not new_added:
            break

    # PARTIAL MATCH
    for rule in rules:
        conditions = rule["if"]
        match_count = sum(1 for cond in conditions if cond in inferred)

        if 0 < match_count < len(conditions):
            suggestions.append(f"{', '.join(conditions)} → possible {rule['then']}")

    return inferred, steps, suggestions

# INPUT
st.markdown("#### 🔍 Enter Symptoms")
user_input = st.text_input("Enter Sympotoms", placeholder="fever, cough, body pain")

# BUTTON
if st.button("🚀 Analyze"):
    if user_input.strip() == "":
        st.warning("⚠ Please enter symptoms")
    else:
        facts = [x.strip().lower() for x in user_input.split(",")]

        final_facts, steps, suggestions = forward_chaining(facts, rules)

        st.markdown("---")

        # 📊 REASONING (CARD)
        st.markdown("## 📊 Reasoning Steps")

        if steps:
            for step in steps:
                st.markdown(f"""
                <div class="card success-card">
                    ✔ {step}
                </div>
                """, unsafe_allow_html=True)
        else:
            st.markdown(f"""
            <div class="card warning-card">
                ❌ No full match found
            </div>
            """, unsafe_allow_html=True)

        # 💡 PARTIAL (CARD)
        if suggestions:
            st.markdown("## 💡 Possible Conditions")

            for s in suggestions:
                st.markdown(f"""
                <div class="card warning-card">
                    ⚠ {s}
                </div>
                """, unsafe_allow_html=True)

        # ✅ FINAL RESULT (CARD)
        st.markdown("## ✅ Final Result")

        for f in final_facts:
            st.markdown(f"""
            <div class="card result-card">
                👉 {f}
            </div>
            """, unsafe_allow_html=True)