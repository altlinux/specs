Name: libp11
Version: 0.3.0
Release: alt1

Summary: Library for using PKCS#11 modules
Group: System/Libraries
License: LGPLv2+

Url: https://github.com/OpenSC/libp11/wiki
Source: %name-%version.tar
Patch: libp11-err-remove-state.patch

# Automatically added by buildreq on Fri Aug 28 2009
BuildRequires: doxygen libltdl7-devel libssl-devel xsltproc

BuildRequires: openssl-devel
BuildRequires: pkgconfig

# needed for testsuite
BuildRequires: softhsm opensc

%description
Libp11 is a library implementing a small layer on top of PKCS#11 API
to make using PKCS#11 implementations easier.

%package devel
Summary: Development files for %name
Group: Development/C++
Requires: %name = %version-%release
Requires: libssl-devel

%description devel
Development files for %name.

%prep
%setup
%patch -p1 -b .test-suite

%build
%autoreconf
%configure --disable-static --enable-api-doc
%make_build

%install
%makeinstall_std

# Use %%doc to install documentation in a standard location
mkdir __docdir
mv %buildroot%_datadir/doc/%name/api/ __docdir/
rm -rf %buildroot%_datadir/doc/%name/

%files
%doc COPYING NEWS
%_libdir/*.so.*

%files devel
%doc examples/ __docdir/api/
%_libdir/libp11.so
%_libdir/pkgconfig/libp11.pc
%_includedir/libp11.h

%changelog
* Fri Oct 30 2015 Michael Shigorin <mike@altlinux.org> 0.3.0-alt1
- 0.3.0
- recreated gear repo to use upstream git
- applied fedora patch and spec bits for API docs

* Mon Sep 21 2015 Michael Shigorin <mike@altlinux.org> 0.2.8-alt1
- 0.2.8
- updated Url:
- reverted Group: (it's not legacy but rather a layer)
- dropped API docs
- minor spec cleanup

* Fri Sep 12 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.2.7-alt1.qa3
- Moved this version into System/Legacy libraries

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

