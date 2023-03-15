use std::io;
use num_bigint::BigUint;
fn main() {

    let mut user_input = String::new();

    io::stdin()
        .read_line(&mut user_input)
        .expect("Неверное число");
    
    let user_input: u32 = user_input.trim().parse().expect("Неверное число");
    
    let result = fib(user_input);
    println!("{result}");
}

fn fib(n:u32) -> usize {

    if n == 0 {
        return  0;
    }

    let mut previous_value: usize = 0;
    let mut value: usize = 1;

    
    for _  in 1..n {
        value = previous_value + value;
        previous_value = value - previous_value;
    }
    value
}
