Name: xemacs-pgg
Version: 1.08
Release: alt1

%define_xemacs_package pgg

Summary: Emacs interface to various PGP implementations
License: GPL
Group: Editors

%description
Emacs interface to various PGP implementations

%prep
%setup -qc

%install
%xemacs_package_install
%xemacs_package_find_files

%files -f %name-files

%changelog
* Tue May 03 2011 Sergey Bolshakov <sbolshakov@altlinux.ru> 1.08-alt1
- 1.08

* Thu May 21 2009 Sergey Bolshakov <sbolshakov@altlinux.ru> 1.07-alt1
- 1.07

* Sat Dec 10 2005 Sergey Bolshakov <sbolshakov@altlinux.ru> 1.06-alt1
- 1.06

* Sat Jan 29 2005 Sergey Bolshakov <sbolshakov@altlinux.ru> 1.05-alt1
- 1.05

* Sat Nov 15 2003 Sergey Bolshakov <sbolshakov@altlinux.ru> 1.04-alt1
- 1.04

* Sat Jun 07 2003 Sergey Bolshakov <s.bolshakov@sam-solutions.net> 1.03-alt1
 - 1.03

* Wed Mar  5 2003 Sergey Bolshakov <s.bolshakov@sam-solutions.net> 1.02-alt1
- 1.02

* Sat Dec 21 2002 Sergey Bolshakov <s.bolshakov@belcaf.com> 1.01-alt2
- #1531 fixed

* Mon Dec 16 2002 Sergey Bolshakov <s.bolshakov@belcaf.com> 1.01-alt1
- 1.01

* Mon Oct 28 2002 Sergey Bolshakov <s.bolshakov@belcaf.com> 1.00-alt1
- first build for %distribution distribution

