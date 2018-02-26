Name: xemacs-eshell
Version: 1.18
Release: alt1

%define_xemacs_package eshell

Summary: Command shell implemented entirely in Emacs Lisp
License: GPL
Group: Editors

%description
Command shell implemented entirely in Emacs Lisp

%prep
%setup -qc

%install
%xemacs_package_install
%xemacs_package_find_files

%files -f %name-files

%changelog
* Tue May 03 2011 Sergey Bolshakov <sbolshakov@altlinux.ru> 1.18-alt1
- 1.18

* Thu May 21 2009 Sergey Bolshakov <sbolshakov@altlinux.ru> 1.17-alt1
- 1.17

* Sat Aug 06 2005 Sergey Bolshakov <sbolshakov@altlinux.ru> 1.10-alt1
- 1.10

* Sat Jan 29 2005 Sergey Bolshakov <sbolshakov@altlinux.ru> 1.08-alt1
- 1.08

* Wed Aug 18 2004 Sergey Bolshakov <sbolshakov@altlinux.ru> 1.07-alt1
- 1.07

* Sat Nov 15 2003 Sergey Bolshakov <sbolshakov@altlinux.ru> 1.06-alt1
- 1.06

* Mon May 19 2003 Sergey Bolshakov <s.bolshakov@sam-solutions.net> 1.05-alt1
 - 1.05

* Thu Mar  6 2003 Sergey Bolshakov <s.bolshakov@sam-solutions.net> 1.04-alt1
- 1.04

* Sat Dec 21 2002 Sergey Bolshakov <s.bolshakov@belcaf.com> 1.03-alt2
- #1531 fixed

* Mon Aug  5 2002 Sergey Bolshakov <s.bolshakov@belcaf.com> 1.03-alt1
- first build for %distribution distribution

