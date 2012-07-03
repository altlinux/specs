Name: xemacs-tooltalk
Version: 1.15
Release: alt3

%define_xemacs_package tooltalk

Summary: Support for building with Tooltalk
License: GPL
Group: Editors

%description
Support for building with Tooltalk

%prep
%setup -qc

%install
%xemacs_package_install
%xemacs_package_find_files

%files -f %name-files

%changelog
* Mon May 25 2009 Sergey Bolshakov <sbolshakov@altlinux.ru> 1.15-alt3
- rebuilt in new env

* Fri Apr 15 2005 Sergey Bolshakov <sbolshakov@altlinux.ru> 1.15-alt2
- rebuilt in new env

* Sat Nov 15 2003 Sergey Bolshakov <sbolshakov@altlinux.ru> 1.15-alt1
- 1.15

* Sat Oct 04 2003 Sergey Bolshakov <sbolshakov@altlinux.ru> 1.14-alt1
- 1.14

* Sat Dec 21 2002 Sergey Bolshakov <s.bolshakov@belcaf.com> 1.13-alt2
- #1531 fixed

* Mon Aug  5 2002 Sergey Bolshakov <s.bolshakov@belcaf.com> 1.13-alt1
- first build for %distribution distribution

