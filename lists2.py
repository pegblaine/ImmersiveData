{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": [
    "the_count = [1, 2, 3, 4, 5]\n",
    "fruits = ['apples', 'oranges', 'pears', 'apricots']\n",
    "change = [1, 'pennies', 2, 'dimes', 3, 'quarters']\n",
    "\n",
    "# this first kind of for-loop goes through a list\n",
    "for number in the_count:\n",
    "     print(f\"This is count {number}\")\n",
    "\n",
    "# same as above\n",
    "for fruit in fruits:\n",
    "     print(f\"A fruit of type: {fruit}\")\n",
    "\n",
    "# also we can go through mixed lists too\n",
    "for i in change:\n",
    "     print(f\"I got {i}\")\n",
    "\n",
    "# we can also build lists, first start with an empty one\n",
    "elements = []\n",
    "\n",
    "# then use the range function to do 0 to 5 counts\n",
    "for i in range(0, 6):\n",
    "     print(f\"Adding {i} to the list.\")\n",
    "     # append is a function that lists understand\n",
    "     elements.append(i)\n",
    "\n",
    "# now we can print them out too\n",
    "for i in elements:\n",
    "     print(f\"Element was: {i}\")"
   ]
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.7.3"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 2
}
