Name: libmary
Version: 1.2.0
Release: alt1
License: GPLv2
Url: https://github.com/erdizz/libmary
Source: %name-%version.tar
Group: System/Libraries
Summary: LibMary is a portability, multithreading, and basic utility library for high-performance network servers written in C++
Packager: Slava Dubrovskiy <dubrsl@altlinux.ru>

BuildRequires: gcc-c++ glib2-devel

%description
LibMary is a portability, multithreading, and basic utility library for
high-performance network servers written in C++

%package devel
Summary: Development package that includes the %name header files
Group: Development/C++
Requires: %name = %version-%release

%description devel
The devel package contains the %name library and the include files

%prep
%setup

%build
./autogen.sh
%configure --disable-static
%make_build

%install
%make DESTDIR=%buildroot install


%check
make -C tests

%files
%_libdir/%{name}*.so.*
%doc AUTHORS COPYING ChangeLog NEWS README

%files devel
%doc docs
%_libdir/*so
%_includedir/*
%_pkgconfigdir/*

%changelog
* Thu Nov 24 2011 Slava Dubrovskiy <dubrsl@altlinux.org> 1.2.0-alt1
- New version

* Wed Jul 27 2011 Slava Dubrovskiy <dubrsl@altlinux.org> 1.0-alt1
- Build for ALT
