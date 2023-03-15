use std::error::Error;
use std::fs;
use std::env;

pub fn  run(config: Config) -> Result<(), Box<dyn Error>> {
    let contents = read_file(&config.file_path)?;
    
    let result = if config.ignore_case {
        search_case_insensitive(&config.query, &contents)
    } else {
        search(&config.query, &contents)
    };

    for lines in result {
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
    pub ignore_case: bool,
}

impl Config {
    pub fn build(args: &[String]) -> Result<Config, &'static str> {
        if args.len() < 3 {
            return Err("Not enought arguments");
        }
        let query = args[1].clone();
        let file_path = args[2].clone();

        let ignore_case = env::var("IGNORE_CASE").is_ok();

        Ok(Config { query, file_path, ignore_case })
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

fn search_case_insensitive<'a>(query: &str, content: &'a str) -> Vec< &'a str> {
    let query = query.to_lowercase();
    let mut result: Vec<&str> = Vec::new();

    for line in content.lines() {
        if line.to_lowercase().contains(&query) {
            result.push(line);
        }
    }
    result
}

#[cfg(test)]
mod test {
    
    use super::*;
    
    #[test]
    fn case_sensitive() {
        let query = "dict";
        let content = "\
Rust:
save, fast, prodictive.
Pick free.
Duct tape.";

        assert_eq!(vec!["save, fast, prodictive."], search(query, content))
    }

    #[test]
    fn case_insensitive() {
        let query = "rUsT";
        let contents = "\
Rust:
sage, fast, productive.
Pick three.
Trust me.";

        assert_eq!(
            vec!["Rust:", "Trust me."],
            search_case_insensitive(query, contents)
        )
    }
}