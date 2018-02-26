Name: xemacs-mule-base
Version: 1.56
Release: alt1

%define_xemacs_mule_package mule-base

Summary: Basic Mule support
License: GPL
Group: Editors

%description
Basic Mule support

%prep
%setup -qc

%install
%xemacs_package_install
%xemacs_package_find_files

%files -f %name-files

%changelog
* Tue May 03 2011 Sergey Bolshakov <sbolshakov@altlinux.ru> 1.56-alt1
- 1.56

* Thu May 21 2009 Sergey Bolshakov <sbolshakov@altlinux.ru> 1.53-alt1
- 1.53

* Sun May 21 2006 Sergey Bolshakov <sbolshakov@altlinux.ru> 1.48-alt1
- 1.48

* Sun Dec 11 2005 Sergey Bolshakov <sbolshakov@altlinux.ru> 1.47-alt2
- rebuilt in new env

* Sat Aug 06 2005 Sergey Bolshakov <sbolshakov@altlinux.ru> 1.47-alt1
- 1.47

* Thu Apr 14 2005 Sergey Bolshakov <sbolshakov@altlinux.ru> 1.46-alt2
- rebuilt in new env

* Sat Feb 07 2004 Sergey Bolshakov <sbolshakov@altlinux.ru> 1.46-alt1
- 1.46

* Sat Nov 15 2003 Sergey Bolshakov <sbolshakov@altlinux.ru> 1.44-alt1
- 1.44

* Sat Jun 07 2003 Sergey Bolshakov <s.bolshakov@sam-solutions.net> 1.43-alt1
 - 1.43

* Sat Dec 21 2002 Sergey Bolshakov <s.bolshakov@belcaf.com> 1.42-alt2
- #1531 fixed

* Mon Aug  5 2002 Sergey Bolshakov <s.bolshakov@belcaf.com> 1.42-alt1
- first build for %distribution distribution

