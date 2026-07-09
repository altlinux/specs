%define soname 0
%define netsurf %_datadir/netsurf-buildsystem

Name: libwapcaplet
Version: 0.4.3
Release: alt1

Summary: String internment library
License: MIT
Group: System/Libraries

Url: https://www.netsurf-browser.org/projects/libwapcaplet

# https://download.netsurf-browser.org/libs/releases/
Source: %name-%version.tar

BuildRequires: gcc-c++ netsurf-buildsystem

%description
LibWapcaplet is a string internment library, written in C. It provides
reference counted string interment and rapid string comparison functionality.
It was developed as part of the NetSurf project and is available for use by
other software under the MIT licence.

%package devel
Summary: Development files for %name
Group: Development/C
%description devel
The %name-devel package contains libraries and header files for
developing applications that use %name.

%package -n %name%soname
Group: System/Libraries
Summary: %name library
%description -n %name%soname
%name library.

%prep
%setup

%build
%install
install -d %buildroot
make install PREFIX=%buildroot NSSHARED=%netsurf COMPONENT_TYPE=lib-shared INCLUDEDIR=%_includedir LIBDIR=%_libdir
#fixed prefix in .pc file
subst 's|%buildroot|/usr|' %buildroot%_libdir/pkgconfig/%name.pc
sed -i 's/\/\/usr\//\//g' %buildroot%_libdir/pkgconfig/%name.pc

%files devel
%doc COPYING README
%_includedir/%name
%_libdir/pkgconfig/%name.pc
%_libdir/%name.so

%files -n %name%soname
%_libdir/%name.so.%soname
%_libdir/%name.so.%{soname}.*

%changelog
* Thu Jul 09 2026 Aleksandr Shamaraev <shad@altlinux.org> 0.4.3-alt1
- Initial build for ALT Linux.

