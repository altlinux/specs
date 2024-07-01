%define _unpackaged_files_terminate_build 1
%def_with zfs
%def_with lz4
%def_enable uv
%def_disable backtrace

Name: libraft
Version: 0.22.1
Release: alt1

Summary: Fully asynchronous C implementation of the Raft consensus protocol.
License: LGPL-3.0-only WITH LGPL-3.0-linking-exception
Group: Development/C

Url: https://github.com/cowsql/%name
Source: %name-%version.tar
Patch: %name-%version.patch

%{?_enable_uv:BuildRequires: pkgconfig(libuv) >= 1.18.0}
%{?_with_lz4:BuildRequires: pkgconfig(liblz4) >= 1.7.1}
%{?_enable_backtrace:BuildRequires: libbacktrace-devel}
BuildRequires: btrfs-progs xfsprogs
%{?_with_zfs:BuildRequires: zfs-utils}
%{?_enable_uv:BuildRequires: libuv-devel >= 1.18.0}

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
%configure \
 	%{subst_with lz4} \
	%{subst_enable uv} \
        %{subst_enable backtrace} \
	--disable-static --disable-fixture
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
* Mon May 06 2024 Nadezhda Fedorova <fedor@altlinux.org> 0.22.1-alt1
- change upstream
- new version v0.22.1

* Thu Aug 03 2023 Alexey Shabalin <shaba@altlinux.org> 0.17.1-alt1
- new version 0.17.1

* Mon Apr 11 2022 Alexey Shabalin <shaba@altlinux.org> 0.13.0-alt1
- new version 0.13.0

* Wed Jan 26 2022 Alexey Shabalin <shaba@altlinux.org> 0.11.3-alt1
- new version 0.11.3

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
