Name: xemacs-prog-modes
Version: 2.21
Release: alt1

%define_xemacs_package prog-modes

Summary: Support for various programming languages
License: GPL
Group: Editors

BuildRequires: xemacs-base xemacs-cc-mode xemacs-dired xemacs-edit-utils xemacs-fsf-compat xemacs-speedbar

%description
Support for various programming languages

%prep
%setup -qc

%install
%xemacs_package_install
%xemacs_package_find_files

%files -f %name-files

%changelog
* Tue May 03 2011 Sergey Bolshakov <sbolshakov@altlinux.ru> 2.21-alt1
- 2.21

* Thu May 21 2009 Sergey Bolshakov <sbolshakov@altlinux.ru> 2.19-alt1
- 2.19

* Sun May 21 2006 Sergey Bolshakov <sbolshakov@altlinux.ru> 2.07-alt1
- 2.07

* Sat Dec 10 2005 Sergey Bolshakov <sbolshakov@altlinux.ru> 2.06-alt1
- 2.06

* Mon Aug  8 2005 Sergey Bolshakov <sbolshakov@altlinux.ru> 2.05-alt1
- 2.05

* Fri May 06 2005 Sergey Bolshakov <sbolshakov@altlinux.ru> 2.03-alt1
- 2.03

* Sat Mar 12 2005 Sergey Bolshakov <sbolshakov@altlinux.ru> 2.02-alt1
- 2.02

* Wed Aug 18 2004 Sergey Bolshakov <sbolshakov@altlinux.ru> 2.01-alt1
- 2.01

* Sat Jun 05 2004 Sergey Bolshakov <sbolshakov@altlinux.ru> 1.96-alt1
- 1.96

* Sat Feb 07 2004 Sergey Bolshakov <sbolshakov@altlinux.ru> 1.94-alt1
- 1.94

* Sat Nov 15 2003 Sergey Bolshakov <sbolshakov@altlinux.ru> 1.91-alt1
- 1.91

* Sat Oct 04 2003 Sergey Bolshakov <sbolshakov@altlinux.ru> 1.89-alt1
- 1.89

* Sat Sep 27 2003 Sergey Bolshakov <sbolshakov@altlinux.ru> 1.83-alt1
 - 1.83

* Sat Jul 05 2003 Sergey Bolshakov <s.bolshakov@sam-solutions.net> 1.79-alt1
 - 1.79

* Sat Jun 07 2003 Sergey Bolshakov <s.bolshakov@sam-solutions.net> 1.73-alt1
 - 1.73

* Thu Mar  6 2003 Sergey Bolshakov <s.bolshakov@sam-solutions.net> 1.72-alt1
- 1.72

* Sat Dec 21 2002 Sergey Bolshakov <s.bolshakov@belcaf.com> 1.67-alt3
- #1531 fixed

* Sat Nov 30 2002 Sergey Bolshakov <s.bolshakov@belcaf.com> 1.67-alt2
- xemacs-el-devel requirement dropped

* Mon Oct 28 2002 Sergey Bolshakov <s.bolshakov@belcaf.com> 1.67-alt1
- 1.67

* Mon Aug  5 2002 Sergey Bolshakov <s.bolshakov@belcaf.com> 1.60-alt1
- first build for %distribution distribution


