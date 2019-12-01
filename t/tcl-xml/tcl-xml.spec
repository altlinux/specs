%define teaname tclxml

Name: tcl-xml
Version: 3.2
Release: alt2

Summary: XML parsers for Tcl
License: BSD
Group: Development/Tcl
Url: http://tclxml.sourceforge.net/

# repacked http://prdownloads.sourceforge.net/tclxml/tclxml-%version.tar.gz
Source: %teaname-%version.tar
Patch1: 0001-reverted-fix-for-sf-bug-596959-seems-unneeded.patch
Patch2: 0002-ALT-TEA.patch
Patch3: 0003-FEDORA-sgmlparser.patch
Patch4: 0004-FEDORA-xmlGenericError.patch

BuildRequires: rpm-build-tcl >= 0.2-alt1
BuildRequires: libxml2-devel rpm-build >= 4.0.4-alt41 tcl-devel >= 8.4.0-alt1
BuildRequires: libxslt-devel
BuildRequires: /usr/bin/xslt-config
BuildRequires: tcllib

Provides: tcl-xml-core tcl-dom-core tcl-xslt
Obsoletes: tcl-xml-core < 3.2
Obsoletes: tcl-dom-core < 3.2
Obsoletes: tcl-xslt < 3.2
Conflicts: tcl-xml-libxml2 < 3.2
Conflicts: tcl-dom-libxml2 < 3.2

%package devel
Summary: Header files for %name
Group: Development/Tcl
Requires: %name

%description
This package provides XML parsers for Tcl scripts.  There is a generic
front-end interface with plugin parser implementations.  A number of parser
implementations or wrappers are provided:
* James Clark's expat library.  This package is known as TclXML/expat.
* Gnome libxml2 library.  This package is known as TclXML/libxml2.
* A generic Tcl implementation, known as TclXML/tcl.

%description devel
This package includes header files for %name.

%prep
%setup -n %teaname-%version
%autopatch -p2

%build
%autoreconf
%configure \
	--disable-static \
	--enable-stub \
	#
%make_build
# build doc
cp -a tclxml-tcl/* .
make doc

%install
%make_install DESTDIR=%buildroot install install-doc
xz ChangeLog

%files
%doc ANNOUNCE ChangeLog* README.html LICENSE
%doc doc/*.html
%_tcllibdir/Tclxml%version/libTclxml%version.so
%_tcllibdir/Tclxml%version/*.tcl
%_mandir/mann/*

%files devel
%_includedir/tclxml
%_tcllibdir/Tclxml%version/libTclxmlstub%version.a

%changelog
* Sun Dec 01 2019 Vladimir D. Seleznev <vseleznv@altlinux.org> 3.2-alt2
- Built and packed manpages.

* Wed Nov 20 2019 Vladimir D. Seleznev <vseleznv@altlinux.org> 3.2-alt1
- Updated to 3.2.
- Moved to tcl-xml package, that provides and obsoletes tcl-xml-core,
  tcl-dom-core and tcl-xslt.
- Dropped tcl-xml-libxml2 subpackage (upstream change).
- Made it conflicts with tcl-xml-libxml2 and tcl-dom-libxml2.
- Compressed ChangeLog.

* Wed Apr 17 2013 Dmitry V. Levin (QA) <qa_ldv@altlinux.org> 3.1-alt4.qa1
- NMU: rebuilt for debuginfo.

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
