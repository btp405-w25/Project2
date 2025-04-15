import React, { useState, useEffect } from "react";
import { useParams, Link } from "react-router-dom"; // Import useParams and Link

function CertificationDetail() {
  const { certificationName } = useParams(); // Get certificationName from URL
  const [certification, setCertification] = useState(null);
  const [loading, setLoading] = useState(true);
  const [error, setError] = useState(null);

  useEffect(() => {
    const fetchCertificationDetail = async () => {
      try {
        const response = await fetch(
          `http://127.0.0.1:8084/foods/certification/${certificationName}`
        );
        if (!response.ok) {
          throw new Error(`HTTP error! status: ${response.status}`);
        }
        const data = await response.json();
        setCertification(data);
        setLoading(false);
      } catch (e) {
        setError(e);
        setLoading(false);
      }
    };

    if (certificationName) {
      fetchCertificationDetail();
    }
  }, [certificationName]);

  if (loading) {
    return (
      <div className="text-center py-4">Loading certification details...</div>
    );
  }

  if (error) {
    return (
      <div className="text-red-500 text-center py-4">
        Error: {error.message}
      </div>
    );
  }

  if (!certification) {
    return <div className="text-center py-4">Certification not found.</div>;
  }

  return (
    <div className="container mx-auto py-8">
      <header className="bg-gray-100 py-4">
        <nav>
          <ul className="flex space-x-4 justify-center">
            <li>
              <Link to="/" className="text-green-600 hover:underline">
                Home
              </Link>
            </li>
            {/* Add other navigation links */}
          </ul>
        </nav>
      </header>
      <h1 className="text-3xl font-bold text-green-700 mb-4">
        {certification.name}
        {certification.image && (
          <img
            src={certification.image}
            alt={certification.name}
            className="inline-block h-10 w-auto ml-2 rounded"
          />
        )}
      </h1>
      <p className="text-gray-700">{certification.certification_description}</p>
    </div>
  );
}

export default CertificationDetail;
