
class Palindrome:

    def palindrome_true_or_false(self, chain):
        chain = chain.lower()
        chain = chain.replace(',', '')
        chain = chain.replace(' ', '')
        chain = chain.replace('á', 'a')
        chain = chain.replace('é', 'e')
        chain = chain.replace('í', 'i')
        chain = chain.replace('ó', 'o')
        chain = chain.replace('ú', 'u')
        if chain == chain[::-1]:
            return True
        else: 
            return False