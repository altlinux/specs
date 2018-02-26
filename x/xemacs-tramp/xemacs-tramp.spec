Name: xemacs-tramp
Version: 1.40
Release: alt1

%define_xemacs_package tramp

Summary: Remote shell-based file editing
License: GPL
Group: Editors

%description
Remote shell-based file editing

%prep
%setup -qc

%install
%xemacs_package_install
%xemacs_package_find_files

%files -f %name-files

%changelog
* Thu May 21 2009 Sergey Bolshakov <sbolshakov@altlinux.ru> 1.40-alt1
- 1.40

* Sun May 21 2006 Sergey Bolshakov <sbolshakov@altlinux.ru> 1.32-alt1
- 1.32

* Sat Dec 10 2005 Sergey Bolshakov <sbolshakov@altlinux.ru> 1.28-alt1
- 1.28

* Sat Aug 06 2005 Sergey Bolshakov <sbolshakov@altlinux.ru> 1.25-alt1
- 1.25

* Fri May 06 2005 Sergey Bolshakov <sbolshakov@altlinux.ru> 1.23-alt1
- 1.23

* Sat Jan 29 2005 Sergey Bolshakov <sbolshakov@altlinux.ru> 1.22-alt1
- 1.22

* Sat Feb 07 2004 Sergey Bolshakov <sbolshakov@altlinux.ru> 1.17-alt1
- 1.17

* Sat Sep 27 2003 Sergey Bolshakov <sbolshakov@altlinux.ru> 1.16-alt1
 - 1.16

* Sat Jul 05 2003 Sergey Bolshakov <s.bolshakov@sam-solutions.net> 1.15-alt1
 - 1.15

* Mon May 19 2003 Sergey Bolshakov <s.bolshakov@sam-solutions.net> 1.12-alt1
 - 1.12

* Wed Mar  5 2003 Sergey Bolshakov <s.bolshakov@sam-solutions.net> 1.11-alt1
- 1.11

* Sat Dec 21 2002 Sergey Bolshakov <s.bolshakov@belcaf.com> 1.10-alt2
- #1531 fixed

* Mon Oct 28 2002 Sergey Bolshakov <s.bolshakov@belcaf.com> 1.10-alt1
- 1.10

* Mon Aug  5 2002 Sergey Bolshakov <s.bolshakov@belcaf.com> 1.05-alt1
- first build for %distribution distribution

