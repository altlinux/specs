Name: xemacs-auctex
Version: 1.51
Release: alt1

%define_xemacs_package auctex

Summary: Basic TeX/LaTeX support
License: GPL
Group: Editors

%description
Basic TeX/LaTeX support

%prep
%setup -qc

%install
%xemacs_package_install
%xemacs_package_find_files

%files -f %name-files

%changelog
* Thu May 21 2009 Sergey Bolshakov <sbolshakov@altlinux.ru> 1.51-alt1
- 1.51

* Sat Mar 12 2005 Sergey Bolshakov <sbolshakov@altlinux.ru> 1.46-alt1
- 1.46

* Sat Jan 29 2005 Sergey Bolshakov <sbolshakov@altlinux.ru> 1.42-alt1
- 1.42

* Wed Aug 18 2004 Sergey Bolshakov <sbolshakov@altlinux.ru> 1.38-alt1
- 1.38

* Sat Feb 07 2004 Sergey Bolshakov <sbolshakov@altlinux.ru> 1.36-alt1
- 1.36

* Mon May 19 2003 Sergey Bolshakov <s.bolshakov@sam-solutions.net> 1.35-alt1
 - 1.35

* Thu Mar  6 2003 Sergey Bolshakov <s.bolshakov@sam-solutions.net> 1.33-alt1
- 1.33

* Sat Dec 21 2002 Sergey Bolshakov <s.bolshakov@belcaf.com> 1.32-alt2
- #1531 fixed

* Mon Aug  5 2002 Sergey Bolshakov <s.bolshakov@belcaf.com> 1.32-alt1
- first build for %distribution distribution

