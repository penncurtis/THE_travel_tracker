import {useState} from 'react'

function NewTripForm({addTrip, updatePostFormData, users}){

    const [formSubmitted, setFormSubmitted] = useState(false)

    return (
        <div className="trip-form">
            <h2>Add New Trip Form</h2>
            {formSubmitted ? <h1>Thanks for adding a new trip!</h1> :
            <form onSubmit={event => {
                addTrip(event)
                setFormSubmitted(formSubmitted => !formSubmitted)
            }}>
                <input onChange={updatePostFormData} type="text" name="username" placeholder="Insert Username" required/>
                <input onChange={updatePostFormData} type="text" name="date_visited" placeholder="Date (YYYY-MM-DD)" required/>
                <input onChange={updatePostFormData} type="text" name="country_name" placeholder="Country name" required/>
                <input type="submit" value="Add Trip"/>
            </form>}
        </div>
    )
}

export default NewTripForm