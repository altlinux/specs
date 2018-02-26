Packager: Denis Smirnov <mithraen@altlinux.ru>

Name: libfcgi
Version: 2.4.0
Release: alt6

Summary: FastCGI library
License: BSD-like
Group: System/Servers

Url: http://www.fastcgi.org/
Source: fcgi-%version.tar.gz

Patch: libfcgi-php-changes.patch
Patch2: libfcgi.cstdio.patch
Patch3: libfcgi.build.patch

# Automatically added by buildreq on Sun Jun 19 2005
BuildRequires: gcc-c++ libstdc++-devel

%description
FastCGI library

%package devel
Summary: FastCGI library
License: BSD-like
Group: System/Servers
Requires: %name = %version-%release

%description devel
FastCGI library

%prep
%setup -q -n fcgi-%version
%patch -p1
%patch2 -p2
%patch3 -p2

%build
touch NEWS AUTHORS ChangeLog
%autoreconf
%configure
# SMP incompatible build
make

%install
%makeinstall

%files devel
%_includedir/*.h
%_libdir/*.so

%files
%_libdir/*.so.*

%doc LICENSE.TERMS README

%changelog
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

