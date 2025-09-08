from flask import Flask, render_template_string, request
# Deepak import your .py code here, so we can use it like a method in the summerize_text()
app = Flask(__name__)

def summarize_text(text):
    return  text[:100] + "..." # Here we can do llm.method(text)

TEMPLATE = """
<!DOCTYPE html>
<html lang="en">
<head>
  <title>Voice Summarizer 🎙️</title>
  <script src="https://cdn.tailwindcss.com"></script>
</head>
<body class="bg-gradient-to-r from-indigo-200 via-purple-200 to-pink-200 min-h-screen flex items-center justify-center">
  <div class="w-full max-w-3xl bg-white rounded-2xl shadow-2xl p-8 text-center">
    <h1 class="text-4xl font-extrabold bg-gradient-to-r from-indigo-600 via-purple-600 to-pink-600 bg-clip-text text-transparent mb-6">
      Voice Summarizer 🎤
    </h1>

    <!-- Only Speak Button -->
    <form method="POST" id="speechForm">
      <input type="hidden" name="input_text" id="input_text">
      <button type="button" onclick="startRecording()" 
        class="px-6 py-3 bg-gradient-to-r from-pink-500 to-indigo-500 hover:from-pink-600 hover:to-indigo-600 text-white rounded-xl shadow-lg transition transform hover:scale-105">
        🎙️ Speak to Summarize
      </button>
    </form>

    {% if summary %}
    <div class="mt-8 text-left">
      <h2 class="text-xl font-semibold text-gray-700 mb-2">Summary</h2>
      <div class="p-4 bg-gray-100 border rounded-xl text-gray-800 leading-relaxed">
        {{ summary }}
      </div>
    </div>
    {% endif %}
  </div>

  <!-- Speech-to-Text Script -->
  <script>
    function startRecording() {
      const recognition = new (window.SpeechRecognition || window.webkitSpeechRecognition)();
      recognition.lang = "en-US";
      recognition.interimResults = false;
      recognition.maxAlternatives = 1;

      recognition.start();

      recognition.onresult = function(event) {
        const spokenText = event.results[0][0].transcript;
        document.getElementById("input_text").value = spokenText;
        document.getElementById("speechForm").submit(); // auto-submit after speaking
      };

      recognition.onerror = function(event) {
        alert("Error: " + event.error);
      };
    }
  </script>
</body>
</html>
"""

@app.route("/", methods=["GET", "POST"])
def home():
    summary = None
    if request.method == "POST":
        input_text = request.form["input_text"]
        summary = summarize_text(input_text)
    return render_template_string(TEMPLATE, summary=summary)

if __name__ == "__main__":
    app.run(debug=True)