import React, { useState } from "react";
import { FaStar } from "react-icons/fa";

const RateVendorForm = () => {
  const [rating, setRating] = useState(0);
  const [hover, setHover] = useState(null);
  const [vendor, setVendor] = useState("");
  const [formData, setFormData] = useState({
    review_text: "",
    delivery_date: "",
    eco_friendly_packaging: false,
    image: null,
  });
  const [showSuccessMessage, setShowSuccessMessage] = useState(false);

  const vendorOptions = [
    "The Conscious Farm Kitchen",
    "BIO RAW",
    "Goodfood",
    "Hellofresh",
    "Green Cherf",
    "SkipTheDishes",
    "Greeen Chef",
  ];

  const handleChange = (e) => {
    const { name, value, type, checked, files } = e.target;

    setFormData((prevData) => ({
      ...prevData,
      [name]:
        type === "checkbox" ? checked : type === "file" ? files[0] : value,
    }));
  };

  const handleSubmit = async (e) => {
    e.preventDefault();

    const formDataToSend = new FormData();
    formDataToSend.append("vendor", vendor);
    formDataToSend.append("rating", rating);
    formDataToSend.append("review_text", formData.review_text);
    formDataToSend.append("delivery_date", formData.delivery_date);
    formDataToSend.append(
      "eco_friendly_packaging",
      formData.eco_friendly_packaging
    );

    if (formData.image) {
      formDataToSend.append("image", formData.image);
    }

    const token = localStorage.getItem("token");
    console.log("Token being sent:", token);

    try {
      const response = await fetch(
        "http://127.0.0.1:8084/polls/delivery_rating/",
        {
          method: "POST",
          headers: {
            Authorization: `Token ${token}`,
          },
          body: formDataToSend,
          credentials: "include",
        }
      );

      console.log("Form Data sent:", Object.fromEntries(formDataToSend));

      if (response.ok) {
        console.log("Form submitted successfully!");

        setShowSuccessMessage(true);
        setTimeout(() => {
          setShowSuccessMessage(false);
        }, 3000);

        // Reset form
        setVendor("");
        setRating(0);
        setFormData({
          review_text: "",
          delivery_date: "",
          eco_friendly_packaging: false,
          image: null,
        });
      } else {
        console.log("Failed to submit form.");
        const errorData = await response.json();
        console.error("Error details:", errorData);
      }
    } catch (error) {
      console.error("Error submitting form:", error);
    }
  };

  return (
    <div className="max-w-xl mx-auto mt-10 bg-white p-6 rounded-xl shadow-lg">
      <h1 className="text-3xl font-bold mb-6 text-green-700">
        Rate a Vendor's Delivery
      </h1>

      <div
        className={`fixed bottom-5 right-5 bg-green-100 border border-green-400 text-green-800 px-4 py-3 rounded shadow-lg z-50 transition-all duration-500 ${
          showSuccessMessage ? "opacity-100" : "opacity-0"
        }`}
      >
        ✅ Form submitted successfully!
      </div>

      <form onSubmit={handleSubmit}>
        {/* Vendor Dropdown */}
        <div className="mb-6">
          <label className="block text-green-800 font-semibold mb-2">
            Vendor
          </label>
          <select
            className="w-full border rounded-md p-2"
            value={vendor}
            onChange={(e) => setVendor(e.target.value)}
            required
          >
            <option value="">----------</option>
            {vendorOptions.map((v, index) => (
              <option key={index} value={v}>
                {v}
              </option>
            ))}
          </select>
        </div>

        {/* Rating Stars */}
        <div className="mb-6">
          <label className="block text-green-800 font-semibold mb-2">
            Rating
          </label>
          <div className="flex">
            {[...Array(5)].map((_, index) => {
              const starValue = index + 1;
              return (
                <label key={index}>
                  <input
                    type="radio"
                    name="rating"
                    value={starValue}
                    className="hidden"
                    onClick={() => setRating(starValue)}
                  />
                  <FaStar
                    className={`cursor-pointer text-4xl ${
                      starValue <= (hover || rating)
                        ? "text-yellow-400"
                        : "text-gray-300"
                    }`}
                    onMouseEnter={() => setHover(starValue)}
                    onMouseLeave={() => setHover(null)}
                  />
                </label>
              );
            })}
          </div>
        </div>

        {/* Image Upload */}
        <div className="mb-4">
          <label className="block mb-1 font-medium">Upload Image</label>
          <input
            type="file"
            name="image"
            accept="image/*"
            onChange={handleChange}
            className="w-full border p-2 rounded"
          />
        </div>

        {/* Review Text */}
        <div className="mb-4">
          <label className="block mb-1 font-medium">Review</label>
          <textarea
            name="review_text"
            value={formData.review_text}
            onChange={handleChange}
            rows="4"
            className="w-full border p-2 rounded"
            placeholder="Write your review here..."
            required
          ></textarea>
        </div>

        {/* Delivery Date */}
        <div className="mb-4">
          <label className="block mb-1 font-medium">Delivery Date</label>
          <input
            type="date"
            name="delivery_date"
            value={formData.delivery_date}
            onChange={handleChange}
            className="w-full border p-2 rounded"
            required
          />
        </div>

        {/* Checkbox */}
        <div className="mb-4 flex items-center">
          <input
            type="checkbox"
            name="eco_friendly_packaging"
            checked={formData.eco_friendly_packaging}
            onChange={handleChange}
            className="mr-2"
          />
          <label className="font-medium">Is the Packaging Eco-friendly?</label>
        </div>

        {/* Buttons */}
        <div className="flex justify-between items-center mt-6">
          <button
            type="submit"
            className="bg-green-600 text-white px-6 py-2 rounded hover:bg-green-700 transition"
          >
            Submit
          </button>
          <a
            href="/"
            className="bg-gray-300 text-gray-800 px-6 py-2 rounded hover:bg-gray-400 transition"
          >
            Discard
          </a>
        </div>
      </form>
    </div>
  );
};

export default RateVendorForm;
