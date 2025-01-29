from models.add_team_page import AddTeamPage
from models.teams_page import TeamsPage

def test_create_team(reset_db, page):
    team_name = "my team"
    
    add_team_page = AddTeamPage(page)
    teams_page = TeamsPage(page)

    add_team_page.go_to_add_team_page()
    add_team_page.create_team(team_name)

    teams_page.go_to_teams_page()
    assert teams_page.check_team_exists(team_name)
