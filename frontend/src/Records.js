import React, { useState, useEffect } from "react";

function Records() {
  const [records, setRecords] = useState([]);
  const [currentPage, setCurrentPage] = useState(1);
  const [totalPages, setTotalPages] = useState(1);

  useEffect(() => {
    fetchRecords(currentPage);
  }, [currentPage]);

  const fetchRecords = async (page) => {
    try {
      const response = await fetch(`http://192.168.0.238:5000/api/records?page=${page}`);
      const data = await response.json();

      setRecords(data.data);
      setTotalPages(data.total_pages);
      setCurrentPage(data.current_page);
    } catch (error) {
      console.error("Error fetching records:", error);
    }
  };

  return (
    <div style={{ textAlign: "center", marginTop: "50px" }}>
      <h1>Listing of Records</h1>

      <table border="1" style={{ margin: "auto", width: "80%" }}>
        <thead>
          <tr>
            <th>Created Time</th>
            <th>Full Name</th>
            <th>Age</th>
            <th>Mortality</th>
          </tr>
        </thead>
        <tbody>
          {records.length > 0 ? (
            records.map((record, index) => (
              <tr key={index}>
                <td>{new Date(record.createdTime * 1000).toLocaleString()}</td>
                <td>{record.fullname}</td>
                <td>{record.age}</td>
                <td>{record.mortality}</td>
              </tr>
            ))
          ) : (
            <tr>
              <td colSpan="4">No records found</td>
            </tr>
          )}
        </tbody>
      </table>

      <div style={{ marginTop: "20px" }}>
        <button onClick={() => setCurrentPage(1)} disabled={currentPage === 1}>First</button>
        <button onClick={() => setCurrentPage(currentPage - 1)} disabled={currentPage === 1}>Previous</button>
        <span style={{ margin: "0 15px" }}>Page {currentPage} of {totalPages}</span>
        <button onClick={() => setCurrentPage(currentPage + 1)} disabled={currentPage === totalPages}>Next</button>
        <button onClick={() => setCurrentPage(totalPages)} disabled={currentPage === totalPages}>Last</button>
      </div>
    </div>
  );
}

export default Records;
