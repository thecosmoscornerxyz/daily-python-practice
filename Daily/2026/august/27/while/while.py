#!/usr/bin/env bash

import subprocess

while True:
    subprocess.run(
        [
            "sudo", "ping", "-c", "4", "8.8.8.8"
        ]
    )
    break
