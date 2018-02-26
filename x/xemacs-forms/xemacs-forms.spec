Name: xemacs-forms
Version: 1.15
Release: alt3

%define_xemacs_package forms

Summary: Forms editing support (obsolete, use Widget instead)
License: GPL
Group: Editors

%description
Forms editing support (obsolete, use Widget instead)

%prep
%setup -qc

%install
%xemacs_package_install
%xemacs_package_find_files

%files -f %name-files

%changelog
* Fri May 22 2009 Sergey Bolshakov <sbolshakov@altlinux.ru> 1.15-alt3
- rebuilt in new env

* Thu Apr 14 2005 Sergey Bolshakov <sbolshakov@altlinux.ru> 1.15-alt2
- rebuilt in new env

* Sat Nov 15 2003 Sergey Bolshakov <sbolshakov@altlinux.ru> 1.15-alt1
- 1.15

* Sat Dec 21 2002 Sergey Bolshakov <s.bolshakov@belcaf.com> 1.14-alt2
- #1531 fixed

* Mon Aug  5 2002 Sergey Bolshakov <s.bolshakov@belcaf.com> 1.14-alt1
- first build for %distribution distribution

