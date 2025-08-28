
import React, { useEffect, useState } from 'react';

function Teams() {
  const [teams, setTeams] = useState([]);

  useEffect(() => {
    fetch(`${process.env.REACT_APP_API_URL || ''}/api/teams/`)
      .then((res) => res.json())
      .then((data) => setTeams(data))
      .catch((err) => console.error('Error fetching teams:', err));
  }, []);

  return (
    <div>
      <h2>Teams</h2>
      <ul>
        {teams.map((team, idx) => (
          <li key={team.id || idx}>{team.name} ({team.members && team.members.join(', ')})</li>
        ))}
      </ul>
    </div>
  );
}

export default Teams;
