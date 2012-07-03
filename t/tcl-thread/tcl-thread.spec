Name: tcl-thread
Version: 2.6.5
Release: alt1

Summary: A tcl extension implementing memory channels
License: BSD
Group: Development/Tcl
Url: http://tcl.sourceforge.net/

Source: %name-%version-%release.tar

Requires: tcl >= 8.5.0-alt0.1

BuildRequires(pre): rpm-build-tcl >= 0.2-alt1
BuildRequires: rpm-build >= 4.0.4-alt41 tcl-devel >= 8.5.0-alt0.1

%description
%name is a tcl extension, which creates threads that contain Tcl 
interpreters, and it lets you send scripts to those threads for
evaluation.
Additionaly, it provides script-level access to basic thread 
synchronization primitives, like mutexes and condition variables.

%prep
%setup
sed -i 's/@lib@/%_lib/' pkgIndex.tcl.in

%build
%configure
%make_build

%install
%makeinstall

%files
%_tcllibdir/libthread%version.so
%_tcldatadir/*
%_mandir/mann/*

%changelog
* Fri Jun 13 2008 Sergey Bolshakov <sbolshakov@altlinux.ru> 2.6.5-alt1
- 2.6.5 released

* Wed Nov 21 2007 Sergey Bolshakov <sbolshakov@altlinux.ru> 2.6.5-alt0.1
- first build for alt linux
