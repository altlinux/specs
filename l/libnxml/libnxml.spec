%def_disable static

Name: libnxml
Version: 0.18.1
Release: alt2

Summary: C library for parsing, writing and creating XML 1.0 and 1.1 files or streams
License: LGPL 2.1
Group: System/Libraries

Url: http://www5.autistici.org/bakunin/codes.php
Source: http://www5.autistici.org/bakunin/libnxml/%name-%version.tar.gz

Packager: Andrey Alexandrov <demion@altlinux.ru>
BuildRequires: libcurl-devel

%package devel
Summary: Headers for %name
Group: Development/C
Requires: %name = %version-%release

%description devel
Headers for building software that uses %name

%if_enabled static
%package devel-static
Summary: Static libraries for %name
Group: Development/C
Requires: %name-devel = %version-%release

%description devel-static
Static libs for building statically linked software that uses %name
%endif

%description
nXML is a C library for parsing, writing and creating XML 1.0 and 1.1 files or streams.
It supports utf-8, utf-16be and utf-16le, ucs-4 (1234, 4321, 2143, 2312).

%prep
%setup

%build
%configure %{subst_enable static}
%make_build

%install
%make_install install DESTDIR=%buildroot

%files
%_libdir/*.so.*
%doc AUTHORS ChangeLog README NEWS

%files devel
%_libdir/*.so
%_includedir/*.h
%_pkgconfigdir/nxml.pc

%if_enabled static
%files -n lib%name-devel-static
%_libdir/%name.a
%endif

%changelog
* Mon Nov 01 2010 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.18.1-alt2
- Rebuilt for soname set-versions

* Wed Feb 03 2010 Repocop Q. A. Robot <repocop@altlinux.org> 0.18.1-alt1.1.qa1
- NMU (by repocop): the following fixes applied:
  * post_ldconfig for libnxml
  * postun_ldconfig for libnxml
  * postclean-05-filetriggers for spec file

* Tue Oct 30 2007 Andrey Alexandrov <demion@altlinux.ru> 0.18.1-alt1.1
- Andreas Krennmair bug fix size_t on macosx

* Mon Aug 14 2007 Andrey Alexandrov <demion@altlinux.ru> 0.18.0-alt1
- initial build
