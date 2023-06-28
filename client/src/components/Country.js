function Country({country, deleteCountry}){
    return (
        <li className="country">
            <h1>Country # {country.id}: {country.name}</h1>
            <img src={country.image} alt={country.name} />
            <p>{country.name}</p>
            <button onClick={() => deleteCountry(country.id)}></button>
        </li>
    )
}

export default Country

