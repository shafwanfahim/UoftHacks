// NameEntryForm.js
import React, { useState } from 'react';

const NameEntryForm = () => {
  // State to store the entered name
  const [name, setName] = useState('');

  // Event handler for input change
  const handleInputChange = (event) => {
    setName(event.target.value);
  };

  // Event handler for form submission
  const handleSubmit = (event) => {
    event.preventDefault();
    // You can perform further actions with the entered name here
    alert(`Hello, ${name}!`);
  };

  return (
    <form onSubmit={handleSubmit}>
      <label>
        Name:
        <input type="text" value={name} onChange={handleInputChange} />
      </label>
      <button type="submit">Submit</button>
    </form>
  );
};

export default NameEntryForm;
