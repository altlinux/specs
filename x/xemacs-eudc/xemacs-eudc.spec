Name: xemacs-eudc
Version: 1.40
Release: alt1

%define_xemacs_package eudc

Summary: Emacs Unified Directory Client
License: GPL
Group: Editors

%description
Emacs Unified Directory Client

%prep
%setup -qc

%install
%xemacs_package_install
%xemacs_package_find_files

%files -f %name-files

%changelog
* Thu May 21 2009 Sergey Bolshakov <sbolshakov@altlinux.ru> 1.40-alt1
- 1.40

* Thu Apr 14 2005 Sergey Bolshakov <sbolshakov@altlinux.ru> 1.39-alt2
- rebuilt in new env

* Sat Nov 15 2003 Sergey Bolshakov <sbolshakov@altlinux.ru> 1.39-alt1
- 1.39

* Sat Jun 07 2003 Sergey Bolshakov <s.bolshakov@sam-solutions.net> 1.38-alt1
 - 1.38

* Thu Mar  6 2003 Sergey Bolshakov <s.bolshakov@sam-solutions.net> 1.37-alt1
- 1.37

* Sat Dec 21 2002 Sergey Bolshakov <s.bolshakov@belcaf.com> 1.36-alt2
- #1531 fixed

* Mon Aug  5 2002 Sergey Bolshakov <s.bolshakov@belcaf.com> 1.36-alt1
- first build for %distribution distribution

