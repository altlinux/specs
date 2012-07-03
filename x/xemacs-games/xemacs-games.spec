Name: xemacs-games
Version: 1.21
Release: alt1

%define_xemacs_package games

Summary: Various games for XEmacs
License: GPL
Group: Editors

%description
Tetris, Sokoban, and Snake for XEmacs

%prep
%setup -qc

%install
%xemacs_package_install
%xemacs_package_find_files

%files -f %name-files

%changelog
* Tue May 03 2011 Sergey Bolshakov <sbolshakov@altlinux.ru> 1.21-alt1
- 1.21

* Thu May 21 2009 Sergey Bolshakov <sbolshakov@altlinux.ru> 1.18-alt1
- 1.18

* Sat Dec 10 2005 Sergey Bolshakov <sbolshakov@altlinux.ru> 1.17-alt1
- 1.17

* Thu Apr 14 2005 Sergey Bolshakov <sbolshakov@altlinux.ru> 1.15-alt2
- rebuilt in new env

* Sat Nov 15 2003 Sergey Bolshakov <sbolshakov@altlinux.ru> 1.15-alt1
- 1.15

* Sat Jul 05 2003 Sergey Bolshakov <s.bolshakov@sam-solutions.net> 1.14-alt1
 - 1.14

* Sat Dec 21 2002 Sergey Bolshakov <s.bolshakov@belcaf.com> 1.13-alt2
- #1531 fixed

* Mon Aug  5 2002 Sergey Bolshakov <s.bolshakov@belcaf.com> 1.13-alt1
- first build for %distribution distribution

