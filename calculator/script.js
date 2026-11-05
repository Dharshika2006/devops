
function calculate(operator) {

    let a = Number(document.getElementById("num1").value);
    let b = Number(document.getElementById("num2").value);
    let result;

    if (document.getElementById("num1").value === "" ||
        document.getElementById("num2").value === "") {
        result = "Please enter both numbers";
    }
    else {
        switch (operator) {

            case '+':
                result = a + b;
                break;

            case '-':
                result = a - b;
                break;

            case '*':
                result = a * b;
                break;

            case '/':
                result = b === 0 ? "Cannot divide by zero" : a / b;
                break;
        }
    }

    document.getElementById("result").innerHTML = "Result: " + result;
}
