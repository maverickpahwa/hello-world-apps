import React from "react";
import { BrowserRouter as Router, Route, Routes, Link } from "react-router-dom";
import Main from "./Main";  // Your main generator page
import Records from "./Records";  // New records listing page

function App() {
  return (
    <Router>
      <div style={{ textAlign: "center", marginTop: "20px" }}>
        <nav>
          <Link to="/main">Home</Link> | <Link to="/records">Records</Link>
        </nav>
        <Routes>
          <Route path="/main" element={<Main />} />
          <Route path="/records" element={<Records />} />
        </Routes>
      </div>
    </Router>
  );
}

export default App;
