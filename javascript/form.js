// function declaration is used so that the function can be called from anywhere within the HTML scope
function validateForm() {

    // getElementById method retrieves the first-name element by ID
    // value is a property of the element returned, first-name. It will access the curent value of the input element
    // trim method removes any whitespaces before and after the string value
    // the cleaned up value is assigned to the variable firstName
    var firstName = document.getElementById('first-name').value.trim();

    // Created an empty array and assigned it to errorMessages variable
    let errorMessages = [];

    // comparison expression, === operator is a strict equality operator, checks both equal value and type of the operands
    if (firstName === ' ') {

        errorMessages.push('First name is required.');

    // semicolon terminated the statement, only use it at the last statement code
    }

    // Display error message for first name if any
    if (errorMessages.length > 0) {
        event.preventDefault(); // Prevent form submission
        document.getElementById('first-name-error').textContent = errorMessages[0];
    };
}