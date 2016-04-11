Name: libepoxy
Version: 1.3.1
Release: alt1

Summary: Direct Rendering Manager runtime library
Group: System/Libraries
License: MIT
Url: http://github.com/anholt/libepoxy

Source: %url/releases/download/v%version/%name-%version.tar.bz2

BuildRequires: libGL-devel libEGL-devel python3 xorg-util-macros

%description
A library for handling OpenGL function pointer management

%package devel
Summary: Development files for libepoxy
Group: Development/C
Requires: %name = %version-%release

%description devel
This package contains libraries and header files for
developing applications that use %name

%prep
%setup

%build
%autoreconf
%configure \
	--disable-static
%make_build

%install
%makeinstall_std

%check
%make check

%files
%_libdir/%name.so.*
%doc README.md

%files devel
%_includedir/epoxy/
%_libdir/%name.so
%_pkgconfigdir/epoxy.pc

%changelog
* Mon Apr 11 2016 Yuri N. Sedunov <aris@altlinux.org> 1.3.1-alt1
- 1.3.1

* Sat Jul 19 2014 Valery Inozemtsev <shrek@altlinux.ru> 1.2-alt1
- initial release

