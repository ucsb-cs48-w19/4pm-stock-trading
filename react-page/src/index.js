import React from 'react';
import ReactDOM from 'react-dom';
import ReactChartkick, { LineChart, PieChart } from 'react-chartkick'
import Chart from 'chart.js'
import './stockgraph.css';

ReactChartkick.addAdapter(Chart)

class Graph extends React.Component {
  render() {
    return (
      <LineChart data={{"2017-01-01": 11, "2017-01-02": 6, "2017-01-03": 7.5}} width="800px" height="500px" xtitle="Date" ytitle="Price" />
    );
  }
}

class Page extends React.Component {
  render() {
    return (
      <div className="game">          
        <Graph />
      </div>
    );
  }
}

// ========================================

ReactDOM.render(
  <Page />,
  document.getElementById('root')
);

