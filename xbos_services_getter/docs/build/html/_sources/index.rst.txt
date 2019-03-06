Welcome to xbos-services-getter's documentation!
================================================

Intro
^^^^^
Allows for easy retrieval of data which is relevant to XBOS projects. 

A Ptyhon 3.5+ wrapper for the XBOS microservices. 

Quick Setup
^^^^^^^^^^^
Using pip for Python 3.5+ run:

.. code-block:: console

   $ pip install xbos-services-getter

Quick Start
^^^^^^^^^^^
To start using the services, set the microservices host address. To get the addresses email me: daniel (dot) lengyel (at) berkeley (dot) edu


Working microservices
^^^^^^^^^^^^^^^^^^^^^

- Comfortband
   Gets the comfortband for a given building and HVAC zone in a timeframe (start, end) and window. 

- Do Not Exceed
   Gets the do not exceed setpoints for a given building and HVAC zone in a timeframe (start, end) and window.  

- Historic Occupancy
   Gets the historic occupancy for a given building and HVAC zone in a timeframe (start, end) and window.

- Price
   Gets the price for a given utility  in a timeframe (start, end) and window.

- Discomfort
   Calculates the discomfort of occupants given an indoor temperature and comfortband.

- HVAC Consumption
   Gets the HVAC consumption for every possible action for a given building and HVAC zone. 

.. -  Outdoor Temperature Historic
    Gets historic outdoor temperatures from weather.gov

Functions
^^^^^^^^^
.. automodule:: xbos_services_getter.xbos_services_getter
   :members:
   :undoc-members:

.. toctree::
   :maxdepth: 2
   :caption: Contents:



Indices and tables
==================

* :ref:`genindex`
* :ref:`modindex`
* :ref:`search`
