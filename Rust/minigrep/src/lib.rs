use std::error::Error;
use std::fs;

pub fn  run(config: Config) -> Result<(), Box<dyn Error>> {
    read_file(&config.file_path)?;
    Ok(())
}


fn read_file(file_path: &str) -> Result<(), Box<dyn Error>> {
    println!("In file {}", file_path);

    let contents = fs::read_to_string(file_path)?;
    println!("With text: {}", contents);
    Ok(())
}

pub struct Config {
    pub query: String,
    pub file_path: String,
}

impl Config {
    pub fn build(args: &[String]) -> Result<Config, &'static str> {
        if args.len() < 3 {
            return Err("Not enought arguments");
        }
        let query = args[1].clone();
        let file_path = args[2].clone();

        Ok(Config { query, file_path })
    }
}