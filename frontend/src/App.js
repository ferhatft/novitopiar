// frontend/src/App.js
import './styles.css';
import React from 'react';
import { BrowserRouter as Router, Route, Routes } from 'react-router-dom';
import Base from './components/Base';
import ManageFollowedOrganizations from './components/ManageFollowedOrganizations';

// Bileşenleri import ediyoruz.
import LoginComponent from './components/auth/LoginComponent';
import RegisterComponent from './components/auth/RegisterComponent';
import PasswordResetComponent from './components/auth/PasswordResetComponent';
import PasswordResetConfirmComponent from './components/auth/PasswordResetConfirmComponent';

function App() {
  return (
    <Router>
      <Routes>
        <Route path="/" element={
          <Base title="Home Page" header="Welcome to Novitopia">
            <p>This is the default content.</p>
          </Base>} 
        />
        <Route path="/manage-followed-organizations/" element={<ManageFollowedOrganizations />} />
        
        {/* Yeni eklediğimiz bileşenleri yollara atayalım */}
        <Route path="/login" element={<LoginComponent />} />
        <Route path="/register" element={<RegisterComponent />} />
        <Route path="/password-reset" element={<PasswordResetComponent />} />
        <Route path="/password-reset/confirm" element={<PasswordResetConfirmComponent />} />

      </Routes>
    </Router>
  );
}

export default App;
