import os
import fire
from dotenv import load_dotenv
import requests
from slugify import slugify

load_dotenv()


def create(service_name):
    api_key = os.getenv('CLOUDFLARE_API_KEY')
    zone_id = os.getenv('CLOUDFLARE_ZONE_ID')
    forward_email = os.getenv('FORWARD_EMAIL')
    email_domain = os.getenv('CLOUDFLARE_EMAIL_DOMAIN')

    headers = {
        'Authorization': f'Bearer {api_key}',
        'Content-Type': 'application/json'
    }

    slug_service_name = slugify(service_name)
    email_address = f'{slug_service_name}@{email_domain}'

    payload = {
        'actions': [
            {
                'type': 'forward',
                'value': [forward_email],
            },
        ],
        'enabled': True,
        'matchers': [
            {
                'field': 'to',
                'type': 'literal',
                'value': email_address,
            },
        ],
        'name': f'Handle e-mails from {service_name}',
        'priority': 0,
    }

    response = requests.post(
        f'https://api.cloudflare.com/client/v4/zones/{zone_id}/email/routing/rules',
        headers=headers,
        json=payload,
    )

    if response.status_code == 200:
        print('E-mail created:', email_address)
    else:
        print('Error creating service!')
        print(response.json())


if __name__ == '__main__':
    fire.Fire(create)
