Name: libbluray
Version: 1.3.4
Release: alt1

Summary: BD library
License: LGPLv2.1
Group: System/Libraries
Url: http://www.videolan.org/developers/libbluray.html

Source: %name-%version-%release.tar

BuildRequires: fontconfig-devel libfreetype-devel libxml2-devel libudfread-devel

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
%configure --disable-bdjava-jar --disable-static
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
* Wed Nov 30 2022 Sergey Bolshakov <sbolshakov@altlinux.ru> 1.3.4-alt1
- 1.3.4 released

* Wed Sep 21 2022 Sergey Bolshakov <sbolshakov@altlinux.ru> 1.3.3-alt1
- 1.3.3 released

* Fri Aug 05 2022 Sergey Bolshakov <sbolshakov@altlinux.ru> 1.3.2-alt1
- 1.3.2 released

* Wed Mar 16 2022 Sergey Bolshakov <sbolshakov@altlinux.ru> 1.3.1-alt1
- 1.3.1 released

* Mon Sep 20 2021 Sergey Bolshakov <sbolshakov@altlinux.ru> 1.3.0-alt1
- 1.3.0 released

* Tue Jan 26 2021 Sergey Bolshakov <sbolshakov@altlinux.ru> 1.2.1-alt1
- 1.2. released

* Wed Jul 01 2020 Anton Farygin <rider@altlinux.ru> 1.2.0-alt1
- 1.2.0

* Mon Sep 30 2019 Sergey Bolshakov <sbolshakov@altlinux.ru> 1.0.2-alt2
- fix ftbfs by actually disable bdjava jar build

* Mon Jun 04 2018 Anton Farygin <rider@altlinux.ru> 1.0.2-alt1
- 1.0.2

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
