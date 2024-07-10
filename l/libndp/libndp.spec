%define _unpackaged_files_terminate_build 1

Name: libndp
Version: 1.9
Release: alt1

Summary: Library for Neighbor Discovery Protocol
License: LGPLv2.1+
Group: System/Libraries
URL: http://libndp.org/
Vcs: https://github.com/jpirko/libndp.git
Source: %name-%version.tar
Patch: %name-%version-%release.patch

%description
This package contains a library which provides a wrapper
for IPv6 Neighbor Discovery Protocol.

%package utils
Summary: Utils for %name
License: LGPLv2.1+
Group: System/Base
Requires: %name = %version-%release

%description utils
This package contains a tool named ndptool for sending and receiving
NDP messages.

%package devel
Summary: Development files for %name
Group: Development/C
Requires: %name = %version-%release

%description devel
This package contains libraries and header files for
developing applications that use %name.

%prep
%setup
%patch -p1

%build
%autoreconf
%configure \
	--disable-static
%make_build

%install
%makeinstall_std

%files
%_libdir/*.so.*

%files utils
%_bindir/*
%_man8dir/*

%files devel
%_includedir/*
%_libdir/*.so
%_libdir/pkgconfig/*.pc

%changelog
* Wed Jul 10 2024 Mikhail Efremov <sem@altlinux.org> 1.9-alt1
- Updated to 1.9.

* Mon May 24 2021 Mikhail Efremov <sem@altlinux.org> 1.8-alt1
- Added Vcs tag.
- Don't use rpm-build-licenses.
- Updated to 1.8.

* Wed Jun 27 2018 Mikhail Efremov <sem@altlinux.org> 1.7-alt1
- Updated to 1.7.

* Mon May 23 2016 Mikhail Efremov <sem@altlinux.org> 1.6-alt1
- Updated to 1.6.

* Tue Aug 05 2014 Mikhail Efremov <sem@altlinux.org> 1.4-alt1
- Updated to 1.4.

* Mon Jul 14 2014 Mikhail Efremov <sem@altlinux.org> 1.3-alt1
- Updated to 1.3.

* Thu Feb 06 2014 Mikhail Efremov <sem@altlinux.org> 1.2-alt1
- Patch from upstream git:
  + fix [cppcheck] Undefined behavior
- Initial build,

