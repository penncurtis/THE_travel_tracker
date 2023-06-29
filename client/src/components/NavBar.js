import {NavLink} from "react-router-dom"

function NavBar(){
    return (
        <nav className="nav-bar">
            <div>
                <NavLink to="/">Home</NavLink>
                <NavLink to="/add_trip">Add Trip</NavLink>
                <NavLink to="/update_trip">Update Trip</NavLink>
                <NavLink to="/search_trip">Search Trip</NavLink>
                <NavLink to="/trips">Trips List</NavLink>
            </div>
        </nav>
    )
}

export default NavBar;