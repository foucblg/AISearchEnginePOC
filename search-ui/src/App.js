import React, { useState } from 'react';

const BACKEND_URL = "http://localhost:8000/data/";

function Search() {
  const [query, setQuery] = useState('');
  const [results, setResults] = useState([]);

  const handleSearch = async () => {
    try {
      const response = await fetch(`http://localhost:8000/search?query=${encodeURIComponent(query)}&k=3`);
      const data = await response.json();
      setResults(data.results);
    } catch (error) {
      console.error('Error fetching:', error);
    }
  };

  return (
    <div style={{ padding: '20px' }}>
      <input
        value={query}
        onChange={(e) => setQuery(e.target.value)}
        placeholder="Enter your query"
        style={{ padding: '8px', width: '60%' }}
      />
      <button onClick={handleSearch} style={{ marginLeft: '10px', padding: '8px' }}>
        Search
      </button>
      <div style={{ marginTop: '20px' }}>
        {results.map((result, index) => (
          <div key={index} style={{ marginBottom: '10px', background: '#f0f0f0', padding: '10px' }}>
            <div style={{ fontWeight: 'bold', marginBottom: '5px' }}>
              Score : {result.score.toFixed(3)} {}
            </div>
            <p>{result.page_content}</p>
            {result.metadata?.source && (
              <a href={`${BACKEND_URL}${result.metadata.source}`} target="_blank" rel="noopener noreferrer">
                <button style={{ marginTop: '5px' }}>View source</button>
              </a>
            )}
          </div>
        ))}
      </div>
    </div>
  );
}

export default Search;