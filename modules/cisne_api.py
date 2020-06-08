import requests
import json
import pandas as pd


def CisneGetData(curr_date, save_json=False):
    '''
    Parameters
    ----------
    curr_date: (str) Date in yyyy-mm-dd

    Return
    ------
    (DataFrame) obj
    (True) if save successfully the file when save_json is enabled.

    Example
    -------
    >> CisneGetData('2020-06-07')
    '''

    LOGIN_URL = "http://intranet.transportescisne.com.br/swan/login"

    # Fill in your details here to be posted to the login form.
    payload = json.load( open('credentials/cisne_credentials.json') )

    # Use 'with' to ensure the session context is closed after use.
    with requests.Session() as S:
        S.post(LOGIN_URL, data=payload)
        # print("Logged successfully!")
        r = S.get("http://intranet.transportescisne.com.br/swan/api/passageiros/"+curr_date)
        if save_json:
            with open('json-'+curr_date, 'w') as file:
                file.write(r.text)
            return True

        # Transform str to json object like
        json_response = json.loads(r.text)

        _linha = []
        _sentido = []
        _faixahr = []
        _passageiros = []

        for i in json_response:
            _linha.append(i['linha'])
            _sentido.append(i['sentido'])
            _faixahr.append(i['faixahr'])
            _passageiros.append(i['passageiros'])
        
        return pd.DataFrame({
            'linha':_linha,
            'sentido':_sentido,
            'faixahr':_faixahr,
            'passageiros':_passageiros
        })