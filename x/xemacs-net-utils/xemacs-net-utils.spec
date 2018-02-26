Name: xemacs-net-utils
Version: 1.56
Release: alt2

%define_xemacs_package net-utils

Summary: Miscellaneous Networking Utilities
License: GPL
Group: Networking/Other

Requires: iputils bind-utils

%description
Miscellaneous Networking Utilities

%prep
%setup -qc

%install
%xemacs_package_install
%xemacs_package_find_files

%files -f %name-files

%changelog
* Thu Feb 04 2010 Sergey Bolshakov <sbolshakov@altlinux.ru> 1.56-alt2
- net-tools dependency dropped

* Thu May 21 2009 Sergey Bolshakov <sbolshakov@altlinux.ru> 1.56-alt1
- 1.56

* Sat Dec 10 2005 Sergey Bolshakov <sbolshakov@altlinux.ru> 1.48-alt1
- 1.48

* Fri May 06 2005 Sergey Bolshakov <sbolshakov@altlinux.ru> 1.46-alt1
- 1.46

* Thu Apr 14 2005 Sergey Bolshakov <sbolshakov@altlinux.ru> 1.44-alt2
- rebuilt in new env

* Wed Aug 18 2004 Sergey Bolshakov <sbolshakov@altlinux.ru> 1.44-alt1
- 1.44

* Sat Jun 05 2004 Sergey Bolshakov <sbolshakov@altlinux.ru> 1.42-alt1
- 1.42

* Sat Feb 07 2004 Sergey Bolshakov <sbolshakov@altlinux.ru> 1.38-alt1
- 1.38

* Sat Nov 15 2003 Sergey Bolshakov <sbolshakov@altlinux.ru> 1.33-alt1
- 1.33

* Sat Jun 07 2003 Sergey Bolshakov <s.bolshakov@sam-solutions.net> 1.32-alt1
 - 1.32

* Thu Mar  6 2003 Sergey Bolshakov <s.bolshakov@sam-solutions.net> 1.31-alt1
- 1.31

* Sat Dec 21 2002 Sergey Bolshakov <s.bolshakov@belcaf.com> 1.27-alt2
- #1531 fixed

* Mon Aug  5 2002 Sergey Bolshakov <s.bolshakov@belcaf.com> 1.27-alt1
- first build for %distribution distribution

