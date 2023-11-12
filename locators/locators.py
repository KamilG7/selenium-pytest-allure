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


class MainSiteLocators:

    main_site_header_xpath = "//input[@class='et_pb_s']"


class LoginPageLocators:

    input_email_id = "user[email]"
    input_password_id = "user[password]"
    login_button_xpath = "//button[contains(text(), 'Sign in')]"
    forgot_password_xpath = "//a[contains(text(), 'Forgot Password')]"
    forgot_password_email_id = "user[email]"
    forgot_password_info_xpath = "//h2[@class='password-reset__heading']"
    forgot_password_submit_name = "commit"
    error_list_xpath = "//li[@class='form-error__list-item']"


class ProfessionalServicesLocators:

    contact_name_id = "wpforms-217788-field_0"
    contact_email_id = "wpforms-217788-field_1"
    job_tittle_id = 'wpforms-217788-field_4'
    company_name_id = "wpforms-217788-field_3"
    message_input_id = "wpforms-217788-field_2"
    captcha_id = "recaptcha-anchor"
    send_message_button_id = "wpforms-submit-217788"
    confirmation_message_xpath = '//div[@class="wpforms-confirmation-container-full wpforms-confirmation-scroll"]/p'
