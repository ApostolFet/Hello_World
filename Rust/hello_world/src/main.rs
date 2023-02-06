fn main() {
    println!("Hello, world! (Rust)");
}

pub struct Guess {
    value: i32,
}

impl Guess {
    pub fn new(value: i32) -> Guess {
        if value <= 0 {
            panic!("Guess value must be greater than or equal to 1, got {}", value);
        } else if value > 100 {
            panic!("Guess value must be less than or equal to 100, got {}", value);
        }

        Guess { value }
    }
}

#[cfg(test)]
mod test {

    use super::*;

    #[test]
    #[should_panic(expected= "less than or equal to 100")]
    fn test_guess_greater_100() {
        Guess::new(200);
    }

    #[test]
    #[should_panic(expected= "greater than or equal to 1")]
    fn test_less_1() {
        Guess::new(0);
    }

    #[test]
    fn test_all_expected_range() {
        for i in 1..100 {
            let result = Guess::new(i);
            assert_eq!(result.value, i);
        } 
    }
}
