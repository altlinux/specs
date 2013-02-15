Name: libnl3
Version: 3.2.21
Release: alt2

Summary: library for applications dealing with netlink sockets
License: LGPL
Group: System/Libraries
Url: http://www.infradead.org/~tgr/libnl/
Packager: Andriy Stepanov <stanv@altlinux.ru>
BuildRequires: glibc-kernheaders flex

Source: %name-%version.tar
Patch1: Declare-nl_object-in-the-netlink.h.patch

%description
The libnl suite is a collection of libraries providing APIs to netlink protocol
based Linux kernel interfaces.  Netlink is a IPC mechanism primarly between the
kernel and user space processes. It was designed to be a more flexible
successor to ioctl to provide mainly networking related kernel configuration
and monitoring interfaces.

%package -n libnl-devel
Summary: header files for libnl, a netlink sockets library
Group: System/Libraries
Requires: %name = %version-%release
Provides: %name-devel = %version-%release
Obsoletes: %name-devel < %version-%release

%description -n libnl-devel
libnl is a library for applications dealing with netlink sockets.

This package contains header files for libnl.

%package utils
Summary: Command line interface utils for libnl3
Group: System/Base
Requires: %name = %version-%release

%description utils
This package contains various libnl3 utils and additional
libraries on which they depend

%prep
%setup
%patch1 -p1

%build
%autoreconf
%configure --disable-static
%make

%install
%makeinstall_std

%files
%_libdir/libnl*.so.*
%config(noreplace) %_sysconfdir/libnl/
%exclude %_libdir/libnl-cli*.so.*

%files -n libnl-devel
%_libdir/libnl*.so
%_includedir/libnl3
%_pkgconfigdir/*.pc

%files utils
%_sbindir/*
%_libdir/libnl-cli*.so.*
%_libdir/libnl/
%_man8dir/*
%exclude %_libdir/libnl/cli/cls/*.la
%exclude %_libdir/libnl/cli/qdisc/*.la

%changelog
* Fri Feb 15 2013 Mikhail Efremov <sem@altlinux.org> 3.2.21-alt2
- Fix netlink.h.

* Wed Feb 13 2013 Mikhail Efremov <sem@altlinux.org> 3.2.21-alt1
- Renamed libnl3-devel -> libnl-devel.
- Added 'utils' subpackage.
- Updated to 3.2.21.

* Fri Dec 21 2012 Andriy Stepanov <stanv@altlinux.ru> 3.2.16-alt1
- Build for ALTLinux

