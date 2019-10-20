/* global google */

import React, { Component } from 'react'
import { WiDaySunny, WiDayRainMix } from 'react-icons/wi'
import { FaChild, } from 'react-icons/fa'
import GoogleMapReact from 'google-map-react'
import Geocode from 'react-geocode'

import Infos from './components/Infos'
import Pregnant from '../assets/pregnant.svg'
import Oldman from '../assets/oldman.svg'

import './Heatmap.css'

import { setApiKey } from '../services/GeoCodeApi'
//import { getAdressFromApi } from '../services/Api'
import bairros from '../mock/bairros'

import Key from '../config/keys'

const AnyReactComponent = ({ toggleHover, handleMouse, bairro, index }) => (
  <div
    className='hover-div'
    onMouseEnter={toggleHover}
    onMouseLeave={toggleHover}
  >
  </div>
);

class Heatmap extends Component {
  static defaultProps = {
    center: {
      lat: -10.9095, lng: -37.0748,
    },
    zoom: 14,
    mapTypeId: 'satellite'
  };

  constructor(props) {
    super(props)
    this.state = {
      heatmapPoints: [],
      hover: false,
      cidade: '',
      bairros: [],
      current_bairro: {
        id: 0,
        nome: '',
        n_pessoas: 0,
        n_criancas_1: 0,
        n_criancas: 893,
        n_idosos: 0,
        cidade: '',
        uf: '',
        vulnerabilidade: 0,
      }

    }
  }

  componentDidMount() {
    setApiKey()
    //this._getAddress('Aracaju')
    bairros.res.map(async (bairro, index) => await this._getAddress(`Aracaju ${bairro.nome}`, index))
  }



  _getAddress = (adress, index) => Geocode.fromAddress(adress).then(
    response => {
      const { lat, lng } = response.results[0].geometry.location
      this.setState({
        heatmapPoints: [...this.state.heatmapPoints, { lat, lng, weight: bairros.res[index].vulnerabilidade }],
        bairros: [...this.state.bairros, bairros.res[index]]
      })
    },
    error => {
      console.error(error)
    }
  )

  _getAddressLatLng = (lat, lng) => Geocode.fromLatLng(`${lat}`, `${lng}`).then(
    response => {
      return response.results[0].formatted_address
    },
    error => {
      console.error(error)
    }
  )

  async handleChange({ center, zoom, bounds, marginBounds }) {
    const address = await this._getAddressLatLng(center.lat, center.lng)
    console.log(this.state.heatmapPoints.length, bairros.res.length)
    bairros.res.map((x, index) => {
      console.log(x, this.state.heatmapPoints[index])
    })
    this._updateCidade(address)
    if (this.state.cidade !== '') {
      //const response = await getAdressFromApi(center.lat, center.lng, this.state.cidade)
      //console.log(response)
    }
  }

  _updateCidade(address) {
    if (address !== null) {
      const cidadeBairro = address.split('-')[address.split('-').length - 3]
      if (cidadeBairro !== null) {
        const cidade = cidadeBairro.split(',')[cidadeBairro.split(',').length - 1].trim()
        if (isNaN(parseInt(cidade, 10)) || cidade !== 'Unnamed Road') {
          this.setState({
            cidade
          })
        }
      }
    }
  }

  toggleHover(index) {
    // aqui //
    this.setState({
      hover: !this.state.hover,
      current_bairro: bairros.res[index],
    })

  }

  render() {
    const heatMapData = {
      positions: this.state.heatmapPoints,
      options: {
        radius: 200,
        opacity: 0.6
      }
    }

    return (
      // Important! Always set the container height explicitly
      <div
        style={{ height: '100vh', width: '100%' }}
      >
        <GoogleMapReact
          ref={(el) => this._googleMap = el}
          bootstrapURLKeys={{ key: Key.apiKey }}
          defaultCenter={this.props.center}
          defaultZoom={this.props.zoom}
          heatmapLibrary={true}
          heatmap={heatMapData}
          onChange={this.handleChange.bind(this)}
        >
          {
            this.state.heatmapPoints.map((points, index) => (
              <AnyReactComponent
                key={index}
                lat={points.lat}
                lng={points.lng}
                bairro={bairros.res[index].nome}
                index={index}
                toggleHover={() => this.toggleHover(index)}
              />
            )
            )
          }
          {
            !this.state.hover && (
              <div className='infos' style={{ position: 'absolute', left: -100, top: -100 }}>
                <span style={{ marginLeft: 97 }}>{this.state.current_bairro.nome}</span>
                <Infos
                  icon={<WiDaySunny size={25} />}
                  titulo={'Temperatura max. do dia'}
                  conteudo={'25ºC'} />
                <Infos icon={<WiDayRainMix size={25} />}
                  titulo={'Precipitação'}
                  conteudo={'10mm'} />
                <Infos icon={<img src={Pregnant} alt='pregnant' height={25} />}
                  titulo={'Porcentagem de mulheres Grávidas'}
                  conteudo={`${((this.state.current_bairro.n_criancas_1 / this.state.current_bairro.n_pessoas) * 100).toFixed(2)}%`} />
                <Infos icon={<FaChild size={20} />}
                  titulo={'Porcentagem de crianças'}
                  conteudo={`${((this.state.current_bairro.n_criancas / this.state.current_bairro.n_pessoas) * 100).toFixed(2)}%`} />
                <Infos hr={true} icon={<img src={Oldman} alt='oldman' height={25} />}
                  titulo={'Porcentagem de idosos'}
                  conteudo={`${((this.state.current_bairro.n_idosos / this.state.current_bairro.n_pessoas) * 100).toFixed(2)}%`} />
              </div>
            )
          }
        </GoogleMapReact>
      </div >
    );
  }
}

export default Heatmap;