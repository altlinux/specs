Name: xemacs-vhdl
Version: 1.22
Release: alt1

%define_xemacs_package vhdl

Summary: Support for VHDL
License: GPL
Group: Editors

%description
Support for VHDL

%prep
%setup -q -c

%install
%xemacs_package_install
%xemacs_package_find_files

%files -f %name-files

%changelog
* Thu May 21 2009 Sergey Bolshakov <sbolshakov@altlinux.ru> 1.22-alt1
- 1.22

* Sun May 21 2006 Sergey Bolshakov <sbolshakov@altlinux.ru> 1.21-alt1
- 1.21

* Sat Mar 12 2005 Sergey Bolshakov <sbolshakov@altlinux.ru> 1.20-alt1
- 1.20

* Sat Jun 05 2004 Sergey Bolshakov <sbolshakov@altlinux.ru> 1.19-alt1
- 1.19

* Sat Nov 15 2003 Sergey Bolshakov <sbolshakov@altlinux.ru> 1.18-alt1
- 1.18

* Sat Jul 05 2003 Sergey Bolshakov <s.bolshakov@sam-solutions.net> 1.17-alt1
 - 1.17

* Thu Mar  6 2003 Sergey Bolshakov <s.bolshakov@sam-solutions.net> 1.16-alt1
- 1.16

* Sat Dec 21 2002 Sergey Bolshakov <s.bolshakov@belcaf.com> 1.15-alt2
- #1531 fixed

* Mon Aug  5 2002 Sergey Bolshakov <s.bolshakov@belcaf.com> 1.15-alt1
- first build for %distribution distribution

