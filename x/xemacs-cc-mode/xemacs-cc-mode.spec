Name: xemacs-cc-mode
Version: 1.45
Release: alt2

%define_xemacs_package cc-mode

Summary: C, C++ and Java language support
License: GPL
Group: Editors

Patch0: %xemacs_package-1.43-fonts-awk.patch

%description
C, C++ and Java language support

%prep
%setup -qc
%patch -p1

%build
%xemacs_byterecompile -C lisp/%xemacs_package

%install
%xemacs_package_install
%xemacs_package_find_files

%files -f %name-files

%changelog
* Fri May 22 2009 Sergey Bolshakov <sbolshakov@altlinux.ru> 1.45-alt2
- rebuilt in new env

* Sat Aug 06 2005 Sergey Bolshakov <sbolshakov@altlinux.ru> 1.45-alt1
- 1.45

* Tue Mar 29 2005 Sergey Bolshakov <sbolshakov@altlinux.ru> 1.43-alt2
- more keywords for AWK mode

* Wed Aug 18 2004 Sergey Bolshakov <sbolshakov@altlinux.ru> 1.43-alt1
- 1.43

* Sat Feb 07 2004 Sergey Bolshakov <sbolshakov@altlinux.ru> 1.42-alt1
- 1.42

* Sat Nov 15 2003 Sergey Bolshakov <sbolshakov@altlinux.ru> 1.41-alt1
- 1.41

* Sat Oct 04 2003 Sergey Bolshakov <sbolshakov@altlinux.ru> 1.40-alt1
- 1.40

* Sat Sep 27 2003 Sergey Bolshakov <sbolshakov@altlinux.ru> 1.39-alt1
 - 1.39

* Mon May 19 2003 Sergey Bolshakov <s.bolshakov@sam-solutions.net> 1.33-alt1
 - 1.33

* Thu Mar  6 2003 Sergey Bolshakov <s.bolshakov@sam-solutions.net> 1.32-alt1
- 1.32

* Sat Dec 21 2002 Sergey Bolshakov <s.bolshakov@belcaf.com> 1.31-alt2
- #1531 fixed

* Mon Oct 28 2002 Sergey Bolshakov <s.bolshakov@belcaf.com> 1.31-alt1
- 1.31

* Mon Aug  5 2002 Sergey Bolshakov <s.bolshakov@belcaf.com> 1.28-alt1
- first build for %distribution distribution

