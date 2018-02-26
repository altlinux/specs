Name: xemacs-xlib
Version: 1.14
Release: alt2

%define_xemacs_package xlib

Summary: XEmacs interface to X server
License: GPL
Group: Graphical desktop/Other

%description
XEmacs interface to X server

%prep
%setup -qc

%install
%xemacs_package_install
%xemacs_package_find_files

%files -f %name-files

%changelog
* Mon May 25 2009 Sergey Bolshakov <sbolshakov@altlinux.ru> 1.14-alt2
- rebuilt in new env

* Fri May 06 2005 Sergey Bolshakov <sbolshakov@altlinux.ru> 1.14-alt1
- 1.14

* Sat Jan 29 2005 Sergey Bolshakov <sbolshakov@altlinux.ru> 1.13-alt1
- 1.13

* Wed Aug 18 2004 Sergey Bolshakov <sbolshakov@altlinux.ru> 1.12-alt1
- 1.12

* Sat Jun  5 2004 Sergey Bolshakov <sbolshakov@altlinux.ru> 1.10-alt1
- 1.10

