def test_upgrade_manager(reset_db,page):
     # Create an employee 
    page.goto("/")
    page.goto("/add_employee")
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
    zip_code = "9410041348971329781349783129871947898713297813428971328947"
    name_input.fill(zip_code)

    name_input = page.locator('input[name="hiring_date"]')
    hiring_date = "2005-07-25"
    name_input.fill(hiring_date)

    name_input = page.locator('input[name="job_title"]')
    job_title = "dev"
    name_input.fill(job_title)


    page.click("text='Add'")
    assert page.url == "https://e.se2.hr.dmerej.info", "Erreur : 500"
