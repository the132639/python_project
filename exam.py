from utils import unzip_with_7z

zip_file_path = 'congrats.7z' # keep as is
dest_path = '.' # keep as is

find_me = '' # 2 letters are missing!
secret_password = find_me + 'bcmpda' 

# WRITE YOUR CODE BELOW
# ----------------------------------------

password_found = False # set password_found to False so it stops when password_found is True

# Loop through all the possible combinations
for char1 in range(97, 123):  # Use a for loop with the values for lowercase letters for the first letter
    if password_found:
        break # Stop the outer loop if the password is found
    for char2 in range(97, 123): # Find the second letter
        if password_found:
            break # Stop the inner loop if the password is found
        find_me = chr(char1) + chr(char2)  # Combine the letters
        secret_password = find_me + 'bcmpda'    
      
        
        # Try to unzip the file with the password
        try:
            if unzip_with_7z(zip_file_path, dest_path, secret_password):
                print("The password is:", secret_password)
                password_found = True
                break  # Exit the loop if the password is found

        except Exception as e:
            print(f"Trying password: {secret_password} - Failed: {str(e)}")

