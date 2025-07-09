> [!IMPORTANT]  
> This project is under development. All source code and features on the main branch are for the purpose of testing or evaluation and not production ready.

# MFD Kernel Namespace

Module to handle kernel namespaces.

## API NETWORK NAMESPACE

* add_namespace_call_command - method for extending command about namespace command call.

## Usage

```Python
from mfd_kernel_namespace import add_namespace_call_command


# Class example
class CustomPing:
    def __init__(self, connection):
        self._conn = connection

    def ping(self, namespace):
        command = add_namespace_call_command("ping 1.0.0.0", namespace)
        self._conn.start_process(command=command)
        # or 
        self._conn.start_process(command=add_namespace_call_command("ping 1.0.0.0", namespace))
```

## OS supported:

* LINUX
* ESXI
* FREEBSD

## Issue reporting

If you encounter any bugs or have suggestions for improvements, you're welcome to contribute directly or open an issue [here](https://github.com/intel/mfd-kernel-namespace/issues).