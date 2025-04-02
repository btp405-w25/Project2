import React from "react";

const Navbar = () => {
  return (
    <nav className="bg-[#00AB40] p-4">
      <div className="max-w-7xl mx-auto flex items-center justify-between">
        <div className="text-white text-2xl font-bold">
          <a to="/">GreenPlate Market</a>
        </div>
        <div className="space-x-6">
          <a
            to="/about"
            className="text-white hover:text-green-300 transition duration-200"
          >
            About
          </a>
          <a
            to="/recipes"
            className="text-white hover:text-green-300 transition duration-200"
          >
            Recipes
          </a>
          <a
            to="/ingredients"
            className="text-white hover:text-green-300 transition duration-200"
          >
            Ingredients
          </a>
          <a
            to="/contact"
            className="text-white hover:text-green-300 transition duration-200"
          >
            Contact
          </a>
        </div>
      </div>
    </nav>
  );
};

export default Navbar;
