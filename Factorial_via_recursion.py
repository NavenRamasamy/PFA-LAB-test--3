#!/usr/bin/env python
# coding: utf-8

# In[ ]:


def factR(n):
    if n == 1:
        return n
    else:
        return n*factR(n - 1)

factR(4)

