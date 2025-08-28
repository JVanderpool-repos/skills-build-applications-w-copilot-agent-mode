
import React, { useEffect, useState } from 'react';

function Leaderboard() {
  const [leaderboard, setLeaderboard] = useState([]);

  useEffect(() => {
    fetch(`${process.env.REACT_APP_API_URL || ''}/api/leaderboard/`)
      .then((res) => res.json())
      .then((data) => setLeaderboard(data))
      .catch((err) => console.error('Error fetching leaderboard:', err));
  }, []);

  return (
    <div>
      <h2>Leaderboard</h2>
      <ul>
        {leaderboard.map((entry, idx) => (
          <li key={entry.id || idx}>{entry.user}: {entry.points} pts</li>
        ))}
      </ul>
    </div>
  );
}

export default Leaderboard;
