%define soname 1

Name: libglibutil

Version: 1.0.79
Release: alt0.1
Summary: Library of glib utilities
License: BSD
Group: System/Libraries
Url: https://github.com/sailfishos/libglibutil
Source: %name-%version.tar

BuildRequires: pkgconfig
BuildRequires: pkgconfig(glib-2.0)

%description
Provides glib utility functions and macros

%package -n %{name}%{soname}
Summary: Library of glib utilities
Group: System/Libraries

%description -n %{name}%{soname}
Provides glib utility functions and macros

%package devel
Summary: Development library for %name
Group: Development/C

%description devel
This package contains the development library for %name.

%prep
%setup

%build
make %_smp_mflags CFLAGS="%optflags" LIBDIR=%_libdir KEEP_SYMBOLS=1 release pkgconfig

%install
make LIBDIR=%_libdir DESTDIR=%buildroot install-dev

%check
make -C test test

%files -n %{name}%{soname}
%_libdir/%name.so.*
%doc LICENSE README

%files devel
%dir %_includedir/gutil
%_libdir/pkgconfig/*.pc
%_libdir/%name.so
%_includedir/gutil/*.h

%changelog
* Thu Aug 15 2024 L.A. Kostis <lakostis@altlinux.ru> 1.0.79-alt0.1
- 1.0.75->1.0.79.

* Mon Dec 18 2023 L.A. Kostis <lakostis@altlinux.ru> 1.0.75-alt0.1
- 1.0.74->1.0.75.

* Wed Sep 13 2023 L.A. Kostis <lakostis@altlinux.ru> 1.0.74-alt0.1
- 1.0.70->1.0.74.

* Fri Jun 30 2023 L.A. Kostis <lakostis@altlinux.ru> 1.0.70-alt0.1
- 1.0.70.

* Sat Apr 29 2023 L.A. Kostis <lakostis@altlinux.ru> 1.0.69-alt0.1
- 1.0.69.

* Thu Mar 30 2023 L.A. Kostis <lakostis@altlinux.ru> 1.0.68-alt0.1
- Initial build for ALTLinux.


