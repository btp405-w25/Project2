"use client";

import { useState } from "react";
import {
  Search,
  MapPin,
  Calendar,
  Leaf,
  ChevronRight,
  ChefHat,
} from "lucide-react";
import RecipeSuggestions from "./RecipeSuggestions";

const SeasonalIngredients = () => {
  const [location, setLocation] = useState("");
  const [season, setSeason] = useState("");
  const [locationTitle, setLocationTitle] = useState("");
  const [ingredients, setIngredients] = useState([]);
  const [showRecipes, setShowRecipes] = useState(false);
  const [isLoading, setIsLoading] = useState(false);
  const [error, setError] = useState(null);

  const handleSearch = async () => {
    if (!location || !season) {
      setError("Please enter both location and season");
      return;
    }

    setIsLoading(true);
    setError(null);

    try {
      const response = await fetch(
        `http://127.0.0.1:8083/api/ingredients/?location=${encodeURIComponent(
          location
        )}&season=${encodeURIComponent(season)}`
      );

      if (!response.ok) {
        throw new Error("Error fetching ingredients");
      }

      const data = await response.json();
      setLocationTitle(location);
      setIngredients(data);
      setShowRecipes(false);
      setError(null);
    } catch (error) {
      console.error("Error fetching ingredients:", error);
      setError("Failed to fetch ingredients. Please try again.");
    } finally {
      setIsLoading(false);
    }
  };

  const handleGetRecipes = () => {
    setShowRecipes(true);
  };

  const seasons = ["Spring", "Summer", "Fall", "Winter"];

  return (
    <div className="max-w-6xl mx-auto px-4 py-8">
      <div className="bg-white rounded-2xl shadow-lg overflow-hidden">
        {/* Header */}
        <div className="bg-gradient-to-r from-green-500 to-green-600 py-8 px-6">
          <h1 className="text-3xl md:text-4xl font-bold text-white text-center">
            Search Seasonal Ingredients
          </h1>
          <p className="text-green-50 text-center mt-2 max-w-2xl mx-auto">
            Discover what's in season in your area and find delicious recipes
            using local, seasonal ingredients.
          </p>
        </div>

        {/* Search Form */}
        <div className="p-6 md:p-8 bg-white">
          <div className="max-w-3xl mx-auto">
            <div className="grid grid-cols-1 md:grid-cols-7 gap-4 items-end">
              <div className="md:col-span-3 space-y-2">
                <label
                  htmlFor="location"
                  className="block text-sm font-medium text-gray-700"
                >
                  Location
                </label>
                <div className="relative">
                  <div className="absolute inset-y-0 left-0 pl-3 flex items-center pointer-events-none">
                    <MapPin className="h-5 w-5 text-gray-400" />
                  </div>
                  <input
                    id="location"
                    type="text"
                    placeholder="Enter city or region..."
                    value={location}
                    onChange={(e) => setLocation(e.target.value)}
                    className="block w-full pl-10 pr-3 py-3 border border-gray-300 rounded-lg shadow-sm focus:outline-none focus:ring-2 focus:ring-green-500 focus:border-green-500"
                  />
                </div>
              </div>

              <div className="md:col-span-3 space-y-2">
                <label
                  htmlFor="season"
                  className="block text-sm font-medium text-gray-700"
                >
                  Season
                </label>
                <div className="relative">
                  <div className="absolute inset-y-0 left-0 pl-3 flex items-center pointer-events-none">
                    <Calendar className="h-5 w-5 text-gray-400" />
                  </div>
                  <select
                    id="season"
                    value={season}
                    onChange={(e) => setSeason(e.target.value)}
                    className="block w-full pl-10 pr-3 py-3 border border-gray-300 rounded-lg shadow-sm focus:outline-none focus:ring-2 focus:ring-green-500 focus:border-green-500 appearance-none"
                  >
                    <option value="">Select a season</option>
                    {seasons.map((s) => (
                      <option key={s} value={s}>
                        {s}
                      </option>
                    ))}
                  </select>
                  <div className="absolute inset-y-0 right-0 flex items-center pr-3 pointer-events-none">
                    <ChevronRight className="h-5 w-5 text-gray-400" />
                  </div>
                </div>
              </div>

              <div className="md:col-span-1">
                <button
                  onClick={handleSearch}
                  disabled={isLoading}
                  className="w-full py-3 px-4 bg-green-600 hover:bg-green-700 text-white font-medium rounded-lg shadow transition duration-200 flex items-center justify-center"
                >
                  {isLoading ? (
                    <div className="animate-spin h-5 w-5 border-2 border-white border-t-transparent rounded-full"></div>
                  ) : (
                    <>
                      <Search className="h-5 w-5 mr-1" />
                      <span>Search</span>
                    </>
                  )}
                </button>
              </div>
            </div>

            {error && (
              <div className="mt-4 p-3 bg-red-50 border border-red-200 rounded-lg">
                <p className="text-red-600 text-sm">{error}</p>
              </div>
            )}
          </div>
        </div>

        {/* Results Section */}
        {locationTitle && season && ingredients.length > 0 && (
          <div className="px-6 md:px-8 pb-8 bg-gray-50 border-t border-gray-100">
            <div className="max-w-3xl mx-auto">
              {/* Ingredients List */}
              <div className="mt-6">
                <div className="flex items-center mb-4">
                  <Leaf className="text-green-500 mr-2" size={20} />
                  <h2 className="text-2xl font-bold text-gray-800">
                    Seasonal Ingredients in {locationTitle} ({season})
                  </h2>
                </div>

                <div className="bg-white p-5 rounded-lg shadow-sm border border-gray-200">
                  <ul className="grid grid-cols-1 sm:grid-cols-2 md:grid-cols-3 gap-3">
                    {ingredients.map((ingredient) => (
                      <li
                        key={ingredient.id}
                        className="flex items-center p-2 rounded-md hover:bg-green-50"
                      >
                        <span className="w-2 h-2 bg-green-500 rounded-full mr-2"></span>
                        <span className="font-medium text-gray-700">
                          {ingredient.name}
                        </span>
                        <span className="ml-1 text-sm text-gray-500">
                          ({ingredient.season})
                        </span>
                      </li>
                    ))}
                  </ul>
                </div>

                {/* Get Recipes Button */}
                <div className="mt-6 flex justify-center">
                  <button
                    onClick={handleGetRecipes}
                    className="px-6 py-3 bg-green-600 hover:bg-green-700 text-white font-medium rounded-lg shadow-md transition duration-200 flex items-center"
                  >
                    <ChefHat className="mr-2" size={18} />
                    Get Recipes
                  </button>
                </div>
              </div>
            </div>
          </div>
        )}

        {/* Recipes Section */}
        {showRecipes && (
          <div className="border-t border-gray-200">
            <RecipeSuggestions location={locationTitle} season={season} />
          </div>
        )}
      </div>
    </div>
  );
};

export default SeasonalIngredients;
