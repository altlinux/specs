Name: libbluray
Version: 0.9.2
Release: alt1
Summary: BD library

Group: System/Libraries
License: LGPL
Url: http://www.videolan.org/developers/libbluray.html

Source: %name-%version-%release.tar

BuildRequires: fontconfig-devel libfreetype-devel libxml2-devel

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

%build
%autoreconf
%configure --disable-bdjava --disable-static
%make_build

%install
%makeinstall

%files
%_libdir/*.so.*

%files devel
%_includedir/*
%_libdir/*.so
%_libdir/pkgconfig/*

%files utils
%_bindir/*

%changelog
* Mon Jan 11 2016 Sergey Bolshakov <sbolshakov@altlinux.ru> 0.9.2-alt1
- 0.9.2 released

* Tue Oct 06 2015 Sergey Bolshakov <sbolshakov@altlinux.ru> 0.9.0-alt1
- 0.9.0 released

* Tue Aug 04 2015 Sergey Bolshakov <sbolshakov@altlinux.ru> 0.8.1-alt1
- 0.8.1 released

* Wed Apr 08 2015 Sergey Bolshakov <sbolshakov@altlinux.ru> 0.7.0-alt1
- 0.7.0 released

* Wed Dec 10 2014 Sergey Bolshakov <sbolshakov@altlinux.ru> 0.6.2-alt1
- 0.6.2 released

* Tue May 27 2014 Sergey Bolshakov <sbolshakov@altlinux.ru> 0.6.0-alt1
- 0.6.0 released

* Tue Sep 17 2013 Sergey Bolshakov <sbolshakov@altlinux.ru> 0.4.0-alt1
- 0.4.0 released

* Tue Apr 30 2013 Sergey Bolshakov <sbolshakov@altlinux.ru> 0.3.0-alt1
- 0.3.0 released

* Sat Feb 23 2013 Sergey Bolshakov <sbolshakov@altlinux.ru> 0.2.3-alt2
- rebuilt with java 1.7.0

* Tue Oct 16 2012 Sergey Bolshakov <sbolshakov@altlinux.ru> 0.2.3-alt1
- 0.2.3 released

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
