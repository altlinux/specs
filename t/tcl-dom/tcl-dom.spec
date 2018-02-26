Name: tcl-dom
Version: 3.1
Release: alt3

Summary: A DOM bindings for Tcl
License: BSD
Group: Development/Tcl
URL: http://tclxml.sourceforge.net/

Source: %name-%version.tar.bz2

BuildRequires: libxml2-devel rpm-build >= 4.0.4-alt41 tcl-devel >= 8.4.0-alt1 tcl-xml-devel = %version

%package core
Summary: A front-end interface and generic DOM implementation for Tcl
Group: Development/Tcl

%package libxml2
Summary: A libxml2-based DOM implementation for Tcl
Group: Development/Tcl
Requires: %name-core = %version-%release tcl-xml-libxml2 = %version

%package devel
Summary: Header files for %name
Group: Development/Tcl
Requires: %name-core = %version-%release

%description
This package provides a DOM binding for Tcl.  It provides one of the
following implementations:
* A Tcl-only implementation
* A C-based implementation based on TclDOMPro
* A wrapper for the Gnome libxml2 library

%description core
This package provides a generic front-end interface and
generic Tcl DOM implementation.

%description libxml2
This package provides a libxml2-based DOM implementation.

%description devel
This package includes header files for %name

%prep
%setup
sed -i 's/@lib@/%_lib/' pkgIndex.tcl.in src-libxml2/pkgIndex.tcl.in

%build
aclocal
autoconf
%configure
pushd src-libxml2
aclocal
autoconf
%configure
make

%install 
%make_install DESTDIR=%buildroot install
%make_install -C src-libxml2 DESTDIR=%buildroot install

%files core
%doc ChangeLog README RELNOTES LICENSE docs examples
%_tcldatadir/Tcldom%version
%_mandir/mann/*

%files libxml2
%_tcllibdir/libtcldom_libxml2%version.so
%_tcldatadir/tcldom_libxml2%version

%files devel
%_includedir/tcldom-libxml2

%changelog
* Wed Jun 27 2007 Sergey Bolshakov <sbolshakov@altlinux.ru> 3.1-alt3
- rebuilt

* Fri Jul 21 2006 Sergey Bolshakov <sbolshakov@altlinux.ru> 3.1-alt2
- fixed build on x86_64

* Sat Feb 25 2006 Sergey Bolshakov <sbolshakov@altlinux.ru> 3.1-alt1
- 3.1 released

* Tue Nov  9 2004 Sergey Bolshakov <sbolshakov@altlinux.ru> 3.0-alt3
- fixed #5469

* Wed Nov  3 2004 Sergey Bolshakov <sbolshakov@altlinux.ru> 3.0-alt2
- rebuilt against new shiny tcl reqprov finder

* Tue Sep 21 2004 Sergey Bolshakov <sbolshakov@altlinux.ru> 3.0-alt1
- 3.0 released

* Thu May 13 2004 Sergey Bolshakov <sbolshakov@altlinux.ru>  3.0-alt0.2
- devel subpackage added

* Wed May 12 2004 Sergey Bolshakov <sbolshakov@altlinux.ru>  3.0-alt0.1
- Initial build for %distribution

