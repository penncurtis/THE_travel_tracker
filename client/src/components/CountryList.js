import Country from './Country'

function CountryList({countries, deleteCountry}){

    const countryComponents = countries.map(country => {
        return <Country key={country.id} country={country} deleteCountry={deleteCountry}/>
    })

    return (
        <ul className="country-list">{countryComponents}</ul>
        )
}

export default CountryList