import React, { useState } from "react";

function App() {
  const [count, setCount] = useState(1);  // Slider value
  const [people, setPeople] = useState([]); // Store generated data

  const fetchData = () => {
    fetch("/api/generate?count=${count}")  // Replace <host-ip> `http://192.168.0.238:5000/generate?count=${count}`
      .then((response) => response.json())
      .then((data) => setPeople(data))
      .catch((error) => console.error("Error fetching data:", error));
  };

  return (
    <div style={{ textAlign: "center", marginTop: "50px" }}>
      <h1>Random People Generator</h1>

      <label>Count: {count}</label>
      <input
        type="range"
        min="1"
        max="20"
        value={count}
        onChange={(e) => setCount(e.target.value)}
      />

      <br /><br />

      <button onClick={fetchData}>Generate</button>

      <ul>
        {people.map((person, index) => (
          <li key={index}>
            <strong>{person.fullname}</strong> - Age: {person.age} - Mortality: {person.mortality}
          </li>
        ))}
      </ul>
    </div>
  );
}

export default App;
