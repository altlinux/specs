Name: xemacs-mail-lib
Version: 1.80
Release: alt1

%define_xemacs_package mail-lib

Summary: Fundamental lisp files for providing email support
License: GPL
Group: Editors

%description
Fundamental lisp files for providing email support

%prep
%setup -qc

%install
%xemacs_package_install
%xemacs_package_find_files

%files -f %name-files

%changelog
* Thu May 21 2009 Sergey Bolshakov <sbolshakov@altlinux.ru> 1.80-alt1
- 1.80

* Sun May 21 2006 Sergey Bolshakov <sbolshakov@altlinux.ru> 1.76-alt1
- 1.76

* Sat Dec 10 2005 Sergey Bolshakov <sbolshakov@altlinux.ru> 1.75-alt1
- 1.75

* Fri May 06 2005 Sergey Bolshakov <sbolshakov@altlinux.ru> 1.73-alt1
- 1.73

* Sat Mar 12 2005 Sergey Bolshakov <sbolshakov@altlinux.ru> 1.71-alt1
- 1.71

* Sat Jan 29 2005 Sergey Bolshakov <sbolshakov@altlinux.ru> 1.70-alt1
- 1.70

* Wed Aug 18 2004 Sergey Bolshakov <sbolshakov@altlinux.ru> 1.67-alt1
- 1.67

* Sat Jun 05 2004 Sergey Bolshakov <sbolshakov@altlinux.ru> 1.65-alt1
- 1.65

* Sat Feb 07 2004 Sergey Bolshakov <sbolshakov@altlinux.ru> 1.64-alt1
- 1.64

* Sat Nov 15 2003 Sergey Bolshakov <sbolshakov@altlinux.ru> 1.63-alt1
- 1.63

* Sat Oct 04 2003 Sergey Bolshakov <sbolshakov@altlinux.ru> 1.62-alt1
- 1.62

* Sat Sep 27 2003 Sergey Bolshakov <sbolshakov@altlinux.ru> 1.60-alt1
 - 1.60

* Sat Jun 07 2003 Sergey Bolshakov <s.bolshakov@sam-solutions.net> 1.59-alt1
 - 1.59

* Mon May 19 2003 Sergey Bolshakov <s.bolshakov@sam-solutions.net> 1.57-alt1
 - 1.57

* Wed Mar  5 2003 Sergey Bolshakov <s.bolshakov@sam-solutions.net> 1.56-alt1
- 1.56

* Sat Dec 21 2002 Sergey Bolshakov <s.bolshakov@belcaf.com> 1.54-alt2
- #1531 fixed

* Mon Dec 16 2002 Sergey Bolshakov <s.bolshakov@belcaf.com> 1.54-alt1
- 1.54

* Mon Oct 28 2002 Sergey Bolshakov <s.bolshakov@belcaf.com> 1.53-alt1
- 1.53

* Mon Aug  5 2002 Sergey Bolshakov <s.bolshakov@belcaf.com> 1.47-alt1
- first build for %distribution distribution

