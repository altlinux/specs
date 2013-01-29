Name: ploop
Version: 1.6
Release: alt1
Group: System/Base
License: GNU GPL
Summary: Ploop tools
URL: http://wiki.openvz.org/Ploop
Packager: Viacheslav Dubrovskyi <dubrsl@altlinux.org>
Source: %name-%version.tar
Patch: %name-%version-alt.patch

Requires: parted
BuildRequires: libxml2-devel libe2fs-devel

%description
This package contains tools to work with ploop devices and images.

%package -n lib%name
Summary: ploop library
Group: System/Base
%description -n lib%name
Parallels loopback (ploop) block device API library

%package -n lib%name-devel-static
Summary: Static ploop library
Group: System/Base
%description -n lib%name-devel-static
Static version of ploop library

%package -n lib%name-devel
Summary: Headers for development with ploop library
Group: System/Base
%description -n lib%name-devel
Headers of ploop library

%prep
%setup
%patch -p1

%build
%make LIBDIR=%_libdir all

%install
mkdir -p %buildroot/%_sbindir
make DESTDIR=%buildroot LIBDIR=%_libdir install

%files
/sbin/*
%_sbindir/*
%_man8dir/*

%files -n lib%name
%_libdir/libploop.so
%_lockdir/%name

%files -n lib%name-devel-static
%_libdir/libploop.a

%files -n lib%name-devel
%_includedir/%name

%changelog
* Tue Jan 29 2013 Slava Dubrovskiy <dubrsl@altlinux.org> 1.6-alt1
- New version

* Thu Jun 14 2012 Slava Dubrovskiy <dubrsl@altlinux.org> 1.4-alt1
- New version

* Wed Apr 18 2012 Slava Dubrovskiy <dubrsl@altlinux.org> 1.2-alt1
- New version

* Sat Mar 24 2012 Slava Dubrovskiy <dubrsl@altlinux.org> 1.1-alt1
- Update to bb3948d45daf3e30d0e05f20d1442376237ac49d

* Tue Mar 13 2012 Slava Dubrovskiy <dubrsl@altlinux.org> 1.0-alt1
- build for ALT

* Tue Mar 13 2012 Kir Kolyshkin <kir@openvz.org> 1.0-1
- initial version
