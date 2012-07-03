Name: xemacs-sounds-wav
Version: 1.12
Release: alt3

%define_xemacs_package sounds-wav

Summary: XEmacs Microsoft wav sound files
License: GPL
Group: Editors

%description
XEmacs Microsoft wav sound files

%prep
%setup -qc

%install
%xemacs_package_install
%xemacs_package_find_files

%files -f %name-files

%changelog
* Mon May 25 2009 Sergey Bolshakov <sbolshakov@altlinux.ru> 1.12-alt3
- rebuilt in new env

* Fri Apr 15 2005 Sergey Bolshakov <sbolshakov@altlinux.ru> 1.12-alt2
- rebuilt in new env

* Sat Nov 15 2003 Sergey Bolshakov <sbolshakov@altlinux.ru> 1.12-alt1
- 1.12

* Sat Oct 04 2003 Sergey Bolshakov <sbolshakov@altlinux.ru> 1.11-alt1
- 1.11

* Sat Dec 21 2002 Sergey Bolshakov <s.bolshakov@belcaf.com> 1.10-alt2
- #1531 fixed

* Mon Aug  5 2002 Sergey Bolshakov <s.bolshakov@belcaf.com> 1.10-alt1
- first build for %distribution distribution

