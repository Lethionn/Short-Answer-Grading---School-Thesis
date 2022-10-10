{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 1,
   "id": "9b6bbd53",
   "metadata": {},
   "outputs": [],
   "source": [
    "from flask import Flask, redirect, url_for, render_template, request, session\n",
    "import features_module as fm"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 2,
   "id": "3743d161",
   "metadata": {},
   "outputs": [],
   "source": [
    "app = Flask(__name__)\n",
    "@app.route('/', methods=['GET', 'POST'])\n",
    "\n",
    "def home_route():\n",
    "    dict={}\n",
    "    if request.method == 'GET':\n",
    "        dict['question']=''\n",
    "        dict['refans']=''\n",
    "        dict['studans']=''\n",
    "        dict['result']=''\n",
    "        dict['display']='none'\n",
    "    elif request.method == 'POST':\n",
    "        dict['question']=request.form['question']\n",
    "        dict['refans']=request.form['refans']\n",
    "        dict['studans']=request.form['studans']\n",
    "        dict['display']='block'\n",
    "        f=fm.get_features([request.form['studans']],request.form['refans'],request.form['question'])\n",
    "        x=fm.get_prob(f)[0]\n",
    "        p=\"\"\n",
    "        c=''\n",
    "        score=round(x[1]*10,1)\n",
    "        if score>5.5:\n",
    "            p='correct'\n",
    "            c='ag'\n",
    "        elif score>3.0:\n",
    "            p='partially correct'\n",
    "            c='ap'\n",
    "        else:\n",
    "            p='wrong'\n",
    "            c='ar'\n",
    "        dict['result']=p\n",
    "        dict['scoreclass']=c\n",
    "        if score>5.5:\n",
    "            score=score+1;\n",
    "        dict['score']=score\n",
    "    return render_template('home.html',data=dict)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "1e285e8a",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      " * Serving Flask app \"__main__\" (lazy loading)\n",
      " * Environment: production\n",
      "   WARNING: This is a development server. Do not use it in a production deployment.\n",
      "   Use a production WSGI server instead.\n",
      " * Debug mode: off\n"
     ]
    },
    {
     "name": "stderr",
     "output_type": "stream",
     "text": [
      "INFO:werkzeug: * Running on http://127.0.0.1:5000/ (Press CTRL+C to quit)\n",
      "INFO:werkzeug:127.0.0.1 - - [21/Jun/2021 01:09:18] \"\u001b[37mGET / HTTP/1.1\u001b[0m\" 200 -\n",
      "INFO:werkzeug:127.0.0.1 - - [21/Jun/2021 01:10:05] \"\u001b[37mPOST / HTTP/1.1\u001b[0m\" 200 -\n",
      "INFO:werkzeug:127.0.0.1 - - [21/Jun/2021 01:10:55] \"\u001b[37mPOST / HTTP/1.1\u001b[0m\" 200 -\n",
      "INFO:werkzeug:127.0.0.1 - - [21/Jun/2021 01:11:28] \"\u001b[37mGET / HTTP/1.1\u001b[0m\" 200 -\n",
      "INFO:werkzeug:127.0.0.1 - - [21/Jun/2021 01:12:18] \"\u001b[37mPOST / HTTP/1.1\u001b[0m\" 200 -\n",
      "INFO:werkzeug:127.0.0.1 - - [21/Jun/2021 01:14:21] \"\u001b[37mPOST / HTTP/1.1\u001b[0m\" 200 -\n",
      "INFO:werkzeug:127.0.0.1 - - [21/Jun/2021 01:14:31] \"\u001b[37mPOST / HTTP/1.1\u001b[0m\" 200 -\n",
      "INFO:werkzeug:127.0.0.1 - - [21/Jun/2021 01:14:41] \"\u001b[37mPOST / HTTP/1.1\u001b[0m\" 200 -\n",
      "INFO:werkzeug:127.0.0.1 - - [21/Jun/2021 01:15:16] \"\u001b[37mPOST / HTTP/1.1\u001b[0m\" 200 -\n",
      "INFO:werkzeug:127.0.0.1 - - [21/Jun/2021 01:16:12] \"\u001b[37mPOST / HTTP/1.1\u001b[0m\" 200 -\n",
      "INFO:werkzeug:127.0.0.1 - - [21/Jun/2021 01:33:38] \"\u001b[37mGET / HTTP/1.1\u001b[0m\" 200 -\n",
      "INFO:werkzeug:127.0.0.1 - - [21/Jun/2021 01:34:10] \"\u001b[37mPOST / HTTP/1.1\u001b[0m\" 200 -\n",
      "INFO:werkzeug:127.0.0.1 - - [21/Jun/2021 01:35:02] \"\u001b[37mPOST / HTTP/1.1\u001b[0m\" 200 -\n",
      "INFO:werkzeug:127.0.0.1 - - [21/Jun/2021 01:35:47] \"\u001b[37mPOST / HTTP/1.1\u001b[0m\" 200 -\n",
      "INFO:werkzeug:127.0.0.1 - - [21/Jun/2021 01:54:45] \"\u001b[37mGET / HTTP/1.1\u001b[0m\" 200 -\n",
      "INFO:werkzeug:127.0.0.1 - - [21/Jun/2021 01:55:19] \"\u001b[37mPOST / HTTP/1.1\u001b[0m\" 200 -\n",
      "INFO:werkzeug:127.0.0.1 - - [21/Jun/2021 01:56:20] \"\u001b[37mPOST / HTTP/1.1\u001b[0m\" 200 -\n",
      "INFO:werkzeug:127.0.0.1 - - [21/Jun/2021 01:56:56] \"\u001b[37mPOST / HTTP/1.1\u001b[0m\" 200 -\n"
     ]
    }
   ],
   "source": [
    "if __name__ == \"__main__\":\n",
    "    app.run(debug=False, use_reloader=False)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "2bec1edd",
   "metadata": {},
   "outputs": [],
   "source": [
    "%tb"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "67ab4827",
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
   "version": "3.9.5"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 5
}
