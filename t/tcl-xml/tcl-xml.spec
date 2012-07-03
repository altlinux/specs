Name: tcl-xml
Version: 3.1
Release: alt4

Summary: XML parsers for Tcl
License: BSD
Group: Development/Tcl
Url: http://tclxml.sourceforge.net/

Source: %name-%version.tar.bz2

BuildRequires: rpm-build-tcl >= 0.2-alt1
BuildRequires: libxml2-devel rpm-build >= 4.0.4-alt41 tcl-devel >= 8.4.0-alt1

%package core
Summary: A front-end interface and generic XML parser for Tcl
Group: Development/Tcl

%package libxml2
Summary: A libxml2-based XML parser for Tcl
Group: Development/Tcl
Requires: %name-core = %version-%release

%package devel
Summary: Header files for %name
Group: Development/Tcl
Requires: %name-core = %version-%release

%description
This package provides XML parsers for Tcl scripts.  There is a generic
front-end interface with plugin parser implementations.  A number of parser
implementations or wrappers are provided:
* James Clark's expat library.  This package is known as TclXML/expat.
* Gnome libxml2 library.  This package is known as TclXML/libxml2.
* A generic Tcl implementation, known as TclXML/tcl.

%description core
This package provides a generic front-end interface with plugin parser
implementations and generic Tcl implementation, known as TclXML/tcl.

%description libxml2
This package provides a libxml2-based XML parser, also known as TclXML/libxml2.

%description devel
This package includes header files for %name

%prep
%setup
sed -i 's/@lib@/%_lib/g' pkgIndex.tcl.in libxml2/pkgIndex.tcl.in

%build
aclocal
autoconf
%configure
pushd libxml2
aclocal
autoconf
%configure
popd
make
make -C libxml2

%install 
%make_install DESTDIR=%buildroot install
%make_install -C libxml2 DESTDIR=%buildroot install

%files core
%doc ChangeLog README RELNOTES LICENSE
%_tcllibdir/libTclxml%version.so
%_tcldatadir/Tclxml%version
%_mandir/mann/*

%files libxml2
%_tcllibdir/libTclXML_libxml2%version.so
%_tcldatadir/TclXML_libxml2%version

%files devel
%_includedir/tclxml
%_includedir/tclxml-libxml2

%changelog
* Sun Aug  5 2007 Sergey Bolshakov <sbolshakov@altlinux.ru> 3.1-alt4
- fixed pure-tcl parser to do hard reset

* Tue Jun 26 2007 Sergey Bolshakov <sbolshakov@altlinux.ru> 3.1-alt3
- rebuilt

* Thu Jul 20 2006 Sergey Bolshakov <sbolshakov@altlinux.ru> 3.1-alt2
- fixed build on x86_64

* Fri Feb 24 2006 Sergey Bolshakov <sbolshakov@altlinux.ru> 3.1-alt1
- 3.1 released

* Fri Aug 26 2005 Sergey Bolshakov <sbolshakov@altlinux.ru> 3.0-alt3
- CVS snapshot @20050826

* Wed Nov  3 2004 Sergey Bolshakov <sbolshakov@altlinux.ru> 3.0-alt2
- rebuilt against new shiny tcl reqprov finder

* Tue Sep 21 2004 Sergey Bolshakov <sbolshakov@altlinux.ru> 3.0-alt1
- 3.0 released

* Thu May 13 2004 Sergey Bolshakov <sbolshakov@altlinux.ru> 3.0-alt0.2
- devel subpackage added

* Wed May 12 2004 Sergey Bolshakov <sbolshakov@altlinux.ru>  3.0-alt0.1
- Initial build for %distribution
