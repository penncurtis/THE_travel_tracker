import {useState} from 'react'


function Search({searchCountry, searchCountries}) {
    return (
        <div className="search-background">
            <input onChange= {searchCountries} className= "search-bar" value={searchCountry} placeholder= 'Search'/>
        </div>
    )
}

export default Search