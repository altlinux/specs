# -*- rpm-spec -*-
# $Id: tcl-ldap,v 1.20 2006/07/21 21:33:23 me Exp $

%define srcname ldap
%define srcver 30

Name: tcl-%srcname
Version: 3.0
Release: alt9.1

Summary: LDAP extension to TCL
License: BSD
Group: Development/Tcl
Url: http://www.sensus.org/tcl

Source0: %name-%version.tar.bz2

BuildRequires: libldap-devel rpm-build >= 4.0.4-alt41 rpm-build-tcl >= 0.2-alt1 tcl-devel >= 8.4.0-alt1

%description
This extension provides a generic binding to LDAP, adding a single
command to the Tcl interpreter that dynamically creates session
command objects each time it is called. The resultant command can be
used to exercise the full range of the LDAP protocol, with the notable
exception of extended operations (a LDAP v3 feature).

%prep
%setup -q -n %srcname%srcver
%teapatch -v

%build
%configure
%make_build

%install
%make_install install DESTDIR=%buildroot

%files
%_tcllibdir/lib%srcname%version.so
%_tcldatadir/%srcname%version/pkgIndex.tcl
%doc license.terms ldap.htm

%changelog
* Thu Sep 24 2009 ALT QA Team Robot <ldv@altlinux.org> 3.0-alt9.1
- Automated blind dumb rebuild with libldap-devel-2.4.16-alt4.4.

* Sat Jul 22 2006 Sergey Bolshakov <sbolshakov@altlinux.ru> 3.0-alt9
- fixed build on x86_64

* Sat Apr 16 2005 Sergey Bolshakov <sbolshakov@altlinux.ru> 3.0-alt8
- rebuilt in new env

* Wed Nov  3 2004 Sergey Bolshakov <sbolshakov@altlinux.ru> 3.0-alt7
- rebuilt against new shiny tcl reqprov finder

* Sat Mar  6 2004 Sergey Bolshakov <sbolshakov@altlinux.ru> 3.0-alt6
- rebuilt in new env

* Sat Sep 27 2003 Sergey Bolshakov <sbolshakov@altlinux.ru> 3.0-alt5
- rebuilt against openldap 2.1.x

* Tue Sep 24 2002 Sergey Bolshakov <s.bolshakov@belcaf.com> 3.0-alt4
- rebuilt in new env

* Wed Jul 17 2002 Sergey Bolshakov <s.bolshakov@belcaf.com> 3.0-alt3
- rebuilt with new tcl layout

* Thu Sep 27 2001 Dmitry V. Levin <ldv@altlinux.ru> 3.0-alt2
- Built with RPM_OPT_FLAGS.

* Mon Sep 24 2001 Sergey Bolshakov <s.bolshakov@belcaf.com> 3.0-alt1
- Initial build for ALT Linux distribution.

