Name: mconfig
Version: 1.2.0
Release: alt1
License: GPLv2
Url: https://github.com/erdizz/mconfig
Source: %name-%version.tar
Group: System/Libraries
Summary: C++ library for working with configuration files
Packager: Slava Dubrovskiy <dubrsl@altlinux.ru>

BuildRequires: gcc-c++ libmary-devel libpargen-devel libscruffy-devel

%description
C++ library for working with configuration files

%package -n lib%name
Summary: C++ library for working with configuration files
Group: System/Libraries
Provides: lib%name = %version-%release

%description -n lib%name
C++ library for working with configuration files

%package -n lib%name-devel
Summary: Development package that includes the lib%name header files
Group: Development/C++
Requires: lib%name = %version-%release

%description -n lib%name-devel
The devel package contains the include files

%prep
%setup

%build
./autogen.sh
%configure --disable-static
%make_build

%install
%make DESTDIR=%buildroot install

%check
#make test

%files -n lib%name
%doc AUTHORS COPYING ChangeLog NEWS README
%_libdir/lib*.so.*

%files -n lib%name-devel
%_includedir/*
%_libdir/*so
%_pkgconfigdir/*

%changelog
* Thu Nov 24 2011 Slava Dubrovskiy <dubrsl@altlinux.org> 1.2.0-alt1
- New version

* Wed Jul 27 2011 Slava Dubrovskiy <dubrsl@altlinux.org> 1.0-alt1
- Build for ALT

