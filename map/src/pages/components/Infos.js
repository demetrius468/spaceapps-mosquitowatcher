import React from 'react'
import './Infos.css'

export default function Info(props) {
  return (
    <>
      <div className='dados'>
        {props.icon}
        <p> {props.titulo}: {props.conteudo}</p>
      </ div>
      {!props.hr && <hr />}
      {props.hr && <div class='size-box' />}
    </>
  )
}