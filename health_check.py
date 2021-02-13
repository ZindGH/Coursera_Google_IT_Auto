#!/usr/bin/env python3
import psutil
import socket
import os
import emails


def send_warning(subject):
    sender = 'automation@example.com'
    receiver = "{}@example.com".format(os.environ["USER"])
    body = 'Please check your system and resolve the issue as soon as possible.'
    message = emails.generate_email(sender, receiver, subject, body)
    emails.send_email(message)
    return None


def cpu_check():
    if psutil.cpu_percent() > 80:
        send_warning('Error - CPU usage is over 80%')
    return None


def memory_check():
    available_memory = psutil.virtual_memory().available
    if available_memory < 500 * 1024 * 1024:
        send_warning('Error - Available memory is less than 500MB')
    return None


def disk_check():
    disk_memory = psutil.disk_usage('/')
    if disk_memory.free / disk_memory.total < 0.2:
        send_warning('Error - Available disk space is less than 20%')
    return None


def internet_check():
    local_host = socket.gethostbyname('localhost')
    if local_host != "127.0.0.1":
        send_warning('Error - localhost cannot be resolved to 127.0.0.1')
    return None


cpu_check()
memory_check()
disk_check()
internet_check()
