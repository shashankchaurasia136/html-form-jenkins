
from pathlib import Path
from bs4 import BeautifulSoup

def test_registration_form():
    html = Path("index.html").read_text(encoding="utf-8")
    soup = BeautifulSoup(html, "html.parser")

    form = soup.find("form", id="registrationForm")
    assert form is not None, "Registration form is missing"

    name = form.find("input", {"name": "name"})
    email = form.find("input", {"name": "email"})
    contact = form.find("input", {"name": "contact"})
    submit = form.find("button", {"type": "submit"})

    assert name is not None, "Name field is missing"
    assert email is not None, "Email field is missing"
    assert contact is not None, "Contact Number field is missing"
    assert submit is not None, "Submit button is missing"

    assert name.get("required") is not None
    assert email.get("required") is not None
    assert contact.get("required") is not None
