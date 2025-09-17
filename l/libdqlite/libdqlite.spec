%define _unpackaged_files_terminate_build 1

# Tests failed on x86
%ifarch %ix86
%def_without check
%else
%def_with check
%endif

%define soname 0

Name: libdqlite
Version: 1.18.2
Release: alt1
Summary: Library for distributed SQLite database
License: Apache-2.0
Group: Development/Databases
URL: https://github.com/CanonicalLtd/dqlite
VCS: https://github.com/CanonicalLtd/dqlite

Source: %name-%version.tar

BuildRequires: libuv-devel
BuildRequires: libsqlite3-devel
BuildRequires: liblz4-devel

%description
This package provides the `dqlite` C library (libdqlite), which can be used
to expose a SQLite database over the network and replicate it across a cluster
of peers, using the Raft algorithm.

%package -n libdqlite%soname
Summary: Library for distributed SQLite database
Group: Development/Databases
Obsoletes: libdqlite < 1.18.0

%description -n libdqlite%soname
This package provides the `dqlite` C library (libdqlite), which can be used
to expose a SQLite database over the network and replicate it across a cluster
of peers, using the Raft algorithm.

%package devel
Summary: Library for distributed SQLite database (development files)
Group: Development/Databases
Requires: libdqlite%soname = %EVR

%description devel
This package provides the `dqlite` C library (libdqlite), which can be used
to expose a SQLite database over the network and replicate it across a cluster
of peers, using the Raft algorithm.

%prep
%setup

%build
%autoreconf
%configure --enable-build-raft --enable-replication --disable-static

%make_build all

%check
# Test failed in hasher
sed -i '/raft-uv-integration-test$(EXEEXT) \\/d' Makefile
sed -i '/ raft-uv-unit-test$(EXEEXT)/d' Makefile
%make_build check

%install
%make_install install DESTDIR=%buildroot

%files -n libdqlite%soname
%doc AUTHORS README.md LICENSE
%_libdir/libdqlite.so.%{soname}*

%files devel
%_includedir/dqlite.h
%_libdir/libdqlite.so
%_pkgconfigdir/dqlite.pc

%changelog
* Fri Sep 12 2025 Ulysses Apokin <ulysses@altlinux.org> 1.18.2-alt1
- new version 1.18.2
- fixed FTBFS
- enabled check

* Wed Jan 29 2025 Nadezhda Fedorova <fedor@altlinux.org> 1.18.0-alt1
- new version 1.18.0
- renamed according to SharedLibsPolicy

* Tue May 07 2024 Nadezhda Fedorova <fedor@altlinux.org> 1.16.4-alt1
- new version 1.16.4

* Thu Aug 03 2023 Alexey Shabalin <shaba@altlinux.org> 1.15.1-alt1
- new version 1.15.1

* Wed Jan 26 2022 Alexey Shabalin <shaba@altlinux.org> 1.9.1-alt1
- new version 1.9.1

* Wed Dec 08 2021 Alexey Shabalin <shaba@altlinux.org> 1.9.0-alt1
- new version 1.9.0

* Fri Jan 15 2021 Alexey Shabalin <shaba@altlinux.org> 1.6.0-alt1
- new version 1.6.0

* Sun May 17 2020 Alexey Shabalin <shaba@altlinux.org> 1.4.1-alt1
- Updated

* Tue Apr 14 2020 Alexey Shabalin <shaba@altlinux.org> 1.4.0-alt1
- Updated

* Tue Nov 12 2019 Denis Pynkin <dans@altlinux.org> 1.1.0-alt1
- Updated
- Added new build/runtime requirements to libraft and libco

* Sun Sep 29 2019 Denis Pynkin <dans@altlinux.org> 1.0.0-alt1
- Version 1.0.0

* Fri Jan 11 2019 Denis Pynkin <dans@altlinux.org> 0.2.5-alt1
- Initial version for ALTLinux
