Name: xemacs-xslt-process
Version: 1.12
Release: alt1

%define_xemacs_package xslt-process

Summary: XSLT processing support
License: GPL
Group: Editors

%description
XSLT processing support

%prep
%setup -qc

%install
%xemacs_package_install
%xemacs_package_find_files

%files -f %name-files

%changelog
* Thu May 21 2009 Sergey Bolshakov <sbolshakov@altlinux.ru> 1.12-alt1
- 1.12

* Fri Apr 15 2005 Sergey Bolshakov <sbolshakov@altlinux.ru> 1.11-alt4
- rebuilt in new env

* Tue Jun  8 2004 Sergey Bolshakov <sbolshakov@altlinux.ru> 1.11-alt3
- rebuilt

* Sat Dec 21 2002 Sergey Bolshakov <s.bolshakov@belcaf.com> 1.11-alt2
- #1531 fixed

* Mon Oct 28 2002 Sergey Bolshakov <s.bolshakov@belcaf.com> 1.11-alt1
- 1.11

* Mon Aug  5 2002 Sergey Bolshakov <s.bolshakov@belcaf.com> 1.10-alt1
- first build for %distribution distribution

