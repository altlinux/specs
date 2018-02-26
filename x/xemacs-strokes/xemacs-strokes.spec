Name: xemacs-strokes
Version: 1.10
Release: alt3

%define_xemacs_package strokes

Summary: Mouse enhancement utility
License: GPL
Group: Editors

%description
Mouse enhancement utility

%prep
%setup -qc

%install
%xemacs_package_install
%xemacs_package_find_files

%files -f %name-files

%changelog
* Mon May 25 2009 Sergey Bolshakov <sbolshakov@altlinux.ru> 1.10-alt3
- rebuilt in new env

* Fri Apr 15 2005 Sergey Bolshakov <sbolshakov@altlinux.ru> 1.10-alt2
- rebuilt in new env

* Sat Nov 15 2003 Sergey Bolshakov <sbolshakov@altlinux.ru> 1.10-alt1
- 1.10

* Sat Oct 04 2003 Sergey Bolshakov <sbolshakov@altlinux.ru> 1.09-alt1
- 1.09

* Sat Dec 21 2002 Sergey Bolshakov <s.bolshakov@belcaf.com> 1.08-alt2
- #1531 fixed

* Mon Aug  5 2002 Sergey Bolshakov <s.bolshakov@belcaf.com> 1.08-alt1
- first build for %distribution distribution

