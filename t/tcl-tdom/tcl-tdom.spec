Name: tcl-tdom
Version: 0.8.3
Release: alt0.1

Summary: A XML/DOM/XPath/XSLT implementation for Tcl
License: MPL
Group: Development/Tcl
Url: http://www.tdom.org

Source: %name-%version-%release.tar

BuildRequires: tcl-devel >= 8.4.0-alt1 libexpat-devel

%description
This package contains a freely distributable extension to Tcl
implementing memory channels, i.e. channels storing the data
placed into them in memory, not on disk.

%prep
%setup
%teapatch

%build
autoconf
%configure
%make_build all test

%install
%makeinstall

%files
%_tcllibdir/libtdom%version.so
%_tcldatadir/tdom%version
%_mandir/mann/*

%changelog
* Sat Feb 23 2008 Sergey Bolshakov <sbolshakov@altlinux.ru> 0.8.3-alt0.1
- first build for %distribution
