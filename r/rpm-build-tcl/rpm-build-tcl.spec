Name: rpm-build-tcl
Version: 0.4
Release: alt1

Summary: RPM helpers to use with Tcl scripts
License: GPL
Group: Development/Tcl
BuildArch: noarch

Source0: %name-%version.tar

PreReq: rpm-build >= 4.0.4-alt44
Requires: /etc/rpm/macros.d
Conflicts: tcl-devel < 0:8.4.7-alt2

%description
%name is set of scripts and rpm macros to assist in tcl modules
build process

%prep
%setup -c

%install
install -p -m0644 -D tcl-macros %buildroot%_sysconfdir/rpm/macros.d/tcl
install -p -m0644 -D tcl-macros.env %buildroot%_sysconfdir/rpm/macros.d/tcl.env
install -p -m0755 -D tcl.req %buildroot%_rpmlibdir/tcl.req
install -p -m0755 -D tcl.req.files %buildroot%_rpmlibdir/tcl.req.files
install -p -m0755 tcl.prov %buildroot%_rpmlibdir/tcl.prov
install -p -m0755 tcl.prov.files %buildroot%_rpmlibdir/tcl.prov.files

%files
%doc README*
%config %_sysconfdir/rpm/macros.d/tcl
%config %_sysconfdir/rpm/macros.d/tcl.env
%_rpmlibdir/tcl.*

%changelog
* Fri Dec 21 2007 Sergey Bolshakov <sbolshakov@altlinux.ru> 0.4-alt1
- modified for use with tm modules, found in tcl8.5

* Tue Sep 25 2007 Sergey Bolshakov <sbolshakov@altlinux.ru> 0.2.1-alt2
- do not require /usr/bin/tclsh to not create circular deps

* Mon Sep 24 2007 Alexey Tourbin <at@altlinux.ru> 0.2.1-alt1
- added new files, for use with new rpm-build:
  + tcl.req.files (.prov.files) - will select tcl files for req/prov
  + /etc/rpm/macros.d/tcl.env - piece of rpm-build scriplets' preamble
  + also placed rpm-build tcl macros to /etc/rpm/macros.d/tcl
- tcl.req: enabled warning when "eval source" fails

* Thu Jul 20 2006 Sergey Bolshakov <sbolshakov@altlinux.ru> 0.2-alt1
- %%teapatch macro resurrected

* Wed Jul 13 2005 Sergey Bolshakov <sbolshakov@altlinux.ru> 0.1-alt0.5
- #6488 again

* Sat Apr 16 2005 Sergey Bolshakov <sbolshakov@altlinux.ru> 0.1-alt0.4
- #6488 fixed

* Sat Nov 20 2004 Sergey Bolshakov <sbolshakov@altlinux.ru> 0.1-alt0.3
- catched 'exit' in scripts, which can abort findreq process

* Tue Nov  2 2004 Sergey Bolshakov <sbolshakov@altlinux.ru> 0.1-alt0.2
- added conflicts to older tcl-devel

* Sat Oct 16 2004 Sergey Bolshakov <sbolshakov@altlinux.ru> 0.1-alt0.1
- Initial release
