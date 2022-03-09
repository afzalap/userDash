import random    


def captcha_challenge():

    # import random
    # str_var = list("shuffle_this_string")
    # random.shuffle(str_var)
    # print ''.join(str_var)
     
    # Characters to be included
    chrs = "Klc2HSweQiRDodg5sWxz90GPyf3EkVMYaqJhmUuZF1BCntLNXIvjTbp67r4A8O"

    chrs_vars = list(chrs)
    random.shuffle(chrs_vars)
    chrs = ''.join(chrs_vars)
     
    n = random.randint(4, 7)
    # Generate n characters from above set and
    # add these characters to captcha.
    captcha = ""
    while (n):
        captcha += chrs[random.randint(1, 100) % 62]
        n -= 1
    return captcha, captcha


# def captcha_challenge():
#     challenge = u''
#     response = u''
#     for i in range(4):
#         digit = random.randint(0,9)
#         challenge += str(digit)
#         response += str((digit + 1) % 10)
#     return challenge, response    


# def captcha_challenge():
#     n = random.randint(4, 7)
#     captcha =''.join(random.SystemRandom().choice([chr(i) for i in range(97, 123)] + [str(i) for i in range(n)]) for _ in range(n))
#     return captcha, captcha

