"""
Day 28: RegEx, Patterns, and Intro to Databases 

https://www.hackerrank.com/challenges/30-regex-patterns
"""
import unittest
import re


class Contacts(object):
    def __init__(self):
        self.contacts = []

    def add(self, name, email):
        self.contacts.append(
            {
                "name": name,
                "email": email,
            }
        )

    def filter(self):
        results = []
        gmail_filter_re = re.compile(r"[a-z.]+@gmail\.com$")

        for contact in self.contacts:
            m = gmail_filter_re.match(contact["email"])
            if m is None:
                continue

            results.append(contact["name"])

        return sorted(results)


if __name__ == '__main__':
    contacts = Contacts()

    N = int(input().strip())
    for a0 in range(N):
        firstName, emailID = input().strip().split(' ')
        firstName, emailID = [str(firstName), str(emailID)]

        contacts.add(firstName, emailID)

    print("\n".join(contacts.filter()))


class TestContacts(unittest.TestCase):
    def test_filter(self):
        contacts = Contacts()
        samples = [
            ("riya", "riya@gmail.com"),
            ("julia", "julia@julia.me"),
            ("julia", "sjulia@gmail.com"),
            ("julia", "julia@gmail.com"),
            ("samantha", "samantha@gmail.com"),
            ("tanya", "tanya@gmail.com"),
        ]

        for item in samples:
            contacts.add(item[0], item[1])

        self.assertEqual(
            ["julia", "julia", "riya", "samantha", "tanya"],
            contacts.filter()
        )

    def test_filter_max(self):
        contacts = Contacts()
        samples = [
            ("riya", "riya@gmail.com"),
            ("julia", "julia@julia.me"),
            ("julia", "sjulia@gmail.com"),
            ("julia", "julia@gmail.com"),
            ("samantha", "samantha@gmail.com"),
            ("tanya", "tanya@gmail.com"),
            ("riya", "ariya@gmail.com"),
            ("julia", "bjulia@julia.me"),
            ("julia", "csjulia@gmail.com"),
            ("julia", "djulia@gmail.com"),
            ("samantha", "esamantha@gmail.com"),
            ("tanya", "ftanya@gmail.com"),
            ("riya", "riya@live.com"),
            ("julia", "julia@live.com"),
            ("julia", "sjulia@live.com"),
            ("julia", "julia@live.com"),
            ("samantha", "samantha@live.com"),
            ("tanya", "tanya@live.com"),
            ("riya", "ariya@live.com"),
            ("julia", "bjulia@live.com"),
            ("julia", "csjulia@live.com"),
            ("julia", "djulia@live.com"),
            ("samantha", "esamantha@live.com"),
            ("tanya", "ftanya@live.com"),
            ("riya", "gmail@riya.com"),
            ("priya", "priya@gmail.com"),
            ("preeti", "preeti@gmail.com"),
            ("alice", "alice@alicegmail.com"),
            ("alice", "alice@gmail.com"),
            ("alice", "gmail.alice@gmail.com"),
        ]

        answer = [
            "alice",
            "alice",
            "julia",
            "julia",
            "julia",
            "julia",
            "preeti",
            "priya",
            "riya",
            "riya",
            "samantha",
            "samantha",
            "tanya",
            "tanya",
        ]

        for item in samples:
            contacts.add(item[0], item[1])

        self.assertEqual(
            answer,
            contacts.filter()
        )
