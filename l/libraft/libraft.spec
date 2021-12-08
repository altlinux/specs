%define _unpackaged_files_terminate_build 1
%def_with zfs

Name: libraft
Version: 0.11.2
Release: alt1

Summary: Fully asynchronous C implementation of the Raft consensus protocol.
License: Apache-2.0
Group: Development/C

Url: https://github.com/canonical/raft
Source: %name-%version.tar
Patch: %name-%version.patch

BuildRequires: pkgconfig(libuv) >= 1.18.0
BuildRequires: pkgconfig(liblz4) >= 1.7.1
BuildRequires: btrfs-progs xfsprogs
%{?_with_zfs:BuildRequires: zfs-utils}

%description
Fully asynchronous C implementation of the Raft consensus protocol.
The library has modular design: its core part implements only the core Raft
algorithm logic, in a fully platform independent way. On top of that, a
pluggable interface defines the I/O implementation for networking (send/receive
RPC messages) and disk persistence (store log entries and snapshots).

%package devel
Summary: Fully asynchronous C implementation of the Raft consensus protocol (development files)
Group: Development/C
Requires: %name = %version-%release

%description devel
Fully asynchronous C implementation of the Raft consensus protocol.
The library has modular design: its core part implements only the core Raft
algorithm logic, in a fully platform independent way. On top of that, a
pluggable interface defines the I/O implementation for networking (send/receive
RPC messages) and disk persistence (store log entries and snapshots).

%prep
%setup
%patch -p1

%build
%autoreconf
%configure --disable-static --disable-fixture
%make_build

%install
%makeinstall_std

%files
%doc AUTHORS README.md LICENSE
%_libdir/%name.so.*

%files devel
%_includedir/raft.h
%_includedir/raft/
%_libdir/%name.so
%_pkgconfigdir/raft.pc

%changelog
* Thu Dec 09 2021 Alexey Shabalin <shaba@altlinux.org> 0.11.2-alt1
- new version 0.11.2

* Tue Aug 17 2021 Michael Shigorin <mike@altlinux.org> 0.9.25-alt2
- introduced zfs knob (on by default)
- spec cleanup

* Fri Jan 15 2021 Alexey Shabalin <shaba@altlinux.org> 0.9.25-alt1
- new version 0.9.25

* Tue Apr 14 2020 Alexey Shabalin <shaba@altlinux.org> 0.9.17-alt1
- Update to 0.9.17

* Wed Nov 13 2019 Denis Pynkin <dans@altlinux.org> 0.9.9-alt1
- Update

* Sun Sep 29 2019 Denis Pynkin <dans@altlinux.org> 0.9.6-alt1
- Initial version for ALTLinux
