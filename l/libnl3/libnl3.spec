%define _unpackaged_files_terminate_build 1
%define soname 200

Name: libnl3
Version: 3.10.0
Release: alt1

Summary: library for applications dealing with netlink sockets
License: LGPLv2.1
Group: System/Libraries
Url: https://github.com/thom311/libnl/
BuildRequires: glibc-kernheaders flex
# For tests
BuildRequires: libcheck-devel
BuildRequires: /proc /dev/kvm rpm-build-vm
Requires: libnl-common
Conflicts: libnl3-utils < 3.10.0

VCS: https://github.com/thom311/libnl 
Source: %name-%version.tar

%description
The libnl suite is a collection of libraries providing APIs to netlink protocol
based Linux kernel interfaces.  Netlink is a IPC mechanism primarly between the
kernel and user space processes. It was designed to be a more flexible
successor to ioctl to provide mainly networking related kernel configuration
and monitoring interfaces.

%package -n libnl-devel
Summary: header files for libnl, a netlink sockets library
Group: System/Libraries
Requires: %name = %EVR
Obsoletes: libnl3-devel < %version-%release

%description -n libnl-devel
libnl is a library for applications dealing with netlink sockets.

This package contains header files for libnl.

%package utils
Summary: Command line interface utils for libnl3
Group: System/Base
Provides: libnl-utils = %EVR

%description utils
This package contains various libnl3 utils and additional
libraries on which they depend

%package -n libnl-common
Summary: Common files for %name
Group: System/Libraries
Conflicts: libnl3 < 3.10.0
Conflicts: libnl3-utils < 3.10.0

%description -n libnl-common
This package contains common libnl3 files.


%prep
%setup

%build
%autoreconf
%configure \
	--disable-static \
	--disable-silent-rules
%make

%install
%makeinstall_std

%check
%make check-progs
vm-run make check

%files
%_libdir/libnl*.so.%soname
%_libdir/libnl*.so.%soname.*

%files -n libnl-common
%_libdir/libnl/
%config(noreplace) %_sysconfdir/libnl/

%files -n libnl-devel
%_libdir/libnl*.so
%_includedir/libnl3
%_pkgconfigdir/*.pc

%files utils
%_bindir/*
%_man8dir/*

%changelog
* Sun Jul 21 2024 Anton Farygin <rider@altlinux.ru> 3.10.0-alt1
- 3.9.0 -> 3.10.0
- the cli library was moved from utils to main libnl3 package
- configuration files was moved from the libnl3 to libnl-common package
- libnl-cli plugins was moved from the libnl3-utils to libnl-common package

* Sat Jan 27 2024 Anton Farygin <rider@altlinux.ru> 3.9.0-alt1
- 3.9.0

* Thu Oct 06 2022 Anton Farygin <rider@altlinux.ru> 3.7.0-alt1
- 3.7.0

* Wed Sep 18 2019 Anton Farygin <rider@altlinux.ru> 3.5.0-alt1
- 3.5.0

* Mon Oct 09 2017 Anton Farygin <rider@altlinux.ru> 3.4.0-alt2
- merge with sem@:
  * enabled tests
  * disabled silent rules

* Mon Oct 09 2017 Anton Farygin <rider@altlinux.ru> 3.4.0-alt1
- Updated to 3.4.0

* Wed Feb 10 2016 Mikhail Efremov <sem@altlinux.org> 3.2.27-alt1
- Updated to 3.2.27.

* Mon Mar 23 2015 Mikhail Efremov <sem@altlinux.org> 3.2.25-alt1
- Drop obsoleted patch.
- Updated to 3.2.25.

* Fri Feb 15 2013 Mikhail Efremov <sem@altlinux.org> 3.2.21-alt2
- Fix netlink.h.

* Wed Feb 13 2013 Mikhail Efremov <sem@altlinux.org> 3.2.21-alt1
- Renamed libnl3-devel -> libnl-devel.
- Added 'utils' subpackage.
- Updated to 3.2.21.

* Fri Dec 21 2012 Andriy Stepanov <stanv@altlinux.ru> 3.2.16-alt1
- Build for ALTLinux

