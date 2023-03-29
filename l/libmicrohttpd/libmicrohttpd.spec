Name: libmicrohttpd
Version: 0.9.76
Release: alt1

Summary: Library providing compact API and implementation of an HTTP/1.1 webserver
License: LGPL-2.1-or-later
Group: System/Libraries
Url: http://www.gnu.org/software/libmicrohttpd/
Vcs: https://gnunet.org/libmicrohttpd.git
Source: %name-%version.tar

BuildRequires: libgnutls-devel >= 2.12.20
# For tests
BuildRequires: curl libcurl-devel

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
# starting with curl-7.82.0 test fails with: curl_easy_perform failed: `Out of memory'
sed -ri '/^\s+TEST_HTTPS_SNI/ s,=.+$,=,' src/testcurl/https/Makefile.am

%build
%autoreconf
%configure \
	--disable-static \
	--disable-doc \
	--disable-examples \
	--enable-gcc-hardening \
	--enable-linker-hardening
%make_build

%install
%makeinstall_std

%check
%make check

%files
%doc AUTHORS COPYING README NEWS ChangeLog
%_libdir/*.so.*

%files devel
%_includedir/*
%_libdir/*.so
%_pkgconfigdir/*

%changelog
* Wed Mar 29 2023 Sergey Bolshakov <sbolshakov@altlinux.ru> 0.9.76-alt1
- 0.9.76 released (fixes: CVE-2023-27371)

* Fri Apr 15 2022 Sergey Bolshakov <sbolshakov@altlinux.ru> 0.9.75-alt2
- disable broken https_sni test

* Mon Dec 27 2021 Alexey Shabalin <shaba@altlinux.org> 0.9.75-alt1
- new version 0.9.75
- add check section

* Sat Apr 24 2021 Evgeny Sinelnikov <sin@altlinux.org> 0.9.72-alt1
- new version 0.9.72

* Sun Jan 03 2021 Alexey Shabalin <shaba@altlinux.org> 0.9.71-alt1
- new version 0.9.71

* Thu Sep 12 2019 Alexey Shabalin <shaba@altlinux.org> 0.9.66-alt1
- new version 0.9.66

* Tue Mar 26 2019 Alexey Shabalin <shaba@altlinux.org> 0.9.63-alt1
- 0.9.63

* Fri Aug 31 2018 Alexey Shabalin <shaba@altlinux.org> 0.9.59-alt1
- 0.9.59
- disable build doc

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
