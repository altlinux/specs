Name: xemacs-eterm
Version: 1.18
Release: alt1

%define_xemacs_package eterm

Summary: Terminal emulation
License: GPL
Group: Editors

%description
Terminal emulation for XEmacs

%prep
%setup -qc

%install
%xemacs_package_install
%xemacs_package_find_files

%files -f %name-files

%changelog
* Tue May 03 2011 Sergey Bolshakov <sbolshakov@altlinux.ru> 1.18-alt1
- 1.18

* Mon May 25 2009 Sergey Bolshakov <sbolshakov@altlinux.ru> 1.17-alt2
- rebuilt in new env

* Sat Aug 06 2005 Sergey Bolshakov <sbolshakov@altlinux.ru> 1.17-alt1
- 1.17

* Thu Apr 14 2005 Sergey Bolshakov <sbolshakov@altlinux.ru> 1.15-alt2
- rebuilt in new env

* Sat Nov 15 2003 Sergey Bolshakov <sbolshakov@altlinux.ru> 1.15-alt1
- 1.15

* Sat Oct 04 2003 Sergey Bolshakov <sbolshakov@altlinux.ru> 1.14-alt1
- 1.14

* Sat Dec 21 2002 Sergey Bolshakov <s.bolshakov@belcaf.com> 1.13-alt2
- #1531 fixed

* Mon Aug  5 2002 Sergey Bolshakov <s.bolshakov@belcaf.com> 1.13-alt1
- first build for %distribution distribution

