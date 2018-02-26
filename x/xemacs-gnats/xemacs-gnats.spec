Name: xemacs-gnats
Version: 1.17
Release: alt2

%define_xemacs_package gnats

Summary: XEmacs bug reports
License: GPL
Group: Editors

%description
XEmacs bug reports

%prep
%setup -qc

%install
%xemacs_package_install
%xemacs_package_find_files

%files -f %name-files

%changelog
* Fri May 22 2009 Sergey Bolshakov <sbolshakov@altlinux.ru> 1.17-alt2
- rebuilt in new env

* Fri May 06 2005 Sergey Bolshakov <sbolshakov@altlinux.ru> 1.17-alt1
- 1.17

* Thu Apr 14 2005 Sergey Bolshakov <sbolshakov@altlinux.ru> 1.16-alt2
- rebuilt in new env

* Sat Nov 15 2003 Sergey Bolshakov <sbolshakov@altlinux.ru> 1.16-alt1
- 1.16

* Sat Dec 21 2002 Sergey Bolshakov <s.bolshakov@belcaf.com> 1.15-alt2
- #1531 fixed

* Mon Aug  5 2002 Sergey Bolshakov <s.bolshakov@belcaf.com> 1.15-alt1
- first build for %distribution distribution

