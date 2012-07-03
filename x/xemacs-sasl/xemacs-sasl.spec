Name: xemacs-sasl
Version: 1.16
Release: alt2

%define_xemacs_package sasl

Summary: Simple Authentication and Security Layer (SASL) library
License: GPL
Group: Editors

%description
Simple Authentication and Security Layer (SASL) library

%prep
%setup -qc

%install
%xemacs_package_install
%xemacs_package_find_files

%files -f %name-files

%changelog
* Fri May 22 2009 Sergey Bolshakov <sbolshakov@altlinux.ru> 1.16-alt2
- rebuilt in new env

* Sat Dec 10 2005 Sergey Bolshakov <sbolshakov@altlinux.ru> 1.16-alt1
- 1.16

* Sat Jan 29 2005 Sergey Bolshakov <sbolshakov@altlinux.ru> 1.15-alt1
- 1.15

* Sat Nov 15 2003 Sergey Bolshakov <sbolshakov@altlinux.ru> 1.14-alt1
- 1.14

* Sat Jul 05 2003 Sergey Bolshakov <s.bolshakov@sam-solutions.net> 1.13-alt1
 - 1.13

* Sat Dec 21 2002 Sergey Bolshakov <s.bolshakov@belcaf.com> 1.12-alt2
- #1531 fixed

* Mon Oct 28 2002 Sergey Bolshakov <s.bolshakov@belcaf.com> 1.12-alt1
- first build for %distribution distribution

