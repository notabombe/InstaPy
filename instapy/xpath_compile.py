#!/usr/bin/env python
# -*- coding: utf-8 -*-

xpath = {
    "bypass_suspicious_login": {
        "bypass_with_sms_option": "//label[contains(text(),'Phone:')]",
        "bypass_with_email_option": "//label[contains(text(),'Email:')]",
        "send_security_code_button": "//button[text()='Send Security Code']",
        "security_code_field": "//input[@id='security_code']",
        "submit_security_code_button": "//button[text()='Submit']",
        "wrong_login": "//p[text()='Please check the code we sent you and try again.']",
    },
    "dismiss_this_was_me": {
        "this_was_me_button": "//button[@name='choice'][text()='This Was Me']"
    },
    "class_selectors": {
        "likes_dialog_body_xpath": "//main",
        "likes_dialog_close_xpath": "//*[*[local-name()='svg']/@aria-label='Close']",
    },
    "confirm_unfollow": {"button_xp": "//button[text()='Unfollow']"},
    "dialog_username_extractor": {"person": "../../*"},
    "dismiss_get_app_offer": {
        "offer_elem": "//*[contains(text(), 'Get App')]",
        "dismiss_elem": "//*[contains(text(), 'Not Now')]",
    },
    "dismiss_notification_offer": {
        "offer_elem_loc": "//div/h2[text()='Turn on Notifications']",
        "dismiss_elem_loc": "//button[text()='Not Now']",
    },
    "dismiss_save_information": {
        "offer_elem_loc": "//*[contains(text(), 'Save Info')]",
        "dismiss_elem_loc": "//*[contains(text(), 'Not Now')]",
    },
    "extract_information": {
        "close_overlay": "//div/div[@role='dialog']",
        "one_pic_elem": "//section/main/article/div[1]/div/div[10]/div[3]/a/div",
        "like_element": "//a[@role='button']/span[text()='Like']/..",
    },
    "extract_post_info": {
        "comment_list": "//div/ul",
        "comments": "//li[@role='menuitem']",
        "load_more_comments_element": "//div/ul/li/div/button",
        "load_more_comments_element_alt": "//div/ul/li[1]/button",
    },
    "find_user_id": {"meta_XP": "//meta[@property='instapp:owner_user_id']"},
    "get_active_users": {
        "profile_posts": "(//div[contains(@class, '_9AhH0')])[{}]",
        "likers_count": "//section/div/div/a/span",
        "likes_button": "//div[@class='Nm9Fw']/a",
        "next_button": "//a[text()='Next']",
        "topCount_elements": "//span[contains(@class,'g47SY')]",
    },
    "get_buttons_from_dialog": {
        "follow_button": "//button[text()='Follow']",
        "unfollow_button": "//button[text() = 'Following']",
    },
    "get_comment_input": {
        "comment_input": "//form/textarea",
        "placeholder": '//textarea[@Placeholder = "Add a comment…"]',
    },
    "get_comments_on_post": {
        "commenter_elem": "//*[contains(@class,'FPmhX')]",
        "comments_block": "//*[contains(@class,'EtaWk')]",
        "like_button_full_XPath": "//*[*[local-name()='svg']/@aria-label='Like']",
        "unlike_button_full_XPath": "//*[*[local-name()='svg']/@aria-label='Unlike']",
    },
    "get_cord_location": {"json_text": "//body"},
    "get_following_status": {
        "follow_button_XP": "//button[text()='Following' or \
                                  text()='Requested' or \
                                  text()='Follow' or \
                                  text()='Follow Back' or \
                                  text()='Unblock']",
        "follow_span_XP_following": "//button/div/span[contains(@aria-label, 'Following')]",
    },
    "get_follow_requests": {
        "list_of_users": "//section/div",
        "view_more_button": "//button[text()='View More']",
    },
    "get_given_user_followers": {"followers_link": "//ul/li[2]/a/span"},
    "get_given_user_following": {
        "all_following": "//a[contains(@href,'following')]/span",
        "topCount_elements": "//span[contains(@class,'g47SY')]",
        "following_link": '//a[@href="/{}/following/"]',
    },
    "get_photo_urls_from_profile": {"photos_a_elems": "//div/a"},
    "get_links_for_location": {
        "top_elements": "//main/article/div[1]",
        "main_elem": "//main/article/div[2]",
    },
    "get_links_from_feed": {"get_links": "//article/div[3]/div[2]/a"},
    "get_links_for_tag": {
        "top_elements": "//main/article/div[1]",
        "main_elem": "//main/article/div[2]",
        "possible_post": "//span[contains(@class, 'g47SY')]",
    },
    "get_number_of_posts": {
        "num_of_posts_txt": "//section/main/div/ul/li[1]/span/span",
        "num_of_posts_txt_no_such_element": "//section/div[3]/div/header/section/ul/li[1]/span/span",
    },
    "get_relationship_counts": {
        "following_count": "//a[contains(@href,'following') and not(contains(@href,'mutual'))]/span",
        "followers_count": "//a[contains(@href,'followers') and not(contains(@href,'mutual'))]/span",
        "topCount_elements": "//span[contains(@class,'g47SY')]",
    },
    "get_source_link": {
        "image": '//img[@class="FFVAD"]',
        "image_alt": '//img[@class="_8jZFn"]',
        "video": '//video[@class="tWeCl"]',
    },
    "get_users_through_dialog": {
        "find_dialog_box": "//body/div[4]/div/div[2]"
    },
    "is_private_profile": {"is_private": '//h2[@class="_kcrwx"]'},
    "like_comment": {
        "comments_block": "//*[contains(@class,'EtaWk')]",
        "span_like_elements": "//span[@aria-label='Like']",
        "comment_like_button": "..",
    },
    "like_image": {
        "like": "//section/span/button/div/span[*[local-name()='svg']/@aria-label='Like']",
        "unlike": "//section/span/button/div/span[*[local-name()='svg']/@aria-label='Unlike']",
        "play": "//*/span[contains(@aria-label, 'Play')]",
    },
    "like_from_image": {
        "main_article": "//main//article//div//div[1]//div[1]//a[1]"
    },
    "login_user": {
        "input_password": "//input[@name='password']",
        "input_username_XP": "//input[@name='username']",
        "login_elem": "//button[text()='Log In']",
        "login_elem_no_such_exception": "//a[text()='Log in']",
        "login_elem_no_such_exception_2": "//div[text()='Log In']",
        "nav": "//nav",
        "website_status": "//span[@id='status']",
        "response_time": "//span[@id='response']",
        "response_code": "//span[@id='code']",
        "account_disabled": "//p[contains(text(),'Your account has been disabled')]",
        "add_phone_number": "//h2[text()='Add Your Phone Number']",
        "suspicious_login_attempt": "//p[text()='Suspicious Login Attempt']",
        "error_alert": "//p[@id='slfErrorAlert']",
        "verification_code": "//input[@name='verificationCode']",
        "confirm": "//button[text()='Confirm']",
    },
    "open_comment_section": {
        "comment_elem": "//button/div[*[local-name()='svg']/@aria-label='Comment']"
    },
    "unfollow": {
        "following_link": "//ul/li[3]/a/span",
        "find_dialog_box": "//section/main/div[2]",
    },
    "watch_story_for_tag": {
        "explore_stories": "//section/main/header/div[1]/div"
    },
    "watch_story_for_user": {
        "explore_stories": "//section/main/div/header/div/div"
    },
    "watch_story": {
        "next_first": "/html/body/span/section/div/div/section/div[2]/button",
        "next": "/html/body/span/section/div/div/section/div[2]/button[2]",
    },
    "likers_from_photo": {
        "liked_counter_button": "//a[contains(@href,'liked_by')]/span",
        "second_counter_button": "//a[contains(@href,'liked_by')]",
    },
    "accept_igcookie_dialogue": {"accept_button": "//button[text()='Accept']"},
}
