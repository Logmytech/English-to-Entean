import sys

PY2 = sys.version_info[0] == 2 #Returns True if Python version is 2 

if PY2:
    from string import maketrans
else:
    maketrans = str.maketrans

FULL_ENGLISH_ALPHABET = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
FULL_ENTEAN_ALPHABET =  "AZYXEWVTISRLPNOMQKJHUGFDCB"

FULL_ENGLISH_ALPHABET += FULL_ENGLISH_ALPHABET.lower()
FULL_ENTEAN_ALPHABET += FULL_ENTEAN_ALPHABET.lower()

tran_tab = maketrans(FULL_ENGLISH_ALPHABET, FULL_ENTEAN_ALPHABET)


def to_entean(text):
    return(text.translate(tran_tab))
    

def main(text=None, with_output=True):

    if text is None:
        if PY2:
            text = raw_input("Enter English text: ")
        else:
            text = input("Enter English text: ")

    if with_output:    
        print(text)
    
    entean_text = to_entean(text)
    
    if with_output:
        print(entean_text)
    

if __name__ == "__main__":
    main()
