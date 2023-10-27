# SPDX-License-Identifier: GPL-2.0-only
%define _unpackaged_files_terminate_build 1
%define _stripped_files_terminate_build 1
%set_verify_elf_method strict

Name: ubdsrv
Version: 1.1
Release: alt1
Summary: ublk: userspace block device driver
License: GPL-2.0-only and LGPL-2.1-only and MIT
Group: System/Kernel and hardware
Url: https://github.com/ming1/ubdsrv
# https://docs.kernel.org/block/ublk.html

Source: %name-%version.tar
# gnutls is unsupported yet: https://github.com/ming1/ubdsrv/issues/59
BuildRequires: gcc-c++
BuildRequires: libgnutls-devel
BuildRequires: liburing-devel
%{?!_without_check:%{?!_disable_check:
BuildRequires: rpm-build-vm
}}

%description
This is the userspace daemon part(ublksrv) of the ublk framework, the
other part is ublk driver [userspace] which supports multiple queue.

%package -n libublksrv-devel
Summary: Development files for %name
Group: Development/C
Requires: %name = %EVR

%description -n libublksrv-devel
%summary.

%prep
%setup
echo "echo '%version'" > utils/genver.sh
sed -i 's!/usr/bin/chown!chown!' utils/ublk_*.sh

%build
%add_optflags %(getconf LFS_CFLAGS)
%autoreconf
%configure --disable-static
%make_build

%install
%makeinstall_std

%check
# Test suite is not usable: https://github.com/ming1/ubdsrv/issues/60
./ublk --version
truncate -s 256M disk.img
vm-run --kvm=cond --sbin --cpu=2 --modules=ublk_drv --heredoc <<EOF
./ublk features
./ublk list
./ublk add -t loop -f disk.img
./ublk add -t null
ls -l /dev/ublk*
# badblocks does not report exit status but writes list of blocks to stdout.
badblocks -w -s /dev/ublkb0 2048 | grep -c . && exit 2 || echo 'No corruption'
badblocks -w -s /dev/ublkb1 1024 | grep -c . && echo 'No false positive' || exit 3
./ublk del -n 0
./ublk del -n 1
EOF

%files
%doc COPYING COPYING.LGPL LICENSE README.rst demo_*.c
%_sbindir/ublk*
%_libdir/libublksrv.so.0*

%files -n libublksrv-devel
%_includedir/ublk*
%_libdir/libublksrv.so
%_pkgconfigdir/ublksrv.pc

%changelog
* Fri Oct 27 2023 Vitaly Chikunov <vt@altlinux.org> 1.1-alt1
- First import v1.1 (2023-10-28).
