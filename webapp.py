{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": [
    "from flask import Flask, render_template, request\n",
    "\n",
    "app = Flask(__name__)\n",
    "\n",
    "books = {\n",
    "    \"روايات\": [\n",
    "        {\"title\": \"الخيميائي\", \"link\": \"https://example.com/alchemist.pdf\"},\n",
    "        {\"title\": \"موسم الهجرة إلى الشمال\", \"link\": \"https://example.com/hijra.pdf\"},\n",
    "    ],\n",
    "    \"تطوير الذات\": [\n",
    "        {\"title\": \"فن اللامبالاة\", \"link\": \"https://example.com/fan.pdf\"},\n",
    "    ],\n",
    "    \"برمجة\": [\n",
    "        {\"title\": \"Python للمبتدئين\", \"link\": \"https://example.com/python.pdf\"},\n",
    "    ]\n",
    "}\n",
    "\n",
    "@app.route(\"/\", methods=[\"GET\", \"POST\"])\n",
    "def index():\n",
    "    results = []\n",
    "    query = \"\"\n",
    "    if request.method == \"POST\":\n",
    "        query = request.form.get(\"query\", \"\").lower()\n",
    "        for category_books in books.values():\n",
    "            for book in category_books:\n",
    "                if query in book['title'].lower():\n",
    "                    results.append(book)\n",
    "    return render_template(\"index.html\", results=results, query=query)\n",
    "\n",
    "if __name__ == \"__main__\":\n",
    "    app.run(debug=True)"
   ]
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3 (ipykernel)",
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
   "version": "3.11.0"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 4
}
