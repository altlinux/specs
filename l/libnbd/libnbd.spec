# SPDX-License-Identifier: GPL-2.0-only
%define _unpackaged_files_terminate_build 1
%define _stripped_files_terminate_build 1
%set_verify_elf_method strict

%define sover 0

Name: libnbd
Version: 1.17.5
Release: alt1
Summary: NBD client library in userspace
License: LGPL-2.1-or-later
Group: Networking/File transfer
Url: https://gitlab.com/nbdkit/libnbd

Source: %name-%version.tar
BuildRequires: bash-completion
BuildRequires: gcc-c++
BuildRequires: hardlink
BuildRequires: libfuse3-devel
BuildRequires: libgnutls-devel
BuildRequires: liburing-devel
BuildRequires: libxml2-devel
BuildRequires: ocaml
BuildRequires: perl-podlators

%description
%summary.

%package -n libnbd%sover
Summary: %name system library
Group: System/Libraries

%description -n libnbd%sover
%summary.

%package devel
Summary: Development files for %name
Group: Development/C
Requires: libnbd%sover = %EVR

%description devel
%summary.

%prep
%setup

%build
%autoreconf
%configure \
    --disable-static \
    --disable-golang \
    --disable-ocaml \
    --disable-python \
    %nil
%make_build

%install
%makeinstall_std
hardlink -v %buildroot

%check
%make_build check

%files
%_bindir/nbd*
%_man1dir/nbd*.1*
%_datadir/bash-completion/completions/*

%files -n libnbd%sover
%_libdir/libnbd.so.%sover
%_libdir/libnbd.so.%sover.*

%files devel
%_includedir/libnbd.h
%_libdir/libnbd.so
%_pkgconfigdir/libnbd.pc
%_man1dir/libnbd-*.1*
%_man3dir/*.3*

%changelog
* Sun Sep 10 2023 Vitaly Chikunov <vt@altlinux.org> 1.17.5-alt1
- Update to v1.17.5 (2023-09-08).

* Mon Aug 07 2023 Vitaly Chikunov <vt@altlinux.org> 1.17.3-alt1
- Update to v1.17.3 (2023-08-04).

* Sun Jul 23 2023 Vitaly Chikunov <vt@altlinux.org> 1.17.2-alt1
- First import v1.17.2 (2023-07-14).
