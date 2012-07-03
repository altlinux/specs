Name: xemacs-mule-ucs
Version: 1.18
Release: alt1

%define_xemacs_mule_package mule-ucs

Summary: Extended coding systems (including Unicode) for XEmacs
License: GPL
Group: Editors

%description
Extended coding systems (including Unicode) for XEmacs

%prep
%setup -qc

%install
%xemacs_package_install
%xemacs_package_find_files

%files -f %name-files

%changelog
* Tue May 03 2011 Sergey Bolshakov <sbolshakov@altlinux.ru> 1.18-alt1
- 1.18

* Thu May 21 2009 Sergey Bolshakov <sbolshakov@altlinux.ru> 1.17-alt1
- 1.17

* Sun Dec 11 2005 Sergey Bolshakov <sbolshakov@altlinux.ru> 1.14-alt2
- rebuilt in new env

* Sat Aug 06 2005 Sergey Bolshakov <sbolshakov@altlinux.ru> 1.14-alt1
- 1.14

* Sat Mar 12 2005 Sergey Bolshakov <sbolshakov@altlinux.ru> 1.11-alt1
- 1.11

* Wed Aug 18 2004 Sergey Bolshakov <sbolshakov@altlinux.ru> 1.06-alt1
- 1.06

* Sat Nov 15 2003 Sergey Bolshakov <sbolshakov@altlinux.ru> 1.05-alt1
- 1.05

* Sat Dec 21 2002 Sergey Bolshakov <s.bolshakov@belcaf.com> 1.04-alt2
- #1531 fixed

* Mon Aug  5 2002 Sergey Bolshakov <s.bolshakov@belcaf.com> 1.04-alt1
- first build for %distribution distribution

