from google.cloud import storage
from google.cloud import aiplatform
import random
import string

# Function to generate a unique identifier for the storage bucket
def generate_uuid(length=8):
    return "".join(random.choices(string.ascii_lowercase + string.digits, k=length))

# Generate a UUID
UUID = generate_uuid()

# Google Cloud project and credentials setup
PROJECT_ID = 'your_project_id_here'
CREDENTIALS = 'your_credentials_here'

# Initialize Vertex AI SDK
aiplatform.init(project=PROJECT_ID, credentials=CREDENTIALS)

# Create a Google Cloud storage client
storage_client = storage.Client(project=PROJECT_ID, credentials=CREDENTIALS)

# Construct a unique name for the bucket
bucket_name = f'carbon-course-bucket-{UUID}'

# Create a new bucket in the specified region
REGION = 'us-central1'
bucket = storage_client.bucket(bucket_name)
bucket.create(location=REGION)

# Write the ML training code to a file
with open('task.py', 'w') as f:
    f.write("""
import numpy as np
from sklearn.datasets import make_blobs
import tensorflow as tf
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense

# Create dataset
classes = 4
m = 100
centers = [[-5, 2], [-2, -2], [1, 2], [5, -2]]
std = 1.0
X_train, y_train = make_blobs(n_samples=m, centers=centers, cluster_std=std, random_state=30)

# Create the model
model = Sequential([
    Dense(2, activation='relu', name="L1"),
    Dense(4, activation='linear', name="L2")
])

model.compile(
    loss=tf.keras.losses.SparseCategoricalCrossentropy(from_logits=True),
    optimizer=tf.keras.optimizers.Adam(0.01),
)

# Train
model.fit(X_train, y_train, epochs=200)
    """)

# Set up a custom training job on Vertex AI
job = aiplatform.CustomTrainingJob(
    display_name='dlai-course-example',
    script_path='task.py',
    container_uri='us-docker.pkg.dev/vertex-ai/training/tf-cpu.2-14.py310:latest',
    staging_bucket=f'gs://{bucket_name}',
    location=REGION,
)

# Run the training job
model = job.run()

# Clean up resources
bucket.delete(force=True)
