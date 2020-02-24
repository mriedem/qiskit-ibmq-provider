# -*- coding: utf-8 -*-

# This code is part of Qiskit.
#
# (C) Copyright IBM 2018, 2012.
#
# This code is licensed under the Apache License, Version 2.0. You may
# obtain a copy of this license in the LICENSE.txt file in the root directory
# of this source tree or at http://www.apache.org/licenses/LICENSE-2.0.
#
# Any modifications or derivative works of this code must retain this
# copyright notice, and modified files need to carry a notice indicating
# that they have been altered from the originals.
"""
================================================================
Jupyter Tools (:mod:`qiskit.providers.ibmq.jupyter`)
================================================================

.. currentmodule:: qiskit.providers.ibmq.jupyter

A Collection of Jupyter magic functions and tools
that extend the functionality of Qiskit for the IBM
Quantum devices.

Detailed information on a single backend
========================================

.. jupyter-execute::

    from qiskit import IBMQ
    import qiskit.providers.ibmq.jupyter

    IBMQ.load_account()
    provider = IBMQ.get_provider(hub='ibm-q')
    backend = provider.get_backend('ibmq_vigo')
    backend

"""
import sys

if ('ipykernel' in sys.modules) and ('spyder' not in sys.modules):

    from IPython import get_ipython          # pylint: disable=import-error
    from qiskit.test.mock import FakeBackend
    from ..ibmqbackend import IBMQBackend
    from .backend_info import backend_widget

    _IP = get_ipython()
    if _IP is not None:
        HTML_FORMATTER = _IP.display_formatter.formatters['text/html']
        # Make backend_widget the html repr for IBM Quantum backends
        HTML_FORMATTER.for_type(IBMQBackend, backend_widget)
        HTML_FORMATTER.for_type(FakeBackend, backend_widget)