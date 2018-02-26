Name: xemacs-psgml-dtds
Version: 1.03
Release: alt3

%define_xemacs_package psgml-dtds

Summary: Deprecated collection of DTDs for psgml
License: GPL
Group: Editors

%description
Deprecated collection of DTDs for psgml

%prep
%setup -qc

%install
%xemacs_package_install
%xemacs_package_find_files

%files -f %name-files

%changelog
* Mon May 25 2009 Sergey Bolshakov <sbolshakov@altlinux.ru> 1.03-alt3
- rebuilt in new env

* Thu Apr 14 2005 Sergey Bolshakov <sbolshakov@altlinux.ru> 1.03-alt2
- rebuilt in new env

* Sat Nov 15 2003 Sergey Bolshakov <sbolshakov@altlinux.ru> 1.03-alt1
- 1.03

* Sat Dec 21 2002 Sergey Bolshakov <s.bolshakov@belcaf.com> 1.02-alt2
- #1531 fixed

* Mon Oct 28 2002 Sergey Bolshakov <s.bolshakov@belcaf.com> 1.02-alt1
- first build for %distribution distribution

