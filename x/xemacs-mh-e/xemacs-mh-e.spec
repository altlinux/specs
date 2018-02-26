Name: xemacs-mh-e
Version: 1.33
Release: alt1

%define_xemacs_package mh-e

Summary: Front end support for MH
License: GPL
Group: Editors

%description
Front end support for MH

%prep
%setup -qc

%install
%xemacs_package_install
%xemacs_package_find_files

%files -f %name-files

%changelog
* Tue May 03 2011 Sergey Bolshakov <sbolshakov@altlinux.ru> 1.33-alt1
- 1.33

* Thu May 21 2009 Sergey Bolshakov <sbolshakov@altlinux.ru> 1.31-alt1
- 1.31

* Fri May 06 2005 Sergey Bolshakov <sbolshakov@altlinux.ru> 1.29-alt1
- 1.29

* Thu Apr 14 2005 Sergey Bolshakov <sbolshakov@altlinux.ru> 1.28-alt2
- rebuilt in new env

* Sat Feb 07 2004 Sergey Bolshakov <sbolshakov@altlinux.ru> 1.28-alt1
- 1.28

* Sat Nov 15 2003 Sergey Bolshakov <sbolshakov@altlinux.ru> 1.27-alt1
- 1.27

* Sat Oct 04 2003 Sergey Bolshakov <sbolshakov@altlinux.ru> 1.25-alt1
- 1.25

* Sat Jun 07 2003 Sergey Bolshakov <s.bolshakov@sam-solutions.net> 1.23-alt1
 - 1.23

* Mon May 19 2003 Sergey Bolshakov <s.bolshakov@sam-solutions.net> 1.19-alt1
 - 1.19

* Thu Mar  6 2003 Sergey Bolshakov <s.bolshakov@sam-solutions.net> 1.17-alt1
- 1.17

* Sat Dec 21 2002 Sergey Bolshakov <s.bolshakov@belcaf.com> 1.16-alt2
- #1531 fixed

* Mon Oct 28 2002 Sergey Bolshakov <s.bolshakov@belcaf.com> 1.16-alt1
- 1.16

* Mon Aug  5 2002 Sergey Bolshakov <s.bolshakov@belcaf.com> 1.14-alt1
- first build for %distribution distribution

