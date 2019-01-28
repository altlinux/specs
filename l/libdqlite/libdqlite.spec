Name: libdqlite
Version: 0.2.5
Release: alt1
Summary: Library for distributed SQLite database
License: Apache v2
Group: Development/Databases
URL: https://github.com/CanonicalLtd/dqlite

Source0: %name-%version.tar

BuildRequires: libuv-devel
# Patched libsqlite3 version is required
BuildRequires: liblxd_sqlite3-devel

%define _unpackaged_files_terminate_build 1

%description
This package provides the `dqlite` C library (libdqlite), which can be used
to expose a SQLite database over the network and replicate it across a cluster
of peers, using the Raft algorithm.

%package devel
Summary: Library for distributed SQLite database (development files)
Group: Development/Databases
Requires: %name = %version-%release

%description devel
This package provides the `dqlite` C library (libdqlite), which can be used
to expose a SQLite database over the network and replicate it across a cluster
of peers, using the Raft algorithm.

%prep
%setup -q -n %name-%version

%build
%autoreconf
%configure --enable-replication --disable-static

%make_build all

%install
%make_install install DESTDIR=%buildroot

%files
%doc AUTHORS README.md LICENSE
%_libdir/%name.so.*

%files devel
%_includedir/dqlite.h
%_libdir/%name.so
%_pkgconfigdir/dqlite.pc

%changelog
* Fri Jan 11 2019 Denis Pynkin <dans@altlinux.org> 0.2.5-alt1
- Initial version for ALTLinux
