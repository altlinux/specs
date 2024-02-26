%define _unpackaged_files_terminate_build 1
%define _stripped_files_terminate_build 1
%set_verify_elf_method strict

Name: libntirpc
Version: 5.0
Release: alt1
Summary: New Transport Independent RPC Library
Group: System/Libraries
License: BSD-3-Clause
Url: https://github.com/nfs-ganesha/ntirpc
Vcs: https://github.com/nfs-ganesha/ntirpc.git
Source: %name-%version.tar
Patch: %name-%version.patch
BuildRequires(pre): rpm-macros-cmake
BuildRequires: cmake ninja-build
BuildRequires: libkrb5-devel
BuildRequires: libnsl2-devel
BuildRequires: libuserspace-rcu-devel

# libtirpc has /etc/netconfig, most machines probably have it anyway
# for NFS client
Requires: libtirpc

%description
This package contains a new implementation of the original libtirpc,
transport-independent RPC (TI-RPC) library for NFS-Ganesha. It has
the following features not found in libtirpc:
 1. Bi-directional operation
 2. Full-duplex operation on the TCP (vc) transport
 3. Thread-safe operating modes
 3.1 new locking primitives and lock callouts (interface change)
 3.2 stateless send/recv on the TCP transport (interface change)
 4. Flexible server integration support
 5. Event channels (remove static arrays of xprt handles, new EPOLL/KEVENT
    integration)

%package devel
Summary: Development headers for %name
Requires: %name = %EVR
Group: Development/C

%description devel
Development headers and auxiliary files for developing with %name.

%prep
%setup
%patch -p1

%build
%add_optflags %(getconf LFS_CFLAGS)
%cmake \
    -DTIRPC_EPOLL=1 \
    -DUSE_GSS=ON \
    -GNinja

%cmake_build

%install
%cmake_install

%files
%_libdir/libntirpc.so.*
%doc COPYING
%doc NEWS README

%files devel
%_libdir/libntirpc.so
%_includedir/ntirpc/
%_pkgconfigdir/libntirpc.pc

%changelog
* Sat Feb 17 2024 Alexey Shabalin <shaba@altlinux.org> 5.0-alt1
- 5.0

* Sat Aug 14 2021 Vitaly Lipatov <lav@altlinux.ru> 3.5-alt1
- new version 3.5 (with rpmrb script)

* Thu Jun 03 2021 Arseny Maslennikov <arseny@altlinux.org> 3.3-alt1.1
- NMU: spec: adapted to new cmake macros.

* Sun Sep 20 2020 Vitaly Lipatov <lav@altlinux.ru> 3.3-alt1
- new version 3.3 (with rpmrb script)

* Sun Sep 20 2020 Vitaly Lipatov <lav@altlinux.ru> 3.2-alt1
- new version 3.2 (with rpmrb script)

* Sun Sep 20 2020 Vitaly Lipatov <lav@altlinux.ru> 1.8.0-alt1
- new version 1.8.0 (with rpmrb script)
- add BR: libuserspace-rcu-devel

* Fri May 17 2019 Vitaly Lipatov <lav@altlinux.ru> 1.7.3-alt1
- new version 1.7.3 (with rpmrb script)

* Wed Mar 27 2019 Vitaly Lipatov <lav@altlinux.ru> 1.7.2-alt1
- new version 1.7.2 (with rpmrb script)

* Sun Nov 04 2018 Vitaly Lipatov <lav@altlinux.ru> 1.7.1-alt1
- new version 1.7.1 (with rpmrb script)

* Sun Sep 30 2018 Vitaly Lipatov <lav@altlinux.ru> 1.7.0-alt1
- new version 1.7.0 (with rpmrb script)

* Sat Jun 09 2018 Vitaly Lipatov <lav@altlinux.ru> 1.6.2-alt1
- new version 1.6.2 (with rpmrb script)

* Fri Jul 28 2017 Vitaly Lipatov <lav@altlinux.ru> 1.5.3-alt1
- new version 1.5.3 (with rpmrb script)

* Sun Jun 11 2017 Vitaly Lipatov <lav@altlinux.ru> 1.5.2-alt1
- new version 1.5.2 (with rpmrb script)

* Sat Sep 24 2016 Vitaly Lipatov <lav@altlinux.ru> 1.4.1-alt1
- new version 1.4.1 (with rpmrb script)

* Thu Jul 21 2016 Vitaly Lipatov <lav@altlinux.ru> 1.4.0-alt2
- cleanup install

* Thu Jul 21 2016 Vitaly Lipatov <lav@altlinux.ru> 1.4.0-alt1
- initial build for ALT Linux Sisyphus

