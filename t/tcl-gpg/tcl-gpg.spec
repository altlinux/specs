Name: tcl-gpg
Version: 1.0
Release: alt2

Summary: A Tcl interface to GNU Privacy Guard
License: BSD
Group: Development/Tcl
Url: http://tclgpg.googlecode.com

Source: %name-%version-%release.tar

Requires: tcl >= 8.5.0-alt0.1

BuildRequires(pre): rpm-build-tcl >= 0.2-alt1
BuildRequires: rpm-build >= 4.0.4-alt41 tcllib tcl-devel >= 8.5.0-alt0.1

%description
%name is a Tcl interface to GNU Privacy Guard with interface similar
to TclGPGME

%prep
%setup
sed -i 's/@lib@/%_lib/' pkgIndex.tcl.in

%build
aclocal
autoconf
%configure
%make_build

%install
%makeinstall

%files
%_tcllibdir/libgpg%version.so
%_tcldatadir/*
%_mandir/mann/*

%changelog
* Mon Jan 11 2010 Sergey Bolshakov <sbolshakov@altlinux.ru> 1.0-alt2
- updated to svn rev.72

* Fri Aug 21 2009 Sergey Bolshakov <sbolshakov@altlinux.ru> 1.0-alt1
- first build for alt linux
