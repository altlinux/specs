Name: xemacs-sh-script
Version: 1.24
Release: alt1

%define_xemacs_package sh-script

Summary: Support for editing shell scripts
License: GPL
Group: Editors

%description
Support for editing shell scripts

%prep
%setup -qc

%install
%xemacs_package_install
%xemacs_package_find_files

%files -f %name-files

%changelog
* Thu May 21 2009 Sergey Bolshakov <sbolshakov@altlinux.ru> 1.24-alt1
- 1.24

* Mon Nov  7 2005 Sergey Bolshakov <sbolshakov@altlinux.ru> 1.21-alt1
- 1.21

* Thu Apr 14 2005 Sergey Bolshakov <sbolshakov@altlinux.ru> 1.18-alt2
- rebuilt in new env

* Sat Nov 15 2003 Sergey Bolshakov <sbolshakov@altlinux.ru> 1.18-alt1
- 1.18

* Thu Mar  6 2003 Sergey Bolshakov <s.bolshakov@sam-solutions.net> 1.17-alt1
- 1.17

* Sat Dec 21 2002 Sergey Bolshakov <s.bolshakov@belcaf.com> 1.16-alt2
- #1531 fixed

* Mon Oct 28 2002 Sergey Bolshakov <s.bolshakov@belcaf.com> 1.16-alt1
- 1.16

* Mon Aug  5 2002 Sergey Bolshakov <s.bolshakov@belcaf.com> 1.15-alt1
- first build for %distribution distribution

