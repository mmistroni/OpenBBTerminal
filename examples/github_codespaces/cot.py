from openbb import obb
from pprint import pprint
import pandas as pd
    
import pandas as pd
import numpy as np
import os
    


def main():
    pd.set_option('display.max_columns', None)
    pd.set_option('display.max_rows', None) # Also handy if you want to see all rows
    pd.set_option('display.width', None)
    import os
    for k in os.environ.keys():
        if 'api_key' in k.lower():
            print(f"{k}={os.environ[k]}")
    print(f"Ffmp key is:{os.environ['fmp_api_key']}")
    
    future_ticker = 'vix'
    cot = obb.regulators.cftc.cot_search(query=future_ticker, provider='cftc').to_df()
    future_id = cot['code'].values.tolist()[0]
    print(f'Id for {future_ticker}={future_id}')
    cot_df = obb.regulators.cftc.cot(id=future_id, provider='cftc').to_df()
    
    

    vix_df  = obb.equity.price.historical(symbol='^VIX', provider='fmp').to_df()
    for c in vix_df.columns:
        print(c)
    

if __name__ == "__main__":
    main()
