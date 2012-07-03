Name: xemacs-scheme
Version: 1.18
Release: alt1

%define_xemacs_package scheme

Summary: Front-end support for Inferior Scheme
License: GPL
Group: Editors

%description
Front-end support for Inferior Scheme

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

* Thu Apr 14 2005 Sergey Bolshakov <sbolshakov@altlinux.ru> 1.14-alt2
- rebuilt in new env

* Sat Nov 15 2003 Sergey Bolshakov <sbolshakov@altlinux.ru> 1.14-alt1
- 1.14

* Thu Mar  6 2003 Sergey Bolshakov <s.bolshakov@sam-solutions.net> 1.13-alt1
- 1.13

* Thu Dec 26 2002 Sergey Bolshakov <s.bolshakov@belcaf.com> 1.12-alt2
- #1531 fixed

* Mon Oct 28 2002 Sergey Bolshakov <s.bolshakov@belcaf.com> 1.12-alt1
- 1.12

* Mon Aug  5 2002 Sergey Bolshakov <s.bolshakov@belcaf.com> 1.11-alt1
- first build for %distribution distribution

