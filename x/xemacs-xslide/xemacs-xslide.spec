Name: xemacs-xslide
Version: 1.09
Release: alt3

%define_xemacs_package xslide

Summary: XSL editing support
License: GPL
Group: Editors

%description
XSL editing support

%prep
%setup -qc

%install
%xemacs_package_install
%xemacs_package_find_files

%files -f %name-files

%changelog
* Mon May 25 2009 Sergey Bolshakov <sbolshakov@altlinux.ru> 1.09-alt3
- rebuilt in new env

* Fri Apr 15 2005 Sergey Bolshakov <sbolshakov@altlinux.ru> 1.09-alt2
- rebuilt in new env

* Sat Nov 15 2003 Sergey Bolshakov <sbolshakov@altlinux.ru> 1.09-alt1
- 1.09

* Sat Sep 27 2003 Sergey Bolshakov <sbolshakov@altlinux.ru> 1.08-alt1
 - 1.08

* Sat Jul 05 2003 Sergey Bolshakov <s.bolshakov@sam-solutions.net> 1.07-alt1
 - 1.07

* Mon May 19 2003 Sergey Bolshakov <s.bolshakov@sam-solutions.net> 1.06-alt1
 - 1.06

* Wed Mar  5 2003 Sergey Bolshakov <s.bolshakov@sam-solutions.net> 1.04-alt1
- 1.04

* Sat Dec 21 2002 Sergey Bolshakov <s.bolshakov@belcaf.com> 1.03-alt2
- #1531 fixed

* Mon Oct 28 2002 Sergey Bolshakov <s.bolshakov@belcaf.com> 1.03-alt1
- 1.03

* Mon Aug  5 2002 Sergey Bolshakov <s.bolshakov@belcaf.com> 1.01-alt1
- first build for %distribution distribution

