#!/usr/bin/env python

"""A script to prepare the source tree for building."""

# This script must have no special requirements because it wont be able to
# import any GRR stuff until the protos are built.

import logging
import os
import subprocess


def MakeProto():
  """Make sure our protos have been compiled to python libraries."""
  # Start running from one directory above the grr directory which is found by
  # this scripts's location as __file__.
  cwd = os.path.dirname(os.path.abspath(__file__))

  # Find all the .proto files.
  protos_to_compile = []
  for (root, _, files) in os.walk(cwd):
    for filename in files:
      full_filename = os.path.join(root, filename)
      if full_filename.endswith(".proto"):
        proto_stat = os.stat(full_filename)
        try:
          pb2_stat = os.stat(full_filename.rsplit(".", 1)[0] + "_pb2.py")
          if pb2_stat.st_mtime >= proto_stat.st_mtime:
            continue

        except (OSError, IOError):
          pass

        protos_to_compile.append(full_filename)

  if protos_to_compile:
    # Find the protoc compiler.
    protoc = os.environ.get("PROTOC", "protoc")
    try:
      output = subprocess.check_output([protoc, "--version"])
    except (IOError, OSError):
      raise RuntimeError("Unable to launch %s protoc compiler. Please "
                         "set the PROTOC environment variable.", protoc)

    if "2.6.1" not in output:
      raise RuntimeError("Incompatible protoc compiler detected. "
                         "We need 2.6.1 not %s" % output)

    for proto in protos_to_compile:
      logging.info("Compiling %s", proto)
      # The protoc compiler is too dumb to deal with full paths - it expects a
      # relative path from the current working directory.
      subprocess.check_call(
          [protoc,
           # Write the python files next to the .proto files.
           "--python_out=.",
           # Standard include paths.
           # We just bring google/proto/descriptor.proto with us to make it
           # easier to install.
           "--proto_path=.", "--proto_path=grr", "--proto_path=grr/proto",
           os.path.relpath(proto, cwd)
          ], cwd=cwd)


if __name__ == "__main__":
  root_logger = logging.getLogger()
  root_logger.setLevel(logging.INFO)

  MakeProto()
