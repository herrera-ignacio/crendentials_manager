# Credentials Manager

This is a credential manager for personal use. Keep all your credentials safe, and access it from anywhere you can run a python shell.

## How it works

The application keeps track and let you update a private encrypted file with all your credentials, let's call it "keys".

Your keys are encrypted using a keyword of your choice. This keyword must never be shared and it's your responsibility to keep it safe. The program will never store this keyword, and it will be asked to you every time you start the application.

As your keys are encrypted, even if they get compromised, there wouldn't be any practical way to read them. Neither the password, the username, or the source. Even so, It's encouraged to keep the file safe and as a single source of truth. You don't want to maintain 2 different keys sets.

## Project Architecture

I try to maintain a Clean Architecture as proposed by Uncle Bob. Given that this is a single-person project, and a small one, some decisions might be taken prioritizing fast delivery over super decoupled components.

The application will let you maintain a private file with all your credentials encrypted by a personal keyword. You will be responsible for keeping your private file with the credentials in a secure storage, and keeping your keyword (private key) safe. The program will never store this private key, so as long as you pick a secure enough keyword, and never share it, there's no practical way to unencrypt your credentials file even if it gets compromised.
