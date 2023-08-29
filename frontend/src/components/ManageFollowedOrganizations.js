import React, { useState, useEffect } from 'react';
import axios from 'axios';

const ManageFollowedOrganizations = () => {
  const [organizations, setOrganizations] = useState([]);
  const [followedOrganizations, setFollowedOrganizations] = useState([]);
  
  // Fetch all organizations
  useEffect(() => {
    axios.get('/api/organizations/')
      .then(response => {
        setOrganizations(response.data);
      });
  }, []);
  
  // Fetch currently followed organizations
  useEffect(() => {
    axios.get('/api/my-followed-organizations/')
      .then(response => {
        setFollowedOrganizations(response.data.map(org => org.id));
      });
  }, []);

  const handleFollowToggle = (orgId) => {
    axios.post(`/api/follow-organization/${orgId}/`)
      .then(response => {
        if (response.data.followed) {
          setFollowedOrganizations(prevState => [...prevState, orgId]);
        } else {
          setFollowedOrganizations(prevState => prevState.filter(id => id !== orgId));
        }
      });
  };

  return (
    <div>
      <h2>Select Organizations to Follow</h2>
      {organizations.map(org => (
        <div key={org.id}>
          <input
            type="checkbox"
            checked={followedOrganizations.includes(org.id)}
            onChange={() => handleFollowToggle(org.id)}
          />
          <label>{org.name}</label>
        </div>
      ))}
    </div>
  );
};

export default ManageFollowedOrganizations;
