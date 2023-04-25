# Credict Card Fraud Detection Service Example

1. Install dependencies:
```bash
pip install -r ./dev-requirements.txt
```

2. Download dataset

The dataset could be found on https://www.openml.org/search?type=data&sort=runs&id=42175&status=active
It is in arff format.

3. Train the fraud detection xgboost model. For details, see the https://www.kaggle.com/code/marcelotc/creditcard-fraud-xgboost-example
   notebook:
```bash
./train.sh
```

4. Run the ML Service locally:
```bash
bentoml serve
```

5. Send test requests:

Visit http://localhost:3000/ in a browser and send test requests via the UI.

Alternatively, send test payloads via CLI:

```bash
curl -X POST -H "Content-Type: application/json" -d @test.json http://127.0.0.1:3000/predict
```

6. Build a docker image for deployment

Build a Bento to lock the model version and dependency tree:
```bash
bentoml build
```

Ensure docker is installed and running, build a docker image with `bentoml containerize`
```bash
bentoml containerize credit_card_fraud_detection:latest
```

Test out the docker image built:

```bash
docker run -it --rm -p 3000:3000 credit_card_fraud_detection:{YOUR BENTO VERSION}
```
