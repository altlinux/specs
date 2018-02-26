Name: xemacs-ecrypto
Version: 0.21
Release: alt1

%define_xemacs_package ecrypto

Summary: Crypto functionality in Emacs Lisp
License: GPL
Group: Editors

%description
Crypto functionality in Emacs Lisp

%prep
%setup -qc

%install
%xemacs_package_install
%xemacs_package_find_files

%files -f %name-files

%changelog
* Thu May 21 2009 Sergey Bolshakov <sbolshakov@altlinux.ru> 0.21-alt1
- 0.21

* Sat Dec 10 2005 Sergey Bolshakov <sbolshakov@altlinux.ru> 0.20-alt1
- 0.20

* Sat Jan 29 2005 Sergey Bolshakov <sbolshakov@altlinux.ru> 0.19-alt1
- 0.19

* Sat Jun 05 2004 Sergey Bolshakov <sbolshakov@altlinux.ru> 0.17-alt1
- 0.17

* Sat Feb 07 2004 Sergey Bolshakov <sbolshakov@altlinux.ru> 0.16-alt1
- 0.16

* Sat Nov 15 2003 Sergey Bolshakov <sbolshakov@altlinux.ru> 0.14-alt1
- 0.14

* Sat Jul 05 2003 Sergey Bolshakov <s.bolshakov@sam-solutions.net> 0.13-alt1
 - 0.13

* Sat Dec 21 2002 Sergey Bolshakov <s.bolshakov@belcaf.com> 0.12-alt2
- #1531 fixed

* Mon Oct 28 2002 Sergey Bolshakov <s.bolshakov@belcaf.com> 0.12-alt1
- first build for %distribution distribution

