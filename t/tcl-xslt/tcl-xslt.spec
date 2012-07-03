Name: tcl-xslt
Version: 3.1
Release: alt3

Summary: A Tcl wrapper for XSLT library
License: BSD
Group: Development/Tcl
URL: http://tclxml.sourceforge.net/

Source: %name-%version.tar.bz2

BuildRequires: libxml2-devel libxslt-devel
BuildRequires: tcl-xml-devel = %version tcl-dom-devel = %version
BuildRequires: tcl-devel >= 8.4.0-alt1 rpm-build >= 4.0.4-alt41

Requires: tcl-xml-libxml2 = %version tcl-dom-libxml2 = %version

%package devel
Summary: Header files for %name
Group: Development/Tcl
Requires: %name = %version-%release

%description
This package provides a Tcl interface to the libxslt library.
The libxslt library is loaded into the Tcl interpeter process.
XSL stylesheets are compiled and managed by a Tcl object,
so reusing a stylesheet is very fast.
TclXSLT also allows XSLT extensions elements and functions
to be implemented as a callback into the application's Tcl code.

%description devel
This package provides a Tcl interface to the libxslt library.
The libxslt library is loaded into the Tcl interpeter process.
XSL stylesheets are compiled and managed by a Tcl object,
so reusing a stylesheet is very fast.
TclXSLT also allows XSLT extensions elements and functions
to be implemented as a callback into the application's Tcl code.

This package includes header files for %name

%prep
%setup
sed -i 's/@lib@/%_lib/' pkgIndex.tcl.in

%build 
aclocal
autoconf
%configure
%make_build

%install 
%make_install DESTDIR=%buildroot install

%files
%doc ChangeLog README RELNOTES LICENSE
%_tcllibdir/libTclxslt%version.so
%_tcldatadir/Tclxslt%version
%_mandir/mann/*

%files devel
%_includedir/*

%changelog
* Wed Jun 27 2007 Sergey Bolshakov <sbolshakov@altlinux.ru> 3.1-alt3
- rebuilt

* Sat Jul 22 2006 Sergey Bolshakov <sbolshakov@altlinux.ru> 3.1-alt2
- fixed build on x86_64

* Sat Feb 25 2006 Sergey Bolshakov <sbolshakov@altlinux.ru> 3.1-alt1
- 3.1 released

* Wed Nov  3 2004 Sergey Bolshakov <sbolshakov@altlinux.ru> 3.0-alt2
- rebuilt against new shiny tcl reqprov finder

* Tue Sep 21 2004 Sergey Bolshakov <sbolshakov@altlinux.ru> 3.0-alt1
- 3.0 released

* Thu May 13 2004 Sergey Bolshakov <sbolshakov@altlinux.ru> 3.0-alt0.2
- devel subpackage added

* Wed May 12 2004 Sergey Bolshakov <sbolshakov@altlinux.ru>  3.0-alt0.1
- Initial build for %distribution


