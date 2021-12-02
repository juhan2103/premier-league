from fastapi import APIRouter
import json

router = APIRouter()

def __get_icon(name):
  with open('../football_json/icon.json', 'r') as f:
      data = json.load(f)
  return data[name]

def get_data():
  with open('../football_json/Premier League.json', 'r') as f:
    data = json.load(f)
  
  return data

def get_team_data():
  with open('../football_json/Premier League_squad.json', 'r') as f:
    data = json.load(f)
  
  return data
# rank_helper
def rank_helper(team) -> dict:
  return {
      "icon": __get_icon(team["team_name"]),
      "name": team["team_name"],
      "round": team["overall_gp"],
      "overall_w": team["overall_w"],
      "overall_d": team["overall_d"],
      "overall_l": team["overall_l"],
      "gd": team["gd"],
      "points": team["points"],
  }

def player_helper(player) -> dict:
  return {
      "name": player["name"],
      "number": player["number"],
      "age": player["age"],
      "position": player["position"],
      "injured": player["injured"],
      "minutes": player["minutes"],
      "appearences": player["appearences"],
      "goals": player["goals"],
      "assists": player["assists"],
      "yellowcards": player["yellowcards"],
      "yellowred": player["yellowred"],
      "redcards": player["redcards"],
  }

