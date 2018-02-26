Name: xemacs-psgml
Version: 1.45
Release: alt1

%define_xemacs_package psgml

Summary: Validated HTML/SGML editing
License: GPL
Group: Editors

%description
Validated HTML/SGML editing

%prep
%setup -qc

%install
%xemacs_package_install
%xemacs_package_find_files

%files -f %name-files

%changelog
* Thu May 21 2009 Sergey Bolshakov <sbolshakov@altlinux.ru> 1.45-alt1
- 1.45

* Fri May 06 2005 Sergey Bolshakov <sbolshakov@altlinux.ru> 1.44-alt1
- 1.44

* Thu Apr 14 2005 Sergey Bolshakov <sbolshakov@altlinux.ru> 1.43-alt2
- rebuilt in new env

* Wed Aug 18 2004 Sergey Bolshakov <sbolshakov@altlinux.ru> 1.43-alt1
- 1.43

* Sat Feb 07 2004 Sergey Bolshakov <sbolshakov@altlinux.ru> 1.42-alt1
- 1.42

* Sat Sep 27 2003 Sergey Bolshakov <sbolshakov@altlinux.ru> 1.41-alt1
 - 1.41

* Mon May 19 2003 Sergey Bolshakov <s.bolshakov@sam-solutions.net> 1.40-alt1
 - 1.40

* Thu Mar  6 2003 Sergey Bolshakov <s.bolshakov@sam-solutions.net> 1.38-alt1
- 1.38

* Sat Dec 21 2002 Sergey Bolshakov <s.bolshakov@belcaf.com> 1.35-alt2
- #1531 fixed

* Mon Oct 28 2002 Sergey Bolshakov <s.bolshakov@belcaf.com> 1.35-alt1
- 1.35

* Mon Aug  5 2002 Sergey Bolshakov <s.bolshakov@belcaf.com> 1.28-alt1
- first build for %distribution distribution

