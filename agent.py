import streamlit as st
import google.generativeai as genai
import os
import time

# --- ΡΥΘΜΙΣΕΙΣ ---
# ⚠️ ΒΑΛΕ ΤΟ ΚΛΕΙΔΙ ΣΟΥ ΕΔΩ
GOOGLE_API_KEY = "AIzaSy...ΤΟ_ΚΛΕΙΔΙ_ΣΟΥ_ΕΔΩ...XYZ"

# Επιλέγουμε το πολύ γρήγορο μοντέλο από τη λίστα σου
MODEL_NAME = "models/gemini-2.5-pro"

st.set_page_config(page_title="Study Guide AI Agent", page_icon="🏛️")
st.title("🤖 Study Guide AI Agent")
st.caption(f"Powered by {MODEL_NAME}")

# Ρύθμιση Gemini
try:
    genai.configure(api_key=GOOGLE_API_KEY)
except Exception as e:
    st.error(f"Πρόβλημα κλειδιού: {e}")

# --- ΣΥΝΑΡΤΗΣΗ: ΑΝΕΒΑΣΜΑ PDF ΣΤΗ GOOGLE ---
@st.cache_resource
def get_uploaded_file(path):
    """
    Ανεβάζει το PDF στους servers της Google μία φορά.
    Αν έχει ανέβει ήδη, το ξαναχρησιμοποιεί.
    """
    if not os.path.exists(path):
        return None

    try:
        with st.spinner("📤 Ανεβάζω τον Οδηγό Σπουδών στο Gemini (Native PDF)..."):
            # 1. Ανέβασμα αρχείου
            sample_file = genai.upload_file(path=path, display_name="Odigos Spoudon")
            
            # 2. Έλεγχος αν είναι έτοιμο (μπορεί να πάρει λίγα δευτερόλεπτα)
            while sample_file.state.name == "PROCESSING":
                time.sleep(2)
                sample_file = genai.get_file(sample_file.name)
                
            if sample_file.state.name == "FAILED":
                st.error("Το ανέβασμα απέτυχε.")
                return None
                
            return sample_file
    except Exception as e:
        st.error(f"Σφάλμα ανεβάσματος: {e}")
        return None

# --- ΚΥΡΙΩΣ ΕΦΑΡΜΟΓΗ ---

# Έλεγχος αν υπάρχει το αρχείο τοπικά
pdf_path = "odigos.pdf"

if os.path.exists(pdf_path):
    # Καλούμε τη συνάρτηση ανεβάσματος
    remote_file = get_uploaded_file(pdf_path)
    
    if remote_file:
        st.success("✅ Ο Οδηγός είναι έτοιμος και διαβάζεται ως PDF!")
    else:
        st.stop()
else:
    st.error("⚠️ Δεν βρέθηκε το αρχείο 'odigos.pdf' στον φάκελο.")
    st.stop()

# --- CHAT ---
if "messages" not in st.session_state:
    st.session_state.messages = []

# Εμφάνιση ιστορικού
for msg in st.session_state.messages:
    with st.chat_message(msg["role"]):
        st.markdown(msg["content"])

# Λήψη ερώτησης
if prompt := st.chat_input("Ρώτησε κάτι για τη σχολή..."):
    # Εμφάνιση ερώτησης χρήστη
    st.session_state.messages.append({"role": "user", "content": prompt})
    with st.chat_message("user"):
        st.markdown(prompt)

    # Απάντηση από το Gemini
    with st.chat_message("assistant"):
        with st.spinner("Διαβάζω το PDF..."):
            try:
                # Δημιουργία του μοντέλου
                model = genai.GenerativeModel(MODEL_NAME)
                
                # Του στέλνουμε το ΑΡΧΕΙΟ + την ΕΡΩΤΗΣΗ
                response = model.generate_content(
                    [
                        "Είσαι ο σύμβουλος σπουδών. Απάντα αναλυτικά στα Ελληνικά, βασισμένος ΜΟΝΟ σε αυτό το αρχείο.", 
                        remote_file, 
                        prompt
                    ]
                )
                
                ans = response.text
                st.markdown(ans)
                st.session_state.messages.append({"role": "assistant", "content": ans})
            
            except Exception as e:
                error_msg = str(e)
                if "429" in error_msg:
                    st.warning("⏳ Πιάσαμε το όριο της Google. Περίμενε λίγο και ξαναδοκίμασε.")
                else:
                    st.error(f"Σφάλμα: {e}")