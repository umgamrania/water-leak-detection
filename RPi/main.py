from flask import Flask, request, render_template, abort

app = Flask(__name__)

@app.route("/set-motor", methods=["POST"])
def set_motor():
    token = request.form.get("token")

    if token == "secret-token":
        state = int(request.form.get("state"))

        if state == 0:
            motor.on()
        elif state == 1:
            motor.off()

        return f"{state}"
    else:
        abort(401)

@app.route("/get-motor", methods=["POST"])
def get_motor():
    token = request.form.get("token")

    if token == "secret-token":
        return f"{motor_state}"
    else:
        abort(401)

if __name__ == "__main__":
    app.run(host="0.0.0.0", debug=True)
