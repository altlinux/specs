Name: xemacs-egg-its
Version: 1.27
Release: alt4

%define_xemacs_mule_package egg-its

Summary: Wnn (4.2 and 6), SJ3 suppor
License: GPL
Group: Editors

%description
Wnn (4.2 and 6), SJ3 suppor

%prep
%setup -qc

%install
%xemacs_package_install
%xemacs_package_find_files

%files -f %name-files

%changelog
* Mon May 25 2009 Sergey Bolshakov <sbolshakov@altlinux.ru> 1.27-alt4
- rebuilt in new env

* Sun Dec 11 2005 Sergey Bolshakov <sbolshakov@altlinux.ru> 1.27-alt3
- rebuilt in new env

* Thu Apr 14 2005 Sergey Bolshakov <sbolshakov@altlinux.ru> 1.27-alt2
- rebuilt in new env

* Sat Nov 15 2003 Sergey Bolshakov <sbolshakov@altlinux.ru> 1.27-alt1
- 1.27

* Sat Dec 21 2002 Sergey Bolshakov <s.bolshakov@belcaf.com> 1.26-alt2
- #1531 fixed

* Mon Aug  5 2002 Sergey Bolshakov <s.bolshakov@belcaf.com> 1.26-alt1
- first build for %distribution distribution

