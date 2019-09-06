import PlaylistController

from flask import Flask, jsonify
app = Flask(__name__)


@app.route('/<city>', methods=['GET'])
def get_playslist(city):
    return PlaylistController.get_playlist(city)


if __name__ == "__main__":
    app.run()