%def_with doc
%define soname 4

Name: jansson
Version: 2.14
Release: alt1

Summary: C library for encoding, decoding and manipulating JSON data
License: MIT
Group: System/Libraries

Url: https://github.com/akheron/jansson
Source: %name-%version.tar
Patch0: %name-%version-%release.patch

%if_with doc
BuildRequires: python3-module-sphinx
%endif

%description
Jansson is a C library for encoding, decoding and manipulating JSON data.
It features:
 - Simple and intuitive API and data model
 - Comprehensive documentation
 - No dependencies on other libraries
 - Full Unicode support (UTF-8)
 - Extensive test suite

%package -n lib%name%soname
Summary: C library for encoding, decoding and manipulating JSON data
Group: System/Libraries
Conflicts: libjansson < 2.14
Obsoletes: libjansson

%description -n lib%name%soname
Jansson is a C library for encoding, decoding and manipulating JSON data.
It features:
 - Simple and intuitive API and data model
 - Comprehensive documentation
 - No dependencies on other libraries
 - Full Unicode support (UTF-8)
 - Extensive test suite

%package -n lib%name-devel
Summary: C library for encoding, decoding and manipulating JSON data
Group: Development/C
Requires: lib%name%soname = %EVR

%description -n lib%name-devel
Jansson is a C library for encoding, decoding and manipulating JSON data.
It features:
 - Simple and intuitive API and data model
 - Comprehensive documentation
 - No dependencies on other libraries
 - Full Unicode support (UTF-8)
 - Extensive test suite

%prep
%setup
%patch0 -p1

%build
%autoreconf
%configure --disable-static
%make_build
%if_with doc
%make html
%endif

%install
%makeinstall_std

%check
%make check

%files -n lib%name%soname
%_libdir/*.so.%soname
%_libdir/*.so.%soname.*
%doc README* LICENSE CHANGES

%files -n lib%name-devel
%_includedir/*.h
%_pkgconfigdir/*
%_libdir/*so
%if_with doc
%doc doc/_build/html/*
%endif

%changelog
* Fri Nov 29 2024 Anton Farygin <rider@altlinux.ru> 2.14-alt1
- 2.13.1 -> 2.14
- updated homepage URL
- renamed according to SharedLibsPolicy

* Tue May 18 2021 Slava Aseev <ptrnine@altlinux.org> 2.13.1-alt2
- fix FTBFS by applying upstream commit 798d40c3f3

* Tue Feb 02 2021 Sergey Bolshakov <sbolshakov@altlinux.ru> 2.13.1-alt1
- 2.13.1 released

* Thu Jun 27 2019 Sergey Bolshakov <sbolshakov@altlinux.ru> 2.12-alt1
- 2.12

* Tue Nov 20 2018 Oleg Solovyov <mcpain@altlinux.org> 2.10-alt1
- 2.10

* Wed May 23 2018 Michael Shigorin <mike@altlinux.org> 2.7-alt2
- introduce doc knob (on by default)
- minor spec cleanup

* Fri Jul 08 2016 Alexey Shabalin <shaba@altlinux.ru> 2.7-alt1
- 2.7

* Mon Sep 08 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 2.6-alt1.git20140827
- Version 2.6

* Sat Dec 15 2012 Slava Dubrovskiy <dubrsl@altlinux.org> 2.4-alt1
- Buld for ALT

