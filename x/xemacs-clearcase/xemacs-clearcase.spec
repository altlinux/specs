Name: xemacs-clearcase
Version: 1.10
Release: alt2

%define_xemacs_package clearcase

Summary: New Clearcase Version Control for XEmacs
License: GPL
Group: Editors

%description
New Clearcase Version Control for XEmacs

%prep
%setup -qc

%install
%xemacs_package_install
%xemacs_package_find_files

%files -f %name-files

%changelog
* Fri May 22 2009 Sergey Bolshakov <sbolshakov@altlinux.ru> 1.10-alt2
- rebuilt in new env

* Sat Aug 06 2005 Sergey Bolshakov <sbolshakov@altlinux.ru> 1.10-alt1
- 1.10

* Sat Jan 29 2005 Sergey Bolshakov <sbolshakov@altlinux.ru> 1.09-alt1
- 1.09

* Sat Nov 15 2003 Sergey Bolshakov <sbolshakov@altlinux.ru> 1.08-alt1
- 1.08

* Mon May 19 2003 Sergey Bolshakov <s.bolshakov@sam-solutions.net> 1.06-alt1
 - 1.06

* Sat Dec 21 2002 Sergey Bolshakov <s.bolshakov@belcaf.com> 1.04-alt2
- #1531 fixed

* Mon Aug  5 2002 Sergey Bolshakov <s.bolshakov@belcaf.com> 1.04-alt1
- first build for %distribution distribution
