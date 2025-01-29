class AddTeamPage:
    def __init__(self, page):
        self.page = page
        self.name_input = page.locator('input[name="name"]')
        self.add_button = page.locator("text='Add'")

    def go_to_add_team_page(self):
        """Navigue vers la page d'ajout d'équipe."""
        self.page.goto("/add_team")

    def create_team(self, team_name):
        """Remplir le formulaire et ajouter une équipe."""
        self.name_input.fill(team_name)
        self.add_button.click()
