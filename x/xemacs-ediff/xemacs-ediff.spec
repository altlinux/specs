Name: xemacs-ediff
Version: 1.81
Release: alt1

%define_xemacs_package ediff

Summary: Interface over GNU patch
License: GPL
Group: Editors

%description
Interface over GNU patch

%prep
%setup -qc

%install
%xemacs_package_install
%xemacs_package_find_files

%files -f %name-files

%changelog
* Tue May 03 2011 Sergey Bolshakov <sbolshakov@altlinux.ru> 1.81-alt1
- 1.81

* Thu May 21 2009 Sergey Bolshakov <sbolshakov@altlinux.ru> 1.77-alt1
- 1.77

* Sun May 21 2006 Sergey Bolshakov <sbolshakov@altlinux.ru> 1.62-alt1
- 1.62

* Sat Dec 10 2005 Sergey Bolshakov <sbolshakov@altlinux.ru> 1.60-alt1
- 1.60

* Sat Aug 06 2005 Sergey Bolshakov <sbolshakov@altlinux.ru> 1.53-alt1
- 1.53

* Sat Mar 12 2005 Sergey Bolshakov <sbolshakov@altlinux.ru> 1.51-alt1
- 1.51

* Sat Jun 05 2004 Sergey Bolshakov <sbolshakov@altlinux.ru> 1.50-alt1
- 1.50

* Sat Nov 15 2003 Sergey Bolshakov <sbolshakov@altlinux.ru> 1.49-alt1
- 1.49

* Sat Jun 07 2003 Sergey Bolshakov <s.bolshakov@sam-solutions.net> 1.47-alt1
 - 1.47

* Thu Mar  6 2003 Sergey Bolshakov <s.bolshakov@sam-solutions.net> 1.46-alt1
- 1.46

* Sat Dec 21 2002 Sergey Bolshakov <s.bolshakov@belcaf.com> 1.44-alt2
- #1531 fixed

* Mon Dec 16 2002 Sergey Bolshakov <s.bolshakov@belcaf.com> 1.44-alt1
- 1.44

* Mon Oct 28 2002 Sergey Bolshakov <s.bolshakov@belcaf.com> 1.43-alt1
- 1.43

* Mon Aug  5 2002 Sergey Bolshakov <s.bolshakov@belcaf.com> 1.41-alt1
- first build for %distribution distribution

