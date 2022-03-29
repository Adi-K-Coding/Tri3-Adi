import math


class Palindrome:
# call function
    def __call__(self, string):
        s = string.strip()
        palindrome1 = s.replace(" ", "").replace("!", "").replace(",", "").replace(".", "").replace("'", "").replace(
            "-", "").replace(":", "").replace(";", "").replace("?", "");
        palindrome = palindrome1.lower()
        # making all letters the same, getting rid of special characters
        print(palindrome)
        ispalindrome = True
        # function to check if string is palidrome
        lengthofinput = (len(palindrome) / 2) + 0.5
        for i in range(0, math.floor(lengthofinput)):
            if palindrome[i] != palindrome[len(palindrome) - (i + 1)]:
                ispalindrome = False
                break
        return ispalindrome;


def runner1():
    palindrome_of = Palindrome()  # object instantiation and run __init__ method
    # Test cases
    print(palindrome_of("ABA"))
    print(palindrome_of("ABBA"))
    print(palindrome_of("racecar"))
    print(palindrome_of("Was it a cat I saw?"))
    print(palindrome_of("A man, a plan, a cat, a ham, a yak, a yam, a hat, a canal - Panama"))
    print(palindrome_of("Doc, Note: I Dissent. A Fast Never Prevents A Fatness. I Diet On Cod."))
    print(palindrome_of("abcdefghijklmnopqrstuvwxyz"))
    print(palindrome_of("This is not a palendrome"))
    print(palindrome_of("This is close but not quite right etiuq ton tub esolc si sihT"))


if __name__ == "__main__":
    runner1()
