Name: xemacs-mmm-mode
Version: 1.05
Release: alt1

%define_xemacs_package mmm-mode

Summary: Multiple major modes in a single buffer
License: GPL
Group: Editors

%description
Multiple major modes in a single buffer

%prep
%setup -qc

%install
%xemacs_package_install
%xemacs_package_find_files

%files -f %name-files

%changelog
* Tue May 03 2011 Sergey Bolshakov <sbolshakov@altlinux.ru> 1.05-alt1
- 1.05

* Thu May 21 2009 Sergey Bolshakov <sbolshakov@altlinux.ru> 1.03-alt1
- 1.03

* Thu Apr 14 2005 Sergey Bolshakov <sbolshakov@altlinux.ru> 1.02-alt2
- rebuilt in new env

* Sat Jun 05 2004 Sergey Bolshakov <sbolshakov@altlinux.ru> 1.02-alt1
- 1.02

* Sat Nov 15 2003 Sergey Bolshakov <sbolshakov@altlinux.ru> 1.01-alt1
- 1.01

* Sat Dec 21 2002 Sergey Bolshakov <s.bolshakov@belcaf.com> 1.00-alt2
- #1531 fixed

* Mon Aug  5 2002 Sergey Bolshakov <s.bolshakov@belcaf.com> 1.00-alt1
- first build for %distribution distribution

