const isMultipleOf = function (...param) {
    let [number1 , number2, limiter] = param
    let sum = 0
    for (let index = 1; index < limiter; index++) 
        if (!(index % number1) || !(index % number2)) 
            sum = sum + index
    return sum
}
console.log(`The value of the sum of the multiples of 3 and 5 1000 times is ${isMultipleOf(3, 5, 1000)}`)