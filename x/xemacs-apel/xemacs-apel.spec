Name: xemacs-apel
Version: 1.34
Release: alt1

%define_xemacs_package apel

Summary: A Portable Emacs Library
License: GPL
Group: Editors

%description
A Portable Emacs Library

%prep
%setup -qc

%install
%xemacs_package_install
%xemacs_package_find_files

%files -f %name-files

%changelog
* Tue May 03 2011 Sergey Bolshakov <sbolshakov@altlinux.ru> 1.34-alt1
- 1.34

* Thu May 21 2009 Sergey Bolshakov <sbolshakov@altlinux.ru> 1.33-alt1
- 1.33

* Sat Dec 10 2005 Sergey Bolshakov <sbolshakov@altlinux.ru> 1.32-alt1
- 1.32

* Sat Aug 06 2005 Sergey Bolshakov <sbolshakov@altlinux.ru> 1.29-alt1
- 1.29

* Thu Apr 14 2005 Sergey Bolshakov <sbolshakov@altlinux.ru> 1.27-alt2
- rebuilt in new env

* Sat Nov 15 2003 Sergey Bolshakov <sbolshakov@altlinux.ru> 1.27-alt1
- 1.27

* Thu Mar  6 2003 Sergey Bolshakov <s.bolshakov@sam-solutions.net> 1.26-alt1
- 1.26

* Sat Dec 21 2002 Sergey Bolshakov <s.bolshakov@belcaf.com> 1.25-alt2
- #1531 fixed

* Mon Aug  5 2002 Sergey Bolshakov <s.bolshakov@belcaf.com> 1.25-alt1
- first build for %distribution distribution
