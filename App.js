// src/App.js
import React, { useEffect, useState } from "react";

function App() {
  const [patients, setPatients] = useState([]);

  useEffect(() => {
    fetch(process.env.REACT_APP_BACKEND_URL + "/api/patients")
      .then((res) => res.json())
      .then((data) => {
        // لو الـ response عبارة عن { patients: [...] }
        setPatients(data.patients);
        // لو عايز تتأكد من البيانات:
        console.log("Fetched patients:", data.patients);
      })
      .catch((err) => {
        console.error("Fetch error:", err);
      });
  }, []);

  return (
    <div style={{ padding: "20px", fontFamily: "sans-serif" }}>
      <h1>Patients</h1>
      <ul>
        {patients.map((p, i) => (
          <li key={i}>{p}</li>
        ))}
      </ul>
    </div>
  );
}

export default App;