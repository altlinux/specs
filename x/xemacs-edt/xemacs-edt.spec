Name: xemacs-edt
Version: 1.14
Release: alt1

%define_xemacs_package edt

Summary: DEC EDIT/EDT emulation
License: GPL
Group: Editors

%description
DEC EDIT/EDT emulation

%prep
%setup -qc

%install
%xemacs_package_install
%xemacs_package_find_files

%files -f %name-files

%changelog
* Thu May 21 2009 Sergey Bolshakov <sbolshakov@altlinux.ru> 1.14-alt1
- 1.14

* Thu Apr 14 2005 Sergey Bolshakov <sbolshakov@altlinux.ru> 1.13-alt2
- rebuilt in new env

* Sat Nov 15 2003 Sergey Bolshakov <sbolshakov@altlinux.ru> 1.13-alt1
- 1.13

* Sat Dec 21 2002 Sergey Bolshakov <s.bolshakov@belcaf.com> 1.12-alt2
- #1531 fixed

* Mon Aug  5 2002 Sergey Bolshakov <s.bolshakov@belcaf.com> 1.12-alt1
- first build for %distribution distribution

