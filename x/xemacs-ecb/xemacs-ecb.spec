Name: xemacs-ecb
Version: 1.22
Release: alt2

%define_xemacs_package ecb

Summary: Emacs source code browser
License: GPL
Group: Editors

%description
Emacs source code browser.
With Java code the ECB works best with the xemacs-jde package.

%prep
%setup -qc

%install
%xemacs_package_install
%xemacs_package_find_files

%files -f %name-files

%changelog
* Fri May 22 2009 Sergey Bolshakov <sbolshakov@altlinux.ru> 1.22-alt2
- rebuilt in new env

* Sat Jan 29 2005 Sergey Bolshakov <sbolshakov@altlinux.ru> 1.22-alt1
- 1.22

* Sat Jun 05 2004 Sergey Bolshakov <sbolshakov@altlinux.ru> 1.18-alt1
- 1.18

* Sat Feb 07 2004 Sergey Bolshakov <sbolshakov@altlinux.ru> 1.14-alt1
- 1.14

* Sat Nov 15 2003 Sergey Bolshakov <sbolshakov@altlinux.ru> 1.13-alt1
- 1.13

* Sat Oct 04 2003 Sergey Bolshakov <sbolshakov@altlinux.ru> 1.12-alt1
- 1.12

* Sat Sep 27 2003 Sergey Bolshakov <sbolshakov@altlinux.ru> 1.10-alt1
 - 1.10

* Sat Jul 05 2003 Sergey Bolshakov <s.bolshakov@sam-solutions.net> 1.08-alt1
 - 1.08

* Mon May 19 2003 Sergey Bolshakov <s.bolshakov@sam-solutions.net> 1.06-alt1
 - 1.06

* Wed Mar  5 2003 Sergey Bolshakov <s.bolshakov@sam-solutions.net> 1.01-alt1
- first build for %distribution distribution

