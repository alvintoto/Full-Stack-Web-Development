// Get DOM elements
const display = document.querySelector('input[name="display"]');
const clear = document.querySelector('input[name="clear"]');
const buttons = document.querySelectorAll('.button input[type="button"]');

// Initialize calculator state
let currentValue = '0';
let operator = null;
let result = null;
let shouldResetDisplay = false;

// Update display with current value
function updateDisplay() {
    display.value = currentValue;
}

// Reset calculator state
function resetCalculator() {
    currentValue = '0';
    operator = null;
    result = null;
    shouldResetDisplay = false;
    updateDisplay();
}

// Update calculator state based on button input
function handleButtonClick(event) {
    const { target } = event;
    const buttonValue = target.value;

    switch (buttonValue) {
        // Handle number button input
        case '0':
        case '1':
        case '2':
        case '3':
        case '4':
        case '5':
        case '6':
        case '7':
        case '8':
        case '9':
            if (currentValue === '0' || shouldResetDisplay) {
                currentValue = buttonValue;
                shouldResetDisplay = false;
            } else {
                currentValue += buttonValue;
            }
            break;

        // Handle decimal button input
        case '.':
            if (!currentValue.includes('.')) {
                currentValue += buttonValue;
            }
            break;

        // Handle operator button input
        case '+':
        case '-':
        case '*':
        case '/':
            if (operator !== null) {
                calculate();
            }
            operator = buttonValue;
            result = parseFloat(currentValue);
            shouldResetDisplay = true;
            break;

        // Handle equals button input
        case '=':
            calculate();
            operator = null;
            shouldResetDisplay = true;
            break;

        // Handle clear button input
        case 'C':
            resetCalculator();
            break;

        // Ignore other button inputs
        default:
            break;
    }

    updateDisplay();
}

// Perform calculation and update display with result
function calculate() {
    if (operator === null) {
        return;
    }

    const currentValueFloat = parseFloat(currentValue);

    switch (operator) {
        case '+':
            result += currentValueFloat;
            break;
        case '-':
            result -= currentValueFloat;
            break;
        case '*':
            result *= currentValueFloat;
            break;
        case '/':
            result /= currentValueFloat;
            break;
        default:
            break;
    }

    currentValue = result.toString();
}

// Attach event listeners to buttons
clear.addEventListener('click', resetCalculator);
buttons.forEach(button => {
    button.addEventListener('click', handleButtonClick);
});

// Make it so user can't type in display
display.addEventListener('keydown', event => {
    event.preventDefault();
}
);
