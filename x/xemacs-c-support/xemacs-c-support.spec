Name: xemacs-c-support
Version: 1.22
Release: alt2

%define_xemacs_package c-support

Summary: Basic add-ons for editing C code
License: GPL
Group: Editors

%description
Basic add-ons for editing C code

%prep
%setup -qc

%install
%xemacs_package_install
%xemacs_package_find_files

%files -f %name-files

%changelog
* Mon May 25 2009 Sergey Bolshakov <sbolshakov@altlinux.ru> 1.22-alt2
- rebuilt in new env

* Sat Dec 10 2005 Sergey Bolshakov <sbolshakov@altlinux.ru> 1.22-alt1
- 1.22

* Fri May 06 2005 Sergey Bolshakov <sbolshakov@altlinux.ru> 1.21-alt1
- 1.21

* Thu Apr 14 2005 Sergey Bolshakov <sbolshakov@altlinux.ru> 1.20-alt2
- rebuilt in new env

* Sat Jun 05 2004 Sergey Bolshakov <sbolshakov@altlinux.ru> 1.20-alt1
- 1.20

* Sat Feb 07 2004 Sergey Bolshakov <sbolshakov@altlinux.ru> 1.19-alt1
- 1.19

* Sat Nov 15 2003 Sergey Bolshakov <sbolshakov@altlinux.ru> 1.18-alt1
- 1.18

* Sat Oct 04 2003 Sergey Bolshakov <sbolshakov@altlinux.ru> 1.17-alt1
- 1.17

* Sat Dec 21 2002 Sergey Bolshakov <s.bolshakov@belcaf.com> 1.16-alt2
- #1531 fixed

* Mon Aug  5 2002 Sergey Bolshakov <s.bolshakov@belcaf.com> 1.16-alt1
- first build for %distribution distribution

