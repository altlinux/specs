Name: libudfread
Version: 1.2.0
Release: alt1

Summary: Library for reading UDF from raw devices and image files
License: LGPLv2.1
Group: System/Libraries
Url: https://code.videolan.org/videolan/libudfread

Source0: %name-%version.tar
Patch0: %name-%version-alt.patch

BuildRequires: meson

%description
Library for reading UDF from raw devices and image files

%package -n libudfread3
Summary: Library for reading UDF from raw devices and image files
Group: System/Libraries

%package devel
Summary: Development files for libudfread
Group: Development/C

%description -n libudfread3
Library for reading UDF from raw devices and image files
This package contains libudfread shared library.

%description devel
This package contains libraries and signature files for
developing applications that use libudfread.

%prep
%setup
%patch0 -p1

%build
%meson
%meson_build

%install
%meson_install


%files -n libudfread3
%_libdir/libudfread.so.3*

%files devel
%_includedir/*
%_libdir/libudfread.so
%_pkgconfigdir/*.pc

%changelog
* Fri Aug 29 2025 Sergey Bolshakov <sbolshakov@altlinux.org> 1.2.0-alt1
- 1.2.0 released

* Sun Oct 03 2021 Anton Farygin <rider@altlinux.ru> 1.1.2-alt2
- disabled static library build

* Wed Apr 14 2021 Anton Farygin <rider@altlinux.org> 1.1.2-alt1
- 1.1.2

* Mon Nov 30 2020 Anton Farygin <rider@altlinux.ru> 1.1.1-alt1
- 1.1.1

* Wed Jul 01 2020 Anton Farygin <rider@altlinux.ru> 1.1.0-alt1
- 1.1.0

* Wed Jun 13 2018 Anton Farygin <rider@altlinux.ru> 1.0.0-alt3
- rebuilt for aarch64

* Mon Jun 04 2018 Anton Farygin <rider@altlinux.ru> 1.0.0-alt2
- fixed cflags in pkgconfig

* Mon Jun 04 2018 Anton Farygin <rider@altlinux.ru> 1.0.0-alt1
- first build for ALT

