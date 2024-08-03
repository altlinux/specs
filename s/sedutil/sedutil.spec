# SPDX-License-Identifier: GPL-2.0-only
%define _unpackaged_files_terminate_build 1
%define _stripped_files_terminate_build 1
%set_verify_elf_method strict

Name: sedutil
Version: 1.20.0
Release: alt1
Summary: DTA sedutil - Self-encrypting drive management software
License: GPL-3.0-or-later
Group: System/Kernel and hardware
Url: https://github.com/Drive-Trust-Alliance/sedutil

Source: %name-%version.tar

BuildRequires: gcc-c++

%description
sedutil - The Drive Trust Alliance Self-Encrypting Drive (SED) Utility.

This program [together with the Pre-Boot Authorization (PBA) image]
allows you to enable the locking on SEDs that comply with the TCG OPAL
2.00 standard on BIOS machines.

** This package provides the sedutil-cli and linuxpba binaries, but not
   the PBA image itself nor any integration into the boot process.

** You must be an administrator/root to run the host management program.

** In Linux, `libata.allow_tpm` must be set to 1 for SATA-based drives,
   including NGFF/M.2 SATA drives. Either adding `libata.allow_tpm=1`
   to the kernel flags at boot time or changing the contents of
   `/sys/module/libata/parameters/allow_tpm` from "0" to "1" on a running
   system if possible will accomplish this. NVMe drives do not need
   this parameter.

*** Standby System Sleep State (S3) is not supported.

%prep
%setup
sed -i 's/tarball/%version-%release/' linux/GitVersion.sh

%build
%add_optflags %(getconf LFS_CFLAGS)
%autoreconf
%configure
%make_build

%install
%makeinstall_std

%check
%buildroot%_sbindir/sedutil-cli -v || :
%buildroot%_sbindir/sedutil-cli -v |& grep -Px '%name version : \Q%version-%release\E'
# Not much is auto-testable, QEMU does not support OPAL drives.
# Scan is tested on unsupported NVME drive:
#   # sedutil-cli --scan
#   Scanning for Opal compliant disks
#   /dev/nvme0 No  Viper M.2 VP4100                         EGFM13.0
#   No more disks present ending scan

%files
%define _customdocdir %_docdir/%name
%doc README.md linux/PSIDRevert_LINUX.txt Common/*.txt
%_sbindir/sedutil-cli
%_sbindir/linuxpba
%_man8dir/sedutil-cli.8*

%changelog
* Sat Aug 03 2024 Vitaly Chikunov <vt@altlinux.org> 1.20.0-alt1
- First import 1.20.0-4-g3ddb986 (2024-02-10).
