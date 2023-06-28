import {NavLink} from "react-router-dom"

function NavBar(){
    return (
        <nav>
            <div>
                <NavLink to="/">Home</NavLink>
            </div>
            <div>
                <NavLink to="/add_trip">Add Trip</NavLink>
                <NavLink to="/update_trip">Update Trip</NavLink>
                <NavLink to="/search_trip">Search Trip</NavLink>
            </div>
        </nav>
    )
}

export default NavBar;