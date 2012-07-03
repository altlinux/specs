Name: xemacs-pc
Version: 1.28
Release: alt2

%define_xemacs_package pc

Summary: PC style interface emulation
License: GPL
Group: Editors

%description
PC style interface emulation

%prep
%setup -qc

%install
%xemacs_package_install
%xemacs_package_find_files

%files -f %name-files

%changelog
* Mon May 25 2009 Sergey Bolshakov <sbolshakov@altlinux.ru> 1.28-alt2
- rebuilt in new env

* Fri May 06 2005 Sergey Bolshakov <sbolshakov@altlinux.ru> 1.28-alt1
- 1.28

* Sat Mar 12 2005 Sergey Bolshakov <sbolshakov@altlinux.ru> 1.27-alt1
- 1.27

* Sat Nov 15 2003 Sergey Bolshakov <sbolshakov@altlinux.ru> 1.26-alt1
- 1.26

* Sat Dec 21 2002 Sergey Bolshakov <s.bolshakov@belcaf.com> 1.25-alt2
- #1531 fixed

* Mon Aug  5 2002 Sergey Bolshakov <s.bolshakov@belcaf.com> 1.25-alt1
- first build for %distribution distribution

