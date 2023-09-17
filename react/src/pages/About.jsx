import React from 'react';

const About = ({ name, role, image }) => {
    return (

        <div className='bg-teal'>

            <div className="text-center my-5">
                <h1 className="text-4xl font-bold">Identification of Different Medicinal Plants/Raw materials through Image Processing Using Machine Learning Algorithms
                </h1>
            </div>


            <div className="red m-10" >
                <h10 ><b>1</b> <b>Data Collection and Preprocessing:</b></h10>
                <ol>
                    <li > <b>--</b> Collect a diverse dataset of images of various medicinal plants
                        These images should cover different angles
                        lighting conditions, and growth stages.</li>
                    <li>  <b>--</b> Annotate the dataset labeling each image with the correct plant species.</li>
                </ol>
                <br />

                <h10> <b>2</b> <b>Feature Extraction:</b> </h10>


                <ol>
                    <li className='ml-2'> <b>2.1</b> Extract relevant features from the images. This step may include techniques like:</li>

                    <li className='ml-3'> <b>--</b>Color histogram analysis to capture the plant's color characteristics.</li>
                    <li className='ml-3'><b>--</b> Texture analysis to identify unique textural patterns in leaves, flowers, or stems.</li>
                    <li className='ml-3'> <b>--</b>Shape analysis to measure and compare the shapes of different plant parts.</li>



                </ol>
                <br />
                <h10 ><b>3</b> <b>Model Selection:</b></h10>
                <ol>
                    <li > <b>--</b> Choose an appropriate machine learning or deep learning model. Convolutional Neural Networks (CNNs) are commonly used for image classification tasks like this.</li>
                    <li>  <b>--</b> Pretrained models like VGG16, ResNet, or Inception can be fine-tuned on your dataset to leverage their feature extraction capabilities.</li>
                </ol>
                <br />
                <h10 ><b>4</b> <b>Training the Model:</b></h10>
                <ol>
                    <li > <b>--</b> Divide the dataset into training, validation, and testing sets.</li>
                    <li>  <b>--</b> Train the chosen model on the training set. The model learns to recognize patterns in the images and associate them with specific plant species.</li>
                    <li>  <b>--</b> Use the validation set to fine-tune hyperparameters and monitor the model's performance to prevent overfitting.</li>
                </ol>
                <br />
                <h10 ><b>5</b> <b>Testing and Evaluation:</b></h10>
                <ol>
                    <li > <b>--</b> Assess the model's performance on the testing dataset to evaluate its accuracy, precision, recall, and F1-score.</li>
                    <li>  <b>--</b>Consider using techniques like data augmentation to improve the model's generalization.</li>

                </ol>
                <br />
                <h10 ><b>6</b> <b>Deployment:</b></h10>
                <ol>
                    <li > <b>--</b>Once the model performs well, deploy it in the desired application. This could be a mobile app, a web tool, or integrated into a larger system.</li>
                    <li>  <b>--</b>Ensure the system can accept images as input and return the predicted plant species as output.</li>

                </ol>
                <br />

                <h10 ><b>7</b> <b>Continual Learning:</b></h10>
                <ol>
                    <li > <b>--</b>Regularly update the model with new data to keep it accurate, as the appearance of plants can vary with seasons and environmental conditions.</li>


                </ol>
                <br />
                <h10 > <b>8</b> <b>User Interface and User Experience (UI/UX):</b></h10>
                <ol>
                    <li > <b>--</b>Design a user-friendly interface for users to upload images of plants.</li>
                    <li > <b>--</b>Provide clear instructions and feedback to the users, such as the identified plant species and its medicinal properties.</li>



                </ol>
                <br />
                <h10 > <b>9</b> <b>Ethical Considerations:</b></h10>
                <ol>
                    <li > <b>--</b>Ensure that the AI model respects ethical and privacy concerns, such as data security and informed consent when collecting images.</li>




                </ol>
                <br />
                <h10 > <b>10</b> <b>Validation and Expert Consultation:</b></h10>
                <ol>
                    <li > <b>--</b>Validate the results of the AI model with experts in botany or pharmacology to ensure accuracy.</li>
                    <li > <b>--</b>The model can be a useful tool for experts but should not replace their knowledge and expertise.</li>



                </ol>
            </div>
            <div className="relative overflow-hidden">
                <img src={image} alt={name} className="w-full h-auto" />
                <div className="absolute top-0 left-0 w-full h-full bg-black opacity-0 hover:opacity-75 transition-opacity duration-300"></div>
                <div className="absolute bottom-0 left-0 w-full p-4 text-white transform translate-y-full transition-transform duration-300 group-hover:translate-y-0">
                    <h3 className="text-lg font-semibold">{name}</h3>
                    <p className="text-sm">{role}</p>
                    <span className="px-2 py-1 bg-red-500 text-white text-xs rounded-full inline-block mt-2">
                        Highlighted
                    </span>
                </div>
            </div>
        </div>
    );

};


export default About;
