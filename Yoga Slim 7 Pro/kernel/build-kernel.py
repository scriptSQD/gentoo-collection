#!/usr/bin/env python

from enum import Enum
import os
from datetime import datetime
from time import sleep

class Colors(Enum):
    LOG="\033[95m"
    GREEN="\033[92m"
    YELLOW="\033[93m"
    RED="\033[91m"
    END="\033[0m"

class Logger:
    def success(message):
        return f"{Colors.GREEN.value}{message}{Colors.END.value}"

    def warning(message):
        return f"{Colors.YELLOW.value}{message}{Colors.END.value}"

    def error(message):
        return f"{Colors.RED.value}{message}{Colors.END.value}"

    def log(message):
        return f"{Colors.LOG.value}{message}{Colors.END.value}"

print(Logger.log(">> Checking for root:\n"))
is_root = os.geteuid() == 0;
if not is_root:
    print(Logger.error(">> This script must be run as root!"))
    exit(1)

src_dir = "/usr/src/linux"

log_timestamp = datetime.now().strftime("%H%M%S_%d%m%Y")
log_dir = f"/tmp/build-kernel/{log_timestamp}"
if not os.path.exists(log_dir):
    os.makedirs(log_dir)


makeflags = '-j16'

common_flags = "-march=znver3 -O2"

cflags = f"{common_flags}"
cxxflags = f"{common_flags}"

toolchain_flags = "CC=/usr/lib/ccache/bin/clang CXX=/usr/lib/ccache/bin/clang++ LLVM=1"

makeopts=f"{makeflags} {toolchain_flags} CFLAGS=\"{cflags}\" CXXFLAGS=\"{cxxflags}\""

print(Logger.log("--------------------------------------------------------------------------------\n"))
print(Logger.log(f">> Moving into src dir: {src_dir}!"))

chdir_resp = os.chdir(src_dir)
if not chdir_resp == None:
    print(Logger.error(f"!! Failed to move into src dir: {src_dir}!"))
    exit(1)

print(Logger.log(">> Now running nconfig on current build tree."))
sleep(3)

nconfig_resp = os.system(f"make {makeopts} nconfig")
if not nconfig_resp == 0:
    print(Logger.error(f"!! `make nconfig` exited with error code: {nconfig_resp}!"))
    exit(1)

print(Logger.log(">> Now proceeding to build kernel."))
sleep(3)

kernelbuild_resp = os.system(f"make {makeopts} | tee {log_dir}/kernelbuild-{log_timestamp}.log")
if not kernelbuild_resp == 0:
    print(Logger.error(f"!! Kernel build failed with error code: {kernelbuild_resp}! (More info"))
    print(Logger.warning(f">> Check out kernel build log at: {log_dir}/kernelbuild-{log_timestamp}.log"))
    exit(1)

print(Logger.log(">> Now proceeding to install modules."))
sleep(3)

modinstall_resp = os.system(f"make {makeopts} modules_install | tee {log_dir}/modinstall-{log_timestamp}.log")
if not modinstall_resp == 0:
    print(Logger.error(f"!! Modules install failed with error code: {modinstall_resp}!"))
    print(Logger.warning(f">> Check out modules install log at: {log_dir}/modinstall-{log_timestamp}.log"))
    exit(1)

kinstall_resp = os.system(f"make {makeopts} install | tee {log_dir}/kinstall={log_timestamp}.log")
if not kinstall_resp == 0:
    print(Logger.error(f"!! Kernel install failed with error code: {kinstall_resp}!"))
    print(Logger.warning(f">> Check out kernel install log at: {log_dir}/kinstall-{log_timestamp}.log"))
    exit(1)

kver = os.popen("make -s kernelrelease").read();
print(Logger.success(f">> Built and installed kernel: {kver}"))

print(Logger.log(">> Finally, constructing initramfs with the help of Dracut!"))
sleep(3)

input(Logger.warning("\nWarning! If you already have an initramfs with the same kernel version, it will be overwritten. Press Enter to continue or Ctrl+C to abort."))

dracut_resp = os.system(f"dracut --force --logfile {log_dir}/dracut-{log_timestamp}.log --kver {kver}")
if not dracut_resp == 0:
    print(Logger.error(f"!! Dracut exited with error code: {dracut_resp}!"))
    print(Logger.warning(f">> Check out Dracut log at: {log_dir}/dracut-{log_timestamp}.log"))
    exit(1)

print(Logger.success(">> All done! You can now find the kernel and initramfs in the ESP directory."))

exit(0)