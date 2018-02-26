Name: xemacs-reftex
Version: 1.34
Release: alt3

%define_xemacs_package reftex

Summary: Emacs support for LaTeX cross-references, citations
License: GPL
Group: Editors

%description
Emacs support for LaTeX cross-references, citations

%prep
%setup -qc

%install
%xemacs_package_install
%xemacs_package_find_files

%files -f %name-files

%changelog
* Fri May 22 2009 Sergey Bolshakov <sbolshakov@altlinux.ru> 1.34-alt3
- rebuilt in new env

* Thu Apr 14 2005 Sergey Bolshakov <sbolshakov@altlinux.ru> 1.34-alt2
- rebuilt in new env

* Sat Jun 05 2004 Sergey Bolshakov <sbolshakov@altlinux.ru> 1.34-alt1
- 1.34

* Sat Nov 15 2003 Sergey Bolshakov <sbolshakov@altlinux.ru> 1.33-alt1
- 1.33

* Sat Oct 04 2003 Sergey Bolshakov <sbolshakov@altlinux.ru> 1.32-alt1
- 1.32

* Sat Sep 27 2003 Sergey Bolshakov <sbolshakov@altlinux.ru> 1.30-alt1
 - 1.30

* Sat Dec 21 2002 Sergey Bolshakov <s.bolshakov@belcaf.com> 1.28-alt2
- #1531 fixed

* Mon Oct 28 2002 Sergey Bolshakov <s.bolshakov@belcaf.com> 1.28-alt1
- 1.28

* Mon Aug  5 2002 Sergey Bolshakov <s.bolshakov@belcaf.com> 1.25-alt1
- first build for %distribution distribution

