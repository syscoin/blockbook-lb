"""
Core module for port handling operations
"""

from subprocess import run

def _modify_port(start=None, end=None, protocol='tcp', hook_tool="open-port"):
    assert protocol in {'tcp', 'udp', 'icmp'}
    if protocol == 'icmp':
        start = None
        end = None
    
    if start and end:
        port = f"{start}-{end}/"
    elif start:
        port = f"{start}/"
    else:
        port = ""
    run([hook_tool, f"{port}{protocol}"])

def enable_ping():
    _modify_port(None, None, protocol='icmp', hook_tool="open-port")

def disable_ping():
    _modify_port(None, None, protocol='icmp', hook_tool="close-port")

def open_port(start, end=None, protocol="tcp"):
    _modify_port(start, end, protocol=protocol, hook_tool="open-port")

def close_port(start, end=None, protocol="tcp"):
    _modify_port(start, end, protocol=protocol, hook_tool="close-port")