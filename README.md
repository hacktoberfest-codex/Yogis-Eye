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


# AWS Cloud Hosting with EC2 Instances, Load Balancer, and Scalability

Welcome to the documentation for deploying your web application on AWS with EC2 instances, an Elastic Load Balancer (ELB), and automatic scalability. This guide will help you set up a robust and scalable hosting environment.

## Table of Contents

- [Introduction](#introduction)
- [Prerequisites](#prerequisites)
- [Getting Started](#getting-started)
  - [Step 1: Launch EC2 Instances](#step-1-launch-ec2-instances)
  - [Step 2: Create an Elastic Load Balancer](#step-2-create-an-elastic-load-balancer)
  - [Step 3: Configure Auto Scaling](#step-3-configure-auto-scaling)
- [Scaling Strategies](#scaling-strategies)
- [Security Considerations](#security-considerations)
- [Contributing](#contributing)


## Introduction

This guide demonstrates how to deploy a highly available and scalable web application infrastructure on AWS. It combines the power of EC2 instances, Elastic Load Balancer (ELB), and Auto Scaling to ensure your application can handle varying loads seamlessly.

## Prerequisites

Before you begin, make sure you have the following:

- An AWS account with necessary permissions.
- Basic knowledge of AWS services like EC2, ELB, and Auto Scaling.
- Your web application code and dependencies ready for deployment.



## Getting Started

Follow these steps to deploy your web application on AWS:

### Step 1: Launch EC2 Instances

1. Launch EC2 instances with your desired Amazon Machine Image (AMI) and instance type.
2. Configure security groups to allow traffic on the required ports (e.g., port 80 for HTTP).
3. Install your application and any necessary dependencies on the instances.
4. Ensure your application is configured to start automatically on instance boot.

### Step 2: Create an Elastic Load Balancer

1. Create an Elastic Load Balancer (ELB) and configure listeners (e.g., HTTP on port 80).
2. Configure health checks to monitor the health of your EC2 instances.
3. Update your DNS records or use Route 53 to point your domain to the ELB's DNS name.

### Step 3: Configure Auto Scaling

1. Create an Auto Scaling Group (ASG) and specify your EC2 instances as part of the group.
2. Define scaling policies and triggers based on metrics like CPU utilization or requests per minute.
3. Set up minimum and maximum instance counts to control the scaling limits.

## Scaling Strategies
Load Balancers for Even Distribution:

Elastic Load Balancers (ELB): ELBs distribute incoming traffic across multiple EC2 instances to ensure high availability and improve fault tolerance. There are three types of ELBs: Application Load Balancers (ALB), Network Load Balancers (NLB), and Classic Load Balancers (CLB), each with specific use cases.

Health Checks: ELBs continuously monitor the health of instances. Unhealthy instances are automatically removed from the load balancer's rotation, ensuring that traffic is directed only to healthy instances.

## Monitoring and Alerting

Discuss how to monitor the health and performance of your AWS resources. Mention AWS CloudWatch for monitoring and setting up alarms to notify you of any issues.

## Security Considerations
Identity and Access Management (IAM):

Overview: AWS IAM allows you to control access to AWS services and resources. It defines who is allowed to do what in your AWS environment.
Best Practices: Follow the principle of least privilege, create IAM roles with specific permissions, use multi-factor authentication (MFA), and regularly review and audit IAM policies.

Backup and Disaster Recovery:

Implement regular backups of your data and ensure it's stored in geographically redundant locations.
Create disaster recovery plans to quickly recover from unexpected failures or data loss.
Security Awareness and Training:

Continuously educate your team on AWS security best practices.
AWS offers training resources and certifications to enhance knowledge and skills.
AWS provides a shared responsibility model, where AWS secures the infrastructure, and customers are responsible for securing their data and applications. By addressing these security considerations and staying informed about evolving threats, you can build a strong security posture in your AWS environment.



## Contributing

If you want to contribute to this documentation or the project itself, please follow the guidelines outlined in the readme.md file (if available).


---
