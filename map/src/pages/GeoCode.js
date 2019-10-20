import Geocode from 'react-geocode'

import Key from '../config/keys'

Geocode.setApiKey(Key.apiKey)

Geocode.fromAddress('Farolandia').then(
  response => {
    const { lat, lng } = response.results[0].geometry.location;
    console.log(lat, lng);
  },
  error => {
    console.error(error)
  }
)