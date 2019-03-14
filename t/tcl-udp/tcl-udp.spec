
# tests don't work in hasher
%def_disable check
%define _unpackaged_files_terminate_build 1

Name: tcl-udp
Version: 1.0.9
Release: alt2

Summary: A tcl extension, wich provides UDP sockets for Tcl
License: BSD
Group: Development/Tcl
Url: http://tcludp.sourceforge.net/

Source: %name-%version-%release.tar

BuildPreReq:  rpm-build-tcl >= 0.2-alt1
BuildRequires: tcl-devel >= 8.4.0-alt1
Requires: tcl >= 8.4.0-alt1
Conflicts: scotty

%description
%summary

%prep
%setup
%teapatch

%build
%configure
make

%check
make test TCLLIBPATH=%buildroot%_tcllibdir

%install
%makeinstall

%files
%doc ChangeLog README license.terms
%_tcllibdir/libudp%version.so
%_tcllibdir/udp%version
%_tcldatadir/udp%version
%_mandir/mann/udp.*

%changelog
* Thu Mar 14 2019 Ivan A. Melnikov <iv@altlinux.org> 1.0.9-alt2
- Package pkgIndex.tcl to fix provides

* Wed Apr 17 2013 Dmitry V. Levin (QA) <qa_ldv@altlinux.org> 1.0.9-alt1.qa1
- NMU: rebuilt for debuginfo.

* Fri Oct 17 2008 Sergey Bolshakov <sbolshakov@altlinux.ru> 1.0.9-alt1
- initial build
