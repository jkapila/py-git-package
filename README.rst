

=========================================================
Py - Git - Package : A modern template for Python Package
=========================================================

.. image:: https://codecov.io/gh/{{codecov_username}}/forutils/branch/master/graph/badge.svg
	  :target: https://codecov.io/gh/{{codecov_username}}/forutils
	  :alt: Code coverage
	  :align: right

..  image:: https://img.shields.io/badge/code%20style-black-000000.svg
	  :target: https://github.com/ambv/black
	  :alt: Code Style
	  :align: right


.. teaser-begin

**sourcecodes** is here to make better features for forecasting purpose.


.. epigraph::
   This is some **awesome text** about your package!!!

Go ahead use the template and create and awesome package


.. teaser-end

.. context-begin

This a python package template based on shoulder of

1. `python-library-template <https://github.com/thclark/python-library-template>`_ as main pakage template created by `Tom Clark  <https://github.com/thclark>`_
2. `Furo  <https://pradyunsg.me/furo/>`_ (Sphinx theme) for Documentation
3. Github Pages for hosting Documentation
4. `Pre-commit  <https://pre-commit.com/>`_ hooks for cleaning and building things before we ake any commit (Includes Sphinx Auto Doc Builds too)

.. context-end


The Documentation generated can be found at `here. <https://jkapila.github.io/py-git-package/>`_

.. role:: raw-html(raw)
    :format: html


:raw-html:`<br />`

.. steps-begin

Use following steps to make use the whole template

1. Do a pre-commit install with :code:`pre-commit install`
2. Add your code in respective places
3. Write documentation
4. Run :code:`sphinx-build -b html -j 2 docsrc docs` to create the documentation and sphinx gallery
	a. (Optional) Check for any errors with precommit :code:`pre-commit run --all-files`
5. Add your files and do your commit with some good message and wait for pre-commeit to do its charm.
6. Correct any error if any from precommit.
7. Push your code to git
8. Host your documentation on github pages by changing folder to docs
9. Showcase you work to world. :)

.. steps-end


:raw-html:`<br />`

TODO
====

1. Add `Sphinx Matplotlib  <https://matplotlib.org/3.1.1/devel/plot_directive.html>`_ native support
2. Add Plotly in Sphinx support via `Plotly Directive <https://github.com/harupy/sphinx-plotly-directive>`_ or `Sphinx Charts <https://github.com/thclark/sphinx-charts>`_
3. Better pre commit hook for documentation rebuilding. (Sphinx build is not working efficiently)
