Name: mycpp
Version: 1.2.0
Release: alt1
License: GPLv2
Url: https://github.com/erdizz/mycpp
Source: %name-%version.tar
Group: System/Libraries
Summary: C++ utility library
Packager: Slava Dubrovskiy <dubrsl@altlinux.ru>

BuildRequires: gcc-c++ libmary-devel

%description
C++ utility library

%package -n lib%name
Summary: C++ utility library
Group: System/Libraries
Provides: lib%name = %version-%release

%description -n lib%name
C++ utility library

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
%_libdir/lib*.so.*
%doc AUTHORS AUTHORS NEWS README ChangeLog

%files -n lib%name-devel
%doc docs/*
%_includedir/*
%_libdir/*so
%_pkgconfigdir/*

%changelog
* Thu Nov 24 2011 Slava Dubrovskiy <dubrsl@altlinux.org> 1.2.0-alt1
- New version

* Wed Jul 27 2011 Slava Dubrovskiy <dubrsl@altlinux.org> 1.0-alt1
- Build for ALT
