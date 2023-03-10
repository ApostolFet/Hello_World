use std::env;
use std::process;

use minigrep::Config;

fn main() {
    let envirement_args: Vec<String> = env::args().collect();

    let config = Config::build(&envirement_args).unwrap_or_else(|err| {
        println!("Problem parsing arguments: {err}");
        process::exit(1);
    });

    if let Err(e) = minigrep::run(config) {
        println!("Aplication error: {e}");
        process::exit(1);
    }
}
