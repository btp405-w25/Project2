import React, { useState, useEffect } from "react";
import { Link } from "react-router-dom";

function FoodList() {
  const [foods, setFoods] = useState([]);
  const [loading, setLoading] = useState(true);
  const [error, setError] = useState(null);

  useEffect(() => {
    const fetchFoods = async () => {
      try {
        const response = await fetch("http://127.0.0.1:8084/foods");
        if (!response.ok) {
          throw new Error(`HTTP error! status: ${response.status}`);
        }
        const data = await response.json();
        setFoods(data);
        setLoading(false);
      } catch (e) {
        setError(e);
        setLoading(false);
      }
    };

    fetchFoods();
  }, []);

  if (loading) {
    return (
      <div className="text-center py-8 text-lg text-gray-600">
        Loading foods...
      </div>
    );
  }

  if (error) {
    return (
      <div className="text-center py-8 text-red-500">
        Error: {error.message}
      </div>
    );
  }

  return (
    <div className="container mx-auto py-8">
      <h1 className="text-3xl font-bold text-green-700 mb-6 text-center">
        Food Products
      </h1>
      <div className="grid grid-cols-1 sm:grid-cols-2 lg:grid-cols-3 gap-6">
        {foods.map((food) => (
          <div key={food.slug}>
            <div
              className={
                "overflow-hidden transition-all duration-300 " + // Added classname
                "border border-gray-200 rounded-md shadow-md hover:shadow-lg " +
                "bg-white"
              }
            >
              <div className="p-4">
                <h2 className="text-xl font-semibold text-green-600">
                  <Link
                    to={`/foods/${food.slug}`}
                    className="hover:text-green-800 transition-colors"
                  >
                    {food.name}
                  </Link>
                </h2>
              </div>
              <div className="p-4 pt-0">
                <p className="text-gray-700">
                  <Link
                    to={`/foods/${food.slug}`}
                    className="hover:text-blue-700 transition-colors"
                  >
                    View Details
                  </Link>
                </p>
              </div>
            </div>
          </div>
        ))}
      </div>
    </div>
  );
}

export default FoodList;
