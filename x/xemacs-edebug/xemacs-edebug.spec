Name: xemacs-edebug
Version: 1.22
Release: alt1

%define_xemacs_package edebug

Summary: An Emacs Lisp debugger
License: GPL
Group: Editors

%description
An Emacs Lisp debugger

%prep
%setup -qc

%install
%xemacs_package_install
%xemacs_package_find_files

%files -f %name-files

%changelog
* Thu May 21 2009 Sergey Bolshakov <sbolshakov@altlinux.ru> 1.22-alt1
- 1.22

* Thu Apr 14 2005 Sergey Bolshakov <sbolshakov@altlinux.ru> 1.21-alt2
- rebuilt in new env

* Wed Aug 18 2004 Sergey Bolshakov <sbolshakov@altlinux.ru> 1.21-alt1
- 1.21

* Sat Nov 15 2003 Sergey Bolshakov <sbolshakov@altlinux.ru> 1.20-alt1
- 1.20

* Sat Oct 04 2003 Sergey Bolshakov <sbolshakov@altlinux.ru> 1.19-alt1
- 1.19

* Sat Jul 05 2003 Sergey Bolshakov <s.bolshakov@sam-solutions.net> 1.18-alt1
 - 1.18

* Mon May 19 2003 Sergey Bolshakov <s.bolshakov@sam-solutions.net> 1.17-alt1
 - 1.17

* Thu Mar  6 2003 Sergey Bolshakov <s.bolshakov@sam-solutions.net> 1.15-alt1
- 1.15

* Sat Dec 21 2002 Sergey Bolshakov <s.bolshakov@belcaf.com> 1.14-alt2
- #1531 fixed

* Mon Aug  5 2002 Sergey Bolshakov <s.bolshakov@belcaf.com> 1.14-alt1
- first build for %distribution distribution

