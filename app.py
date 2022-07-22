#!/usr/bin/env python
# coding: utf-8

# In[ ]:


from flask import Flask,request,render_template


# In[ ]:


import joblib


# In[ ]:


app = Flask(__name__)


# In[ ]:


@app.route("/",methods = ["GET","POST"])
def index():
    if request.method == "POST":
        rates=float(request.form.get("rates"))
        print(rates)
        model1=joblib.load("regression")
        r1=model1.predict([[rates]])
        model2=joblib.load("tree")
        r2=model2.predict([[rates]])
        return(render_template("index.html",results1=r1,result2=r2))
    else:
        return(render_template("index.html",results1="WARNING",result2="WARNING"))


# In[ ]:


#if __name__ == "__main__":
#    app.run()


# In[ ]:





# In[ ]:





# In[ ]:




