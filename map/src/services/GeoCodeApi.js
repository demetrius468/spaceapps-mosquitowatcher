import Geocode from 'react-geocode'
import Key from '../config/keys'

export function setApiKey() {
  Geocode.setApiKey(Key.apiKey)
}

export function getAddress(address) {
  Geocode.fromAddress(address).then(
    response => {
      //const { lat, lng } = response.results[0].geometry.location
      return response.results[0].geometry.location
    },
    error => {
      console.error(error)
    }
  )
}

export function getAddressLatLng(lat, lng) {
  Geocode.fromLatLng(`${lat}`, `${lng}`).then(
    response => {
      return response.results[0].formatted_address
    },
    error => {
      console.error(error)
    }
  )
}

export function setLanguage(lang) {
  Geocode.setLanguage(lang);
}

export function setRegion(region) {
  Geocode.setRegion(region);

}