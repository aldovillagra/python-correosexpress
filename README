Correos express
===

Python API Correos express carrier.

Features
--------

- Services
- Test connection
- Create/Send shipments to Correos express
- Get label shipment in PDF

Usage Examples
--------------

Example API in test.py file

Services
--------

.. code-block:: python

    from correosexpress.utils import services
    services()

Test connection
---------------

.. code-block:: python

    with API(username, debug) as asm_api:
        print asm_api.test_connection()

Create/send shipment to Correos express
---------------------------

.. code-block:: python

    with Picking(username, debug) as picking_api:
        data = {...}
        reference, label, error = picking_api.create(data)

Get label shipment
------------------

.. code-block:: python

    with Picking(username, debug) as picking_api:
        data = {...}
        label = picking_api.label(data)
