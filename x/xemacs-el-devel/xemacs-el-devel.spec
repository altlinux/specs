Name: xemacs-el-devel
Version: 1.82
Release: alt1

%define_xemacs_package xemacs-devel

Summary: Emacs Lisp developer support
License: GPL
Group: Editors

%description
Emacs Lisp developer support

%prep
%setup -qc

%install
%xemacs_package_install
%xemacs_package_find_files

%files -f %name-files

%changelog
* Tue May 03 2011 Sergey Bolshakov <sbolshakov@altlinux.ru> 1.82-alt1
- 1.82

* Fri May 22 2009 Sergey Bolshakov <sbolshakov@altlinux.ru> 1.79-alt1
- 1.79

* Sat Dec 10 2005 Sergey Bolshakov <sbolshakov@altlinux.ru> 1.72-alt1
- 1.72

* Sat Jan 29 2005 Sergey Bolshakov <sbolshakov@altlinux.ru> 1.70-alt1
- 1.70

* Wed Aug 18 2004 Sergey Bolshakov <sbolshakov@altlinux.ru> 1.64-alt1
- 1.64

* Sat Jun  5 2004 Sergey Bolshakov <sbolshakov@altlinux.ru> 1.63-alt1
- 1.63

* Sat Feb  7 2004 Sergey Bolshakov <sbolshakov@altlinux.ru> 1.61-alt1
- 1.61

* Sat Nov 15 2003 Sergey Bolshakov <sbolshakov@altlinux.ru> 1.60-alt1
- 1.60

* Sat Sep 27 2003 Sergey Bolshakov <sbolshakov@altlinux.ru> 1.58-alt1
- 1.58

* Sat Jun  7 2003 Sergey Bolshakov <s.bolshakov@sam-solutions.net> 1.55-alt1
- 1.55

* Mon May 19 2003 Sergey Bolshakov <s.bolshakov@sam-solutions.net> 1.52-alt1
- 1.52

* Thu Mar  6 2003 Sergey Bolshakov <s.bolshakov@sam-solutions.net> 1.50-alt1
- 1.50

* Sat Dec 21 2002 Sergey Bolshakov <s.bolshakov@belcaf.com> 1.48-alt2
- #1531 fixed

* Mon Oct 28 2002 Sergey Bolshakov <s.bolshakov@belcaf.com> 1.48-alt1
- 1.48

* Mon Aug  5 2002 Sergey Bolshakov <s.bolshakov@belcaf.com> 1.47-alt1
- first build for %distribution distribution

