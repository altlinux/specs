Name: xemacs-edit-utils
Version: 2.43
Release: alt1

%define_xemacs_package edit-utils

Patch: edit-utils-2.40-infodir.patch

Summary: Miscellaneous editor extensions, you probably need this
License: GPL
Group: Editors

%description
Miscellaneous editor extensions, you probably need this

%prep
%setup -qc
%patch -p1

%install
%xemacs_package_install
%xemacs_package_find_files

%files -f %name-files

%changelog
* Tue May 03 2011 Sergey Bolshakov <sbolshakov@altlinux.ru> 2.43-alt1
- 2.43

* Thu May 21 2009 Sergey Bolshakov <sbolshakov@altlinux.ru> 2.40-alt1
- 2.40

* Sun May 21 2006 Sergey Bolshakov <sbolshakov@altlinux.ru> 2.34-alt1
- 2.34

* Sat Dec 10 2005 Sergey Bolshakov <sbolshakov@altlinux.ru> 2.32-alt1
- 2.32

* Mon Nov  7 2005 Sergey Bolshakov <sbolshakov@altlinux.ru> 2.24-alt2
- attempt to fix setnu mode

* Sat Aug 06 2005 Sergey Bolshakov <sbolshakov@altlinux.ru> 2.24-alt1
- 2.24

* Sat Mar 12 2005 Sergey Bolshakov <sbolshakov@altlinux.ru> 2.22-alt1
- 2.22

* Sat Jan 29 2005 Sergey Bolshakov <sbolshakov@altlinux.ru> 2.19-alt1
- 2.19

* Wed Aug 18 2004 Sergey Bolshakov <sbolshakov@altlinux.ru> 2.14-alt1
- 2.14

* Sat Jun 05 2004 Sergey Bolshakov <sbolshakov@altlinux.ru> 2.12-alt1
- 2.12

* Sat Feb 07 2004 Sergey Bolshakov <sbolshakov@altlinux.ru> 2.11-alt1
- 2.11

* Sat Nov 15 2003 Sergey Bolshakov <sbolshakov@altlinux.ru> 2.10-alt1
- 2.10

* Sat Sep 27 2003 Sergey Bolshakov <sbolshakov@altlinux.ru> 2.07-alt1
 - 2.07

* Sat Jul 05 2003 Sergey Bolshakov <s.bolshakov@sam-solutions.net> 2.02-alt1
 - 2.02

* Mon May 19 2003 Sergey Bolshakov <s.bolshakov@sam-solutions.net> 2.00-alt1
 - 2.00

* Wed Mar  5 2003 Sergey Bolshakov <s.bolshakov@sam-solutions.net> 1.98-alt1
- 1.98

* Sat Dec 21 2002 Sergey Bolshakov <s.bolshakov@belcaf.com> 1.95-alt2
- #1531 fixed

* Mon Dec 16 2002 Sergey Bolshakov <s.bolshakov@belcaf.com> 1.95-alt1
- 1.95

* Mon Oct 28 2002 Sergey Bolshakov <s.bolshakov@belcaf.com> 1.93-alt1
- 1.93

* Mon Aug  5 2002 Sergey Bolshakov <s.bolshakov@belcaf.com> 1.89-alt1
- first build for %distribution distribution

