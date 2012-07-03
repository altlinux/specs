%def_without test

Name: tcl-udp
Version: 1.0.9
Release: alt1

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
%if_with test
make test TCLSH_ENV='LD_LIBRARY_PATH=.'
%endif

%install
%makeinstall

%files
%doc ChangeLog README license.terms
%_tcllibdir/libudp%version.so
%_tcldatadir/udp%version
%_mandir/mann/udp.*

%changelog
* Fri Oct 17 2008 Sergey Bolshakov <sbolshakov@altlinux.ru> 1.0.9-alt1
- initial build
