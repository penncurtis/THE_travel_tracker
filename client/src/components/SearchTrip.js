import {useState} from 'react'


function SearchTrip({searchTrip, searchTrips}) {

    return (
        <div className="search-background">
            <input onChange= {searchTrips} className= "search-bar" value={searchTrip} placeholder= 'Search by user ID'/>
        </div>
    )
}

export default SearchTrip