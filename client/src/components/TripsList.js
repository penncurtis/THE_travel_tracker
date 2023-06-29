import Trip from './Trip'

function TripsList({trips}){

    const tripComponents = trips.map(trip => {
        return <Trip key={trip.id} trip={trip} />
    })

    return (
        <div className="trip-list">{tripComponents}</div>
        )
}

export default TripsList