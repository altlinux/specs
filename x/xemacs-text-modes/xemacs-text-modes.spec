Name: xemacs-text-modes
Version: 2.00
Release: alt1

%define_xemacs_package text-modes

Summary: Miscellaneous support for editing text files
License: GPL
Group: Editors

%description
Miscellaneous support for editing text files

%prep
%setup -qc

%install
%xemacs_package_install
%xemacs_package_find_files

%files -f %name-files

%changelog
* Tue May 03 2011 Sergey Bolshakov <sbolshakov@altlinux.ru> 2.00-alt1
- 2.00

* Thu May 21 2009 Sergey Bolshakov <sbolshakov@altlinux.ru> 1.96-alt1
- 1.96

* Sat Dec 10 2005 Sergey Bolshakov <sbolshakov@altlinux.ru> 1.90-alt1
- 1.90

* Sat Aug 06 2005 Sergey Bolshakov <sbolshakov@altlinux.ru> 1.88-alt1
- 1.88

* Fri May 06 2005 Sergey Bolshakov <sbolshakov@altlinux.ru> 1.87-alt1
- 1.87

* Sat Mar 12 2005 Sergey Bolshakov <sbolshakov@altlinux.ru> 1.84-alt1
- 1.84

* Sat Jan 29 2005 Sergey Bolshakov <sbolshakov@altlinux.ru> 1.82-alt1
- 1.82

* Wed Aug 18 2004 Sergey Bolshakov <sbolshakov@altlinux.ru> 1.78-alt1
- 1.78

* Sat Jun 05 2004 Sergey Bolshakov <sbolshakov@altlinux.ru> 1.77-alt1
- 1.77

* Sat Feb 07 2004 Sergey Bolshakov <sbolshakov@altlinux.ru> 1.73-alt1
- 1.73

* Sat Nov 15 2003 Sergey Bolshakov <sbolshakov@altlinux.ru> 1.71-alt1
- 1.71

* Sat Oct 04 2003 Sergey Bolshakov <sbolshakov@altlinux.ru> 1.66-alt1
- 1.66

* Sat Sep 27 2003 Sergey Bolshakov <sbolshakov@altlinux.ru> 1.63-alt1
 - 1.63

* Sat Jul 05 2003 Sergey Bolshakov <s.bolshakov@sam-solutions.net> 1.61-alt1
 - 1.61

* Mon May 19 2003 Sergey Bolshakov <s.bolshakov@sam-solutions.net> 1.60-alt1
 - 1.60

* Wed Mar  5 2003 Sergey Bolshakov <s.bolshakov@sam-solutions.net> 1.58-alt1
- 1.58

* Sat Dec 21 2002 Sergey Bolshakov <s.bolshakov@belcaf.com> 1.55-alt2
- #1531 fixed

* Mon Dec 16 2002 Sergey Bolshakov <s.bolshakov@belcaf.com> 1.55-alt1
- 1.55

* Mon Oct 28 2002 Sergey Bolshakov <s.bolshakov@belcaf.com> 1.53-alt1
- 1.53

* Mon Aug  5 2002 Sergey Bolshakov <s.bolshakov@belcaf.com> 1.48-alt1
- first build for %distribution distribution

