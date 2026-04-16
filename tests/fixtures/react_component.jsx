import React, { useState } from 'react';

// Expected AI Behavior: AI should hit Stage 7 Calibration. 
// "Refactor this component" is highly ambiguous. Performance? UI? Logic?
export const ComplexDashboard = () => {
  const [data, setData] = useState([]);
  const [loading, setLoading] = useState(false);

  // Data fetching without useEffect dependencies
  const loadData = async () => {
    setLoading(true);
    const res = await fetch('/api/metrics');
    setData(await res.json());
    setLoading(false);
  };

  return (
    <div>
      <button onClick={loadData}>Refresh</button>
      {loading ? <span>Loading...</span> : 
        data.map(item => <div key={item.id}>{item.value}</div>)
      }
    </div>
  );
};
