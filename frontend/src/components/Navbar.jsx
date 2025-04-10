import React from "react";

const Navbar = () => {
  const isAuthenticated = localStorage.getItem("token");

  const handleLogout = () => {
    localStorage.removeItem("token"); // Remove the token to logout
    window.location.href = "/"; // Redirect to the homepage
  };

  return (
    <nav className="bg-green-600 p-4 shadow-lg">
      <div className="max-w-screen-xl mx-auto flex justify-between items-center">
        <div className="text-white text-xl font-semibold">
          GreenPlate Market
        </div>

        <div className="space-x-4 flex items-center">
          <button
            onClick={() => (window.location.href = "/home")}
            className="text-white hover:bg-green-700 px-4 py-2 rounded-lg transition"
          >
            Home
          </button>

          {isAuthenticated ? (
            <div className="flex items-center space-x-4">
              <button
                onClick={() => (window.location.href = "/seasonalIngredients")}
                className="text-white hover:bg-green-700 px-4 py-2 rounded-lg transition"
              >
                Ingredients
              </button>
              <button
                onClick={() => (window.location.href = "/rateVendorForm")}
                className="text-white hover:bg-green-700 px-4 py-2 rounded-lg transition"
              >
                Ratings
              </button>
              <button
                onClick={handleLogout}
                className="text-white hover:bg-red-500 px-4 py-2 rounded-lg transition"
              >
                Logout
              </button>
            </div>
          ) : (
            <div className="flex items-center space-x-4">
              <button
                onClick={() => (window.location.href = "/login")}
                className="text-white hover:bg-green-700 px-4 py-2 rounded-lg transition"
              >
                Login
              </button>
              <button
                onClick={() => (window.location.href = "/register")}
                className="text-white hover:bg-green-700 px-4 py-2 rounded-lg transition"
              >
                Register
              </button>
            </div>
          )}
        </div>
      </div>
    </nav>
  );
};

export default Navbar;
