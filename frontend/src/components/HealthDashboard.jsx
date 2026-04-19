import React from 'react';
import FileUpload from './FileUpload';

function HealthDashboard({ predictionData, setPredictionData }) {
  const getStatusColor = (status) => {
    if (status === 'Safe') return '#4CAF50'
    if (status === 'Warning') return '#FF9800'
    return '#F44336'
  }

  return (
    <div style={styles.container}>
      <h2 style={styles.header}>Battery Health Dashboard</h2>
      
      <FileUpload setPredictionData={setPredictionData} />
      
      {predictionData ? (
        <div style={styles.resultsGrid}>
          {/* Health Status Card */}
          <div style={{
            ...styles.card,
            backgroundColor: getStatusColor(predictionData.health_status),
            color: 'white',
          }}>
            <h3>Health Status</h3>
            <p style={styles.bigNumber}>{predictionData.health_status}</p>
          </div>

          {/* Remaining Life Card */}
          <div style={styles.card}>
            <h3>Remaining Useful Life</h3>
            <p style={styles.bigNumber}>{predictionData.RUL}</p>
            <p>cycles remaining</p>
          </div>

          {/* Capacity Card */}
          <div style={styles.card}>
            <h3>Current Capacity</h3>
            <p style={styles.bigNumber}>{predictionData.capacity.toFixed(2)}</p>
            <p>Ah</p>
          </div>

          {/* Stress Level Card */}
          <div style={styles.card}>
            <h3>Stress Level</h3>
            <p style={styles.bigNumber}>{predictionData.stress_level}</p>
          </div>
        </div>
      ) : (
        <p style={styles.placeholder}>Click the button above to analyze battery health</p>
      )}
    </div>
  )
}

const styles = {
  container: {
    padding: '40px',
    maxWidth: '1200px',
    margin: '0 auto',
  },
  header: {
    textAlign: 'center',
    color: '#1a1a2e',
    marginBottom: '20px',
  },
  resultsGrid: {
    display: 'grid',
    gridTemplateColumns: 'repeat(auto-fit, minmax(250px, 1fr))',
    gap: '20px',
    marginTop: '30px',
  },
  card: {
    backgroundColor: 'white',
    padding: '30px',
    borderRadius: '10px',
    boxShadow: '0 2px 8px rgba(0,0,0,0.1)',
    textAlign: 'center',
  },
  bigNumber: {
    fontSize: '48px',
    fontWeight: 'bold',
    margin: '10px 0',
  },
  placeholder: {
    textAlign: 'center',
    color: '#666',
    fontSize: '18px',
    marginTop: '50px',
  },
}

export default HealthDashboard