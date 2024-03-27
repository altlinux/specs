%define soname 0
%{?optflags_lto:%global optflags_lto %optflags_lto -ffat-lto-objects}
Name: libfcgi
Version: 2.4.2
Release: alt1

Summary: FastCGI library
License: OML
Group: System/Servers
URL: https://github.com/FastCGI-Archives/fcgi2
Source: %name-%version.tar

BuildRequires: gcc-c++ libstdc++-devel

%description
FastCGI is a language independent, scalable, open extension
to CGI that provides high performance without the limitations
of server specific APIs.

%package devel
Summary: FastCGI library
Group: System/Servers
Requires: %name = %EVR

%description devel
The %name-devel package contains libraries and header files for
developing applications that use %name.


%prep
%setup

%build
%autoreconf
%configure
%make

%install
%makeinstall

%files
%doc LICENSE.TERMS README.md
%_libdir/*.so.%soname
%_libdir/*.so.%soname.*
%exclude %_bindir/cgi-fcgi

%files devel
%_includedir/*.h
%_libdir/*.so
%_libdir/pkgconfig/*.pc
%exclude %_libdir/*.a

%changelog
* Wed Mar 27 2024 Anton Farygin <rider@altlinux.ru> 2.4.2-alt1
- 2.4.2 (Fixes: CVE-2012-6687)

* Mon Oct 25 2021 Anton Farygin <rider@altlinux.ru> 2.4.0-alt9
- NMU: fixed build with LTO

* Thu Feb 07 2013 Denis Smirnov <mithraen@altlinux.ru> 2.4.0-alt8
- exclude %_bindir/cgi-fcgi

* Fri Feb 01 2013 Denis Smirnov <mithraen@altlinux.ru> 2.4.0-alt7
- exclude static libs

* Tue May 22 2012 Denis Smirnov <mithraen@altlinux.ru> 2.4.0-alt6
- fix build

* Thu Oct 28 2010 Denis Smirnov <mithraen@altlinux.ru> 2.4.0-alt5.1
- rebuild (with the help of girar-nmu utility)

* Mon Jul 13 2009 Denis Smirnov <mithraen@altlinux.ru> 2.4.0-alt5
- fix building with new glibc

* Sun Mar 25 2007 Denis Smirnov <mithraen@altlinux.ru> 2.4.0-alt4
- add patch for recent php compatibility (lakostis@)

* Wed May 03 2006 Denis Smirnov <mithraen@altlinux.ru> 2.4.0-alt3
- fix build

* Mon Jan 02 2006 Denis Smirnov <mithraen@altlinux.ru> 2.4.0-alt2
- fixed x86_64 build, bug #8697

* Sun Nov 07 2005 LAKostis <lakostis at altlinux.ru> 2.4.0-alt1.1
- NMU;
- add missing requires for -devel.
- cleanup buildrequires.

* Sun Jun 19 2005 Denis Smirnov <mithraen@altlinux.ru> 2.4.0-alt1
- build

