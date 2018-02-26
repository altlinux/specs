Name: xemacs-mew
Version: 1.19
Release: alt2

%define_xemacs_package mew

Summary: Messaging in an Emacs World
License: GPL
Group: Editors

%description
Messaging in an Emacs World

%prep
%setup -qc

%install
%xemacs_package_install
%xemacs_package_find_files

%files -f %name-files

%changelog
* Fri May 22 2009 Sergey Bolshakov <sbolshakov@altlinux.ru> 1.19-alt2
- rebuilt in new env

* Sat Aug 06 2005 Sergey Bolshakov <sbolshakov@altlinux.ru> 1.19-alt1
- 1.19

* Thu Apr 14 2005 Sergey Bolshakov <sbolshakov@altlinux.ru> 1.18-alt2
- rebuilt in new env

* Sat Nov 15 2003 Sergey Bolshakov <sbolshakov@altlinux.ru> 1.18-alt1
- 1.18

* Sat Dec 21 2002 Sergey Bolshakov <s.bolshakov@belcaf.com> 1.17-alt2
- #1531 fixed

* Mon Aug  5 2002 Sergey Bolshakov <s.bolshakov@belcaf.com> 1.17-alt1
- first build for %distribution distribution

