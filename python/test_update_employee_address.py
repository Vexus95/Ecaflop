from models.add_team_page import AddTeamPage
from models.teams_page import TeamsPage

def test_create_team(reset_db, page):

    add_team_page = AddTeamPage(page)
    teams_page = TeamsPage(page)

    # Create an employee 
    add_team_page.go_to_add_team_page()
    name_input = page.locator('input[name="name"]')
    name = "john snow"
    name_input.fill(name)

    name_input = page.locator('input[name="email"]')
    email = "john@efrei.fr"
    name_input.fill(email)

    name_input = page.locator('input[name="address_line1"]')
    address = "test town"
    name_input.fill(address)

    name_input = page.locator('input[name="city"]')
    city = "town"
    name_input.fill(city)

    name_input = page.locator('input[name="zip_code"]')
    zip_code = "94100"
    name_input.fill(zip_code)

    name_input = page.locator('input[name="hiring_date"]')
    hiring_date = "2005-07-25"
    name_input.fill(hiring_date)

    name_input = page.locator('input[name="job_title"]')
    job_title = "dev"
    name_input.fill(job_title)

    page.click("text='Add'")

    # Goto the team list
    teams_page.go_to_teams_page()
    
    # Check the new team is there
    assert page.is_visible(f"td:has-text('{name}')")


    # Update the date 
    page.click("text='Edit'")
    page.click("text='Update address'")

    name_input = page.locator('input[name="address_line1"]')
    address = "test town updated"
    name_input.fill(address)

    page.click("text='Update'")

    page.click("text='Update address'")

    address_line1_input = page.locator('input[name="address_line1"]')
    assert address_line1_input.input_value() == "test town updated"

    # Verify address_line2 is empty
    address_line2_input = page.locator('input[name="address_line2"]')
    assert address_line2_input.input_value() == "", "Le champ address 2 doit être vide"





