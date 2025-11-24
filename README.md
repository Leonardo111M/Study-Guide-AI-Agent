# 🎓 Study Guide AI Agent

Ένας έξυπνος βοηθός σπουδών βασισμένος σε Τεχνητή Νοημοσύνη, που απαντάει σε ερωτήσεις φοιτητών αντλώντας πληροφορίες απευθείας από τον Οδηγό Σπουδών (PDF).

Το project χρησιμοποιεί το **Google Gemini 2.5 PRO** για ταχύτατη ανάλυση εγγράφων και το **Streamlit** για το περιβάλλον χρήστη.

## 🚀 Δυνατότητες

* **Native PDF Analysis:** Διαβάζει το αρχείο PDF αυτούσιο (όχι ως απλό κείμενο), κατανοώντας πίνακες, μορφοποίηση και δομή.
* **Gemini 2.5 PRO:** Χρησιμοποιεί το πιο γρήγορο μοντέλο της Google με τεράστιο context window.
* **Caching:** Ανεβάζει το αρχείο στους servers της Google μία φορά για βελτιστοποίηση ταχύτητας.
* **Φιλικό UI:** Απλό περιβάλλον chat μέσω Streamlit.

## 🛠️ Τεχνολογίες

* [Python 3.12](https://www.python.org/)
* [Streamlit](https://streamlit.io/)
* [Google Generative AI SDK](https://ai.google.dev/)

## ⚙️ Εγκατάσταση & Εκτέλεση

Ακολουθήστε τα παρακάτω βήματα για να τρέξετε την εφαρμογή στον υπολογιστή σας.

### 1. Προαπαιτούμενα
Βεβαιωθείτε ότι έχετε εγκατεστημένη την **Python 3.12**.

### 2. Εγκατάσταση Βιβλιοθηκών
Ανοίξτε το τερματικό (PowerShell/CMD) και τρέξτε:

```
pip install -r requirements.txt
```
### 3. ⚙️ Ρύθμιση

  1. Τοποθετήστε το αρχείο του οδηγού σπουδών στον ίδιο φάκελο με το όνομα odigos.pdf.
  2. Ανοίξτε το αρχείο agent.py και προσθέστε το Google API Key σας στη μεταβλητή GOOGLE_API_KEY.

Προσοχή: Μην ανεβάσετε το API Key σας δημόσια στο GitHub! Αν κάνετε το repo δημόσιο, χρησιμοποιήστε st.secrets ή environment variables.
google-generativeai

### 4. Εκκίνηση

Τρέξτε την εφαρμογή με την εντολή:
```
streamlit run agent.py
```

## 📁 Δομή Αρχείων:

*  agent.py: Ο κύριος κώδικας της εφαρμογής (Streamlit + Gemini Logic).
*  odigos.pdf: Το αρχείο PDF που περιέχει τις πληροφορίες του τμήματος.
*  requirements.txt: Η λίστα με τις απαραίτητες βιβλιοθήκες Python.

## 🛡️ License
This project is open-source and available under the MIT License.
