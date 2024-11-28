// frontend/src/Header.js
import React from 'react';
import { Link } from 'react-router-dom';
import './Header.css';

function Header({ auth }) {
  return (
    <header className="header">
      <nav>
        <ul>
          <li><Link to="/">Dashboard</Link></li>
          <li><Link to="/faturas">Faturas</Link></li>
          <li><Link to="/faturamento">Faturamento</Link></li>
          <li><Link to="/despesas">Despesas</Link></li>
        </ul>
      </nav>
    </header>
  );
}

export default Header;