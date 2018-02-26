Name: xemacs-re-builder
Version: 1.05
Release: alt2

%define_xemacs_package re-builder

Summary: Interactive development tool for regular expressions
License: GPL
Group: Editors

%description
Interactive development tool for regular expressions.

%prep
%setup -qc

%install
%xemacs_package_install
%xemacs_package_find_files

%files -f %name-files

%changelog
* Fri May 22 2009 Sergey Bolshakov <sbolshakov@altlinux.ru> 1.05-alt2
- rebuilt in new env

* Sat Dec 10 2005 Sergey Bolshakov <sbolshakov@altlinux.ru> 1.05-alt1
- 1.05

* Fri May  6 2005 Sergey Bolshakov <sbolshakov@altlinux.ru> 1.02-alt1
- 1.02

