Name: xemacs-haskell-mode
Version: 1.11
Release: alt1

%define_xemacs_package haskell-mode

Summary: Haskell mode for XEmacs
License: GPL
Group: Editors

%description
Haskell mode for XEmacs

%prep
%setup -qc

%install
%xemacs_package_install
%xemacs_package_find_files

%files -f %name-files

%changelog
* Thu May 21 2009 Sergey Bolshakov <sbolshakov@altlinux.ru> 1.11-alt1
- 1.11

* Sun May 21 2006 Sergey Bolshakov <sbolshakov@altlinux.ru> 1.08-alt1
- 1.08

* Thu Apr 14 2005 Sergey Bolshakov <sbolshakov@altlinux.ru> 1.07-alt2
- rebuilt in new env

* Wed Aug 18 2004 Sergey Bolshakov <sbolshakov@altlinux.ru> 1.07-alt1
- 1.07

* Sat Nov 15 2003 Sergey Bolshakov <sbolshakov@altlinux.ru> 1.06-alt1
- 1.06

* Wed Mar  5 2003 Sergey Bolshakov <s.bolshakov@sam-solutions.net> 1.05-alt1
- 1.05

* Sat Dec 21 2002 Sergey Bolshakov <s.bolshakov@belcaf.com> 1.03-alt2
- #1531 fixed

* Mon Aug  5 2002 Sergey Bolshakov <s.bolshakov@belcaf.com> 1.03-alt1
- first build for %distribution distribution

