Name: xemacs-escreen
Version: 1.01
Release: alt3

%define_xemacs_package escreen

Summary: Screen-like addon to XEmacs
License: GPL
Group: Editors

%description
Multiple editing sessions withing a single frame (like screen)

%prep
%setup -qc

%install
%xemacs_package_install
%xemacs_package_find_files

%files -f %name-files

%changelog
* Mon May 25 2009 Sergey Bolshakov <sbolshakov@altlinux.ru> 1.01-alt3
- rebuilt in new env

* Thu Apr 14 2005 Sergey Bolshakov <sbolshakov@altlinux.ru> 1.01-alt2
- rebuilt in new env

* Sat Jun  5 2004 Sergey Bolshakov <sbolshakov@altlinux.ru> 1.01-alt1
- 1.01

