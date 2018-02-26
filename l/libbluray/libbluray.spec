Name: libbluray
Version: 0.2.2
Release: alt1
Summary: BD library

Group: System/Libraries
License: LGPL
Url: http://www.videolan.org/developers/libbluray.html

Source: %name-%version-%release.tar

BuildRequires: /proc
BuildRequires: ant java-1.6.0-openjdk-devel libxml2-devel

%description
%summary

%package devel
Summary: Development files for %name
Group: Development/C
Requires: %name = %version-%release

%package utils
Summary: Utilities using %name
Group: File tools
Requires: %name = %version-%release

%description devel
This package contains the headers and libraries for libbluray development.

%description utils
This package contains various utilities using libbluray library.

%prep
%setup
sed -i s,noinst_PROGRAMS,bin_PROGRAMS, src/examples/Makefile.am

%build
%autoreconf
%configure --with-jdk=/usr/lib/jdk --enable-bdjava
%make_build

%install
%makeinstall
install -pm0644 -D src/.libs/libbluray.jar %buildroot%_datadir/libbluray/libbluray.jar

%files
%_libdir/*.so.*
%_datadir/libbluray

%files devel
%_includedir/*
%_libdir/*.so
%_libdir/pkgconfig/*

%files utils
%_bindir/*

%changelog
* Wed Mar 21 2012 Sergey Bolshakov <sbolshakov@altlinux.ru> 0.2.2-alt1
- 0.2.2 released

* Mon Dec 12 2011 Sergey Bolshakov <sbolshakov@altlinux.ru> 0.2.1-alt2
- examples packaged (closes: #26693)

* Fri Dec 02 2011 Sergey Bolshakov <sbolshakov@altlinux.ru> 0.2.1-alt1
- 0.2.1 released

* Wed Oct 26 2011 Sergey Bolshakov <sbolshakov@altlinux.ru> 0.2-alt0.3
- updated from git.e037110f

* Fri Aug 26 2011 Sergey Bolshakov <sbolshakov@altlinux.ru> 0.2-alt0.2
- updated from git.8e5d241e

* Wed May 11 2011 Sergey Bolshakov <sbolshakov@altlinux.ru> 0.2-alt0.1
- updated from git

* Thu Oct 14 2010 Sergey Bolshakov <sbolshakov@altlinux.ru> 0.1-alt0.1
- initial
