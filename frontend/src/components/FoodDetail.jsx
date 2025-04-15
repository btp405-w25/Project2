import React, { useState, useEffect } from "react";
import { useParams, Link } from "react-router-dom";
import L from "leaflet";
import "leaflet/dist/leaflet.css";

const FoodDetail = () => {
  const { foodSlug } = useParams();
  const [food, setFood] = useState(null);
  const [loading, setLoading] = useState(true);
  const [error, setError] = useState(null);

  useEffect(() => {
    const fetchFoodDetail = async () => {
      try {
        const response = await fetch(`http://127.0.0.1:8084/foods/${foodSlug}`);
        if (!response.ok) {
          throw new Error(`HTTP error! status: ${response.status}`);
        }
        const data = await response.json();
        setFood(data);
        setLoading(false);
      } catch (e) {
        setError(e);
        setLoading(false);
      }
    };

    if (foodSlug) {
      fetchFoodDetail();
    }
  }, [foodSlug]);

  useEffect(() => {
    if (food && food.latitude && food.longitude) {
      const mapContainer = document.getElementById("map");
      if (mapContainer && !mapContainer._leaflet_id) {
        const map = L.map("map").setView([food.latitude, food.longitude], 10);

        L.tileLayer("https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png", {
          attribution:
            '&copy; <a href="https://www.openstreetmap.org/copyright">OpenStreetMap</a> contributors',
        }).addTo(map);

        L.marker([food.latitude, food.longitude])
          .addTo(map)
          .bindPopup(food.name)
          .openPopup();

        return () => {
          map.remove();
        };
      }
    }
  }, [food]);

  if (loading) {
    return (
      <div className="text-center py-8 text-lg text-gray-600">
        Loading food details...
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

  if (!food) {
    return (
      <div className="text-center py-8 text-gray-600">Food not found.</div>
    );
  }

  return (
    <div className="container mx-auto py-10">
      <div className="bg-white shadow-lg rounded-lg overflow-hidden">
        {/* Header Section */}
        <div className="md:flex">
          {food.image && (
            <img
              src={food.image}
              alt={food.name}
              className="w-full h-auto max-h-96 object-cover md:w-1/2"
            />
          )}
          <div className="p-8 md:w-2/3 flex flex-col justify-between">
            {" "}
            {/* Adjusted text container width */}
            <div>
              <h1 className="text-3xl font-bold text-green-700 mb-3">
                {food.name}
              </h1>
              <p className="text-gray-700 leading-relaxed">
                {food.food_description}
              </p>
            </div>
            {food.purchase_link && (
              <Link
                to={food.purchase_link}
                target="_blank"
                rel="noopener noreferrer"
                className="inline-block bg-green-500 hover:bg-green-700 text-white font-bold py-3 px-6 rounded-full mt-4 self-start"
              >
                Buy Now
              </Link>
            )}
          </div>
        </div>

        {/* Origin Section */}
        <section className="p-8 border-t">
          <h2 className="text-xl font-semibold text-green-600 mb-4">Origin</h2>
          <div className="grid grid-cols-1 md:grid-cols-2 gap-8">
            {" "}
            {/* Using grid for better layout */}
            <div>
              <p className="text-gray-700 leading-relaxed font-semibold">
                Cultivated at:{" "}
                <span className="font-medium">{food.food_origin}</span>
              </p>
            </div>
            <div>
              {food.latitude && food.longitude ? (
                <div id="map" className="h-64 rounded-md shadow-md"></div>
              ) : (
                <p className="text-gray-700">
                  Origin coordinates not available.
                </p>
              )}
            </div>
          </div>
        </section>

        {/* Certifications Section */}
        <section className="p-8 border-t">
          <h2 className="text-xl font-semibold text-green-600 mb-4">
            Certifications
          </h2>
          {food.certifications && food.certifications.length > 0 ? (
            <div className="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-6">
              {food.certifications.map((certification) => (
                <Link
                  key={certification.name}
                  to={`/foods/certification/${certification.name}`}
                  target="_blank"
                  className="block p-4 bg-gray-100 rounded-md shadow-sm hover:shadow-md transition duration-200"
                >
                  <h3 className="font-semibold text-green-500 mb-2">
                    {certification.name}
                  </h3>
                  {certification.image && (
                    <img
                      src={certification.image}
                      alt={certification.name}
                      className="h-16 w-auto rounded-md object-contain mx-auto"
                    />
                  )}
                  {!certification.image && (
                    <div className="inline-flex items-center justify-center h-16 w-16 rounded-md bg-gray-300 text-sm font-semibold">
                      {certification.name.substring(0, 2).toUpperCase()}
                    </div>
                  )}
                </Link>
              ))}
            </div>
          ) : (
            <p className="text-gray-700">
              No certifications listed for this food.
            </p>
          )}
        </section>

        {/* Farming Practices Section */}
        <section className="p-8 border-t">
          <h2 className="text-xl font-semibold text-green-600 mb-4">
            Farming Practices
          </h2>
          {food.farming_practices && food.farming_practices.length > 0 ? (
            <ul className="list-disc list-inside text-gray-700 leading-relaxed">
              {food.farming_practices.map((practice) => (
                <li key={practice.name}>{practice.name}</li>
              ))}
            </ul>
          ) : (
            <p className="text-gray-700">
              No specific farming practices listed.
            </p>
          )}
        </section>

        {/* Impact Section */}
        <section className="p-8 border-t">
          <h2 className="text-xl font-semibold text-green-600 mb-4">Impact</h2>
          {food.impact_metric ? (
            <div className="grid grid-cols-1 md:grid-cols-3 gap-6">
              <div className="bg-gray-100 rounded-md p-4 shadow-sm">
                <h3 className="font-semibold text-green-500 mb-2">
                  Water Usage
                </h3>
                <p className="text-gray-700">
                  {food.impact_metric.water_usage}
                </p>
              </div>
              <div className="bg-gray-100 rounded-md p-4 shadow-sm">
                <h3 className="font-semibold text-green-500 mb-2">
                  CO2 Emissions
                </h3>
                <p className="text-gray-700">
                  {food.impact_metric.co2_emissions}
                </p>
              </div>
              <div className="bg-gray-100 rounded-md p-4 shadow-sm">
                <h3 className="font-semibold text-green-500 mb-2">Land Use</h3>
                <p className="text-gray-700">{food.impact_metric.land_use}</p>
              </div>
            </div>
          ) : (
            <p className="text-gray-700">
              Sustainability impact metrics not available.
            </p>
          )}
        </section>
      </div>
    </div>
  );
};

export default FoodDetail;
