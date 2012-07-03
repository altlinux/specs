Name: xemacs-footnote
Version: 1.16
Release: alt3

%define_xemacs_package footnote

Summary: Footnoting in mail message editing modes
License: GPL
Group: Editors

%description
Footnoting in mail message editing modes

%prep
%setup -qc

%install
%xemacs_package_install
%xemacs_package_find_files

%files -f %name-files

%changelog
* Mon May 25 2009 Sergey Bolshakov <sbolshakov@altlinux.ru> 1.16-alt3
- rebuilt in new env

* Thu Apr 14 2005 Sergey Bolshakov <sbolshakov@altlinux.ru> 1.16-alt2
- rebuilt in new env

* Sat Nov 15 2003 Sergey Bolshakov <sbolshakov@altlinux.ru> 1.16-alt1
- 1.16

* Sat Dec 21 2002 Sergey Bolshakov <s.bolshakov@belcaf.com> 1.15-alt2
- #1531 fixed

* Mon Aug  5 2002 Sergey Bolshakov <s.bolshakov@belcaf.com> 1.15-alt1
- first build for %distribution distribution

