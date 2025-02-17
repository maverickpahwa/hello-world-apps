// # Version": 1.0.0
import React, { useState } from "react";

function Main() {
  const [count, setCount] = useState(1);  // Slider value
  const [people, setPeople] = useState([]); // Store generated data
  const [saveStatus, setSaveStatus] = useState("");

  const fetchData = () => {
    fetch(`http://192.168.0.238:5000/api/generate?count=${count}`)
      .then((response) => response.json())
      .then((data) => {
        // Add createdTime (epoch time) in React
        const updatedData = data.map(person => ({
          ...person,
          createdTime: Math.floor(Date.now() / 1000)  // Current epoch time
        }));
        setPeople(updatedData);
      })
      .catch((error) => console.error("Error fetching data:", error));
  };

  const saveData = async () => {
    try {
      const response = await fetch("http://192.168.0.238:5000/api/save", {
        method: "POST",
        headers: {
          "Content-Type": "application/json",
        },
        body: JSON.stringify(people),  // Send updated data with createdTime
      });

      const result = await response.json();
      if (response.ok) {
        setSaveStatus(`Saved ${result.saved_count} entries successfully!`);
      } else {
        setSaveStatus(`Error: ${result.error}`);
      }
    } catch (error) {
      console.error("Error saving data:", error);
      setSaveStatus("Error saving data");
    }
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
      <button onClick={saveData} style={{ marginLeft: "10px" }}>Save Data</button>

      <ul>
        {people.map((person, index) => (
          <li key={index}>
            <strong>{person.fullname}</strong> - Age: {person.age} - Mortality: {person.mortality}  
            <br />
            <small>Created Time: {new Date(person.createdTime * 1000).toLocaleString()}</small>
          </li>
        ))}
      </ul>

      {saveStatus && <p>{saveStatus}</p>}
    </div>
  );
}

export default Main;
