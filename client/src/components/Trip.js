import {useState, useEffect} from 'react'


function Trip({trip}){

    const [toggle, setToggle] = useState(false)

    function toggleCard() {
        setToggle(toggle => !toggle)
    }


    return (
        <div className="card">
            <h1>Trip # {trip.id}: {trip.country_id}</h1>
            <img onClick={toggleCard} src={trip.date_visited} alt={trip.country_id}/>
            <p>{trip.country_id}</p>
        </div>
    )
}

export default Trip