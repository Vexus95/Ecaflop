def test_delete_team(reset_db, page):

    # Create a team 
    page.goto("/")
    page.goto("/add_team")
    name_input = page.locator('input[name="name"]')
    team_name = "my team"
    name_input.fill(team_name)
    page.click("text='Add'")

    # Goto the team list
    page.goto("/teams")

    # Check the new team is there
    assert page.is_visible(f"td:has-text('{team_name}')")

    # delete a team 
    page.goto("/")
    page.goto("/teams")
    page.click("text='Delete'")
    page.click("text='Proceed'")