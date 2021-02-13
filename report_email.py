#!/usr/bin/env python3
import os
import datetime
import reports
import emails

proj_folder = os.getcwd() + '/supplier-data/descriptions/'


def generate_pdf(path):
    files = os.listdir(path)
    pdf = ''
    for file in files:
        if file.endswith('.txt'):
            with open(path + file, 'r') as f:
                text = f.read().splitlines()
                pdf += 'name: ' + text[0] + '<br/>' + 'weight: ' + text[1] + '<br/><br/>'
    return pdf


if __name__ == "__main__":
    # PDF creation
    path_to_save = os.getcwd() + '/tmp/processed.pdf'
    current_date = datetime.date.today().strftime('%B, %d %Y')
    title = 'Processed Update on ' + current_date
    body = generate_pdf(proj_folder)
    reports.generate_report(path_to_save, title, body)
    # Sending email
    sender = 'automation@example.com'
    receiver = "{}@example.com".format(os.environ["USER"])
    subject = 'Upload Completed - Online Fruit Store'
    body = 'All fruits are uploaded to our website successfully.' \
           ' A detailed list is attached to this email.'
    attachment = '/tmp/processed.pdf'
    message = emails.generate_email(sender, receiver, subject, body, attachment)
    emails.send_email(message)
