# Copyright (C) 2025 Intel Corporation
# SPDX-License-Identifier: MIT

# Put here only the dependencies required to run the module.
# Development and test requirements should go to the corresponding files.
"""Simple example of usage."""
from mfd_kernel_namespace import add_namespace_call_command


# Class example
class CustomPing:
    def __init__(self, connection):
        self._conn = connection

    def ping(self, namespace):
        command = add_namespace_call_command("ping 1.0.0.1", namespace)
        self._conn.start_process(command=command)
        # or
        self._conn.start_process(command=add_namespace_call_command("ping 1.0.0.1", namespace))
