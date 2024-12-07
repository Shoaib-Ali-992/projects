from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

class Account:
    def __init__(self, name, balance):
        self.name = name
        self.balance = balance

    def debit(self, amount):
        self.balance += amount

    def credit(self, amount):
        if self.balance >= amount:
            self.balance -= amount
        else:
            return "Insufficient balance"

    def get_balance(self):
        return self.balance


class UserProfile(Account):
    def __init__(self, username, password, name, balance):
        super().__init__(name, balance)
        self.username = username
        self.__password = password

    def validate_password(self, password):
        return self.__password == password

# Predefined user
user = UserProfile("shoaib", "12345", "Shoaib", 89900)

@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        username = request.form["username"]
        password = request.form["password"]

        if user.username == username and user.validate_password(password):
            return redirect(url_for("dashboard"))
        else:
            return render_template("index.html", error="Invalid credentials.")
    return render_template("index.html")

@app.route("/dashboard", methods=["GET", "POST"])
def dashboard():
    if request.method == "POST":
        action = request.form["action"]
        amount = float(request.form.get("amount", 0))

        if action == "debit":
            user.debit(amount)
        elif action == "credit":
            result = user.credit(amount)
            if result:
                return render_template("dashboard.html", user=user, error=result)

    return render_template("dashboard.html", user=user)

if __name__ == "__main__":
    app.run(debug=True)
