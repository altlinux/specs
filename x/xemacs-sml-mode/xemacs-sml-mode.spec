Name: xemacs-sml-mode
Version: 0.12
Release: alt2

%define_xemacs_package sml-mode

Summary: SML editing support
License: GPL
Group: Editors

%description
SML editing support

%prep
%setup -qc

%install
%xemacs_package_install
%xemacs_package_find_files

%files -f %name-files

%changelog
* Fri May 22 2009 Sergey Bolshakov <sbolshakov@altlinux.ru> 0.12-alt2
- rebuilt in new env

* Sat Dec 10 2005 Sergey Bolshakov <sbolshakov@altlinux.ru> 0.12-alt1
- 0.12

* Fri Apr 15 2005 Sergey Bolshakov <sbolshakov@altlinux.ru> 0.11-alt2
- rebuilt in new env

* Sat Feb 07 2004 Sergey Bolshakov <sbolshakov@altlinux.ru> 0.11-alt1
- 0.11

* Sat Nov 15 2003 Sergey Bolshakov <sbolshakov@altlinux.ru> 0.10-alt1
- 0.10

* Mon May 19 2003 Sergey Bolshakov <s.bolshakov@sam-solutions.net> 0.09-alt1
 - 0.09

* Wed Mar  5 2003 Sergey Bolshakov <s.bolshakov@sam-solutions.net> 0.07-alt1
- 0.07

* Sat Dec 21 2002 Sergey Bolshakov <s.bolshakov@belcaf.com> 0.05-alt2
- #1531 fixed

* Mon Dec 16 2002 Sergey Bolshakov <s.bolshakov@belcaf.com> 0.05-alt1
- 0.05

* Mon Oct 28 2002 Sergey Bolshakov <s.bolshakov@belcaf.com> 0.03-alt1
- first build for %distribution distribution

