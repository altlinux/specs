Name: liblog4cpp
Version: 1.1.1
Release: alt3
Summary: Log for C++
Group: Development/C++

License: LGPL-2.1
Url: http://log4cpp.sourceforge.net/
Source: %name-%version.tar

BuildRequires: gcc-c++ doxygen

%description
Log for C++ is a library of classes for flexible logging to files, syslog,
and other destinations. It is modeled after the Log for Java library and
stays as close to its API as is reasonable.

%package devel
Summary: development tools for Log for C++
Group: Development/C++
Requires: %name = %version

%description devel
The %name-devel package contains the static libraries and header files
needed for development with %name.


%prep
%setup

%build
./autogen.sh
%configure 	--enable-doxygen --disable-static

%make_build

%install
%makeinstall

%files
%_libdir/lib*.so.*
%doc AUTHORS COPYING INSTALL NEWS README THANKS ChangeLog

%files devel
%_includedir/*
%_mandir/man3/*
%_bindir/log4cpp-config
%_libdir/lib*.so
%_libdir/pkgconfig/*
%_datadir/aclocal/*.m4

%changelog
* Wed Aug 25 2021 Alexei Takaseev <taf@altlinux.org> 1.1.1-alt3
- Disable static
- Fix License:

* Wed Jun 03 2015 Alexei Takaseev <taf@altlinux.org> 1.1.1-alt2
- rebuild with gcc-c++ 5.1

* Thu Apr 30 2015 Alexei Takaseev <taf@altlinux.org> 1.1.1-alt1
- Initial build for ALT
