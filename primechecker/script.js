
function checkPrime() {

    let n = Number(document.getElementById("num").value);
    let prime = true;

    if (document.getElementById("num").value === "" || !Number.isInteger(n)) {
        document.getElementById("result").innerHTML = "Enter a valid integer";
        return;
    }

    if (n <= 1) {
        prime = false;
    }
    else {
        for (let i = 2; i <= n / 2; i++) {
            if (n % i === 0) {
                prime = false;
                break;
            }
        }
    }

    if (prime)
        document.getElementById("result").innerHTML = n + " is Prime";
    else
        document.getElementById("result").innerHTML = n + " is Not Prime";
}
