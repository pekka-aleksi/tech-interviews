NGINX: Load Balancer in LUA
===

This was a very small piece of code that was testing my skills with basic web things and Linux administration. This is a configuration file with inline LUA that gets fed to NGINX.

I was asked to create a load balancer (a small piece of code in this case) that takes an incoming HTTP request and depending on the precise URL that was requested (including the parameters) it redirects the request to one server, or another.

The system tries to keep the balance by taking the URL and running it through the MD5 function, and then making the decision based on the first hexadecimals of the MD5 hash. The idea was just a "proof of concept" thing and was not meant to be taken seriously.

Trying to run this is not worth the effort albeit it's possible. You will need to install a special version of NGINX which is called `openresty` because the load balancing code is written in LUA.