Name: xemacs-os-utils
Version: 1.41
Release: alt1

%define_xemacs_package os-utils

Summary: Miscellaneous O/S utilities
License: GPL
Group: Editors

%description
Miscellaneous O/S utilities

%prep
%setup -qc

%install
%xemacs_package_install
%xemacs_package_find_files

%files -f %name-files

%changelog
* Thu May 21 2009 Sergey Bolshakov <sbolshakov@altlinux.ru> 1.41-alt1
- 1.41

* Sun May 21 2006 Sergey Bolshakov <sbolshakov@altlinux.ru> 1.37-alt1
- 1.37

* Sat Mar 12 2005 Sergey Bolshakov <sbolshakov@altlinux.ru> 1.36-alt1
- 1.36

* Sat Feb 07 2004 Sergey Bolshakov <sbolshakov@altlinux.ru> 1.35-alt1
- 1.35

* Sat Nov 15 2003 Sergey Bolshakov <sbolshakov@altlinux.ru> 1.34-alt1
- 1.34

* Sat Sep 27 2003 Sergey Bolshakov <sbolshakov@altlinux.ru> 1.32-alt1
 - 1.32

* Sat Jul 05 2003 Sergey Bolshakov <s.bolshakov@sam-solutions.net> 1.31-alt1
 - 1.31

* Thu Mar  6 2003 Sergey Bolshakov <s.bolshakov@sam-solutions.net> 1.30-alt1
- 1.30

* Sat Dec 21 2002 Sergey Bolshakov <s.bolshakov@belcaf.com> 1.29-alt2
- #1531 fixed

* Mon Oct 28 2002 Sergey Bolshakov <s.bolshakov@belcaf.com> 1.29-alt1
- 1.29

* Mon Aug  5 2002 Sergey Bolshakov <s.bolshakov@belcaf.com> 1.28-alt1
- first build for %distribution distribution

