use std::io;
use rand::Rng;
use std::cmp::Ordering;

fn main() {
   //println!("Hello, world!");
    println!("Please input your guess: ");
    let mut guess = String::new();
    let random_number = rand::thread_rng().gen_range(1, 114515);
    io::stdin().read_line(&mut guess)
        .expect("Failed to read the line");
    println!("Your input: {}", guess);
    let guess: u64 = guess.trim().parse()
        .expect("Please type a number!");
    match guess.cmp(&random_number) {
        Ordering::Less => println!("Your guesses is smaller than expected."),
        Ordering::Equal => println!("Your guesses is equal to the generated number."),
        Ordering::Greater => println!("Your guesses is greater to the generated number."),
    }
    println!("Random number: {}", random_number);
}

