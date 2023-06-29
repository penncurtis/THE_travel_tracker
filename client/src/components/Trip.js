import {useState, useEffect} from 'react'


function Trip({trip}){

    const [toggle, setToggle] = useState(false)

    function toggleCard() {
        setToggle(toggle => !toggle)
    }


    return (
        <div className="card">
            <h1>Trip # {trip.id}: {trip.country_id}</h1>
            <p>{trip.date_visited}</p>
            <p>{trip.country_id}</p>
        </div>
    )
}

export default Trip