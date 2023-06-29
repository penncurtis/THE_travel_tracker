import {useState} from 'react'


function Search({search, searchCountry}) {
    return (
        <div className="search-background">
            <input onChange= {searchCountry} className= "search-bar" value={search} placeholder= 'Search'/>
        </div>
    )
}

export default Search