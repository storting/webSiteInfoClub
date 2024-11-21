from flask import Flask, request, render_template

app = Flask(__name__)
f = open("Users.txt", "r")

try:
    text = f.read()
    phone_numberBase = text.rpartition('|')[0]
    passwordBase = text.rpartition('|')[2]
    print(f"\n\t\t\{phone_numberBase}\n")
    print(f"\t\t\{passwordBase}\n")
finally:
    f.close()

@app.route("/")
def index():
    return render_template("index.html")

@app.route('/process', methods=['POST', 'GET'])
def process():
    if request.method == "POST":
        phone_number = request.form.get('phone_number')
        password = request.form.get('password')
        if(password == passwordBase and phone_number == phone_numberBase):
            print(f"\n\t\t\tAuth select\n\t\t\tWelcome {phone_number}\n")
            return f"\n\t\t\tAuth select\n\t\t\tWelcome {phone_number}\n"
        else:
            print(f"\n\t\t\tAuth NOT select\n")
            print(f"\n\t\t\{phone_numberBase} &&& {phone_number}\n")
            print(f"\t\t\{passwordBase} &&& {password}\n")
            return f"\n\t\t\tAuth NOT select\n"
    else:
        return "Method not allowed." 

if __name__ == "__main__":
    app.run(debug=True)