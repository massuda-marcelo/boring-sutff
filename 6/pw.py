#! python
#  encoding: utf-8

# Boring Stuff
# Ex 6-1 Password locker

import sys, pyperclip

PASSWORDS = {
    'email'     : 'kjdfsdaoihsdnvjjp32ir0i0jvj',
    'blog'      : 'iu2dfjdsgio94995eoasmc.>:><',
    'luggage'   : '34989'
}

def main() :
    if (len(sys.argv) < 2):
        print('Usage: python pw.py account - copy account password')
        sys.exit()

    account = sys.argv[1]

    if (account in PASSWORDS):
        pyperclip.copy(PASSWORDS[account])
        print('Password for ' + account + ' copied to clipboard')
    else:
        print('There is no account named ' + account)

if __name__ == '__main__':
    main()
