class TeamsPage:
    def __init__(self, page):
        self.page = page
        self.team_list = page.locator("table") 
        self.delete_button = page.locator("text='Delete'")  
        self.proceed_button = page.locator("text='Proceed'")  

    def go_to_teams_page(self):
        """Navigue vers la page des équipes."""
        self.page.goto("/teams")

    def check_team_exists(self, team_name):
        """Vérifie si une équipe est présente dans la liste."""
        return self.page.is_visible(f"td:has-text('{team_name}')")

    def delete_team(self):
        """Supprime une équipe."""
        self.delete_button.click()
        self.proceed_button.click()
