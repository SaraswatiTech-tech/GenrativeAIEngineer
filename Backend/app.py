from flask import Flask, render_template, request

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def home():

    message = ""

    if request.method == "POST":

        Account_HolderName = request.form["holder_name"]

        Account_Number = int(
            request.form["account_number"]
        )

        Account_Balance = float(
            request.form["account_balance"]
        )

        deposit_amount = float(
            request.form["deposit_amount"]
        )

        withdrawal_amount = float(
            request.form["withdrawal_amount"]
        )

        is_Account_Active = request.form.get(
            "account_active"
        )

        Account_Balance = (
            Account_Balance + deposit_amount
        )

        if is_Account_Active:

            if Account_Balance >= withdrawal_amount:

                Account_Balance = (
                    Account_Balance - withdrawal_amount
                )

                message = (
                    f"Withdrawal successful. "
                    f"Updated Balance: "
                    f"{Account_Balance}"
                )

            else:

                message = (
                    "Insufficient balance "
                    "for withdrawal."
                )

        else:

            message = (
                "Account is not active. "
                "Cannot perform withdrawal."
            )

    return render_template(
        "index.html",
        message=message
    )

if __name__ == "__main__":
    app.run(debug=True)