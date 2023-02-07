use std::error::Error;
use std::fs;

pub fn  run(config: Config) -> Result<(), Box<dyn Error>> {
    let contents = read_file(&config.file_path)?;

    for lines in search(&config.query, &contents) {
        println!("{lines}")
    }
    Ok(())
}


fn read_file(file_path: &str) -> Result<String, Box<dyn Error>> {

    let contents = fs::read_to_string(file_path)?;

    Ok(contents)
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

fn search<'a>(query: &str, content: &'a str) -> Vec< &'a str> {
    let mut result: Vec<&str> = Vec::new();
    
    
    for lines in content.lines() {
        if lines.contains(query) {
            result.push(lines);
        }
    }
    result
}

#[cfg(test)]
mod test {
    
    use super::*;
    
    #[test]
    fn one_result() {
        let query = "dict";
        let content = "\
Rust:
save, fast, prodictive.
Pick free.";

        assert_eq!(vec!["save, fast, prodictive."], search(query, content))
    } 
}