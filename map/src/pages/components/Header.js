import React from 'react'
import { Link } from 'react-router-dom'
import { FaMap, FaMapMarkerAlt } from 'react-icons/fa'

import './Header.css'

export default function Header() {
  return (
    <header id="main-header">
      <div className="header-content">
        <Link to="/">
          <FaMap size={25} />
        </Link>
        <Link to="/new">
          <FaMapMarkerAlt size={25} />
        </Link>
      </div>
    </header>
  )
}