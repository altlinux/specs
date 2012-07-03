%define oname uriparser
Name: liburiparser
Version: 0.7.5
Release: alt1.qa1

Summary: A strictly RFC 3986 compliant URI parsing library

License: BSD
Group: System/Libraries
Url: http://uriparser.sourceforge.net/

Packager: Vitaly Lipatov <lav@altlinux.ru>

Source: http://prdownloads.sourceforge.net/uriparser/%oname-%version.tar.bz2

# Automatically added by buildreq on Sat Mar 07 2009
BuildRequires: gcc-c++ libcpptest-devel

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
%setup -q -n %oname-%version

%build
# reconf failed with AM_PROG_CC_C_
#%__autoreconf
%configure --disable-static --disable-doc
%make_build

%install
%makeinstall_std

%files
%doc doc/*.{htm,txt} AUTHORS ChangeLog
%_libdir/lib*.so.*

%files devel
%_libdir/lib*.so
%_includedir/%oname/
%_pkgconfigdir/*

%changelog
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

