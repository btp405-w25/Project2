import React from "react";
import Navbar from "./components/Navbar";
import Login from "./components/Login";
import Register from "./components/Register";
import SeasonalIngredients from "./components/SeasonalIngredients";
import RateVendorForm from "./components/RateVendorForm";
import FoodList from "./components/FoodList"; // Import FoodList
import FoodDetail from "./components/FoodDetail"; // Import FoodDetail
import CertificationDetail from "./components/CertificationDetail"; // Import CertificationDetail
import Home from "./components/Home";
import {
  BrowserRouter as Router,
  Routes,
  Route,
  Navigate,
} from "react-router-dom";

const App = () => {
  const isAuthenticated = localStorage.getItem("token");

  return (
    <Router>
      <div>
        <Navbar />
        <Routes>
          <Route path="/" element={<Home />} />
          <Route
            path="/foodList"
            element={
              isAuthenticated ? (
                <FoodList /> // Render FoodList on the home page if authenticated
              ) : (
                <Navigate to="/login" />
              )
            }
          />
          <Route path="/login" element={<Login />} />
          <Route path="/register" element={<Register />} />
          <Route
            path="/seasonalIngredients"
            element={<SeasonalIngredients />}
          />
          {/* Route to display details for a specific food */}
          <Route path="/foods/:foodSlug" element={<FoodDetail />} />
          {/* Route to display details for a specific certification */}
          <Route
            path="/foods/certification/:certificationName"
            element={<CertificationDetail />}
          />
          <Route
            path="/rateVendorForm"
            element={
              isAuthenticated ? <RateVendorForm /> : <Navigate to="/login" />
            }
          />
        </Routes>
      </div>
    </Router>
  );
};

export default App;
