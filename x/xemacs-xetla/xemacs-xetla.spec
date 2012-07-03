Name: xemacs-xetla
Version: 1.02
Release: alt1

%define_xemacs_package xetla

Summary: XEmacs frontend to GNU arch (tla)
License: GPL
Group: Editors

%description
XEmacs frontend to GNU arch (tla)

%prep
%setup -qc

%install
%xemacs_package_install
%xemacs_package_find_files

%files -f %name-files

%changelog
* Thu May 21 2009 Sergey Bolshakov <sbolshakov@altlinux.ru> 1.02-alt1
- 1.02

* Sun Jan 22 2006 Sergey Bolshakov <sbolshakov@altlinux.ru> 1.01-alt1
- 1.01

* Fri May  6 2005 Sergey Bolshakov <sbolshakov@altlinux.ru> 1.00-alt1
- 1.00

