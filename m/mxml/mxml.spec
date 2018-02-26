Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>
%def_enable shared
%def_enable static
%def_enable threads
%def_disable debug

%define Name Mini-XML
Name: mxml
%define lname lib%name
Version: 2.7
Release: alt1
Summary: %Name documentation generator
Group: Text tools
License: %lgpl2plus with exceptions
Url: http://www.minixml.org/
Source: %name-%version.tar
Provides: %{name}doc = %version-%release
Obsoletes: %{name}doc < %version-%release
Requires: %lname = %version-%release

# Automatically added by buildreq on Sun Jul 27 2008
BuildRequires: gcc-c++
BuildRequires: rpm-build-licenses

%description
mxmldoc scans the specified C and C++ source files to produce an XML
representation of globally accessible classes, constants, enumerations,
functions, structures, typedefs, unions, and variables. The XML file is
updated as necessary and a HTML representation of the XML file is
written to the standard output. If no source files are specified then
the current XML file is converted to HTML on the standard output.


%if_enabled shared
%package -n %lname
Summary: %Name library
Group: System/Libraries

%description -n %lname
%Name is a small XML parsing library that you can use to read XML
and XML-like data files in your application without requiring large
non-standard libraries.
%endif


%package -n %lname-devel
Summary: %Name library header
Group: Development/C
Requires: %lname%{?_disable_shared:-devel-static} = %version-%release

%description -n %lname-devel
%Name is a small XML parsing library that you can use to read XML
and XML-like data files in your application without requiring large
non-standard libraries.
This package includes headers and other files necessary to build
applications that use %Name.


%if_enabled static
%package -n %lname-devel-static
Summary: %Name library
Group: Development/C
Requires: %lname-devel = %version-%release

%description -n %lname-devel-static
%Name is a small XML parsing library that you can use to read XML
and XML-like data files in your application without requiring large
non-standard libraries.
This package includes %Name static library.
%endif


%package doc
Summary: %Name documentation
Group: Documentation
BuildArch: noarch

%description doc
%Name is a small XML parsing library that you can use to read XML
and XML-like data files in your application without requiring large
non-standard libraries.
This package includes %Name documentation.


%prep
%setup


%build
%configure \
    %{subst_enable debug} \
    %{subst_enable shared} \
    %{subst_enable threads} \
    --with-docdir=%_docdir/%name-%version
%make_build


%install
%make_install BUILDROOT=%buildroot install


%files
%_bindir/*
%_man1dir/*


%if_enabled shared
%files -n %lname
%_libdir/*.so.*
%endif


%files -n %lname-devel
%_pkgconfigdir/*
%_includedir/*
%{?_enable_shared:%_libdir/*.so}
%_man3dir/*


%if_enabled static
%files -n %lname-devel-static
%_libdir/*.a
%endif


%files doc
%_docdir/%name-%version


%changelog
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
