Name: xemacs-hm--html-menus
Version: 1.24
Release: alt1

%define_xemacs_package hm--html-menus

Summary: HTML editing support
License: GPL
Group: Editors

%description
HTML editing support

%prep
%setup -qc

%install
%xemacs_package_install
%xemacs_package_find_files

%files -f %name-files

%changelog
* Thu May 21 2009 Sergey Bolshakov <sbolshakov@altlinux.ru> 1.24-alt1
- 1.24

* Thu Apr 14 2005 Sergey Bolshakov <sbolshakov@altlinux.ru> 1.23-alt2
- rebuilt in new env

* Sat Nov 15 2003 Sergey Bolshakov <sbolshakov@altlinux.ru> 1.23-alt1
- 1.23

* Sat Jul 05 2003 Sergey Bolshakov <s.bolshakov@sam-solutions.net> 1.21-alt1
 - 1.21

* Mon May 19 2003 Sergey Bolshakov <s.bolshakov@sam-solutions.net> 1.20-alt1
 - 1.20

* Sat Dec 21 2002 Sergey Bolshakov <s.bolshakov@belcaf.com> 1.18-alt2
- #1531 fixed

* Mon Aug  5 2002 Sergey Bolshakov <s.bolshakov@belcaf.com> 1.18-alt1
- first build for %distribution distribution

