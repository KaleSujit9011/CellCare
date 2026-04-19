import React from 'react'

function NavBar({ currentPage, setCurrentPage }) {
  return (
    <nav style={styles.nav}>
      <h1 style={styles.title}> Battery Health Monitor</h1>
      <div style={styles.buttons}>
        <button 
          onClick={() => setCurrentPage('health')}
          style={{
            ...styles.button,
            ...(currentPage === 'health' ? styles.active : {})
          }}
        >
          Health Dashboard
        </button>
        <button 
          onClick={() => setCurrentPage('technical')}
          style={{
            ...styles.button,
            ...(currentPage === 'technical' ? styles.active : {})
          }}
        >
          Technical Analysis
        </button>
      </div>
    </nav>
  )
}

const styles = {
  nav: {
    display: 'flex',
    justifyContent: 'space-between',
    alignItems: 'center',
    padding: '20px 40px',
    backgroundColor: '#1a1a2e',
    color: 'white',
  },
  title: {
    margin: 0,
    fontSize: '24px',
  },
  buttons: {
    display: 'flex',
    gap: '10px',
  },
  button: {
    padding: '10px 20px',
    border: 'none',
    borderRadius: '5px',
    cursor: 'pointer',
    backgroundColor: '#16213e',
    color: 'white',
    fontSize: '14px',
  },
  active: {
    backgroundColor: '#0f3460',
    fontWeight: 'bold',
  },
}

export default NavBar