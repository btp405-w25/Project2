import React, { useState, useEffect } from "react";
import Navbar from "./components/Navbar";
import Login from "./components/Login";
import Register from "./components/Register";
import SeasonalIngredients from "./components/SeasonalIngredients";
const App = () => {
  const [currentPage, setCurrentPage] = useState("home"); // Default page to "home"

  // Check the URL and set the current page on component mount
  useEffect(() => {
    const pathname = window.location.pathname;
    if (pathname === "/login") {
      setCurrentPage("login");
    } else if (pathname === "/register") {
      setCurrentPage("register");
    } else if (pathname === "/seasonalIngredients") {
      setCurrentPage("seasonalIngredients");
    } else {
      setCurrentPage("home"); // Default page
    }
  }, []);

  return (
    <div>
      <Navbar setCurrentPage={setCurrentPage} />{" "}
      {/* Pass the setCurrentPage function to Navbar */}
      {currentPage === "login" && <Login />}
      {currentPage === "register" && <Register />}
      {currentPage === "seasonalIngredients" && <SeasonalIngredients />}
      {currentPage === "home" && <div>Welcome to the home page!</div>}
    </div>
  );
};

export default App;
