%define _customdocdir %_defaultdocdir/%name-%version
%define oname libp11
%define sover 2

Name: %oname-%sover
Version: 0.2.9
Release: alt1.git20131021

Summary: Library for using PKCS#11 modules
Group: System/Libraries
License: LGPLv2+

URL: http://www.opensc-project.org/libp11
Source: %name-%version.tar

# Automatically added by buildreq on Fri Aug 28 2009
BuildRequires: doxygen libltdl7-devel libssl-devel xsltproc

%description
Libp11 is a library implementing a small layer on top of PKCS#11 API to
make using PKCS#11 implementations easier.

%package -n %oname-devel
Summary: Development files for %name
Group: Development/C++
Requires: %name = %version-%release
Requires: libssl-devel

%description -n %oname-devel
Development files for %name.

%prep
%setup

%build
%autoreconf
%configure \
	--docdir=%_customdocdir \
	--disable-static \
	--enable-doc \
	--enable-api-doc \
	--with-apidocdir
%make_build

%install
%makeinstall_std

install -d %buildroot%_customdocdir
cp -fR doc/api.out/html %buildroot%_customdocdir/api
cp -fR examples %buildroot%_customdocdir/

%files
%dir %_customdocdir
%_customdocdir/README
%_customdocdir/NEWS
%_libdir/*.so.*
#%%_defaultdocdir/%%name-%%version

%files -n %oname-devel
%dir %_customdocdir
%_customdocdir/api
%_customdocdir/examples
%_libdir/*.so
%_includedir/*
%_pkgconfigdir/%oname.pc


%changelog
* Fri Sep 12 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.2.9-alt1.git20131021
- Version 0.2.9

* Sun Apr 14 2013 Dmitry V. Levin (QA) <qa_ldv@altlinux.org> 0.2.7-alt1.qa2
- NMU: rebuilt for debuginfo.

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

