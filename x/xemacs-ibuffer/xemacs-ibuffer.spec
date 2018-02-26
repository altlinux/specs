Name: xemacs-ibuffer
Version: 1.10
Release: alt1

%define_xemacs_package ibuffer

Summary: Advanced replacement for buffer-menu
License: GPL
Group: Editors

%description
Advanced replacement for buffer-menu

%prep
%setup -qc

%install
%xemacs_package_install
%xemacs_package_find_files

%files -f %name-files

%changelog
* Tue May 03 2011 Sergey Bolshakov <sbolshakov@altlinux.ru> 1.10-alt1
- 1.10

* Mon May 25 2009 Sergey Bolshakov <sbolshakov@altlinux.ru> 1.09-alt3
- rebuilt in new env

* Thu Apr 14 2005 Sergey Bolshakov <sbolshakov@altlinux.ru> 1.09-alt2
- rebuilt in new env

* Sat Nov 15 2003 Sergey Bolshakov <sbolshakov@altlinux.ru> 1.09-alt1
- 1.09

* Sat Dec 21 2002 Sergey Bolshakov <s.bolshakov@belcaf.com> 1.08-alt2
- #1531 fixed

* Mon Aug  5 2002 Sergey Bolshakov <s.bolshakov@belcaf.com> 1.08-alt1
- first build for %distribution distribution

