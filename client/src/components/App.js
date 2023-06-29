import '../App.css';
import {useState, useEffect} from 'react'
import { Route, Switch } from "react-router-dom"

import NavBar from './NavBar'
import Header from './Header'
import CountryList from './CountryList'
import TripsList from './TripsList'
import NewTripForm from './NewTripForm'
import UpdateTripForm from './UpdateTripForm'
import Search from './Search'
import SearchTrip from './SearchTrip'
import Login from "./Login"
import Signup from "./Signup"
import UserDetails from "./UserDetails"


function App() {

  const [countries, setCountries] = useState([])
  const [trips, setTrips] = useState([])
  const [postFormData, setPostFormData] = useState({})
  const [idToUpdate, setIdToUpdate] = useState(0)
  const [patchFormData, setPatchFormData] = useState({})
  const [users, setUsers] = useState([])
  const [searchCountry, setSearchCountry] = useState('')
  const [searchTrip, setSearchTrip] = useState(NaN)
  const [currentUser, setCurrentUser] = useState(null)

  // http://127.0.0.1:7000

  useEffect(() => {
    fetch('/countries')
    .then(response => response.json())
    .then(countryData => setCountries(countryData))
  }, [])

  useEffect(() => {
    fetch('/trips')
    .then(response => response.json())
    .then(tripData => setTrips(tripData))
  }, [])

  // useEffect(() => {
  //   if(trips.length > 0 && trips[0].id){
  //     setIdToUpdate(trips[0].id)
  //   }
  // }, [trips])

  useEffect(() => {
    fetch('/users')
    .then(response => response.json())
    .then(userData => setUsers(userData))
  }, [])

  useEffect(() => {
    fetch('/check_session')
    .then(res => {
      if (res.ok) {
        res.json()
        .then( data => setCurrentUser(data) )
      }
    })
  }, [])

  function attemptSignup(userInfo) {
    fetch('/login', {
      method: 'POST',
      headers: {
        'Content-Type': 'application/json',
        'Accepts': 'application/json'
      },
      body: JSON.stringify(userInfo)
    })
    .then(res => res.json())
    .then(data => setCurrentUser(data))
  }

  function logout() {
    setCurrentUser(null)
    fetch('/logout', { method: "DELETE" })
  }

  function addTrip(event){
    event.preventDefault()
   

    console.log(postFormData)

    fetch('/trips', {
      method: "POST",
      headers: {
        "Content-Type": "application/json",
        "Accept": "application/json"
      },
      body: JSON.stringify(postFormData)
    })
    .then(response => response.json())
    .then(newTrip => setTrips(trips => [...trips, newTrip]))
  }

  function updateTrip(event){
    event.preventDefault()
    console.log(patchFormData)
    fetch(`/trips/${idToUpdate}`, {
      method: "PATCH",
      headers: {
        "Content-Type": "application/json",
        "Accept": "application/json"
      },
      body: JSON.stringify(patchFormData)
    })
    .then(response => response.json())
    .then(updatedTrip => {
      setTrips(trips => {
        return trips.map(trip => {
          if(trip.id === updatedTrip.id){
            return updatedTrip
          }
          else{
            return trip
          }
        })
      })
    })
  }

  function deleteTrip(event, id){
    event.preventDefault()
    fetch(`/trips/${id}`, {
      method: "DELETE"
    })
    .then(() => {
      alert('Trip deleted!')
      setTrips(trips => {
      return trips.filter(trip => {
        return trip.id !== id
      })
    })})
  }

  function searchCountries(e) {
      setSearchCountry(e.target.value)
  }

  const filterCountry = countries.filter(country => {
      if (searchCountry ==='') {
          return true
      }
      return country.country_name.toLowerCase().includes(searchCountry.toLowerCase())
  })

  function searchTrips(e) {
    setSearchTrip(parseInt(e.target.value))
  }

  const filterTrip = trips.filter(trip => {
    if (isNaN(searchTrip)) {
        return true
    }
    return trip.user_id === searchTrip
  })

  function updatePostFormData(event){
    setPostFormData({...postFormData, [event.target.name]: event.target.value})
  }

  function updatePatchFormData(event){
    setPatchFormData({...patchFormData, [event.target.name]: event.target.value})
  }

  return (
    <div className="app">
      <NavBar/>
      <Header />
      <Switch>
        <Route exact path="/">
          <h1>Welcome! Here is the list of Countries:</h1>
          <Search searchCountry = {searchCountry} searchCountries = {searchCountries} />
          <CountryList countries={filterCountry}/>
        </Route>
        <Route path="/trips">
           < TripsList users = {users} trips={trips} deleteTrip={deleteTrip} countries={filterCountry} />
        </Route>
        <Route path="/add_trip">
          <NewTripForm users = {users} addTrip={addTrip} updatePostFormData={updatePostFormData}/>
        </Route>
        <Route path="/update_trip">
          <UpdateTripForm updateTrip={updateTrip} setIdToUpdate={setIdToUpdate} updatePatchFormData={updatePatchFormData} trips={trips} deleteTrip={deleteTrip}/>
        </Route>
        <Route path="/search_trip">
          <SearchTrip searchTrip = {searchTrip} searchTrips = {searchTrips}/>
          <TripsList users = {users} trips={filterTrip} />
        </Route>
      </Switch>
    </div>
  );
}

export default App;