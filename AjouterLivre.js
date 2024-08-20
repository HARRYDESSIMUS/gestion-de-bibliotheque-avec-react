import React, { useState } from 'react';

function AjouterLivre() {
  const [titre, setTitre] = useState('');
  const [auteur, setAuteur] = useState('');
  const [isbn, setIsbn] = useState('');

  const handleSubmit = (e) => {
    e.preventDefault();

    fetch('/api/livres', {
      method: 'POST',
      headers: { 'Content-Type': 'application/json' },
      body: JSON.stringify({ titre, auteur, isbn }),
    }).then(() => window.location.reload());
  };
  

  return (
    <form onSubmit={handleSubmit}>
      <h2>Ajouter un Nouveau Livre</h2>
      <input
        type="text"
        placeholder="Titre"
        value={titre}
        onChange={(e) => setTitre(e.target.value)}
        required
        form/>
      <input
        type="text"
        placeholder="Auteur"
        value={auteur}
        onChange={(e) => setAuteur(e.target.value)}
        required
      />
      <input
        type="text"
        placeholder="ISBN"
        value={isbn}
        onChange={(e) => set
        />
        )
    
