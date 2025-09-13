from flask import Flask, render_template_string, request

app = Flask(__name__)

# Dummy QA function (replace with LLM later)
def answer_question(context, question):
    if not context.strip() or not question.strip():
        return "Please provide both a story and a question."
    # Just a fake logic for now (replace with NLP/LLM)
    if question.lower() in context.lower():
        return f"Yes, '{question}' is mentioned in the story."
    return "Sorry, I couldn't find the answer in the story."

TEMPLATE = """
<html>
<head>
  <title>Story Q&A App 🎙️</title>
  <script src="https://cdn.tailwindcss.com"></script>
</head>
<body class="bg-gradient-to-r from-indigo-200 via-purple-200 to-pink-200 min-h-screen flex items-center justify-center">
  <div class="w-full max-w-5xl bg-white rounded-2xl shadow-2xl p-8">
    <h1 class="text-4xl font-extrabold text-center bg-gradient-to-r from-indigo-600 via-purple-600 to-pink-600 bg-clip-text text-transparent mb-8">
      Story Q&A Summarizer 🎤✍️
    </h1>

    <form method="POST" id="qaForm" class="grid grid-cols-1 md:grid-cols-2 gap-6">
      <div class="bg-gray-50 p-6 rounded-xl shadow-lg flex flex-col">
        <h2 class="text-xl font-semibold text-gray-700 mb-4">Story Input</h2>
        <textarea 
          id="story_text" 
          name="story_text" 
          rows="6" 
          placeholder="Paste your story or text here..." 
          class="w-full p-3 rounded-lg border focus:ring-2 focus:ring-indigo-400"
        >{{ request.form.get('story_text', '') }}</textarea>

        <h2 class="text-lg font-semibold text-gray-700 mt-6 mb-2">Ask a Question</h2>
        <input 
          type="text" 
          id="question_text" 
          name="question_text" 
          placeholder="Type or speak your question..." 
          class="w-full p-3 rounded-lg border focus:ring-2 focus:ring-pink-400"
          value="{{ request.form.get('question_text', '') }}"
        />

        <div class="mt-4 flex justify-between">
          <button type="button" onclick="startRecording()" 
            class="px-4 py-2 bg-pink-500 hover:bg-pink-600 text-white rounded-lg shadow-md transition">
            🎙️ Ask by Voice
          </button>
          <button type="submit" 
            class="px-4 py-2 bg-indigo-500 hover:bg-indigo-600 text-white rounded-lg shadow-md transition">
            ➡️ Get Answer
          </button>
        </div>
      </div>

      <!-- Output Card -->
      <div class="bg-gray-50 p-6 rounded-xl shadow-lg flex flex-col">
        <h2 class="text-xl font-semibold text-gray-700 mb-4">Answer</h2>
        <div class="w-full h-full p-3 rounded-lg border bg-white text-gray-800 leading-relaxed">
          {% if answer %}
            {{ answer }}
          {% else %}
            <span class="text-gray-400">Answer will appear here...</span>
          {% endif %}
        </div>
      </div>

    </form>
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
        document.getElementById("question_text").value = spokenText;
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
    answer = None
    if request.method == "POST":
        story_text = request.form.get("story_text", "")
        question_text = request.form.get("question_text", "")
        answer = answer_question(story_text, question_text)
    return render_template_string(TEMPLATE, answer=answer)

if __name__ == "__main__":
    app.run(host='0.0.0.0',debug=True)