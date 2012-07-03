Name: xemacs-ps-print
Version: 1.12
Release: alt1

%define_xemacs_package ps-print

Summary: Printing functions and utilities
License: GPL
Group: Editors

%description
Printing functions and utilities

%prep
%setup -qc

%install
%xemacs_package_install
%xemacs_package_find_files

%files -f %name-files

%changelog
* Thu May 21 2009 Sergey Bolshakov <sbolshakov@altlinux.ru> 1.12-alt1
- 1.12

* Thu Apr 14 2005 Sergey Bolshakov <sbolshakov@altlinux.ru> 1.11-alt2
- rebuilt in new env

* Wed Aug 18 2004 Sergey Bolshakov <sbolshakov@altlinux.ru> 1.11-alt1
- 1.11

* Sat Jun 05 2004 Sergey Bolshakov <sbolshakov@altlinux.ru> 1.10-alt1
- 1.10

* Sat Nov 15 2003 Sergey Bolshakov <sbolshakov@altlinux.ru> 1.09-alt1
- 1.09

* Sat Dec 21 2002 Sergey Bolshakov <s.bolshakov@belcaf.com> 1.08-alt2
- #1531 fixed

* Mon Oct 28 2002 Sergey Bolshakov <s.bolshakov@belcaf.com> 1.08-alt1
- 1.08

* Mon Aug  5 2002 Sergey Bolshakov <s.bolshakov@belcaf.com> 1.04-alt1
- first build for %distribution distribution

