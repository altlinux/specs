Name: xemacs-efs
Version: 1.34
Release: alt1

%define_xemacs_package efs

Summary: Treat files on remote systems the same as local files
License: GPL
Group: Editors

%description
Treat files on remote systems the same as local files

%prep
%setup -qc

%install
%xemacs_package_install
%xemacs_package_find_files

%files -f %name-files

%changelog
* Thu May 21 2009 Sergey Bolshakov <sbolshakov@altlinux.ru> 1.34-alt1
- 1.34

* Sat Jan 29 2005 Sergey Bolshakov <sbolshakov@altlinux.ru> 1.33-alt1
- 1.33

* Sat Nov 15 2003 Sergey Bolshakov <sbolshakov@altlinux.ru> 1.32-alt1
- 1.32

* Sat Oct 04 2003 Sergey Bolshakov <sbolshakov@altlinux.ru> 1.31-alt1
- 1.31

* Sat Dec 21 2002 Sergey Bolshakov <s.bolshakov@belcaf.com> 1.29-alt2
- #1531 fixed

* Mon Aug  5 2002 Sergey Bolshakov <s.bolshakov@belcaf.com> 1.29-alt1
- first build for %distribution distribution

