from trial2vec import Trial2Vec, load_demo_data

# Load pretrained model
model = Trial2Vec()
model.from_pretrained()

# Load demo clinical trials
data = load_demo_data()
test_data = {'x': data['x']}

# Predict similar trials (retrieval)
pred = model.predict(test_data)

# See top-5 results for first trial
print(pred[0][:5])
