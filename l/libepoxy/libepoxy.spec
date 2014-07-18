Summary: Direct Rendering Manager runtime library
Name: libepoxy
Version: 1.2
Release: alt1
License: MIT
Group: System/Libraries
URL: http://github.com/anholt/libepoxy

Source0: %name-%version.tar.gz

BuildRequires: libGL-devel libEGL-devel python3 xorg-util-macros

%description
A library for handling OpenGL function pointer management

%package devel
Summary: Development files for libepoxy
Group: Development/C

%description devel
This package contains libraries and header files for
developing applications that use %name

%prep
%setup -q

%build
%autoreconf
%configure \
	--disable-static
%make_build

%install
%make DESTDIR=%buildroot install

%check
%make check

%files
%_libdir/%name.so.0*

%files devel
%_includedir/epoxy
%_libdir/%name.so
%_pkgconfigdir/*.pc

%changelog
* Sat Jul 19 2014 Valery Inozemtsev <shrek@altlinux.ru> 1.2-alt1
- initial release

