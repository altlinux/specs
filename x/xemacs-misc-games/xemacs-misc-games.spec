Name: xemacs-misc-games
Version: 1.22
Release: alt1

%define_xemacs_package misc-games

Summary: Other amusements and diversions
License: GPL
Group: Editors

%description
Other amusements and diversions

%prep
%setup -qc

%install
%xemacs_package_install
%xemacs_package_find_files

%files -f %name-files

%changelog
* Thu May 21 2009 Sergey Bolshakov <sbolshakov@altlinux.ru> 1.22-alt1
- 1.22

* Thu Apr 14 2005 Sergey Bolshakov <sbolshakov@altlinux.ru> 1.18-alt2
- rebuilt in new env

* Sat Nov 15 2003 Sergey Bolshakov <sbolshakov@altlinux.ru> 1.18-alt1
- 1.18

* Sat Oct 04 2003 Sergey Bolshakov <sbolshakov@altlinux.ru> 1.17-alt1
- 1.17

* Thu Mar  6 2003 Sergey Bolshakov <s.bolshakov@sam-solutions.net> 1.16-alt1
- 1.16

* Sat Dec 21 2002 Sergey Bolshakov <s.bolshakov@belcaf.com> 1.15-alt2
- #1531 fixed

* Mon Aug  5 2002 Sergey Bolshakov <s.bolshakov@belcaf.com> 1.15-alt1
- first build for %distribution distribution

