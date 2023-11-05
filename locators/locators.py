class RegistrationLocators:


    registration_name_id = "user[first_name]"
    registration_surname_id = "user[last_name]"
    registration_email_id = "user[email]"
    registration_password_id = "user[password]"
    terms_checkbox_id = "user[terms]"
    registration_submit_button_xpath = "//div/button[@class='button button-primary g-recaptcha']"
    terms_of_use_link_text = "Terms of Use"
    privacy_policy_link_text = "Customer Privacy Policy"
    error_list_xpath = "//ul/li[@class='form-error__list-item']"
    user_drop_xpath = "//li/button[@class='dropdown__toggle-button']"
    sign_out_xpath = "//a[contains(text(), 'Sign Out')]"
    sign_in_xpath = "//a[contains(text(), 'Sign In')]"