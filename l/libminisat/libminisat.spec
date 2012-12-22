
Name: libminisat
Version: 2.2.0
Release: alt2

Packager: Michael Pozhidaev <msp@altlinux.ru>
License: BSD style
URL: http://minisat.se

Summary: The library for Boolean satisfiability problem solving
Group: System/Libraries

Source: %name-%version.tar.gz

BuildRequires: gcc-c++ zlib-devel

%package devel
Summary: C/C++ development files for %name
Group: Development/C
Requires: %name = %version-%release

%package devel-static
Summary: The static library with %name functions
Group: Development/C
Requires: %name-devel = %version-%release

%description
This package contains libminisat library as Deepsolver engine for SAT solving. You can find
original library at http://minisat.se. 

%description devel
C/C++ development files for lib%name.

%description devel-static
The static library with %name functions.

%prep
%setup -q
%build
./autogen.sh
%configure
%make_build

%install
make DESTDIR=%buildroot install 
%__rm -f %buildroot%_libdir/lib%name.la

%files
%doc AUTHORS COPYING README
%_libdir/%name-*.so*

%files devel
%_includedir/minisat.h
%_libdir/%name.so

%files devel-static
%_libdir/%name.a

%changelog
* Sat Dec 22 2012 Michael Pozhidaev <msp@altlinux.ru> 2.2.0-alt2
- Variable value assumption support added

* Sun Oct 28 2012 Michael Pozhidaev <msp@altlinux.ru> 2.2.0-alt1
- Initial package

