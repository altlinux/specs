Name: xemacs-view-process
Version: 1.13
Release: alt3

%define_xemacs_package view-process

Summary: A Unix process browsing tool
License: GPL
Group: Editors

Requires: procps

%description
A Unix process browsing tool

%prep
%setup -qc

%install
%xemacs_package_install
%xemacs_package_find_files

%files -f %name-files

%changelog
* Mon May 25 2009 Sergey Bolshakov <sbolshakov@altlinux.ru> 1.13-alt3
- rebuilt in new env

* Fri Apr 15 2005 Sergey Bolshakov <sbolshakov@altlinux.ru> 1.13-alt2
- rebuilt in new env

* Sat Nov 15 2003 Sergey Bolshakov <sbolshakov@altlinux.ru> 1.13-alt1
- 1.13

* Sat Dec 21 2002 Sergey Bolshakov <s.bolshakov@belcaf.com> 1.12-alt2
- #1531 fixed

* Mon Oct 28 2002 Sergey Bolshakov <s.bolshakov@belcaf.com> 1.12-alt1
- 1.12

* Mon Aug  5 2002 Sergey Bolshakov <s.bolshakov@belcaf.com> 1.11-alt1
- first build for %distribution distribution

