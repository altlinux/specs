Name: libmtquery
Version: 0.0.1
Release: alt3.1.qa3

Summary: multitran translation query library
License: LGPL
Group: System/Libraries

Source: %name-%{version}alpha3.tar.bz2
Patch: libmtquery-0.0.1-alt-DSO.patch

# Automatically added by buildreq on Tue Nov 09 2004
BuildRequires: gcc-c++ libbtree-devel libfacet-devel libmtsupport-devel libstdc++-devel

%description
multitran translation query library

%package devel
Summary: Development part of %name
Group: Development/C++
Requires: %name = %version-%release

%description devel
Contents header files and development libraries for %name

%package devel-static
Summary: Static libraries for %name
Group: Development/C++
Requires: %name-devel = %version-%release

%description devel-static
Contents static libraries for %name

%prep
%setup -q -n %name-%{version}alpha3
%patch -p2

%build
%make_build DEBUG_LDFLAGS=

%install
%makeinstall

%files
%doc ChangeLog
%_libdir/*.so.*

%files devel
%_libdir/*.so
%_includedir/*

%files devel-static
%_libdir/*.a

%changelog
* Wed Jun 13 2012 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.0.1-alt3.1.qa3
- Fixed build

* Sat Nov 27 2010 Igor Vlasenko <viy@altlinux.ru> 0.0.1-alt3.1.qa2
- rebuild using girar-nmu to require/provide setversion 
  by request of mithraen@

* Thu Nov 12 2009 Repocop Q. A. Robot <repocop@altlinux.org> 0.0.1-alt3.1.qa1
- NMU (by repocop): the following fixes applied:
  * post_ldconfig for libmtquery
  * postun_ldconfig for libmtquery
  * postclean-05-filetriggers for spec file

* Mon Mar 13 2006 Stanislav Ievlev <inger@altlinux.org> 0.0.1-alt3.1
- rebuild

* Mon Jan 24 2005 Stanislav Ievlev <inger@altlinux.org> 0.0.1-alt3
- alpha3

* Thu Jan 20 2005 ALT QA Team Robot <qa-robot@altlinux.org> 0.0.1-alt2.1
- Rebuilt with libstdc++.so.6.

* Thu Jan 13 2005 Stanislav Ievlev <inger@altlinux.org> 0.0.1-alt2
- alpha2

* Tue Nov 09 2004 Stanislav Ievlev <inger@altlinux.org> 0.0.1-alt1
- initial build

