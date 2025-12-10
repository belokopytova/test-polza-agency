import dns.resolver
import re

def is_valid_email(email: str) -> bool:

    pattern = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
    return re.match(pattern, email) is not None

def check_domain(domain: str):

    try:
        dns.resolver.resolve(domain, "NS")
    except Exception:
        return 'домен отсутствует'

    try:
        mx_records = dns.resolver.resolve(domain, 'MX')
        if mx_records:
            return 'домен валиден'
        else:
            return 'MX-записи отсутствуют или некорректны'
    except Exception:
        return 'MX-записи отсутствуют или некорректны'

def check_emails(list_emails: list):
    for email in list_emails:
        if is_valid_email(email):
            domain = email.split('@')[-1].strip().lower()
        else:
            print(f'{email}: домен отсутствует')
            continue
        result = check_domain(domain)
        print(f'{email}: {result}')
    return


if __name__ == '__main__':

    emails = [
        'test12@mail.ru',
        'test@rambler.ru',
        'test123@454.45.ru',
        'notexists@sfssdfsfvvvvdd.ru',
        'email123@gmail.com',
        'testtest',
        'test@'
    ]

    check_emails(emails)
