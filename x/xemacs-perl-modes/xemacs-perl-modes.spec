Name: xemacs-perl-modes
Version: 1.14
Release: alt1

%define_xemacs_package perl-modes

Summary: Perl support
License: GPL
Group: Editors

%description
Perl support

%prep
%setup -qc

%install
%xemacs_package_install
%xemacs_package_find_files

%files -f %name-files

%changelog
* Thu May 21 2009 Sergey Bolshakov <sbolshakov@altlinux.ru> 1.14-alt1
- 1.14

* Sun May 21 2006 Sergey Bolshakov <sbolshakov@altlinux.ru> 1.09-alt1
- 1.09

* Fri May 06 2005 Sergey Bolshakov <sbolshakov@altlinux.ru> 1.08-alt1
- 1.08

* Sat Mar 12 2005 Sergey Bolshakov <sbolshakov@altlinux.ru> 1.07-alt1
- 1.07

* Wed Aug 18 2004 Sergey Bolshakov <sbolshakov@altlinux.ru> 1.06-alt1
- 1.06

* Sat Nov 15 2003 Sergey Bolshakov <sbolshakov@altlinux.ru> 1.05-alt1
- 1.05

* Wed Mar  5 2003 Sergey Bolshakov <s.bolshakov@sam-solutions.net> 1.04-alt1
- 1.04

* Sat Dec 21 2002 Sergey Bolshakov <s.bolshakov@belcaf.com> 1.02-alt2
- #1531 fixed

* Mon Oct 28 2002 Sergey Bolshakov <s.bolshakov@belcaf.com> 1.02-alt1
- first build for %distribution distribution

