import React, { useEffect, useState } from "react";

function App() {
  const [message, setMessage] = useState("Loading...");

  useEffect(() => {
    fetch("http://192.168.0.238:5000")  // Ensure this is correct
      .then((response) => response.json())
      .then((data) => setMessage(data.message))
      .catch((error) => {
        console.error("Error fetching message:", error);
        setMessage("Error fetching message");
      });
  }, []);

  return <h1>{message}</h1>;
}

export default App;
