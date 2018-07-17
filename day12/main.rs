use std::fs::File;
use std::io::prelude::*;
use std::collections::HashMap;

fn main() {
    solve("input.txt", true);
}

fn solve(filename: &str, hard_mode: bool) {
    let mut pos: usize = 0;
    let mut variables = HashMap::new();

    variables.insert('a', 0i32);
    variables.insert('b', 0i32);
    variables.insert('c', 0i32);
    variables.insert('d', 0i32);

    if hard_mode {
        variables.insert('c', 1i32);
    }

    let mut file = File::open(filename).expect("Line 22");
    let mut content = String::new();

    file.read_to_string(&mut content).expect("Line 25");
    let instructions: Vec<&str> = content.split('\n').collect();

    while pos < instructions.len() {
        let instruction: Vec<&str> = instructions[pos].split(' ').collect();
        if instruction[0] == "cpy" {
            cpy(&mut variables, &instruction[1], &instruction[2]);
            pos += 1;
        } else if instruction[0] == "inc" {
            inc(&mut variables, &instruction[1]);
            pos += 1;
        } else if instruction[0] == "dec" {
            dec(&mut variables, &instruction[1]);
            pos += 1;
        } else if instruction[0] == "jnz" {
            pos = jnz(&mut variables, pos, &instruction[1], &instruction[2]);
        }
    }

    let a = 'a';
    println!("{}", variables[&a]);
}

fn cpy(variables: &mut HashMap<char, i32>, x: &str, y: &str) {
    let key = y.chars().next().expect("Line 49");

    if x.parse::<i32>().is_ok() {
        let new_val: i32 = x.parse().expect("Line 52");
        variables.insert(key, new_val);
    } else {
        let x_key = x.chars().next().expect("Line 55");
        let new_val = variables[&x_key];
        variables.insert(key, new_val);
    }
}

fn inc(variables: &mut HashMap<char, i32>, x: &str) {
    let key = x.chars().next().expect("Line 62");
    let new_val = variables[&key];
    variables.insert(key, new_val + 1);
}

fn dec(variables: &mut HashMap<char, i32>, x: &str) {
    let key = x.chars().next().expect("Line 68");
    let new_val = variables[&key];
    variables.insert(key, new_val - 1);
}

fn jnz(variables: &mut HashMap<char, i32>, pos: usize, x: &str, y: &str) -> usize {
    let result: usize;
    let first_char = x.chars().next().expect("Line 75");

    if (x.len() == 1 && first_char == '0') || (variables.contains_key(&first_char) && variables[&first_char] == 0) {
        return pos + 1;
    }

    let temp_num: isize = y.trim().parse().expect("Line 81");
    let num = temp_num.abs() as usize;

    if temp_num < 0 {
        result = pos - num;
    } else {
        result = pos + num;
    }
    result
}
