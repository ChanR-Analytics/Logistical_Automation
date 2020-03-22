import re

def gmail_to_slides_parser(contact_list: str) -> str:
    contacts_as_list = contact_list.split(",")
    emails = [email[email.index("<")+1:-1] for email in contacts_as_list]
    return ", ".join(emails)
