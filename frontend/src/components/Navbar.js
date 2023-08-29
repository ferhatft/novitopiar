// frontend/src/components/Navbar.js

import React from 'react';
import { Link } from 'react-router-dom';

const Navbar = () => {
    return (
        <div className="collapse navbar-collapse" id="navbarNav">
            <ul className="navbar-nav">
                <li className="nav-item">
                    <Link className="nav-link" to="/admin">Admin</Link>
                </li>
                <li className="nav-item">
                    <Link className="nav-link" to="/login">Login</Link>
                </li>
                <li className="nav-item">
                    <Link className="nav-link" to="/register">Register</Link>
                </li>
                <li className="nav-item">
                    <Link className="nav-link" to="/password-reset-request">Password Reset Request</Link>
                </li>
                <li className="nav-item">
                    <Link className="nav-link" to="/api-organization-list-create">Organizations API</Link>
                </li>
                <li className="nav-item">
                    <Link className="nav-link" to="/organization-filter-page">Organizations Filter</Link>
                </li>
                <li className="nav-item">
                    <Link className="nav-link" to="/api-organization-filter">Organizations Filter API</Link>
                </li>
                <li className="nav-item">
                    <Link className="nav-link" to="/manage-followed-organizations">Manage Followed Organizations</Link>
                </li>
                <li className="nav-item">
                    <Link className="nav-link" to="/my-followed-organizations">My Followed Organizations API</Link>
                </li>
                <li className="nav-item">
                    <Link className="nav-link" to="/schema-swagger-ui">API Documentation</Link>
                </li>
            </ul>
        </div>
    );
};

export default Navbar;
