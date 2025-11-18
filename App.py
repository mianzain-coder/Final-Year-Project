from flask import Flask, request, jsonify, render_template
import random

app = Flask(__name__)

# -------------------- SHORT TEMPLATES --------------------
short_templates = [
    "Get {product} today and enjoy amazing benefits!",
    "Introducing {product} – your next big upgrade!",
    "{product} is all you need for a better experience!"
]

# -------------------- LONG TEMPLATES --------------------
long_templates = [
    "{product} brings a refreshing blend of quality, comfort, and performance — designed for people who want more value with less effort. Every detail has been crafted to make your daily experience smoother, smarter and noticeably better.",
    "If you're looking for reliability and modern ease in one place, {product} is built just for you. Its refined design, practical features, and user-friendly experience make it the perfect everyday choice for anyone who values quality.",
    "With {product}, every moment becomes more convenient, more enjoyable and more meaningful. It delivers comfort, performance and a touch of innovation that makes your routine feel elevated without adding effort.",
    "{product} is not just a product — it’s a statement of style, efficiency and long-lasting performance. Designed with precision and built to impress, it offers the perfect balance between practicality and elegance.",
    "Experience the refined simplicity of {product}. Thoughtfully created to match your lifestyle, it blends innovation with comfort and delivers a polished experience that makes a real difference in your everyday routine."
]

# -------------------- CAPTIONS --------------------
captions_templates = [
    "Level up with {product}! 🚀🔥",
    "Your vibe needs {product} 💫",
    "Experience the magic of {product} ✨"
]

# -------------------- HASHTAGS --------------------
hashtags_templates = [
    "#{product} #TrendingNow #MustHave #Viral #BestChoice #TopRated",
    "#{product} #NewLaunch #Innovation #TechLife #DailyUse"
]

# -------------------- SLOGANS --------------------
slogan_templates = [
    "{product}: Make Every Moment Count",
    "{product}: Feel the Difference",
    "{product}: Designed For You"
]

# -------------------- AD COPY --------------------
adcopy_templates = [
    "Upgrade your life with {product} — grab it today and feel the change!",
    "{product} is here! Don’t miss out on the best deal of the year!"
]

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/generate', methods=['POST'])
def generate():
    data = request.json
    product = data.get('product', '')
    feature = data.get('feature', '')

    if not product:
        return jsonify({"error": "Product name is required"}), 400

    if feature == "short":
        content = random.choice(short_templates).format(product=product)
    elif feature == "long":
        content = random.choice(long_templates).format(product=product)
    elif feature == "caption":
        content = random.choice(captions_templates).format(product=product)
    elif feature == "hashtag":
        content = random.choice(hashtags_templates).format(product=product)
    elif feature == "slogan":
        content = random.choice(slogan_templates).format(product=product)
    elif feature == "adcopy":
        content = random.choice(adcopy_templates).format(product=product)
    else:
        content = "Invalid feature selected."

    return jsonify({"content": content})

if __name__ == '__main__':
    app.run(debug=True)
