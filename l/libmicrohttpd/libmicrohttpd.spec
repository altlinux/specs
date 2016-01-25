Name: libmicrohttpd
Version: 0.9.44
Release: alt2

Summary: Library providing compact API and implementation of an HTTP/1.1 webserver
License: LGPL
Group: System/Libraries
Url: http://www.gnu.org/software/libmicrohttpd/

Source: %name-%version-%release.tar

BuildRequires: makeinfo
BuildRequires: libcurl-devel libgcrypt-devel libgnutls-devel libssl-devel zlib-devel

%description
Library providing compact API and implementation of an HTTP/1.1 webserver

%package devel
Summary: Development files for %name
Group: Development/C++
Requires: %name = %version-%release

%description devel
This package contains the headers and libraries for libmicrohttpd development.

%prep
%setup

%build
%autoreconf
%configure --disable-static
%make_build

%install
%makeinstall

%files
#%doc AUTHORS COPYING README ChangeLog
%_libdir/*.so.*

%files devel
%_includedir/*
%_libdir/*.so
%_libdir/pkgconfig/*
%_infodir/*.info*
%_man3dir/*

%changelog
* Mon Jan 25 2016 Sergey Bolshakov <sbolshakov@altlinux.ru> 0.9.44-alt2
- add makeinfo to buildreq

* Tue Oct 06 2015 Sergey Bolshakov <sbolshakov@altlinux.ru> 0.9.44-alt1
- 0.9.44

* Sat Jan 10 2015 Sergey Bolshakov <sbolshakov@altlinux.ru> 0.9.39-alt1
- 0.9.39

* Tue Jun 24 2014 Sergey Bolshakov <sbolshakov@altlinux.ru> 0.9.36-alt1
- 0.9.36

* Fri Aug 19 2011 Sergey Bolshakov <sbolshakov@altlinux.ru> 0.9.13-alt1
- 0.9.13 released

* Sat Dec 04 2010 Sergey Bolshakov <sbolshakov@altlinux.ru> 0.9.3-alt1
- 0.9.3 released

* Wed Nov 10 2010 Sergey Bolshakov <sbolshakov@altlinux.ru> 0.9.2-alt1
- 0.9.2 released

* Mon Jul 26 2010 Sergey Bolshakov <sbolshakov@altlinux.ru> 0.9-alt1
- initial build for ALT Linux
