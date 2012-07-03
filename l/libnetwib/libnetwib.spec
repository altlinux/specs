Packager: Repocop Q. A. Robot <repocop@altlinux.org>
%define origname netwib

Name: libnetwib
Version: 5.34.0
Release: alt2

Summary: Functions for network programs
License: GPL
Group: System/Libraries

Url: http://www.laurentconstantin.com/en/netw/netwib/
Source: http://www.laurentconstantin.com/common/netw/netwib/download/v5/%origname-%version-src.tgz
#Patch0: netwib-5.33.0-alt.patch

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
%setup -q -n %origname-%version-src
#%%patch0 -p1

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
%_libdir/libnetwib*.so
%_man3dir/netwib*

%files doc
%doc doc README.TXT

%files devel
%_includedir/netwib*
%_bindir/netwib*-config

%changelog
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
