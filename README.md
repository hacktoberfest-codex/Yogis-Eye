# FastAPI and PostgreSQL in Docker

This repository provides a simple example of setting up a FastAPI application with a PostgreSQL database using Docker for containerization. It demonstrates how to create a RESTful API using FastAPI and use a PostgreSQL database as the backend storage.

## Prerequisites

Before you begin, ensure you have the following dependencies installed on your system:

- [Docker](https://www.docker.com/)
- [Docker Compose](https://docs.docker.com/compose/)

## Getting Started

Follow these steps to get the project up and running:
1. Clone the repository to your local machine:

    ```bash
    git clone https://github.com/ITER-SIH/Team-37.git
    ```
2. Navigate to the project directory:

    ```bash
    cd app
    ```
3. Build Docker image using Docker Compose:
    ```bash
    docker-compose build
    ```
4. run docker containers
    ```bash
    docker-compose up
    ```
5. Once containers are up and running, you can access the FastAPI application at http://localhost:8000.

## API Documentation
The FastAPI application provides the following endpoints:

- **`GET /plants/{plant_id}`**: Retrieve a plant with plant_id
- **`GET /details/(plant_id)`**: Retrieve details of plant with plant_id
- **`POST /plants/`**: create a plant with plant_text and other details
- **`POST /predict_plant`**: predict a plant after uploading image


# ML Documentation

## Transfer learning on custom dataset using EffNetv3 model
EffNet is a PyTorch-based deep learning model designed for image classification tasks. It uses the EfficientNet architecture as its backbone for feature extraction and classification. This model provides a powerful yet lightweight solution for a variety of image classification applications.

### Model Architecture
EffNet consists of the following components:

- **Backbone**:  EffNet uses the **`efficientnet_b1`** architecture as its backbone. This backbone is pretrained on a large dataset and can extract meaningful features from input images.

- **Classifier**: The classifier head of EffNet consists of multiple fully connected layers with batch normalization and PReLU activation functions. It reduces the feature dimensionality to the desired embedding size and performs the final classification.

### Model Prediction function

```bash
def predict(img):
    if torch.cuda.is_available():
        DEVICE = torch.device(type='cuda')
    else:
        DEVICE = torch.device('cpu')


    model= EffNet(num_classes=NUM_CLASSES, embedding_size=EMBEDDING_SIZE)
    model.load_state_dict(torch.load(W_PATH,map_location=torch.device(DEVICE)))
    image = Image.open(io.BytesIO(img))
    image = my_transforms(image)

    model.to(DEVICE)
    model.eval()


    with torch.inference_mode():
        
        image = image.to(DEVICE)
        image = image.unsqueeze(0)
        with autocast():
            logits = model.forward(image)

            y_pred = torch.softmax(logits, dim=1).argmax(dim=1).detach().cpu()

    return CLASS_LABEL[y_pred.item()]
```

