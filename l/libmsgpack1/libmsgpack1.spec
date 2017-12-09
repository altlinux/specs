%define oname msgpack
Name: libmsgpack1
Version: 1.4.1
Release: alt2

Summary: Binary-based efficient object serialization library

License: Boost Software License, Version 1.0
Group: System/Libraries
Url: http://msgpack.org

Packager: Vitaly Lipatov <lav@altlinux.ru>

# Source-url: https://github.com/msgpack/msgpack-c/releases/download/cpp-%version/%oname-%version.tar.gz
Source: %name-%version.tar
Patch: msgpack-fix-int-float-test.patch

BuildRequires: gcc-c++ >= 4.8

# for %%check
BuildRequires: libgtest-devel
BuildRequires: zlib-devel

Provides: %oname = %version-%release
Obsoletes: %oname

%description
MessagePack is a binary-based efficient object serialization
library. It enables to exchange structured objects between many
languages like JSON. But unlike JSON, it is very fast and small.

%package devel
Summary: Libraries and header files for %name
Group: Development/C++
Requires: %name = %version-%release

Conflicts: libmsgpack-devel

%description devel
Libraries and header files for %name

%prep
%setup
#patch0 -p1 -b .fix-int-float-test
# set correct soname
%__subst "s|SOVERSION 2 VERSION 2.0.0|SOVERSION 1 VERSION 1.0.0|g" CMakeLists.txt
%__subst "s|2:0:0|1:0:0|g" src/Makefile*

%build
%autoreconf
%configure --disable-static
%make_build

%check
make check

%install
%makeinstall_std

%files
%doc AUTHORS COPYING ChangeLog LICENSE_1_0.txt NOTICE README README.md
%_libdir/libmsgpackc.so.1
%_libdir/libmsgpackc.so.1.0.0

%files devel
%_includedir/msgpack.*
%_includedir/msgpack/
%_libdir/libmsgpackc.so
%_pkgconfigdir/msgpack.pc

%changelog
* Sat Dec 09 2017 Vitaly Lipatov <lav@altlinux.ru> 1.4.1-alt2
- build as libmsgpack1 with soname 1.0.0 for autobahn-cpp build

* Tue Jul 26 2016 Vitaly Lipatov <lav@altlinux.ru> 1.4.1-alt1
- new version 1.4.1 (with rpmrb script)

* Mon Jan 11 2016 Vitaly Lipatov <lav@altlinux.ru> 1.3.0-alt1
- new version 1.3.0 (with rpmrb script)

* Sun Nov 15 2015 Vitaly Lipatov <lav@altlinux.ru> 1.2.0-alt1
- new version 1.2.0 (with rpmrb script)

* Sun Nov 15 2015 Vitaly Lipatov <lav@altlinux.ru> 1.1.0-alt1
- new version 1.1.0 (with rpmrb script)

* Sun Nov 15 2015 Vitaly Lipatov <lav@altlinux.ru> 0.5.9-alt2
- initial manual build for ALT Linux

* Mon Sep 21 2015 Igor Vlasenko <viy@altlinux.ru> 0.5.9-alt1_4
- update to new release by fcimport

* Wed Sep 10 2014 Igor Vlasenko <viy@altlinux.ru> 0.5.9-alt1_1
- update to new release by fcimport

* Thu Jun 26 2014 Igor Vlasenko <viy@altlinux.ru> 0.5.8-alt1_2
- update to new release by fcimport

* Thu Jan 23 2014 Igor Vlasenko <viy@altlinux.ru> 0.5.8-alt1_1
- update to new release by fcimport

* Thu Oct 10 2013 Igor Vlasenko <viy@altlinux.ru> 0.5.7-alt1_5
- update to new release by fcimport

* Tue Aug 27 2013 Igor Vlasenko <viy@altlinux.ru> 0.5.7-alt1_4
- update to new release by fcimport

* Fri Apr 26 2013 Igor Vlasenko <viy@altlinux.ru> 0.5.7-alt1_3
- initial fc import

