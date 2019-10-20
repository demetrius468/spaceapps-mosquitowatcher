import axios from 'axios'

const api = axios.create({
  baseURL: 'localhost:8000',
  timeout: 1000,
  headers: {},
})

export async function getAdressFromApi(lat, long, cidade) {
  try {
    const response = await api.get(`tracker/bairros/?lat=${lat}&long=${long}&cidade=${cidade}`)
    return response.data
  } catch (error) {
    console.error(error)
  }
}
