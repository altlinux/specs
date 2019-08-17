%define oname thread

Name: tcl-thread
Version: 2.8.2
Release: alt1

Summary: A tcl extension implementing memory channels
License: BSD
Group: Development/Tcl
Url: http://tcl.sourceforge.net/

# repacked thread%version.tar.gz from https://sourceforge.net/projects/tcl/files/
Source: %oname%version.tar
Patch1: 0001-Alt-TEA.patch

Requires: tcl >= 8.5.0-alt0.1

BuildRequires(pre): rpm-build-tcl >= 0.2-alt1
BuildRequires: rpm-build >= 4.0.4-alt41 tcl-devel >= 8.5.0-alt0.1

%package devel
Summary: A tcl extension implementing memory channels - development files
Group: Development/C
Requires: %name = %EVR

%description
%name is a tcl extension, which creates threads that contain Tcl 
interpreters, and it lets you send scripts to those threads for
evaluation.
Additionaly, it provides script-level access to basic thread 
synchronization primitives, like mutexes and condition variables.

%description devel
%name is a tcl extension, which creates threads that contain Tcl 
interpreters, and it lets you send scripts to those threads for
evaluation.
Additionaly, it provides script-level access to basic thread 
synchronization primitives, like mutexes and condition variables.

This package contains development files.

%prep
%setup -q -n %oname%version
%patch1 -p1
sed -i 's/@lib@/%_lib/' pkgIndex.tcl.in

%build
%configure
%make_build

%install
%makeinstall

%files
%_tcllibdir/libthread%version.so
%_tcldatadir/%oname%version
%_mandir/mann/*

%files devel
%_includedir/*.h

%changelog
* Sat Aug 17 2019 Vladimir D. Seleznev <vseleznv@altlinux.org> 2.8.2-alt1
- 2.8.2.

* Sun Apr 30 2017 Vladimir D. Seleznev <vseleznv@altlinux.org> 2.8.0-alt1
- 2.8.0 released

* Wed Apr 17 2013 Dmitry V. Levin (QA) <qa_ldv@altlinux.org> 2.6.5-alt1.qa1
- NMU: rebuilt for debuginfo.

* Fri Jun 13 2008 Sergey Bolshakov <sbolshakov@altlinux.ru> 2.6.5-alt1
- 2.6.5 released

* Wed Nov 21 2007 Sergey Bolshakov <sbolshakov@altlinux.ru> 2.6.5-alt0.1
- first build for alt linux
