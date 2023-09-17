import React, { useState } from 'react';

const ImageUploadWithForm = () => {
    const [selectedImage, setSelectedImage] = useState(null);
    const [formData, setFormData] = useState({
        name: '',
        familyName: '',
        description: '',
        biologicalName: '',
        url: '',
    });

    const handleImageUpload = (e) => {
        const file = e.target.files[0];
        if (file) {
            const reader = new FileReader();
            reader.onload = () => {
                setSelectedImage(reader.result);
            };
            reader.readAsDataURL(file);
        }
    };

    const handleChange = (e) => {
        const { name, value } = e.target;
        setFormData({
            ...formData,
            [name]: value,
        });
        console.log(formData);
    };

    return (
        <div className="min-h-screen  flex flex-col items-center justify-center my-10">
            <div className="bg-white shadow-md rounded-lg p-6 w-96">
                <h1 className="text-2xl font-semibold mb-4">Upload an Image</h1>
                {selectedImage ? (
                    <div className="mb-4">
                        <img
                            src={selectedImage}
                            alt="Uploaded"
                            className="w-full h-auto rounded-lg"
                        />
                    </div>
                ) : (
                    <div className="border-dashed border-2 border-gray-300 p-6 rounded-lg mb-4 text-center">
                        <input
                            type="file"
                            accept="image/*"
                            onChange={handleImageUpload}
                            className="hidden"
                            id="fileInput"
                        />
                        <label
                            htmlFor="fileInput"
                            className="cursor-pointer text-blue-500 hover:text-blue-700"
                        >
                            Click to Upload
                        </label>
                    </div>
                )}
                {selectedImage && (
                    <button
                        onClick={() => setSelectedImage(null)}
                        className=" text-white font-semibold py-2 mx-auto  px-4 rounded-lg bg-green-600"
                    >
                        About Plant
                    </button>
                )}
                <form>
                    <div className="mb-4 py-2">
                        <input
                            type="text"
                            name="name"
                            value={formData.name}
                            onChange={handleChange}
                            placeholder="Name"
                            className="border rounded-lg py-2 px-3 w-full"
                        />
                    </div>
                    <div className="mb-4">
                        <input
                            type="text"
                            name="familyName"
                            value={formData.familyName}
                            onChange={handleChange}
                            placeholder="Family Name"
                            className="border rounded-lg py-2 px-3 w-full"
                        />
                    </div>
                    <div className="mb-4">
                        <textarea
                            name="description"
                            value={formData.description}
                            onChange={handleChange}
                            placeholder="Description"
                            className="border rounded-lg py-2 px-3 w-full h-32 resize-none"
                        />
                    </div>
                    <div className="mb-4">
                        <input
                            type="text"
                            name="biologicalName"
                            value={formData.biologicalName}
                            onChange={handleChange}
                            placeholder="Biological Name"
                            className="border rounded-lg py-2 px-3 w-full"
                        />
                    </div>
                    <div className="mb-4">
                        <input
                            type="text"
                            name="url"
                            value={formData.url}
                            onChange={handleChange}
                            placeholder="URL"
                            className="border rounded-lg py-2 px-3 w-full"
                        />
                    </div>
                </form>

            </div>
        </div>
    );
};

export default ImageUploadWithForm;
