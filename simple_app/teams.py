from flask import Blueprint,jsonify

team_bp=Blueprint('team',__name__) # the teams blueprint

DEVS=["JONA","JERRY"]
OPS=["Jannet"]

_Teams={1:DEVS,2:OPS}

@team_bp.route('/teams')
def get_all_teams():
    return jsonify(_Teams)

@team_bp.route('/team/<int:id>')
def get_a_team(id):
    return jsonify(_Teams[id])