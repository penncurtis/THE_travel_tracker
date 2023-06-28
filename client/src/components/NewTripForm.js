import {useState} from 'react'

function NewTripForm({addTrip, updatePostFormData}){

    const [formSubmitted, setFormSubmitted] = useState(false)

    return (
        <div className="trip-form">
            <h2>Add New Trip Form</h2>
            {formSubmitted ? <h1>Thanks for adding a new trip!</h1> :
            <form onSubmit={event => {
                addTrip(event)
                setFormSubmitted(formSubmitted => !formSubmitted)
            }}>
                <input onChange={updatePostFormData} type="text" name="name" placeholder="Hotel name" required/>
                <input onChange={updatePostFormData} type="text" name="image" placeholder="Image URL" required/>
                <input type="submit" value="Add Trip"/>
            </form>}
        </div>
    )
}

export default NewTripForm