fn feistel_cipher(text: u32, key: u32, rounds: usize) -> u32 {
    let mut left = text >> 16;
    let mut right = text & 0xFFFF;

    for _ in 0..rounds {
        let temp = left;
        left = right ^ (left.wrapping_add(key));
        right = temp;
    }

    let result = (left << 16) | right;
    result
}

fn main() {
    let plaintext = 0b11011010101100101111000010101010;
    let key = 0b10111001010101110111001010111010;
    let rounds = 16;

    let ciphertext = feistel_cipher(plaintext, key, rounds);

    println!("Plaintext: {:032b}", plaintext);
    println!("Ciphertext: {:032b}", ciphertext);
}
