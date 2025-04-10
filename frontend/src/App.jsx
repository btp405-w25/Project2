import React from "react";
import Navbar from "./components/Navbar";
import Login from "./components/Login";
import Register from "./components/Register";
import SeasonalIngredients from "./components/SeasonalIngredients";
import RateVendorForm from "./components/RateVendorForm";
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
        <Navbar />{" "}
        {/* Navbar doesn't need setCurrentPage anymore if using Link */}
        <Routes>
          <Route
            path="/"
            element={
              isAuthenticated ? (
                <div>Welcome to the home page!</div>
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
