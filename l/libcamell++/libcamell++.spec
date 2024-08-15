%define soname 1

Name: libcamell++
Version: 1.2.5
Release: alt1

Summary: X-Window routines Library
License: GPLv3
Group: System/Libraries

URL: https://github.com/saahriktu/camell-
Source: %name-%version.tar

BuildRequires: libX11-devel gcc-c++

%description
C++ X11 input/output layer library

%package -n libcamell++%soname
Summary: X-Window routines Library
Group: System/Libraries

%description -n libcamell++%soname
C++ X11 input/output layer library

%package devel
Summary: Development files for C++ X11 input/output layer library
Group: Development/C

%description devel
This package provides header files to include and libraries to link with
C++ X11 input/output layer library

%prep
%setup

%build
%make

%install
libdir=%_libdir prefix=%_usr %makeinstall_std

%files -n libcamell++%soname
%_libdir/libcamell++.so.*

%files devel
%_includedir/camell++/camell++.hpp
%_libdir/libcamell++.so

%changelog
* Fri Jun 14 2024 Artem Kurashov <saahriktu@altlinux.org> 1.2.5-alt1
- Initial package.
