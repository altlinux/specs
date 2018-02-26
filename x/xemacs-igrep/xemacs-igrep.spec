Name: xemacs-igrep
Version: 1.16
Release: alt1

%define_xemacs_package igrep

Summary: Enhanced front-end for Grep
License: GPL
Group: Editors

Requires: grep

%description
Enhanced front-end for Grep

%prep
%setup -qc

%install
%xemacs_package_install
%xemacs_package_find_files

%files -f %name-files

%changelog
* Thu May 21 2009 Sergey Bolshakov <sbolshakov@altlinux.ru> 1.16-alt1
- 1.16

* Sat Dec 10 2005 Sergey Bolshakov <sbolshakov@altlinux.ru> 1.14-alt1
- 1.14

* Thu Apr 14 2005 Sergey Bolshakov <sbolshakov@altlinux.ru> 1.13-alt2
- rebuilt in new env

* Wed Aug 18 2004 Sergey Bolshakov <sbolshakov@altlinux.ru> 1.13-alt1
- 1.13

* Sat Nov 15 2003 Sergey Bolshakov <sbolshakov@altlinux.ru> 1.12-alt1
- 1.12

* Sat Oct 04 2003 Sergey Bolshakov <sbolshakov@altlinux.ru> 1.11-alt1
- 1.11

* Sat Dec 21 2002 Sergey Bolshakov <s.bolshakov@belcaf.com> 1.10-alt2
- #1531 fixed

* Mon Dec 16 2002 Sergey Bolshakov <s.bolshakov@belcaf.com> 1.10-alt1
- 1.10

* Mon Oct 28 2002 Sergey Bolshakov <s.bolshakov@belcaf.com> 1.09-alt1
- 1.09

* Mon Aug  5 2002 Sergey Bolshakov <s.bolshakov@belcaf.com> 1.08-alt1
- first build for %distribution distribution

