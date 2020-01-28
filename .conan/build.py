#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os
from cpt.packager import ConanMultiPackager
from dotenv import load_dotenv


if __name__ == "__main__":
    dotenv_path = os.path.join(os.path.dirname(__file__), '.env')
    load_dotenv(dotenv_path)

    builder = ConanMultiPackager(
        use_docker=True,
        docker_run_options='--network host')
    builder.add_common_builds(pure_c=False)
    builder.update_build_if(
        lambda build: build.settings["compiler.libcxx"] == "libc++",
        new_settings={"compiler.libcxx": "libstdc++11"})
    builder.run()
