Name: xemacs-supercite
Version: 1.21
Release: alt2

%define_xemacs_package supercite

Summary: An Emacs citation tool for news & mail messages
License: GPL
Group: Editors

%description
An Emacs citation tool for news fill me mail messages

%prep
%setup -qc

%install
%xemacs_package_install
%xemacs_package_find_files

%files -f %name-files

%changelog
* Fri May 22 2009 Sergey Bolshakov <sbolshakov@altlinux.ru> 1.21-alt2
- rebuilt in new env

* Sat Dec 10 2005 Sergey Bolshakov <sbolshakov@altlinux.ru> 1.21-alt1
- 1.21

* Fri Apr 15 2005 Sergey Bolshakov <sbolshakov@altlinux.ru> 1.20-alt2
- rebuilt in new env

* Sat Nov 15 2003 Sergey Bolshakov <sbolshakov@altlinux.ru> 1.20-alt1
- 1.20

* Sat Dec 21 2002 Sergey Bolshakov <s.bolshakov@belcaf.com> 1.19-alt2
- #1531 fixed

* Mon Aug  5 2002 Sergey Bolshakov <s.bolshakov@belcaf.com> 1.19-alt1
- first build for %distribution distribution

