Name: xemacs-elib
Version: 1.13
Release: alt1

%define_xemacs_package elib

Summary: Portable Emacs Lisp utilities library
License: GPL
Group: Editors

%description
Portable Emacs Lisp utilities library

%prep
%setup -qc

%install
%xemacs_package_install
%xemacs_package_find_files

%files -f %name-files

%changelog
* Thu May 21 2009 Sergey Bolshakov <sbolshakov@altlinux.ru> 1.13-alt1
- 1.13

* Thu Apr 14 2005 Sergey Bolshakov <sbolshakov@altlinux.ru> 1.11-alt2
- rebuilt in new env

* Sat Nov 15 2003 Sergey Bolshakov <sbolshakov@altlinux.ru> 1.11-alt1
- 1.11

* Sat Dec 21 2002 Sergey Bolshakov <s.bolshakov@belcaf.com> 1.10-alt2
- #1531 fixed

* Mon Aug  5 2002 Sergey Bolshakov <s.bolshakov@belcaf.com> 1.10-alt1
- first build for %distribution distribution

