Name: xemacs-fortran-modes
Version: 1.05
Release: alt2

%define_xemacs_package fortran-modes

Summary: Fortran support
License: GPL
Group: Editors

%description
Fortran support

%prep
%setup -qc

%install
%xemacs_package_install
%xemacs_package_find_files

%files -f %name-files

%changelog
* Mon May 25 2009 Sergey Bolshakov <sbolshakov@altlinux.ru> 1.05-alt2
- rebuilt in new env

* Sun Jan 22 2006 Sergey Bolshakov <sbolshakov@altlinux.ru> 1.05-alt1
- 1.05

* Thu Apr 14 2005 Sergey Bolshakov <sbolshakov@altlinux.ru> 1.04-alt2
- rebuilt in new env

* Sat Jun 05 2004 Sergey Bolshakov <sbolshakov@altlinux.ru> 1.04-alt1
- 1.04

* Sat Nov 15 2003 Sergey Bolshakov <sbolshakov@altlinux.ru> 1.03-alt1
- 1.03

* Wed Mar  5 2003 Sergey Bolshakov <s.bolshakov@sam-solutions.net> 1.02-alt1
- 1.02

* Sat Dec 21 2002 Sergey Bolshakov <s.bolshakov@belcaf.com> 1.01-alt2
- #1531 fixed

* Mon Oct 28 2002 Sergey Bolshakov <s.bolshakov@belcaf.com> 1.01-alt1
- first build for %distribution distribution

