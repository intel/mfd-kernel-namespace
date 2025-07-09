# Copyright (C) 2025 Intel Corporation
# SPDX-License-Identifier: MIT
"""Tests for `mfd_kernel_namespace` package."""

from mfd_kernel_namespace.network_namespace import add_namespace_call_command


class TestMfdKernelNamespace:
    def test_add_namespace_call_command(self):
        assert add_namespace_call_command("ethtool -i", "NS1") == "ip netns exec NS1 ethtool -i"
        assert add_namespace_call_command("ethtool -i", None) == "ethtool -i"

    def test_add_namespace_call_command_with_echo(self):
        assert add_namespace_call_command("echo 1 > /proc/...", "NS1") == "ip netns exec NS1 sh -c 'echo 1 > /proc/...'"
        assert add_namespace_call_command("echo 1 > /proc/...", None) == "echo 1 > /proc/..."
