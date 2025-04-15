import React from "react";
import { Link } from "react-router-dom";

const HomePage = () => {
  return (
    <div className="min-h-screen bg-gradient-to-b from-green-50 to-white">
      <header className="container mx-auto py-20 text-center">
        <h1 className="mb-4 text-4xl font-bold text-green-600 md:text-5xl">
          Welcome to GreenPlate Market
        </h1>
        <p className="mx-auto max-w-2xl text-lg text-gray-600">
          Your marketplace for sustainable and local food. Connecting conscious
          consumers with eco-friendly producers.
        </p>
      </header>

      <section className="container mx-auto px-4 py-8">
        <div className="grid grid-cols-1 gap-8 md:grid-cols-2 lg:grid-cols-3">
          {/* Feature 1: Searchable Directory */}
          <div className="rounded-lg bg-white p-6 shadow-md transition-all hover:shadow-lg">
            <h2 className="mb-3 text-xl font-semibold text-green-600">
              Find Local & Sustainable Producers
            </h2>
            <p className="mb-6 text-gray-700">
              Easily discover and purchase from verified farmers and producers
              committed to sustainable practices.
            </p>
            <Link
              to="/producers"
              className="inline-flex items-center rounded-full bg-green-600 px-5 py-2.5 text-white transition-colors hover:bg-green-700"
            >
              Browse Producers
              <svg
                xmlns="http://www.w3.org/2000/svg"
                className="ml-2 h-4 w-4"
                viewBox="0 0 24 24"
                fill="none"
                stroke="currentColor"
                strokeWidth="2"
                strokeLinecap="round"
                strokeLinejoin="round"
              >
                <path d="M5 12h14"></path>
                <path d="m12 5 7 7-7 7"></path>
              </svg>
            </Link>
          </div>

          {/* Feature 2: Seasonal Meal Planning */}
          <div className="rounded-lg bg-white p-6 shadow-md transition-all hover:shadow-lg">
            <h2 className="mb-3 text-xl font-semibold text-green-600">
              Seasonal Meal Ideas
            </h2>
            <p className="mb-6 text-gray-700">
              Get recipe suggestions based on fresh, local, and seasonal
              ingredients. Reduce waste and enjoy delicious meals!
            </p>
            <Link
              to="/meal-planning"
              className="inline-flex items-center rounded-full bg-green-600 px-5 py-2.5 text-white transition-colors hover:bg-green-700"
            >
              Plan Your Meals
              <svg
                xmlns="http://www.w3.org/2000/svg"
                className="ml-2 h-4 w-4"
                viewBox="0 0 24 24"
                fill="none"
                stroke="currentColor"
                strokeWidth="2"
                strokeLinecap="round"
                strokeLinejoin="round"
              >
                <path d="M5 12h14"></path>
                <path d="m12 5 7 7-7 7"></path>
              </svg>
            </Link>
          </div>

          {/* Feature 3: Carbon Footprint Tracking */}
          <div className="rounded-lg bg-white p-6 shadow-md transition-all hover:shadow-lg">
            <h2 className="mb-3 text-xl font-semibold text-green-600">
              Track Your Impact
            </h2>
            <p className="mb-6 text-gray-700">
              Understand the environmental impact of your food choices with our
              carbon footprint calculator.
            </p>
            <Link
              to="/carbon-footprint"
              className="inline-flex items-center rounded-full bg-green-600 px-5 py-2.5 text-white transition-colors hover:bg-green-700"
            >
              Calculate Footprint
              <svg
                xmlns="http://www.w3.org/2000/svg"
                className="ml-2 h-4 w-4"
                viewBox="0 0 24 24"
                fill="none"
                stroke="currentColor"
                strokeWidth="2"
                strokeLinecap="round"
                strokeLinejoin="round"
              >
                <path d="M5 12h14"></path>
                <path d="m12 5 7 7-7 7"></path>
              </svg>
            </Link>
          </div>

          {/* Feature 4: Sustainability Sorted Cart */}
          <div className="rounded-lg bg-white p-6 shadow-md transition-all hover:shadow-lg">
            <h2 className="mb-3 text-xl font-semibold text-green-600">
              Eco-Conscious Cart
            </h2>
            <p className="mb-6 text-gray-700">
              Our cart helps you prioritize sustainable options, making it
              easier to make green purchasing decisions.
            </p>
            <Link
              to="/cart"
              className="inline-flex items-center rounded-full bg-green-600 px-5 py-2.5 text-white transition-colors hover:bg-green-700"
            >
              View Your Cart
              <svg
                xmlns="http://www.w3.org/2000/svg"
                className="ml-2 h-4 w-4"
                viewBox="0 0 24 24"
                fill="none"
                stroke="currentColor"
                strokeWidth="2"
                strokeLinecap="round"
                strokeLinejoin="round"
              >
                <path d="M5 12h14"></path>
                <path d="m12 5 7 7-7 7"></path>
              </svg>
            </Link>
          </div>

          {/* Feature 5: Food Waste Reduction Tips */}
          <div className="rounded-lg bg-white p-6 shadow-md transition-all hover:shadow-lg">
            <h2 className="mb-3 text-xl font-semibold text-green-600">
              Reduce Food Waste
            </h2>
            <p className="mb-6 text-gray-700">
              Get personalized tips and recommendations to minimize food waste
              based on your habits.
            </p>
            <Link
              to="/waste-reduction"
              className="inline-flex items-center rounded-full bg-green-600 px-5 py-2.5 text-white transition-colors hover:bg-green-700"
            >
              Learn More
              <svg
                xmlns="http://www.w3.org/2000/svg"
                className="ml-2 h-4 w-4"
                viewBox="0 0 24 24"
                fill="none"
                stroke="currentColor"
                strokeWidth="2"
                strokeLinecap="round"
                strokeLinejoin="round"
              >
                <path d="M5 12h14"></path>
                <path d="m12 5 7 7-7 7"></path>
              </svg>
            </Link>
          </div>

          {/* Feature 6: Sustainability Score */}
          <div className="rounded-lg bg-white p-6 shadow-md transition-all hover:shadow-lg">
            <h2 className="mb-3 text-xl font-semibold text-green-600">
              Your Sustainability Score
            </h2>
            <p className="mb-6 text-gray-700">
              Track your progress and see how your choices contribute to a more
              sustainable food system.
            </p>
            <Link
              to="/sustainability-score"
              className="inline-flex items-center rounded-full bg-green-600 px-5 py-2.5 text-white transition-colors hover:bg-green-700"
            >
              Check Your Score
              <svg
                xmlns="http://www.w3.org/2000/svg"
                className="ml-2 h-4 w-4"
                viewBox="0 0 24 24"
                fill="none"
                stroke="currentColor"
                strokeWidth="2"
                strokeLinecap="round"
                strokeLinejoin="round"
              >
                <path d="M5 12h14"></path>
                <path d="m12 5 7 7-7 7"></path>
              </svg>
            </Link>
          </div>
        </div>
      </section>

      <section className="container mx-auto mt-16 px-4 pb-16">
        <div className="rounded-lg bg-white p-8 shadow-sm">
          <h2 className="mb-6 text-center text-2xl font-semibold text-green-600">
            Our Commitment
          </h2>
          <p className="mb-8 text-center text-lg leading-relaxed text-gray-700">
            At GreenPlate Market, we believe in a future where food choices
            nourish both people and the planet.
          </p>
          <div className="grid grid-cols-1 gap-8 md:grid-cols-2">
            <div>
              <h3 className="mb-4 font-semibold text-green-600">
                What We Stand For
              </h3>
              <ul className="space-y-2 text-gray-700">
                <li className="flex items-start">
                  <span className="mr-2 text-green-500">•</span>
                  <span>
                    Connecting you with local farmers who prioritize
                    sustainability.
                  </span>
                </li>
                <li className="flex items-start">
                  <span className="mr-2 text-green-500">•</span>
                  <span>
                    Providing transparent information about the origin and
                    impact of your food.
                  </span>
                </li>
                <li className="flex items-start">
                  <span className="mr-2 text-green-500">•</span>
                  <span>
                    Empowering you to reduce your carbon footprint and minimize
                    food waste.
                  </span>
                </li>
                <li className="flex items-start">
                  <span className="mr-2 text-green-500">•</span>
                  <span>
                    Building a community that values ethical and environmentally
                    responsible consumption.
                  </span>
                </li>
              </ul>
            </div>
            <div className="flex items-center justify-center">
              <Link
                to="/about"
                className="inline-flex items-center rounded-full bg-green-600 px-6 py-3 text-white transition-colors hover:bg-green-700"
              >
                Learn More About Us
                <svg
                  xmlns="http://www.w3.org/2000/svg"
                  className="ml-2 h-4 w-4"
                  viewBox="0 0 24 24"
                  fill="none"
                  stroke="currentColor"
                  strokeWidth="2"
                  strokeLinecap="round"
                  strokeLinejoin="round"
                >
                  <path d="M5 12h14"></path>
                  <path d="m12 5 7 7-7 7"></path>
                </svg>
              </Link>
            </div>
          </div>
        </div>
      </section>

      <footer className="border-t border-gray-200 bg-green-600 py-8">
        <div className="container mx-auto text-center">
          <p className="text-white">
            &copy; 2025 GreenPlate Market. All rights reserved.
          </p>
        </div>
      </footer>
    </div>
  );
};

export default HomePage;
