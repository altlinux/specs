Name: libnl3
Version: 3.2.16
Release: alt1

Summary: library for applications dealing with netlink sockets
License: LGPL
Group: System/Libraries
Url: http://www.infradead.org/~tgr/libnl/
Packager: Andriy Stepanov <stanv@altlinux.ru>
BuildRequires: glibc-kernheaders flex

Source: %name-%version.tar

%description
The libnl suite is a collection of libraries providing APIs to netlink protocol
based Linux kernel interfaces.  Netlink is a IPC mechanism primarly between the
kernel and user space processes. It was designed to be a more flexible
successor to ioctl to provide mainly networking related kernel configuration
and monitoring interfaces.

%package devel
Summary: header files for libnl, a netlink sockets library
Group: System/Libraries
Requires: %name = %version

%description devel
libnl is a library for applications dealing with netlink sockets.

This package contains header files for libnl.

%prep
%setup

%build
%autoreconf -fisv
%configure
%make

%install
%makeinstall

%files
%_sbindir/*
%_libdir/libnl*.so.*
%_libdir/libnl/cli/*/*.so
%_sysconfdir/libnl/pktloc
%_sysconfdir/libnl/classid
%_man8dir/*

%files devel
%_libdir/libnl*.so
%_includedir/libnl3
%_pkgconfigdir/*.pc

%changelog
* Fri Dec 21 2012 Andriy Stepanov <stanv@altlinux.ru> 3.2.16-alt1
- Build for ALTLinux

