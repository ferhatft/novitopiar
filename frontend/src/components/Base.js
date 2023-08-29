// frontend/src/components/Base.js
import React from 'react';
import { Link } from 'react-router-dom';
import Navbar from './Navbar';


const Base = ({ title, header, children }) => {
  return (
    <div>
      <head>
        {/*... rest of the head code ...*/}
      </head>
      <body>
        <nav className="navbar navbar-expand-lg navbar-light bg-light">
          <Link className="navbar-brand" to="/">Novitopia</Link>
          <Navbar />
        </nav>

        <header>
          <h1>{header || 'Default Header'}</h1>
        </header>

        <main>
          {children || 'Default Content'}
        </main>

        {/*... rest of the body code ...*/}
      </body>
    </div>
  );
};

export default Base;
