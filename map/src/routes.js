import React from 'react';
import { BrowserRouter, Route } from "react-router-dom";

import Header from './pages/components/Header';
import Heatmap from './pages/Heatmap';

function Routes() {
  return (
    <BrowserRouter>
      <Header />
      <Route path="/" exact component={Heatmap} />
      {/*<Route path="/dev/:id" exact component={Main} />
      <Route path="/dev/:id/matchs" exact component={Match} />*/}
    </BrowserRouter >
  )
}

export default Routes;