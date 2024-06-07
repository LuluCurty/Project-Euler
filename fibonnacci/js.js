const fibonacci = function () {
    let temp, num1=0, num2=1, sum = 0
    const array = [0]
    while(num2 < 4000000){
        if(!(num2 % 2)) array.push(num2)
        temp = num1 + num2
        num1 = num2
        num2 = temp
    }
    array.forEach(element => { sum = element + sum })
    array.push(sum)
    return array[array.length-1]
}