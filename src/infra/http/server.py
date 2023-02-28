from flask import Flask, request, jsonify
from flask_apscheduler import APScheduler

from src.app import VendingApp
from src.exceptions import VendingAlreadyInUseException, NoCoinInserted

app = Flask(__name__)
scheduler = APScheduler()
scheduler.api_enabled = True
scheduler.init_app(app)
scheduler.start()

vending_app = VendingApp()


@app.route('/insert/<machine_id>')
def insert_coin(machine_id: int):
    try:
        vending_app.insert_coin(int(machine_id))
        return jsonify(message="success", ), 200

    except KeyError:
        return jsonify(message="No such vending machine"), 404

    except VendingAlreadyInUseException:
        return jsonify(message="This Machine is already in use"), 423

    except:
        return jsonify(message="Something went wrong"), 500


@app.route('/purchase/<machine_id>', methods=["POST"])
def purchase(machine_id: int):
    try:
        supply = request.json.get("supply", None)
        if not supply or supply not in ["soda", "coffee"]:
            return jsonify(message="Please choose a valid supply"), 400

        vending_app.submit_order(int(machine_id))
        return jsonify(message="success"), 200

    except KeyError:
        return jsonify(message="No such vending machine"), 404
    except NoCoinInserted:
        return jsonify(message="No such vending machine"), 404
    except:
        return jsonify(message="Something went wrong"), 500


@scheduler.task('interval', id='set_left_vending_to_idle', seconds=1, misfire_grace_time=None)
def set_left_vending_to_idle():
    vending_app.set_left_vending_to_idle()


if __name__ == '__main__':
    app.run()
