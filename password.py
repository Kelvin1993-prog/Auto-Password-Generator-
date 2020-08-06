{
 "cells": [
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "### Password  Generator"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 11,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "What is your desired password length? 6\n",
      "9Ee{fg\n"
     ]
    }
   ],
   "source": [
    "\n",
    "def my_password(*password):\n",
    "    \"\"\" Generates auto password\n",
    "    \"\"\"\n",
    "    import random\n",
    "    #the characters you want your password to generate from\n",
    "    char = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789!@#$%^&*()_+{}|\"?\"'\n",
    "\n",
    "    length = input('What is your desired password length? ') \n",
    "    length = int(length) #required password length\n",
    "\n",
    "    password = ''\n",
    "    for p in range(length):\n",
    "        password += random.choice(char)\n",
    "    print(password)\n",
    "my_password()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": []
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3",
   "language": "python",
   "name": "python3"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 4
}
