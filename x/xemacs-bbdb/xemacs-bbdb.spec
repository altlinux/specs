Name: xemacs-bbdb
Version: 1.32
Release: alt1

%define_xemacs_package bbdb

Summary: The Big Brother Data Base
License: GPL
Group: Editors

Patch: %xemacs_package-1.26-alt-perl.patch

%description
The Big Brother Data Base

%prep
%setup -qc
%patch -p1

%install
%xemacs_package_install
%xemacs_package_find_files

%files -f %name-files

%changelog
* Thu May 21 2009 Sergey Bolshakov <sbolshakov@altlinux.ru> 1.32-alt1
- 1.32

* Sat Dec 10 2005 Sergey Bolshakov <sbolshakov@altlinux.ru> 1.29-alt1
- 1.29

* Sat Aug 06 2005 Sergey Bolshakov <sbolshakov@altlinux.ru> 1.26-alt1
- 1.26

* Sat Jan 29 2005 Sergey Bolshakov <sbolshakov@altlinux.ru> 1.25-alt1
- 1.25

* Tue Jan 11 2005 Sergey Bolshakov <sbolshakov@altlinux.ru> 1.24-alt2
- rebuilt in new env

* Sat Nov 15 2003 Sergey Bolshakov <sbolshakov@altlinux.ru> 1.24-alt1
- 1.24

* Sat Jun 07 2003 Sergey Bolshakov <s.bolshakov@sam-solutions.net> 1.23-alt1
 - 1.23

* Sat Dec 21 2002 Sergey Bolshakov <s.bolshakov@belcaf.com> 1.21-alt2
- #1531 fixed

* Mon Aug  5 2002 Sergey Bolshakov <s.bolshakov@belcaf.com> 1.21-alt1
- first build for %distribution distribution

