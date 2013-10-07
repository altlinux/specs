Name: ploop
Version: 1.9
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
make DESTDIR=%buildroot LIBDIR=%_libdir TMPFILESDIR=%_tmpfilesdir install

%files
/sbin/*
%_sbindir/*
%_man8dir/*

%files -n lib%name
%_libdir/libploop.so.*
%_lockdir/%name
%_tmpfilesdir/*

%files -n lib%name-devel-static
%_libdir/libploop.a

%files -n lib%name-devel
%_libdir/libploop.so
%_includedir/%name

%changelog
* Sun Oct 20 2013 Slava Dubrovskiy <dubrsl@altlinux.org> 1.9-alt1
- New version

* Mon Aug 05 2013 Slava Dubrovskiy <dubrsl@altlinux.org> 1.8-alt1
- New version

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
