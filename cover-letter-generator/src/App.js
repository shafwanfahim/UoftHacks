import React, { useState, useEffect } from 'react';
import logo from './logo.svg';
import './App.css';
import NameEntryForm from './pages/CoverLetterGenPage'

function App() {
  const [currentTime, setCurrentTime] = useState(0);

  useEffect(() => {
    fetch('/time').then(res => res.json()).then(data => {
      setCurrentTime(data.time);
    });
  }, []);

  return (
    <div className="App">
      <NameEntryForm></NameEntryForm>
      <header>The currentTime is {currentTime}</header>
    </div>
  );
}

export default App;