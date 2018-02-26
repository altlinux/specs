Name: xemacs-ispell
Version: 1.32
Release: alt2

%define_xemacs_package ispell

Summary: Spell-checking with GNU ispell
License: GPL
Group: Editors

%description
Spell-checking with GNU ispell or aspell

%prep
%setup -q -c

%install
%xemacs_package_install
%xemacs_package_find_files

%files -f %name-files

%changelog
* Fri May 22 2009 Sergey Bolshakov <sbolshakov@altlinux.ru> 1.32-alt2
- rebuilt in new env

* Sat Dec 10 2005 Sergey Bolshakov <sbolshakov@altlinux.ru> 1.32-alt1
- 1.32

* Sat Mar 12 2005 Sergey Bolshakov <sbolshakov@altlinux.ru> 1.31-alt1
- 1.31

* Sat Feb 07 2004 Sergey Bolshakov <sbolshakov@altlinux.ru> 1.29-alt1
- 1.29

* Sat Nov 15 2003 Sergey Bolshakov <sbolshakov@altlinux.ru> 1.26-alt1
- 1.26

* Sat Oct 18 2003 Sergey Bolshakov <sbolshakov@altlinux.ru> 1.24-alt4
- switched to aspell

* Sat Dec 21 2002 Sergey Bolshakov <s.bolshakov@belcaf.com> 1.24-alt3
- #1531 fixed

* Mon Oct 28 2002 Sergey Bolshakov <s.bolshakov@belcaf.com> 1.24-alt2
- missing requires added

* Mon Aug  5 2002 Sergey Bolshakov <s.bolshakov@belcaf.com> 1.24-alt1
- first build for %distribution distribution

