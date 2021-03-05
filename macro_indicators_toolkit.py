from fredapi import Fred
fred = Fred(api_key='YOUR API KEY')

def treasury_ten_year():
    """
    Returns: 10-Year Treasury Constant Maturity Rate
    """
    treasury_lt = fred.get_series('DGS10')
    return treasury_lt

def treasury_one_year():
    """
    Returns: 1-Year Treasury Constant Maturity Rate
    """
    treasury_st = fred.get_series('DGS1')
    return treasury_st

def treasury_three_month():
    """
    Returns: 3-Month Treasury Constant Maturity Rate
    """
    treasury_stm = fred.get_series('DGS3MO')
    return treasury_stm

def unemployment_rate_us():
    """
    Return: Unemployment Rate
    """
    unempl = fred.get_series('UNRATE')
    return unempl

def unemployment_rate_by_state(start_date = '2020-01-01'):
    """
    Input: start date of the observations
    Returns: Unemployment Rate by State
    """
    states = ["AL", "AK", "AZ", "AR", "CA", "CO", "CT", "DC", "DE", "FL", "GA", "HI", "ID", "IL", "IN", "IA", "KS", "KY", "LA", "ME", "MD", "MA", "MI", "MN", "MS", "MO", "MT", "NE", "NV", "NH", "NJ", "NM", "NY", "NC", "ND", "OH", "OK", "OR", "PA", "RI", "SC", "SD", "TN", "TX", "UT", "VT", "VA", "WA", "WV", "WI", "WY"]
    by_state = []
    for st in states:
        data = fred.get_series(f'{st}UR', observation_start=start_date)
        by_state.append(data)
    df_ur = pd.concat(by_state, axis=1)
    df_ur.columns = states
    return df_ur

def sp_500():
    """
    Returns: S&P 500 for last 10 years, Index
    """
    sp = fred.get_series('SP500')
    return sp

def gdp_us():
    """
    Returns: Real US GDP, Billions of Dollars
    """
    gdp = fred.get_series('GDPC1')
    gdp.dropna(inplace=True)
    return gdp

def breakeven_inflation_us():
    """
    Returns: 10-Year Breakeven Inflation Rate
    Note: current inflation = same date, previous year
    """
    infl = fred.get_series('T10YIE')
    return infl

def consumption():
    """
    Returns: Real Personal Consumption Expenditures, Billions of Dollars
    """
    consmp = fred.get_series('PCEC96')
    consmp.dropna(inplace=True)
    return consmp






