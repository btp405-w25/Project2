import { useState, useEffect } from "react";
import { ChefHat } from "lucide-react";
import RecipeCard from "./RecipeCard";

const RecipeSuggestions = ({ location, season }) => {
  const [recipes, setRecipes] = useState([]);

  useEffect(() => {
    if (!location || !season) return;

    const fetchRecipes = async () => {
      try {
        const response = await fetch(
          `http://127.0.0.1:8084/api/recipes/?location=${encodeURIComponent(
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

      <div className="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-2 gap-14 max-w-5xl mx-auto px-4">
        {recipes.map((recipe) => (
          <RecipeCard key={recipe.id} recipe={recipe} /> // using RecipeCard for each recipe
        ))}
      </div>
    </div>
  );
};

export default RecipeSuggestions;
