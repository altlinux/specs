Name: xemacs-jde
Version: 1.52
Release: alt1

%define_xemacs_package jde

Summary: Java language and development support
License: GPL
Group: Editors

Requires: findutils grep

%description
Java language and development support

%prep
%setup -qc

%install
%xemacs_package_install
%xemacs_package_find_files

%files -f %name-files

%changelog
* Thu May 21 2009 Sergey Bolshakov <sbolshakov@altlinux.ru> 1.52-alt1
- 1.52

* Sun May 21 2006 Sergey Bolshakov <sbolshakov@altlinux.ru> 1.51-alt1
- 1.51

* Sat Aug 06 2005 Sergey Bolshakov <sbolshakov@altlinux.ru> 1.48-alt1
- 1.48

* Thu Apr 14 2005 Sergey Bolshakov <sbolshakov@altlinux.ru> 1.46-alt2
- rebuilt in new env

* Sat Nov 15 2003 Sergey Bolshakov <sbolshakov@altlinux.ru> 1.46-alt1
- 1.46

* Mon May 19 2003 Sergey Bolshakov <s.bolshakov@sam-solutions.net> 1.45-alt1
 - 1.45

* Wed Mar  5 2003 Sergey Bolshakov <s.bolshakov@sam-solutions.net> 1.43-alt1
- 1.43

* Sat Dec 21 2002 Sergey Bolshakov <s.bolshakov@belcaf.com> 1.38-alt2
- #1531 fixed

* Mon Oct 28 2002 Sergey Bolshakov <s.bolshakov@belcaf.com> 1.38-alt1
- 1.38

* Mon Aug  5 2002 Sergey Bolshakov <s.bolshakov@belcaf.com> 1.35-alt1
- first build for %distribution distribution

