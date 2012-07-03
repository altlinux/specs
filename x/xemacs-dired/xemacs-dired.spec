Name: xemacs-dired
Version: 1.20
Release: alt1

%define_xemacs_package dired

Summary: Manage file systems
License: GPL
Group: Editors

%description
Manage file systems

%prep
%setup -qc

%install
%xemacs_package_install
%xemacs_package_find_files

%files -f %name-files

%changelog
* Tue May 03 2011 Sergey Bolshakov <sbolshakov@altlinux.ru> 1.20-alt1
- 1.20

* Thu May 21 2009 Sergey Bolshakov <sbolshakov@altlinux.ru> 1.19-alt1
- 1.19

* Fri May 06 2005 Sergey Bolshakov <sbolshakov@altlinux.ru> 1.17-alt1
- 1.17

* Sat Jan 29 2005 Sergey Bolshakov <sbolshakov@altlinux.ru> 1.16-alt1
- 1.16

* Sat Nov 15 2003 Sergey Bolshakov <sbolshakov@altlinux.ru> 1.15-alt1
- 1.15

* Sat Oct 04 2003 Sergey Bolshakov <sbolshakov@altlinux.ru> 1.14-alt1
- 1.14

* Thu Mar  6 2003 Sergey Bolshakov <s.bolshakov@sam-solutions.net> 1.13-alt1
- 1.13

* Sat Dec 21 2002 Sergey Bolshakov <s.bolshakov@belcaf.com> 1.12-alt2
- #1531 fixed

* Mon Aug  5 2002 Sergey Bolshakov <s.bolshakov@belcaf.com> 1.12-alt1
- first build for %distribution distribution

