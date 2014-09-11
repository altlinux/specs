%define origname netwib

Name: libnetwib
Version: 5.39.0
Release: alt1

Summary: Functions for network programs
License: GPL
Group: System/Libraries

Url: http://www.laurentconstantin.com/en/netw/netwib/
Source: http://www.laurentconstantin.com/common/netw/netwib/download/v5/%origname-%version-src.tgz
Source1: html.tar

# Automatically added by buildreq on Wed Feb 15 2006
BuildRequires: libnet2-devel libpcap-devel

%description
Netwib provides most functions needed by network programs. Its objective is
to let programmers easily create network programs. This library provides
features for Ethernet, IPv4, IPv6, UDP, TCP, ICMP, ARP, and RARP protocols.
It supports spoofing, sniffing, client, and server creation. Furthermore,
netwib contains high level functions dealing with data handling.

This package contains the header files, the static library and development
documentation.

%package doc
Summary: Documentation for %name library
Group: Development/Documentation
BuildArch: noarch

%package devel
Summary: Headers and libraries for %name
Group: Development/C
Requires: %name = %version-%release

%description doc
The %name-doc package contains documntation of %name library

%description devel
The %name-devel package contains the header files and libraries needed
to develop programs that use the %name library.

%prep
%setup -n %origname-%version-src
tar -xf %SOURCE1

%build
cd src
./genemake
%make libnetwib.so

%install
rm -f doc/gpl.txt
cd src
%makeinstall INSTINCLUDE=%buildroot%_includedir \
	INSTLIB=%buildroot%_libdir \
	INSTBIN=%buildroot%_bindir \
	INSTMAN3=%buildroot%_man3dir \
	installso

%files
%doc doc/*.txt README.TXT
%_libdir/libnetwib*.so
%_man3dir/netwib*

%files doc
%doc html/*

%files devel
%_includedir/netwib*
%_bindir/netwib*-config

%changelog
* Thu Sep 11 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 5.39.0-alt1
- Version 5.39.0

* Mon Apr 22 2013 Repocop Q. A. Robot <repocop@altlinux.org> 5.34.0-alt2.qa2
- NMU (by repocop). See http://www.altlinux.org/Tools/Repocop
- applied repocop fixes:
  * arch-dep-package-consists-of-usr-share for libnetwib-doc

* Sun Apr 14 2013 Dmitry V. Levin (QA) <qa_ldv@altlinux.org> 5.34.0-alt2.qa1
- NMU: rebuilt for debuginfo.

* Wed Nov 10 2010 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 5.34.0-alt2
- Rebuilt for soname set-versions

* Wed Nov 04 2009 Igor Vlasenko <viy@altlinux.ru> 5.34.0-alt1.1
- NMU (by repocop): the following fixes applied:
  * post_ldconfig for libnetwib
  * postun_ldconfig for libnetwib

* Fri Apr 21 2006 Vladimir V Kamarzin <vvk@altlinux.ru> 5.34.0-alt1
- new version (5.34.0)
- Removed netwib-5.33.0-alt.patch (merged with upstream)

* Mon Mar 20 2006 Vladimir V Kamarzin <vvk@altlinux.ru> 5.33.0-alt2
- Fixed linking and build with --as-needed
- Docs moved to separate package

* Wed Feb 15 2006 Vladimir V Kamarzin <vvk@altlinux.ru> 5.33.0-alt1
- Initial build for Sisyphus (adopted spec from Dries Verachtert <dries at
  ulyssis.org>)
