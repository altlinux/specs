Name: xemacs-crisp
Version: 1.15
Release: alt2

%define_xemacs_package crisp

Summary: Crisp/Brief emulation
License: GPL
Group: Editors

%description
Crisp/Brief emulation

%prep
%setup -qc

%install
%xemacs_package_install
%xemacs_package_find_files

%files -f %name-files

%changelog
* Mon May 25 2009 Sergey Bolshakov <sbolshakov@altlinux.ru> 1.15-alt2
- rebuilt in new env

* Fri May 06 2005 Sergey Bolshakov <sbolshakov@altlinux.ru> 1.15-alt1
- 1.15

* Thu Apr 14 2005 Sergey Bolshakov <sbolshakov@altlinux.ru> 1.14-alt2
- rebuilt in new env

* Sat Nov 15 2003 Sergey Bolshakov <sbolshakov@altlinux.ru> 1.14-alt1
- 1.14

* Sat Oct 04 2003 Sergey Bolshakov <sbolshakov@altlinux.ru> 1.13-alt1
- 1.13

* Sat Dec 21 2002 Sergey Bolshakov <s.bolshakov@belcaf.com> 1.12-alt2
- #1531 fixed

* Mon Aug  5 2002 Sergey Bolshakov <s.bolshakov@belcaf.com> 1.12-alt1
- first build for %distribution distribution

