import React from 'react'

function TechnicalDashboard() {
  const API_URL = 'http://localhost:8000'
  
  const plots = [
    { name: 'degradation_curve', title: 'Capacity Degradation Over Cycles' },
    { name: 'rul_curve', title: 'Remaining Useful Life Curve' },
    { name: 'stress_features_curves', title: 'Stress Features Evolution' },
    { name: 'stress_distribution_curve', title: 'Stress Level Distribution' },
    { name: 'actual_vs_predicted_RandomForest', title: 'Random Forest - Actual vs Predicted' },
    { name: 'actual_vs_predicted_XGBoost', title: 'XGBoost - Actual vs Predicted' },
    { name: 'feature_importance_Random_Forest', title: 'Feature Importance - Random Forest' },
    { name: 'feature_importanceXGBoost', title: 'Feature Importance - XGBoost' },
    { name: 'correlation_heatmap', title: 'Feature Correlation Heatmap' },
    { name: 'model_comparison', title: 'Model Performance Comparison' },
    { name: 'safe_vs_dangerous', title: 'Battery Health Classification' },
  ]

  return (
    <div style={styles.container}>
      <h2 style={styles.header}>Technical Analysis Dashboard</h2>
      <div style={styles.plotsGrid}>
        {plots.map((plot) => (
          <div key={plot.name} style={styles.plotCard}>
            <h3 style={styles.plotTitle}>{plot.title}</h3>
            <img 
              src={`${API_URL}/plots/${plot.name}`} 
              alt={plot.title}
              style={styles.plotImage}
            />
          </div>
        ))}
      </div>
    </div>
  )
}

const styles = {
  container: {
    padding: '40px',
    maxWidth: '1400px',
    margin: '0 auto',
  },
  header: {
    textAlign: 'center',
    color: '#1a1a2e',
    marginBottom: '40px',
  },
  plotsGrid: {
    display: 'grid',
    gridTemplateColumns: 'repeat(auto-fit, minmax(500px, 1fr))',
    gap: '30px',
  },
  plotCard: {
    backgroundColor: 'white',
    padding: '20px',
    borderRadius: '10px',
    boxShadow: '0 2px 8px rgba(0,0,0,0.1)',
  },
  plotTitle: {
    marginBottom: '15px',
    color: '#1a1a2e',
    fontSize: '18px',
  },
  plotImage: {
    width: '100%',
    height: 'auto',
    borderRadius: '5px',
  },
}

export default TechnicalDashboard