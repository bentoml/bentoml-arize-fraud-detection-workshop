

import bentoml
import pandas as pd

runner = bentoml.xgboost.get("fraud_det").to_runner()
# runner2 = bentoml.pytorch.get....
svc = bentoml.Service("credit_card_fraud_detection", runners=[runner])

@svc.api(input=bentoml.io.JSON(), output=bentoml.io.JSON())
def predict(input_json):
    with bentoml.monitor("fraud_det") as mon:
        mon.log(input_json["Amount"], "Amount", role="feature", data_type="numerical")
        for i in range(1, 29):
            col_name = f"V{i}"
            mon.log(input_json[col_name], col_name, role="feature", data_type="numerical")
    
        df = pd.DataFrame.from_dict(input_json, orient='index').transpose()
        result = runner.predict.run(df)[0]
        mon.log(result, "prediction", role="prediction", data_type="categorical")
    
    return {"result": result}
