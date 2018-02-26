Name: xemacs-emerge
Version: 1.11
Release: alt3

%define_xemacs_package emerge

Summary: Another interface over GNU patch
License: GPL
Group: Editors

Requires: diffutils

%description
Another interface over GNU patch

%prep
%setup -qc

%install
%xemacs_package_install
%xemacs_package_find_files

%files -f %name-files

%changelog
* Mon May 25 2009 Sergey Bolshakov <sbolshakov@altlinux.ru> 1.11-alt3
- rebuilt in new env

* Thu Apr 14 2005 Sergey Bolshakov <sbolshakov@altlinux.ru> 1.11-alt2
- rebuilt in new env

* Sat Nov 15 2003 Sergey Bolshakov <sbolshakov@altlinux.ru> 1.11-alt1
- 1.11

* Sat Oct 04 2003 Sergey Bolshakov <sbolshakov@altlinux.ru> 1.10-alt1
- 1.10

* Sat Dec 21 2002 Sergey Bolshakov <s.bolshakov@belcaf.com> 1.09-alt2
- #1531 fixed

* Mon Aug  5 2002 Sergey Bolshakov <s.bolshakov@belcaf.com> 1.09-alt1
- first build for %distribution distribution

