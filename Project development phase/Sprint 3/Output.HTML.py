#!/usr/bin/env python
# coding: utf-8

# In[ ]:


<!DOCTYPE html>


# In[ ]:


<html>


# In[ ]:


<head>


# In[ ]:


<meta charset="utf-8">


# In[ ]:


<title>OUTPUT</title>


# In[ ]:


</head>


# In[ ]:


<body>


# In[ ]:


<style>


# In[ ]:


* {


# In[ ]:


box-sizing: border-box;


# In[ ]:


}


# In[ ]:


body {


# In[ ]:


margin: 0px;


# In[ ]:


padding: 0px;


# In[ ]:


font: poppins;


# In[ ]:


}


# In[ ]:


#main {


# In[ ]:


background-color: beige;


# In[ ]:


width: 100%;


# In[ ]:


height: 50vh;


# In[ ]:


position: relative;


# In[ ]:


}


# In[ ]:


nav {


# In[ ]:


display: flex;


# In[ ]:


justify-content: space-around;


# In[ ]:


align-items: center;


# In[ ]:


top: 0;


# In[ ]:


bottom: 0;


# In[ ]:


width: 100%;


# In[ ]:


background-color: rgb(255, 255, 255);


# In[ ]:


z-index: 1;


# In[ ]:


}


# In[ ]:


.menu {


# In[ ]:


list-style: none;


# In[ ]:


display: flex;


# In[ ]:


}


# In[ ]:


a {


# In[ ]:


text-decoration: none;


# In[ ]:


}


# In[ ]:


.menu li a {


# In[ ]:


height: 40px;


# In[ ]:


line-height: 43px;


# In[ ]:


margin: 3px;


# In[ ]:


padding: 0px 22px;


# In[ ]:


display: flex;


# In[ ]:


text-transform: uppercase;


# In[ ]:


font-size: 0.8em;


# In[ ]:


font-weight: 500;


# In[ ]:


letter-spacing: 1px;


# In[ ]:


color: gray;


# In[ ]:


}


# In[ ]:


.content {


# In[ ]:


background-color: #eaf275;


# In[ ]:


display: flex;


# In[ ]:


width: 90%;


# In[ ]:


justify-content: space-around;


# In[ ]:


align-items: center;


# In[ ]:


position: absolute;


# In[ ]:


left: 50%;


# In[ ]:


right: 50%;


# In[ ]:


transform: translate(-50%, -50%);


# In[ ]:


}


# In[ ]:


.content-new{


# In[ ]:


background-color: #eaf275;


# In[ ]:


display: flex;


# In[ ]:


width: 90%;


# In[ ]:


height:45%;


# In[ ]:


justify-content: space-around;


# In[ ]:


align-items: center;


# In[ ]:


position: absolute;


# In[ ]:


left: 50%;


# In[ ]:


right: 50%;


# In[ ]:


transform: translate(-50%, -50%);


# In[ ]:


}


# In[ ]:


.main-text {


# In[ ]:


width: 500px;


# In[ ]:


}


# In[ ]:


.main-text h1 {


# In[ ]:


font-size: 3.5em;


# In[ ]:


color: #1c3548;     


# In[ ]:


block-size: 0ex;


# In[ ]:


margin: 0px 0px 10px 0px;


# In[ ]:


line-height: 60px;


# In[ ]:


}


# In[ ]:


.main-text p {


# In[ ]:


color: rgb(0, 0, 0);


# In[ ]:


}


# In[ ]:


.menu li a:hover {


# In[ ]:


background-color: #23cdaf;


# In[ ]:


color: white;


# In[ ]:


box-shadow: 5px 10px 30px rgba(24, 139, 119, 0.2);


# In[ ]:


transition: all ease 0.2s;


# In[ ]:


}


# In[ ]:


</style>


# In[ ]:


<section id ="main">


# In[ ]:


<nav>


# In[ ]:


<span class="menu-space"></span>


# In[ ]:


<h2>Liver Patient Predction</h2>


# In[ ]:


<ul class="menu">


# In[ ]:


<li><a href="{{ url_for('home') }}">home</a></li>


# In[ ]:


</ul>


# In[ ]:


</nav>


# In[ ]:


</section>


# In[ ]:


<div class="content-new">


# In[ ]:


<h3>You have Liver disease problem, you must and should consult a doctor. Take care


# In[ ]:


</h3>


# In[ ]:


</div>


# In[ ]:


</body>


# In[ ]:


</html>

