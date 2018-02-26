Name: xemacs-sgml
Version: 1.11
Release: alt3

%define_xemacs_package sgml

Summary: SGML/Linuxdoc-SGML editing
License: GPL
Group: Editors

%description
SGML/Linuxdoc-SGML editing

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

* Sat Feb 07 2004 Sergey Bolshakov <sbolshakov@altlinux.ru> 1.11-alt1
- 1.11

* Sat Nov 15 2003 Sergey Bolshakov <sbolshakov@altlinux.ru> 1.10-alt1
- 1.10

* Sat Oct 04 2003 Sergey Bolshakov <sbolshakov@altlinux.ru> 1.09-alt1
- 1.09

* Sat Dec 21 2002 Sergey Bolshakov <s.bolshakov@belcaf.com> 1.08-alt2
- #1531 fixed

* Mon Aug  5 2002 Sergey Bolshakov <s.bolshakov@belcaf.com> 1.08-alt1
- first build for %distribution distribution

