import React from "react";
import LivreList from "./components/LivreList";
import AjouterLivre from "./components/AjouterLivre";

function App() {
  return (
    <div className="App">
      <h1>Bibliothèque</h1>
      <AjouterLivre />
      <LivreList />
    </div>
  );
}

export default App;
