%define oname uriparser
Name: liburiparser
Version: 0.8.5
Release: alt1

Summary: A strictly RFC 3986 compliant URI parsing library

License: BSD
Group: System/Libraries
Url: https://uriparser.github.io/

Packager: Vitaly Lipatov <lav@altlinux.ru>

# Source-url: https://github.com/uriparser/uriparser/archive/uriparser-%version.tar.gz
Source: %name-%version.tar

BuildRequires: gcc-c++ libcpptest-devel doxygen graphviz

%description
uriparser is a strictly RFC 3986 compliant URI parsing library.
uriparser is cross-platform, fast, supports Unicode.

%package devel
Summary: Header files for uriparser
Group: Development/Other
Requires: %name = %version-%release

%description devel
Header files for uriparser.

%prep
%setup

%build
%autoreconf
%configure --disable-static
%make_build

%install
touch doc/html/FIXME.map
%makeinstall_std

%files
%doc AUTHORS ChangeLog
%_bindir/uriparse
%_libdir/lib*.so.*

%files devel
%_docdir/%oname/
%_libdir/lib*.so
%_includedir/%oname/
%_pkgconfigdir/*

%changelog
* Wed Feb 07 2018 Vitaly Lipatov <lav@altlinux.ru> 0.8.5-alt1
- new version (0.8.5) with rpmgs script
- change URL and source URL

* Fri Apr 22 2016 Vitaly Lipatov <lav@altlinux.ru> 0.8.4-alt1
- new version 0.8.4 (with rpmrb script)

* Sat Aug 15 2015 Vitaly Lipatov <lav@altlinux.ru> 0.8.2-alt1
- new version 0.8.2 (with rpmrb script)

* Wed Apr 02 2014 Vitaly Lipatov <lav@altlinux.ru> 0.8.0-alt1
- new version 0.8.0 (with rpmrb script)

* Sat Sep 14 2013 Vitaly Lipatov <lav@altlinux.ru> 0.7.9-alt1
- new version 0.7.9 (with rpmrb script)

* Tue Aug 27 2013 Vitaly Lipatov <lav@altlinux.ru> 0.7.8-alt1
- new version 0.7.8 (with rpmrb script)

* Sun Apr 14 2013 Dmitry V. Levin (QA) <qa_ldv@altlinux.org> 0.7.5-alt1.qa2
- NMU: rebuilt for debuginfo.

* Thu Nov 25 2010 Igor Vlasenko <viy@altlinux.ru> 0.7.5-alt1.qa1
- rebuild using girar-nmu to require/provide setversion 
  by request of mithraen@

* Sat Mar 07 2009 Vitaly Lipatov <lav@altlinux.ru> 0.7.5-alt1
- new version 0.7.5 (with rpmrb script)

* Thu Sep 04 2008 Vitaly Lipatov <lav@altlinux.ru> 0.7.2-alt1
- new version 0.7.2 (with rpmrb script)

* Tue Apr 29 2008 Vitaly Lipatov <lav@altlinux.ru> 0.7.1-alt1
- new version 0.7.1 (with rpmrb script)

* Thu Apr 10 2008 Vitaly Lipatov <lav@altlinux.ru> 0.7.0-alt1
- new version 0.7.0 (with rpmrb script)

* Wed Feb 27 2008 Vitaly Lipatov <lav@altlinux.ru> 0.6.4-alt1
- new version 0.6.4 (with rpmrb script)

* Mon Dec 24 2007 Vitaly Lipatov <lav@altlinux.ru> 0.6.1-alt1
- new version 0.6.1 (with rpmrb script)

* Sat Oct 13 2007 Vitaly Lipatov <lav@altlinux.ru> 0.6.0-alt1
- new version 0.6.0 (with rpmrb script)

* Tue Sep 18 2007 Vitaly Lipatov <lav@altlinux.ru> 0.5.2-alt1
- new version 0.5.2 (with rpmrb script)

* Sun Aug 05 2007 Vitaly Lipatov <lav@altlinux.ru> 0.5.0-alt1
- new version 0.5.0 (with rpmrb script)

* Sun Aug 05 2007 Vitaly Lipatov <lav@altlinux.ru> 0.4.1-alt1
- initial build for ALT Linux Sisyphus (spec from PLD)

