#!/usr/bin/env python
# coding: utf-8

# ---
# layout: post
# title: OS
# subtitle: Exercícios e Referências
# tags: [python, pycharm, jupyter, package, os]
# image: /img/posts/pandas_icon.png
# bigimg: /img/posts/pandas_big.png
# gh-repo: michelmetran/package_os
# gh-badge: [follow, star, watch, fork]
# comments: true
# 
# ---

# # Caminhos e endereços

# In[1]:


import os


# In[27]:


# Pasta Atual
os.getcwd()


# In[9]:


# Altera a pasta
os.chdir('/home/michel/Geodata/SourceCode/michelmetran.github.io')
os.getcwd()


# In[ ]:


# Vai para a Pasta do Usuário
os.path.expanduser('~')


# In[ ]:


# Vai para a pasta de um arquivo específicos
os.path.dirname('/home/michel/Geodata/SourceCode/package_pandas/pandas.ipynb')


# In[15]:


# Altera a pasta
os.chdir('/home/michel/Geodata/SourceCode/package_os')
os.getcwd()


# In[16]:


from importlib import reload
reload(os)


# ## Pastas e Diretórios

# In[ ]:


# Cria Diretório
os.makedirs('directory')


# In[ ]:


import shutil
shutil.rmtree('directory')


# ## Loops

# In[ ]:





# In[19]:


get_ipython().run_line_magic('run', "'../codes/files/create_folders.py'")
create_folders('', ['data', 'data/Dados Originais', 'docs', 'maps'])


# In[20]:


# %load '../codes/files/export_jupyter.py'
def export_jupyter(path, extensions=['html', 'markdown', 'latex', 'pdf', 'python'], today=True):
    """
    Export .ipynb file to others formats
    :return: File in other formats
    """
    # Import Packages
    import os
    import datetime

    # Data
    timestamp = datetime.datetime.now()
    srt_today = (str(timestamp.year) + '-' +
                 str(f"{timestamp.month:02d}") + '-' +
                 str(f"{timestamp.day:02d}"))

    # Extensions
    for extension in extensions:
        if today==True:
            os.system('jupyter nbconvert --to {} {} --output {}'.
                      format(extension, get_jupyternotebook_name(),
                             os.path.join(path, srt_today+'-'+get_jupyternotebook_name().split('.')[0])))
            print('Arquivo {} exportado corretamente para o formato {} usando prefixo da data.'.
                  format(get_jupyternotebook_name(), extension))

        else:
            os.system('jupyter nbconvert --to {} {} --output {}'.
                      format(extension, get_jupyternotebook_name(),
                             os.path.join(path, get_jupyternotebook_name().split('.')[0])))
            print('Arquivo {} exportado corretamente para o formato {} sem usar prefixo da data.'.
                  format(get_jupyternotebook_name(), extension))


# In[24]:


# %load '../codes/files/get_jupyternotebook_name.py'
def get_jupyternotebook_name():
    """
    Returns the name of the current notebook as a string
    From https://mail.scipy.org/pipermail/ipython-dev/2014-June/014096.html
    :return: Returns the name of the current notebook as a string
    """
    # Import Packages
    from IPython.core.display import Javascript
    from IPython.display import display

    display(Javascript('IPython.notebook.kernel.execute("theNotebook = " +     "\'"+IPython.notebook.notebook_name+"\'");'))

    # Result
    return theNotebook


# In[26]:


export_jupyter('docs',['pdf'], False)
export_jupyter('docs', ['markdown'], True)


# In[28]:


get_jupyternotebook_name()


# In[ ]:




