Name: xemacs-ruby-modes
Version: 1.04
Release: alt1

%define_xemacs_package ruby-modes

Summary: Ruby support
License: GPL
Group: Editors

%description
Ruby editing support

%prep
%setup -qc

%install
%xemacs_package_install
%xemacs_package_find_files

%files -f %name-files

%changelog
* Tue May 03 2011 Sergey Bolshakov <sbolshakov@altlinux.ru> 1.04-alt1
- 1.04

* Mon May 25 2009 Sergey Bolshakov <sbolshakov@altlinux.ru> 1.02-alt3
- rebuilt in new env

* Thu Apr 14 2005 Sergey Bolshakov <sbolshakov@altlinux.ru> 1.02-alt2
- rebuilt in new env

* Sat Nov 15 2003 Sergey Bolshakov <sbolshakov@altlinux.ru> 1.02-alt1
- 1.02

* Wed Mar  5 2003 Sergey Bolshakov <s.bolshakov@sam-solutions.net> 1.01-alt1
- 1.01

* Sat Dec 21 2002 Sergey Bolshakov <s.bolshakov@belcaf.com> 1.00-alt2
- #1531 fixed

* Mon Oct 28 2002 Sergey Bolshakov <s.bolshakov@belcaf.com> 1.00-alt1
- first build for %distribution distribution

