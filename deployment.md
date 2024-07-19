### Generate Powerful SecretKey
to generate powerful secretkey for django app enter the command below in the terminal with activated venv:

`python manage.py shell -c "from django.core.management.utils import get_random_secret_key; print(get_random_secret_key())"`

paste the generated and printed secretkey in the .env file.

### Resolve Deploy Warnings
Set the `DEBUG` in `.env` file to True.
I added some code, you need to change the `DEBUG` flag in `RefrallApp/settings.py` to `False` and all the warnings will be gone.

#### Warning:
- When `DEBUG` is `False` in `.env` file, the usual `python manage.py runserver` will work but server will not respond `localhost:8000`, because it will not support `https`. to run django server on local machine supporting ssl, use `daphne`. I added it to `requirements.txt`.
- To run server on local machine with ssl using daphne, after running `pip install -r requirements.txt`, run:
    1. `openssl req -x509 -newkey rsa:4096 -keyout key.pem -out cert.pem -days 365 -nodes` this will generate a free ssl certificate for local
    2. `daphne -e ssl:8000:privateKey=key.pem:certKey=cert.pem ReferralApp.asgi:application`
`


#### Warning:
- To resolve all the warnings, we should enable the HSTS, When you turn `DEBUG` flag to `False` the added code in `RefrallApp/settings.py` will enable HSTS,
Before enabling HSTS, ensure that your entire site and all subdomains support HTTPS, as browsers will not allow users to bypass the security once HSTS is enabled.
- `SECURE_HSTS_PRELOAD`: This indicates that your site is ready to be included in browsers' HSTS preload lists. If you set this to True, you should submit your domain to the HSTS preload list maintained by Google. take a look at here: `https://hstspreload.org/`


### Changed DB
When you use `DEBUG=False` in `.env` file, db changes to `POSTGRESQL`, and this needs `psycopg2` to be installed. I added it to `requirements.txt` file.

## Deploy
To Deploy check this:
`https://fly.io/docs/django/getting-started/`
I used this document to install flyctl and deploy:
`https://fly.io/django/`
0. install flyctl on mac os
   1. brew install flyctl
1. pull the repository I made
2. in the root, run fly launch
3. when it asks "Do you want to tweak these settings before proceeding?" please enter y
4. in the opened browser tab, select damc organisation
5. in app name enter "refapp"
6. in postgres section choose the option "fly automated postgres"
7. and then when fly launch process completed, run "fly deploy"

