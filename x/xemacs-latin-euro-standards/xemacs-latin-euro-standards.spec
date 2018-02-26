Name: xemacs-latin-euro-standards
Version: 1.09
Release: alt1

%define_xemacs_mule_package latin-euro-standards

Summary: Support for the Latin{7,8,9,10} character sets & coding systems.
License: GPL
Group: Editors

%description
Support for the Latin{7,8,9,10} character sets & coding systems.

%prep
%setup -qc

%install
%xemacs_package_install
%xemacs_package_find_files

%files -f %name-files

%changelog
* Tue May 03 2011 Sergey Bolshakov <sbolshakov@altlinux.ru> 1.09-alt1
- 1.09

* Thu May 21 2009 Sergey Bolshakov <sbolshakov@altlinux.ru> 1.08-alt1
- 1.08

* Sun Dec 11 2005 Sergey Bolshakov <sbolshakov@altlinux.ru> 1.07-alt2
- rebuilt in new env

* Sat Aug 06 2005 Sergey Bolshakov <sbolshakov@altlinux.ru> 1.07-alt1
- 1.07

* Fri May 06 2005 Sergey Bolshakov <sbolshakov@altlinux.ru> 1.04-alt1
- 1.04

* Sat Mar 12 2005 Sergey Bolshakov <sbolshakov@altlinux.ru> 1.03-alt1
- 1.03

