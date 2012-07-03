Name: xemacs-base
Version: 2.30
Release: alt1

%define_xemacs_package xemacs-base

Summary: Fundamental XEmacs support, you almost certainly need this
License: GPL
Group: Editors

%description
Fundamental XEmacs support, you almost certainly need this

%prep
%setup -qc

%install
%xemacs_package_install
%xemacs_package_find_files

%files -f %name-files

%changelog
* Tue May 03 2011 Sergey Bolshakov <sbolshakov@altlinux.ru> 2.30-alt1
- 2.30

* Mon May 25 2009 Sergey Bolshakov <sbolshakov@altlinux.ru> 2.19-alt1
- 2.19

* Sun May 21 2006 Sergey Bolshakov <sbolshakov@altlinux.ru> 2.03-alt1
- 2.03

* Sun Jan 22 2006 Sergey Bolshakov <sbolshakov@altlinux.ru> 2.01-alt1
- 2.01

* Sat Dec 10 2005 Sergey Bolshakov <sbolshakov@altlinux.ru> 2.00-alt1
- 2.00

* Fri May  6 2005 Sergey Bolshakov <sbolshakov@altlinux.ru> 1.97-alt1
- 1.97

* Sat Mar 12 2005 Sergey Bolshakov <sbolshakov@altlinux.ru> 1.96-alt1
- 1.96

* Sat Jan 29 2005 Sergey Bolshakov <sbolshakov@altlinux.ru> 1.94-alt1
- 1.94

* Wed Aug 18 2004 Sergey Bolshakov <sbolshakov@altlinux.ru> 1.87-alt1
- 1.87

* Sat Jun  5 2004 Sergey Bolshakov <sbolshakov@altlinux.ru> 1.86-alt1
- 1.86

* Sat Feb  7 2004 Sergey Bolshakov <sbolshakov@altlinux.ru> 1.84-alt1
- 1.84

* Sat Nov 15 2003 Sergey Bolshakov <sbolshakov@altlinux.ru> 1.82-alt1
- 1.82

* Sat Oct  4 2003 Sergey Bolshakov <sbolshakov@altlinux.ru> 1.81-alt1
- 1.81

* Sat Jul  5 2003 Sergey Bolshakov <s.bolshakov@sam-solutions.net> 1.78-alt1
- 1.78

* Sat Jun  7 2003 Sergey Bolshakov <s.bolshakov@sam-solutions.net> 1.77-alt1
- 1.77

* Wed Mar  5 2003 Sergey Bolshakov <s.bolshakov@sam-solutions.net> 1.75-alt1
- 1.75

* Sat Dec 21 2002 Sergey Bolshakov <s.bolshakov@belcaf.com> 1.71-alt2
- #1531 fixed

* Mon Dec 16 2002 Sergey Bolshakov <s.bolshakov@belcaf.com> 1.71-alt1
- 1.71

* Mon Oct 28 2002 Sergey Bolshakov <s.bolshakov@belcaf.com> 1.70-alt1
- 1.70

* Mon Aug  5 2002 Sergey Bolshakov <s.bolshakov@belcaf.com> 1.66-alt1
- first build for %distribution distribution

