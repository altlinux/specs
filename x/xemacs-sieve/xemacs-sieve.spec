Name: xemacs-sieve
Version: 1.18
Release: alt2

%define_xemacs_package sieve

Summary: Manage Sieve email filtering scripts
License: GPL
Group: Editors

%description
Manage Sieve email filtering scripts

%prep
%setup -qc

%install
%xemacs_package_install
%xemacs_package_find_files

%files -f %name-files

%changelog
* Fri May 22 2009 Sergey Bolshakov <sbolshakov@altlinux.ru> 1.18-alt2
- rebuilt in new env

* Sat Dec 10 2005 Sergey Bolshakov <sbolshakov@altlinux.ru> 1.18-alt1
- 1.18

* Sat Jan 29 2005 Sergey Bolshakov <sbolshakov@altlinux.ru> 1.17-alt1
- 1.17

* Wed Aug 18 2004 Sergey Bolshakov <sbolshakov@altlinux.ru> 1.16-alt1
- 1.16

* Sat Feb 07 2004 Sergey Bolshakov <sbolshakov@altlinux.ru> 1.15-alt1
- 1.15

* Sat Nov 15 2003 Sergey Bolshakov <sbolshakov@altlinux.ru> 1.14-alt1
- 1.14

* Mon May 19 2003 Sergey Bolshakov <s.bolshakov@sam-solutions.net> 1.13-alt1
 - 1.13

* Wed Mar  5 2003 Sergey Bolshakov <s.bolshakov@sam-solutions.net> 1.11-alt1
- 1.11

* Sat Dec 21 2002 Sergey Bolshakov <s.bolshakov@belcaf.com> 1.10-alt2
- #1531 fixed

* Mon Oct 28 2002 Sergey Bolshakov <s.bolshakov@belcaf.com> 1.10-alt1
- 1.10

* Mon Aug  5 2002 Sergey Bolshakov <s.bolshakov@belcaf.com> 1.07-alt1
- first build for %distribution distribution

