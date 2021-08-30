%define _unpackaged_files_terminate_build 1
%global optflags_lto %optflags_lto -ffat-lto-objects

Name: mxml
Version: 3.2
Release: alt2

Summary: Small XML file parsing library
License: Apache-2.0
Group: Development/C
URL: https://www.msweet.org/mxml/
Source: %name-%version.tar

Patch0: %name-%version-%release.patch

BuildRequires: gcc
BuildRequires: make

%description
Mini-XML is a small XML parsing library that you can use to read XML data files
or strings in your application without requiring large non-standard libraries.
Mini-XML provides the following functionality:

- Reading of UTF-8 and UTF-16 and writing of UTF-8 encoded XML files and
  strings.
- Data is stored in a linked-list tree structure, preserving the XML data
  hierarchy.
- SAX (streamed) reading of XML files and strings to minimize memory usage.
- Supports arbitrary element names, attributes, and attribute values with no
  preset limits, just available memory.
- Supports integer, real, opaque ("cdata"), and text data types in "leaf" nodes.
- Functions for creating and managing trees of data.
- "Find" and "walk" functions for easily locating and navigating trees of data.

Mini-XML doesn't do validation or other types of processing on the data
based upon schema files or other sources of definition information.

%package -n lib%name
Summary: Small XML file parsing library
Group: System/Libraries

%description -n lib%name
Mini-XML is a small XML parsing library that you can use to read XML data files
or strings in your application without requiring large non-standard libraries.
Mini-XML provides the following functionality:

- Reading of UTF-8 and UTF-16 and writing of UTF-8 encoded XML files and
  strings.
- Data is stored in a linked-list tree structure, preserving the XML data
  hierarchy.
- SAX (streamed) reading of XML files and strings to minimize memory usage.
- Supports arbitrary element names, attributes, and attribute values with no
  preset limits, just available memory.
- Supports integer, real, opaque ("cdata"), and text data types in "leaf" nodes.
- Functions for creating and managing trees of data.
- "Find" and "walk" functions for easily locating and navigating trees of data.

Mini-XML doesn't do validation or other types of processing on the data
based upon schema files or other sources of definition information.

%package -n lib%name-devel
Summary: Mini-XML library header
Group: Development/C
Requires: lib%name = %EVR

%description -n lib%name-devel
Mini-XML is a small XML parsing library that you can use to read XML data files
or strings in your application without requiring large non-standard libraries.
This package includes headers and other files necessary to build
applications that use Mini-XML.

%package doc
Summary: Mini-XML documentation
Group: Documentation
BuildArch: noarch

%description doc
Mini-XML is a small XML parsing library that you can use to read XML data files
or strings in your application without requiring large non-standard libraries.
This package includes Mini-XML documentation.

%package -n lib%name-devel-static
Summary: Mini-XML library
Group: Development/C
Requires: lib%name-devel = %EVR

%description -n lib%name-devel-static
Mini-XML is a small XML parsing library that you can use to read XML data files
or strings in your application without requiring large non-standard libraries.
This package includes Mini-XML static library.

%prep
%setup
%patch0 -p1

%build
%configure \
    --enable-shared \
    --enable-threads \
    --with-docdir=%_docdir/%name-%version
%make_build

%install
%make_install BUILDROOT=%buildroot install

%files -n lib%name
%_libdir/*.so.*

%files -n lib%name-devel
%_includedir/*
%_libdir/*.so
%_pkgconfigdir/*
%_man3dir/*

%files doc
%_docdir/%name-%version

%files -n lib%name-devel-static
%_libdir/*.a

%changelog
* Mon Aug 30 2021 Danil Shein <dshein@altlinux.org> 3.2-alt2
- added -ffat-lto-objects to %%optflags_lto

* Tue Jan 19 2021 Danil Shein <dshein@altlinux.org> 3.2-alt1
- Version 3.2

* Thu Jun 05 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 2.8-alt1
- Version 2.8

* Tue Feb 28 2012 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 2.7-alt1
- Version 2.7

* Tue Dec 13 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 2.6-alt3
- Disabled setting of RPATH

* Wed Feb 09 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 2.6-alt2
- Rebuilt for debuginfo

* Fri Oct 29 2010 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 2.6-alt1
- Version 2.6

* Thu Oct 28 2010 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 2.5-alt3
- Rebuilt for soname set-versions

* Mon Nov 02 2009 Igor Vlasenko <viy@altlinux.ru> 2.5-alt2.1
- NMU (by repocop): the following fixes applied:
  * post_ldconfig for libmxml
  * postun_ldconfig for libmxml

* Sun Jul 27 2008 Led <led@altlinux.ru> 2.5-alt2
- added missed postscripts

* Sun Jul 27 2008 Led <led@altlinux.ru> 2.5-alt1
- 2.5
- fixed License

* Fri Jan 14 2005 Yuri N. Sedunov <aris@altlinux.ru> 2.1-alt1
- 2.1

* Fri Sep 17 2004 Yuri N. Sedunov <aris@altlinux.ru> 2.0-alt1
- First build for Sisyphus.

