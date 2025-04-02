import { useState, useEffect } from "react";
import { ChefHat, Leaf, Thermometer } from "lucide-react";

const RecipeSuggestions = ({ location, season }) => {
  const [recipes, setRecipes] = useState([]);

  useEffect(() => {
    if (!location || !season) return;

    const fetchRecipes = async () => {
      try {
        const response = await fetch(
          `http://127.0.0.1:8083/api/recipes/?location=${encodeURIComponent(
            location
          )}&season=${encodeURIComponent(season)}`
        );

        if (!response.ok) throw new Error("Failed to fetch recipes");

        const data = await response.json();
        setRecipes(Array.isArray(data) ? data : []);
      } catch (err) {
        console.error("Error fetching recipes:", err);
      }
    };

    fetchRecipes();
  }, [location, season]);

  return (
    <div className="w-full py-12 bg-white">
      <div className="text-center mb-8">
        <h2 className="text-3xl font-bold text-gray-800 flex items-center justify-center">
          <ChefHat className="text-green-500 mr-2" size={28} />
          Recipe Suggestions
        </h2>
      </div>

      <div className="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-2 gap-8 max-w-6xl mx-auto px-4">
        {recipes.map((recipe) => {
          // Accessing the correct fields in the recipe data
          const {
            name,
            ingredients,
            instructions,
            dietary_preferences,
            carbon_footprint,
          } = recipe;

          return (
            <div
              key={recipe.id}
              className="bg-white border rounded-xl shadow-md overflow-hidden"
            >
              {/* Recipe Header */}
              <div className="bg-gradient-to-r from-green-50 to-blue-50 p-4 border-b">
                <h3 className="text-xl font-bold text-center">
                  {name || "Unnamed Recipe"}
                </h3>
              </div>

              {/* Recipe Content */}
              <div className="p-4">
                {/* Ingredients */}
                <div className="mb-4">
                  <h4 className="text-lg font-semibold mb-2 flex items-center">
                    <div className="w-1 h-5 bg-green-500 rounded-full mr-2"></div>
                    Ingredients
                  </h4>
                  <ul className="space-y-1 pl-2">
                    {ingredients && Array.isArray(ingredients) ? (
                      ingredients.map((item, i) => (
                        <li key={i} className="flex items-start">
                          <span className="inline-block w-2 h-2 rounded-full bg-green-400 mt-2 mr-2"></span>
                          <span>{item.trim()}</span>
                        </li>
                      ))
                    ) : (
                      <li>No ingredients listed</li>
                    )}
                  </ul>
                </div>

                {/* Instructions */}
                <div className="mb-4">
                  <h4 className="text-lg font-semibold mb-2 flex items-center">
                    <div className="w-1 h-5 bg-blue-500 rounded-full mr-2"></div>
                    Instructions
                  </h4>
                  <ol className="space-y-2 pl-2">
                    {instructions && instructions.length > 0 ? (
                      instructions.split(";").map((step, i) => (
                        <li key={i} className="flex items-start">
                          <span className="inline-flex justify-center items-center w-5 h-5 rounded-full bg-blue-100 text-blue-700 text-xs font-medium mr-2 mt-0.5">
                            {i + 1}
                          </span>
                          <span>{step.trim()}</span>{" "}
                          {/* Use trim to remove any leading/trailing spaces */}
                        </li>
                      ))
                    ) : (
                      <li>No instructions available</li>
                    )}
                  </ol>
                </div>

                {/* Footer Info */}
                <div className="mt-4 pt-3 border-t grid grid-cols-2 gap-2">
                  <div className="flex items-center">
                    <Leaf className="text-green-500 mr-2" size={16} />
                    <div>
                      <p className="text-xs text-gray-500">Dietary</p>
                      <p className="text-sm font-medium">
                        {dietary_preferences || "N/A"}
                      </p>
                    </div>
                  </div>
                  <div className="flex items-center">
                    <Thermometer className="text-orange-500 mr-2" size={16} />
                    <div>
                      <p className="text-xs text-gray-500">Carbon Footprint</p>
                      <p className="text-sm font-medium">
                        {carbon_footprint
                          ? `${carbon_footprint} kg CO₂`
                          : "N/A"}
                      </p>
                    </div>
                  </div>
                </div>
              </div>
            </div>
          );
        })}
      </div>
    </div>
  );
};

export default RecipeSuggestions;
