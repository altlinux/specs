Name: xemacs-calc
Version: 1.26
Release: alt2

%define_xemacs_package calc

Summary: Emacs calculator
License: GPL
Group: Editors

%description
Emacs calculator

%prep
%setup -qc

%install
%xemacs_package_install
%xemacs_package_find_files

%files -f %name-files

%changelog
* Fri May 22 2009 Sergey Bolshakov <sbolshakov@altlinux.ru> 1.26-alt2
- rebuilt in new env

* Sat Jan 29 2005 Sergey Bolshakov <sbolshakov@altlinux.ru> 1.26-alt1
- 1.26

* Wed Aug 18 2004 Sergey Bolshakov <sbolshakov@altlinux.ru> 1.25-alt1
- 1.25

* Sat Nov 15 2003 Sergey Bolshakov <sbolshakov@altlinux.ru> 1.24-alt1
- 1.24

* Sat Dec 21 2002 Sergey Bolshakov <s.bolshakov@belcaf.com> 1.23-alt2
- #1531 fixed

* Mon Aug  5 2002 Sergey Bolshakov <s.bolshakov@belcaf.com> 1.23-alt1
- first build for %distribution distribution

