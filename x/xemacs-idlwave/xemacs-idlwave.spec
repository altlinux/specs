Name: xemacs-idlwave
Version: 1.32
Release: alt2

%define_xemacs_package idlwave

Summary: Editing and Shell mode for the Interactive Data Language
License: GPL
Group: Editors

%description
Editing and Shell mode for the Interactive Data Language

%prep
%setup -qc

%install
%xemacs_package_install
%xemacs_package_find_files

%files -f %name-files

%changelog
* Fri May 22 2009 Sergey Bolshakov <sbolshakov@altlinux.ru> 1.32-alt2
- rebuilt in new env

* Sat Aug 06 2005 Sergey Bolshakov <sbolshakov@altlinux.ru> 1.32-alt1
- 1.32

* Thu Apr 14 2005 Sergey Bolshakov <sbolshakov@altlinux.ru> 1.31-alt2
- rebuilt in new env

* Sat Nov 15 2003 Sergey Bolshakov <sbolshakov@altlinux.ru> 1.31-alt1
- 1.31

* Sat Sep 27 2003 Sergey Bolshakov <sbolshakov@altlinux.ru> 1.30-alt1
 - 1.30

* Thu Mar  6 2003 Sergey Bolshakov <s.bolshakov@sam-solutions.net> 1.28-alt1
- 1.28

* Sat Dec 21 2002 Sergey Bolshakov <s.bolshakov@belcaf.com> 1.27-alt2
- #1531 fixed

* Mon Oct 28 2002 Sergey Bolshakov <s.bolshakov@belcaf.com> 1.27-alt1
- 1.27

* Mon Aug  5 2002 Sergey Bolshakov <s.bolshakov@belcaf.com> 1.25-alt1
- first build for %distribution distribution

