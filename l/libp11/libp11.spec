%define _customdocdir %_defaultdocdir/%name-%version

Name: libp11
Version: 0.2.7
Release: alt1.qa1

Summary: Library for using PKCS#11 modules
Group: System/Libraries
License: LGPLv2+

URL: http://www.opensc-project.org/libp11
Source: %name-%version.tar
Patch: %name-%version-%release.patch

Packager: Lebedev Sergey <barabashka@altlinux.org>

# Automatically added by buildreq on Fri Aug 28 2009
BuildRequires: doxygen libltdl7-devel libssl-devel xsltproc

%description
Libp11 is a library implementing a small layer on top of PKCS#11 API to
make using PKCS#11 implementations easier.

%package devel
Summary: Development files for %name
Group: Development/C++
Requires: %name = %version-%release
Requires: libssl-devel

%description devel
Development files for %name.

%prep
%setup -q
%patch -p1

%build
%autoreconf
%configure \
	--docdir=%_customdocdir \
	--disable-static \
	--enable-doc \
	--enable-api-doc
%make_build

%install
%makeinstall_std

%files
%dir %_customdocdir
%_customdocdir/README
%_customdocdir/NEWS
%_libdir/*.so.*
#%%_defaultdocdir/%%name-%%version

%files devel
%dir %_customdocdir
%_customdocdir/api
%_customdocdir/wiki
%_libdir/*.so
%_includedir/*
%_pkgconfigdir/%name.pc


%changelog
* Thu Nov 25 2010 Igor Vlasenko <viy@altlinux.ru> 0.2.7-alt1.qa1
- rebuild using girar-nmu to require/provide setversion 
  by request of mithraen@

* Tue Jun 29 2010 Alexey I. Froloff <raorn@altlinux.org> 0.2.7-alt1
- [0.2.7]

* Wed Sep 09 2009 Alexey I. Froloff <raorn@altlinux.org> 0.2.6-alt2
- devel subpackage should require libssl-devel

* Fri Aug 28 2009 Alexey I. Froloff <raorn@altlinux.org> 0.2.6-alt1
- [0.2.6] (closes: #21289)
- Developer docs moved to devel subpackage
- Packaged API documentation

* Wed Dec 03 2008 Lebedev Sergey <barabashka@altlinux.org> 0.2.4-alt1
- initial build

